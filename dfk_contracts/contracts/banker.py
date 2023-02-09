
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x4b1F4C7981465F814c4A78d79be21558A60f57F2",
    "sd": ""
}

ABI = """[
    {"type": "constructor", "inputs": [{"name": "_factory", "type": "address", "internalType": "address"}, {"name": "_bank", "type": "address", "internalType": "address"}, {"name": "_govToken", "type": "address", "internalType": "address"}, {"name": "_weth", "type": "address", "internalType": "address"}], "stateMutability": "nonpayable"},
    {"name": "LogBridgeSet", "type": "event", "inputs": [{"name": "token", "type": "address", "indexed": true, "internalType": "address"}, {"name": "bridge", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "LogConvert", "type": "event", "inputs": [{"name": "server", "type": "address", "indexed": true, "internalType": "address"}, {"name": "token0", "type": "address", "indexed": true, "internalType": "address"}, {"name": "token1", "type": "address", "indexed": true, "internalType": "address"}, {"name": "amount0", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "amount1", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "amountGovToken", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "OwnershipTransferred", "type": "event", "inputs": [{"name": "previousOwner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "newOwner", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "bank", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "bridgeFor", "type": "function", "inputs": [{"name": "token", "type": "address", "internalType": "address"}], "outputs": [{"name": "bridge", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "convert", "type": "function", "inputs": [{"name": "token0", "type": "address", "internalType": "address"}, {"name": "token1", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "convertMultiple", "type": "function", "inputs": [{"name": "token0", "type": "address[]", "internalType": "address[]"}, {"name": "token1", "type": "address[]", "internalType": "address[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "factory", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IUniswapV2Factory"}], "stateMutability": "view"},
    {"name": "owner", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "renounceOwnership", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setBridge", "type": "function", "inputs": [{"name": "token", "type": "address", "internalType": "address"}, {"name": "bridge", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "transferOwnership", "type": "function", "inputs": [{"name": "newOwner", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class Banker(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def bank(self) -> address:
        return self.contract.functions.bank().call()

    def bridge_for(self, token:address) -> address:
        return self.contract.functions.bridgeFor(token).call()

    def convert(self, cred:Credentials, token0:address, token1:address) -> TxReceipt:
        tx = self.contract.functions.convert(token0, token1)
        return self.send_transaction(tx, cred)

    def convert_multiple(self, cred:Credentials, token0:Sequence[address], token1:Sequence[address]) -> TxReceipt:
        tx = self.contract.functions.convertMultiple(token0, token1)
        return self.send_transaction(tx, cred)

    def factory(self) -> address:
        return self.contract.functions.factory().call()

    def owner(self) -> address:
        return self.contract.functions.owner().call()

    def renounce_ownership(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.renounceOwnership()
        return self.send_transaction(tx, cred)

    def set_bridge(self, cred:Credentials, token:address, bridge:address) -> TxReceipt:
        tx = self.contract.functions.setBridge(token, bridge)
        return self.send_transaction(tx, cred)

    def transfer_ownership(self, cred:Credentials, new_owner:address) -> TxReceipt:
        tx = self.contract.functions.transferOwnership(new_owner)
        return self.send_transaction(tx, cred)