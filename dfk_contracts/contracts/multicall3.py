
from ..abi_contract_wrapper import ABIContractWrapper
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xcA11bde05977b3631167028862bE2a173976CA11",
    "sd": "0xcA11bde05977b3631167028862bE2a173976CA11"
}

ABI = """[
    {"name": "aggregate", "type": "function", "inputs": [{"name": "calls", "type": "tuple[]", "components": [{"name": "target", "type": "address", "internalType": "address"}, {"name": "callData", "type": "bytes", "internalType": "bytes"}], "internalType": "struct Multicall3.Call[]"}], "outputs": [{"name": "blockNumber", "type": "uint256", "internalType": "uint256"}, {"name": "returnData", "type": "bytes[]", "internalType": "bytes[]"}], "stateMutability": "view"},
    {"name": "aggregate3", "type": "function", "inputs": [{"name": "calls", "type": "tuple[]", "components": [{"name": "target", "type": "address", "internalType": "address"}, {"name": "allowFailure", "type": "bool", "internalType": "bool"}, {"name": "callData", "type": "bytes", "internalType": "bytes"}], "internalType": "struct Multicall3.Call3[]"}], "outputs": [{"name": "returnData", "type": "tuple[]", "components": [{"name": "success", "type": "bool", "internalType": "bool"}, {"name": "returnData", "type": "bytes", "internalType": "bytes"}], "internalType": "struct Multicall3.Result[]"}], "stateMutability": "view"},
    {"name": "aggregate3Value", "type": "function", "inputs": [{"name": "calls", "type": "tuple[]", "components": [{"name": "target", "type": "address", "internalType": "address"}, {"name": "allowFailure", "type": "bool", "internalType": "bool"}, {"name": "value", "type": "uint256", "internalType": "uint256"}, {"name": "callData", "type": "bytes", "internalType": "bytes"}], "internalType": "struct Multicall3.Call3Value[]"}], "outputs": [{"name": "returnData", "type": "tuple[]", "components": [{"name": "success", "type": "bool", "internalType": "bool"}, {"name": "returnData", "type": "bytes", "internalType": "bytes"}], "internalType": "struct Multicall3.Result[]"}], "stateMutability": "payable"},
    {"name": "blockAndAggregate", "type": "function", "inputs": [{"name": "calls", "type": "tuple[]", "components": [{"name": "target", "type": "address", "internalType": "address"}, {"name": "callData", "type": "bytes", "internalType": "bytes"}], "internalType": "struct Multicall3.Call[]"}], "outputs": [{"name": "blockNumber", "type": "uint256", "internalType": "uint256"}, {"name": "blockHash", "type": "bytes32", "internalType": "bytes32"}, {"name": "returnData", "type": "tuple[]", "components": [{"name": "success", "type": "bool", "internalType": "bool"}, {"name": "returnData", "type": "bytes", "internalType": "bytes"}], "internalType": "struct Multicall3.Result[]"}], "stateMutability": "view"},
    {"name": "getBasefee", "type": "function", "inputs": [], "outputs": [{"name": "basefee", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getBlockHash", "type": "function", "inputs": [{"name": "blockNumber", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "blockHash", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "getBlockNumber", "type": "function", "inputs": [], "outputs": [{"name": "blockNumber", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getChainId", "type": "function", "inputs": [], "outputs": [{"name": "chainid", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getCurrentBlockCoinbase", "type": "function", "inputs": [], "outputs": [{"name": "coinbase", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "getCurrentBlockDifficulty", "type": "function", "inputs": [], "outputs": [{"name": "difficulty", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getCurrentBlockGasLimit", "type": "function", "inputs": [], "outputs": [{"name": "gaslimit", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getCurrentBlockTimestamp", "type": "function", "inputs": [], "outputs": [{"name": "timestamp", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getEthBalance", "type": "function", "inputs": [{"name": "addr", "type": "address", "internalType": "address"}], "outputs": [{"name": "balance", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getLastBlockHash", "type": "function", "inputs": [], "outputs": [{"name": "blockHash", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "tryAggregate", "type": "function", "inputs": [{"name": "requireSuccess", "type": "bool", "internalType": "bool"}, {"name": "calls", "type": "tuple[]", "components": [{"name": "target", "type": "address", "internalType": "address"}, {"name": "callData", "type": "bytes", "internalType": "bytes"}], "internalType": "struct Multicall3.Call[]"}], "outputs": [{"name": "returnData", "type": "tuple[]", "components": [{"name": "success", "type": "bool", "internalType": "bool"}, {"name": "returnData", "type": "bytes", "internalType": "bytes"}], "internalType": "struct Multicall3.Result[]"}], "stateMutability": "view"},
    {"name": "tryBlockAndAggregate", "type": "function", "inputs": [{"name": "requireSuccess", "type": "bool", "internalType": "bool"}, {"name": "calls", "type": "tuple[]", "components": [{"name": "target", "type": "address", "internalType": "address"}, {"name": "callData", "type": "bytes", "internalType": "bytes"}], "internalType": "struct Multicall3.Call[]"}], "outputs": [{"name": "blockNumber", "type": "uint256", "internalType": "uint256"}, {"name": "blockHash", "type": "bytes32", "internalType": "bytes32"}, {"name": "returnData", "type": "tuple[]", "components": [{"name": "success", "type": "bool", "internalType": "bool"}, {"name": "returnData", "type": "bytes", "internalType": "bytes"}], "internalType": "struct Multicall3.Result[]"}], "stateMutability": "nonpayable"}
]
"""     

