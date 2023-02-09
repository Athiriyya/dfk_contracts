
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x794C07912474351b3134E6D6B3B7b3b4A07cbAAa",
    "sd": "0x36fAE766e51f17F8218C735f58426E293498Db2B"
}

ABI = """[
    {"type": "constructor", "inputs": [{"name": "_feeToSetter", "type": "address", "internalType": "address"}], "stateMutability": "nonpayable"},
    {"name": "PairCreated", "type": "event", "inputs": [{"name": "token0", "type": "address", "indexed": true, "internalType": "address"}, {"name": "token1", "type": "address", "indexed": true, "internalType": "address"}, {"name": "pair", "type": "address", "indexed": false, "internalType": "address"}, {"name": "", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "allPairs", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "allPairsLength", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "createPair", "type": "function", "inputs": [{"name": "tokenA", "type": "address", "internalType": "address"}, {"name": "tokenB", "type": "address", "internalType": "address"}], "outputs": [{"name": "pair", "type": "address", "internalType": "address"}], "stateMutability": "nonpayable"},
    {"name": "feeTo", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "feeToSetter", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "getPair", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "pairCodeHash", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "pure"},
    {"name": "setFeeTo", "type": "function", "inputs": [{"name": "_feeTo", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setFeeToSetter", "type": "function", "inputs": [{"name": "_feeToSetter", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class UniswapV2Factory(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def all_pairs(self, a:uint256) -> address:
        return self.contract.functions.allPairs(a).call()

    def all_pairs_length(self) -> uint256:
        return self.contract.functions.allPairsLength().call()

    def create_pair(self, cred:Credentials, token_a:address, token_b:address) -> TxReceipt:
        tx = self.contract.functions.createPair(token_a, token_b)
        return self.send_transaction(tx, cred)

    def fee_to(self) -> address:
        return self.contract.functions.feeTo().call()

    def fee_to_setter(self) -> address:
        return self.contract.functions.feeToSetter().call()

    def get_pair(self, a:address, b:address) -> address:
        return self.contract.functions.getPair(a, b).call()

    def pair_code_hash(self) -> bytes32:
        return self.contract.functions.pairCodeHash().call()

    def set_fee_to(self, cred:Credentials, _fee_to:address) -> TxReceipt:
        tx = self.contract.functions.setFeeTo(_fee_to)
        return self.send_transaction(tx, cred)

    def set_fee_to_setter(self, cred:Credentials, _fee_to_setter:address) -> TxReceipt:
        tx = self.contract.functions.setFeeToSetter(_fee_to_setter)
        return self.send_transaction(tx, cred)