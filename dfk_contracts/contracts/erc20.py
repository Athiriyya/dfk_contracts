
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": None,
    "sd": None
}

ABI = """[
    {"name": "Approval", "type": "event", "inputs": [{"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "spender", "type": "address", "internalType": "address", "indexed": true}, {"name": "value", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "Transfer", "type": "event", "inputs": [{"name": "from", "type": "address", "internalType": "address", "indexed": true}, {"name": "to", "type": "address", "internalType": "address", "indexed": true}, {"name": "value", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "allowance", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "spender", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "approve", "type": "function", "inputs": [{"name": "spender", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "balanceOf", "type": "function", "inputs": [{"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "burn", "type": "function", "inputs": [{"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "burnFrom", "type": "function", "inputs": [{"name": "account", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "decimals", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "decreaseAllowance", "type": "function", "inputs": [{"name": "spender", "type": "address", "internalType": "address"}, {"name": "subtractedValue", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "increaseAllowance", "type": "function", "inputs": [{"name": "spender", "type": "address", "internalType": "address"}, {"name": "addedValue", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "mint", "type": "function", "inputs": [{"name": "to", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "name", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "supportsInterface", "type": "function", "inputs": [{"name": "interfaceId", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "symbol", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "totalSupply", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "transfer", "type": "function", "inputs": [{"name": "recipient", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "transferFrom", "type": "function", "inputs": [{"name": "sender", "type": "address", "internalType": "address"}, {"name": "recipient", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"}
]
"""     

class ERC20(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def allowance(self, contract_address:address, owner:address, spender:address) -> uint256:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        return contract.functions.allowance(owner, spender).call()

    def approve(self, cred:Credentials, contract_address:address, spender:address, amount:uint256) -> TxReceipt:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        tx = contract.functions.approve(spender, amount)
        return self.send_transaction(tx, cred)

    def balance_of(self, contract_address:address, account:address) -> uint256:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        return contract.functions.balanceOf(account).call()

    def burn(self, cred:Credentials, contract_address:address, amount:uint256) -> TxReceipt:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        tx = contract.functions.burn(amount)
        return self.send_transaction(tx, cred)

    def burn_from(self, cred:Credentials, contract_address:address, account:address, amount:uint256) -> TxReceipt:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        tx = contract.functions.burnFrom(account, amount)
        return self.send_transaction(tx, cred)

    def decimals(self, contract_address:address) -> uint8:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        return contract.functions.decimals().call()

    def decrease_allowance(self, cred:Credentials, contract_address:address, spender:address, subtracted_value:uint256) -> TxReceipt:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        tx = contract.functions.decreaseAllowance(spender, subtracted_value)
        return self.send_transaction(tx, cred)

    def increase_allowance(self, cred:Credentials, contract_address:address, spender:address, added_value:uint256) -> TxReceipt:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        tx = contract.functions.increaseAllowance(spender, added_value)
        return self.send_transaction(tx, cred)

    def mint(self, cred:Credentials, contract_address:address, to:address, amount:uint256) -> TxReceipt:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        tx = contract.functions.mint(to, amount)
        return self.send_transaction(tx, cred)

    def name(self, contract_address:address) -> string:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        return contract.functions.name().call()

    def supports_interface(self, contract_address:address, interface_id:bytes4) -> bool:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        return contract.functions.supportsInterface(interface_id).call()

    def symbol(self, contract_address:address) -> string:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        return contract.functions.symbol().call()

    def total_supply(self, contract_address:address) -> uint256:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        return contract.functions.totalSupply().call()

    def transfer(self, cred:Credentials, contract_address:address, recipient:address, amount:uint256) -> TxReceipt:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        tx = contract.functions.transfer(recipient, amount)
        return self.send_transaction(tx, cred)

    def transfer_from(self, cred:Credentials, contract_address:address, sender:address, recipient:address, amount:uint256) -> TxReceipt:
        contract = self.get_custom_contract(contract_address, abi=self.abi)
        tx = contract.functions.transferFrom(sender, recipient, amount)
        return self.send_transaction(tx, cred)