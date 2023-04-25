#! /usr/bin/env python
from web3 import Web3
from web3.middleware.geth_poa import geth_poa_middleware
from web3.logs import DISCARD

from .credentials import Credentials

from .solidity_types import (address, ChecksumAddress, TxReceipt, AttributeDict)
from web3.contract.contract import Contract
from typing import Dict, Tuple, Union, Optional, Any, Sequence

DEFAULT_TIMEOUT = 30
DEFAULT_MAX_GAS = 50
DEFAULT_MAX_PRIORITY_GAS = 3

W3_INSTANCES: Dict[str, Web3] = {}

class ABIContractWrapper:
    def __init__(self, 
                 contract_address:str, 
                 abi:str,
                 rpc:str,
                 max_gas_gwei:float=DEFAULT_MAX_GAS,
                 max_priority_gwei:float=DEFAULT_MAX_PRIORITY_GAS):
        self.rpc = rpc
        # self.contract_address = contract_address
        self.abi = abi
        self.nonces: Dict[address, int] = {}
        self.timeout = DEFAULT_TIMEOUT

        # This one superclass may be used by many contracts, who don't all need to
        # create separate Web3 instances. Just use one per RPC
        global W3_INSTANCES
        w3 = W3_INSTANCES.get(self.rpc, None)
        if not w3:
            w3 = Web3(Web3.HTTPProvider(self.rpc))
            w3.middleware_onion.inject(geth_poa_middleware, layer=0)
            W3_INSTANCES[self.rpc] = w3
        self.w3 = w3
        self.contract_address:ChecksumAddress = self.w3.to_checksum_address(contract_address)

        self.max_gas_wei = self.w3.to_wei(max_gas_gwei, 'gwei')
        self.max_priority_wei = self.w3.to_wei(max_priority_gwei, 'gwei')

        self.contract = self.w3.eth.contract(self.contract_address, abi=self.abi)

    def get_nonce_and_update(self, address:address, force_fetch=True) -> int:
        # FIXME: I think there's a bug in the caching logic below that lets
        # nonces run ahead of where they should be and causes transactions to
        # fail.
        # So force_fetch is set to true, which fetches the appropriate nonce for
        # every transaction
        # - Athiriyya 13 December 2022

        # We keep track of our own nonce, and only re-fetch it if a 'nonce too low'
        # error gets thrown       
        nonce = self.nonces.get(address, 0) 
        if force_fetch or nonce == 0:
            nonce = self.w3.eth.get_transaction_count( address, 'pending')

        # Store the next nonce this address will use, and return the current one
        self.nonces[address] = nonce + 1
        return nonce

    def get_gas_dict_and_update(self, address:address) -> Dict[str, int]:
        nonce = self.get_nonce_and_update(address)
         
        legacy = False
        if legacy:
            # TODO: it's expensive to query for fees with every transaction. 
            # Maybe query only once a minute?
            gas, gas_price = self.get_legacy_gas_fee()
            gas_dict = {
                'gas': gas, 
                'gasPrice':gas_price, 
                'nonce':nonce
            }
        else:
            gas_dict = {
                'from': address, 
                'maxFeePerGas': int(self.max_gas_wei), 
                'maxPriorityFeePerGas': int(self.max_priority_wei), 
                'nonce': nonce
            }
        return gas_dict

    def call_contract_function(self, function_name:str, *args) -> Any:
        contract_func = getattr(self.contract, function_name)
        return contract_func(*args).call()

    def get_custom_contract(self, contract_address:ChecksumAddress, abi:str | None=None) -> Contract:
        # TODO: Many custom contracts for e.g. ERC20 tokens could
        # be re-used by caching a contracts dictionary keyed by address
        # For now, just return a new contract
        abi = abi or self.abi
        checked_addr = self.w3.to_checksum_address(contract_address)
        contract = self.w3.eth.contract(checked_addr, abi=abi)
        return contract

    def send_transaction(self,
                         tx,
                         cred:Credentials,
                         extra_dict:Dict[str,Any] | None = None
                        ) -> TxReceipt:
        # Some transactions require extra information or fees when building 
        # the transaction. e.g. bridging functions need a {'value': <bridge_fee_in_wei>}
        # argument. If supplied, add that extra info
        address = cred.address  
        gas_dict = self.get_gas_dict_and_update(address)
        if extra_dict:
            gas_dict.update(extra_dict)
        tx_dict = tx.build_transaction(gas_dict)    
        signed_tx = self.w3.eth.account.sign_transaction(tx_dict, private_key=cred.private_key)
        try:
            self.w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        except Exception as e:
            if 'nonce too low' in str(e):
                nonce = self.get_nonce_and_update(address, force_fetch=True)
                return self.send_transaction( tx, cred)
            # otherwise, raise
            raise(e)

        receipt = self.w3.eth.wait_for_transaction_receipt(
            transaction_hash=signed_tx.hash,
            poll_latency=1,
            timeout=self.timeout,
        )
        return receipt

    def get_legacy_gas_fee(self) ->Tuple[int, int]:
        # See: https://web3py.readthedocs.io/en/stable/gas_price.html#gas-price-api
        # Some transactions may require a gas dict with the keys {'gasPrice': x_wei, '': y_wei}
        block = self.w3.eth.get_block("pending")
        base_gas = block.get('gasUsed', 2_500_000) + self.w3.to_wei(50, 'gwei')
        gas_limit =block.get('gasLimit', 2_500_000)

        return base_gas, gas_limit

    def tx_receipt_for_hash(self, tx_hash:address) -> TxReceipt:
        tx_receipt = self.w3.eth.get_transaction_receipt(tx_hash)
        return tx_receipt

    def parse_events(self, tx_receipt:TxReceipt, event_names:Sequence[str] | None = None) -> Dict[str, AttributeDict]:
        event_dicts = {}
        for event in self.contract.events: # type: ignore
            eds = event().process_receipt(tx_receipt, errors=DISCARD)
            if eds:
                for ed in eds:
                    event_dicts.setdefault(ed.event,[]).append(ed)
        if event_names:
            event_dicts = {k:v for k,v in event_dicts.items() if k in event_names}
        return event_dicts        