class Multicall3(ABIContractWrapper):
    def __init__(self, chain_key:str, rpc:str):
        contract_address = CONTRACT_ADDRESS[chain_key]
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def aggregate(self, calls:Sequence[tuple], block_identifier:BlockIdentifier = 'latest') -> Tuple[uint256, List[bytes]]:
        return self.contract.functions.aggregate(calls).call(block_identifier=block_identifier)

    def aggregate3(self, calls:Sequence[tuple], block_identifier:BlockIdentifier = 'latest') -> List[tuple]:
        return self.contract.functions.aggregate3(calls).call(block_identifier=block_identifier)

    def aggregate3_value(self, cred:Credentials, calls:Sequence[tuple]) -> TxReceipt:
        tx = self.contract.functions.aggregate3Value(calls)
        return self.send_transaction(tx, cred)

    def block_and_aggregate(self, calls:Sequence[tuple], block_identifier:BlockIdentifier = 'latest') -> Tuple[uint256, bytes32, List[tuple]]:
        return self.contract.functions.blockAndAggregate(calls).call(block_identifier=block_identifier)

    def get_basefee(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.getBasefee().call(block_identifier=block_identifier)

    def get_block_hash(self, block_number:uint256, block_identifier:BlockIdentifier = 'latest') -> bytes32:
        return self.contract.functions.getBlockHash(block_number).call(block_identifier=block_identifier)

    def get_block_number(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.getBlockNumber().call(block_identifier=block_identifier)

    def get_chain_id(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.getChainId().call(block_identifier=block_identifier)

    def get_current_block_coinbase(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.getCurrentBlockCoinbase().call(block_identifier=block_identifier)

    def get_current_block_difficulty(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.getCurrentBlockDifficulty().call(block_identifier=block_identifier)

    def get_current_block_gas_limit(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.getCurrentBlockGasLimit().call(block_identifier=block_identifier)

    def get_current_block_timestamp(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.getCurrentBlockTimestamp().call(block_identifier=block_identifier)

    def get_eth_balance(self, addr:address, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.getEthBalance(addr).call(block_identifier=block_identifier)

    def get_last_block_hash(self, block_identifier:BlockIdentifier = 'latest') -> bytes32:
        return self.contract.functions.getLastBlockHash().call(block_identifier=block_identifier)

    def try_aggregate(self, require_success:bool, calls:Sequence[tuple], block_identifier:BlockIdentifier = 'latest') -> List[tuple]:
        return self.contract.functions.tryAggregate(require_success, calls).call(block_identifier=block_identifier)

    def try_block_and_aggregate(self, cred:Credentials, require_success:bool, calls:Sequence[tuple]) -> TxReceipt:
        tx = self.contract.functions.tryBlockAndAggregate(require_success, calls)
        return self.send_transaction(tx, cred)