
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xBbd7c4Be2e54fF5e013471162e1ABAD7AB74c3C3",
    "sd": ""
}

ABI = """[
    {"name": "Approval", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "spender", "type": "address", "indexed": true, "internalType": "address"}, {"name": "value", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "Transfer", "type": "event", "inputs": [{"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "value", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "allowance", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "spender", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "approve", "type": "function", "inputs": [{"name": "spender", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "balanceOf", "type": "function", "inputs": [{"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "burn", "type": "function", "inputs": [{"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "burnFrom", "type": "function", "inputs": [{"name": "account", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "burnable", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "decimals", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "decreaseAllowance", "type": "function", "inputs": [{"name": "spender", "type": "address", "internalType": "address"}, {"name": "subtractedValue", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "increaseAllowance", "type": "function", "inputs": [{"name": "spender", "type": "address", "internalType": "address"}, {"name": "addedValue", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_name", "type": "string", "internalType": "string"}, {"name": "_symbol", "type": "string", "internalType": "string"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "mint", "type": "function", "inputs": [{"name": "to", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "name", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "symbol", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "toggleBurnable", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "togglePause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "totalSupply", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "transfer", "type": "function", "inputs": [{"name": "to", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "transferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class RaffleTicket(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def allowance(self, owner:address, spender:address) -> uint256:
        return self.contract.functions.allowance(owner, spender).call()

    def approve(self, cred:Credentials, spender:address, amount:uint256) -> TxReceipt:
        tx = self.contract.functions.approve(spender, amount)
        return self.send_transaction(tx, cred)

    def balance_of(self, account:address) -> uint256:
        return self.contract.functions.balanceOf(account).call()

    def burn(self, cred:Credentials, amount:uint256) -> TxReceipt:
        tx = self.contract.functions.burn(amount)
        return self.send_transaction(tx, cred)

    def burn_from(self, cred:Credentials, account:address, amount:uint256) -> TxReceipt:
        tx = self.contract.functions.burnFrom(account, amount)
        return self.send_transaction(tx, cred)

    def burnable(self) -> bool:
        return self.contract.functions.burnable().call()

    def decimals(self) -> uint8:
        return self.contract.functions.decimals().call()

    def decrease_allowance(self, cred:Credentials, spender:address, subtracted_value:uint256) -> TxReceipt:
        tx = self.contract.functions.decreaseAllowance(spender, subtracted_value)
        return self.send_transaction(tx, cred)

    def increase_allowance(self, cred:Credentials, spender:address, added_value:uint256) -> TxReceipt:
        tx = self.contract.functions.increaseAllowance(spender, added_value)
        return self.send_transaction(tx, cred)

    def initialize(self, cred:Credentials, _name:string, _symbol:string) -> TxReceipt:
        tx = self.contract.functions.initialize(_name, _symbol)
        return self.send_transaction(tx, cred)

    def mint(self, cred:Credentials, to:address, amount:uint256) -> TxReceipt:
        tx = self.contract.functions.mint(to, amount)
        return self.send_transaction(tx, cred)

    def name(self) -> string:
        return self.contract.functions.name().call()

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
        return self.send_transaction(tx, cred)

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def symbol(self) -> string:
        return self.contract.functions.symbol().call()

    def toggle_burnable(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.toggleBurnable()
        return self.send_transaction(tx, cred)

    def toggle_pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.togglePause()
        return self.send_transaction(tx, cred)

    def total_supply(self) -> uint256:
        return self.contract.functions.totalSupply().call()

    def transfer(self, cred:Credentials, to:address, amount:uint256) -> TxReceipt:
        tx = self.contract.functions.transfer(to, amount)
        return self.send_transaction(tx, cred)

    def transfer_from(self, cred:Credentials, _from:address, to:address, amount:uint256) -> TxReceipt:
        tx = self.contract.functions.transferFrom(_from, to, amount)
        return self.send_transaction(tx, cred)

    def unpause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unpause()
        return self.send_transaction(tx, cred)