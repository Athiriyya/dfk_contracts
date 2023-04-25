#! /usr/bin/env python
from web3 import Web3
from web3.middleware.geth_poa import geth_poa_middleware

from .abi_contract_wrapper import ABIContractWrapper

from .solidity_types import *
from typing import Dict, Tuple, Union, Optional, Any

DEFAULT_TIMEOUT = 30
DEFAULT_MAX_GAS = 50
DEFAULT_MAX_PRIORITY_GAS = 3

W3_INSTANCES: Dict[str, Web3] = {}

class ABIMultiContractWrapper(ABIContractWrapper):
    def __init__(self, 
                 abi:str,
                 rpc:str,
                 max_gas_gwei:float=DEFAULT_MAX_GAS,
                 max_priority_gwei:float=DEFAULT_MAX_PRIORITY_GAS):
        self.rpc = rpc
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

        self.max_gas_wei = self.w3.to_wei(max_gas_gwei, 'gwei')
        self.max_priority_wei = self.w3.to_wei(max_priority_gwei, 'gwei')
