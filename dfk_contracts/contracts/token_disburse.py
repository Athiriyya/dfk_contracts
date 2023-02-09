
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x123165B3a30fdA3655B30cfC10135C1CA3C21bFC",
    "sd": ""
}

ABI = """[
    {"name": "DisbursementAdded", "type": "event", "inputs": [{"name": "id", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "recipient", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "startTime", "type": "uint64", "indexed": false, "internalType": "uint64"}, {"name": "duration", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
    {"name": "DisbursementClaim", "type": "event", "inputs": [{"name": "id", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "recipient", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "DisbursementUpdated", "type": "event", "inputs": [{"name": "id", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "reduction", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "startTime", "type": "uint64", "indexed": false, "internalType": "uint64"}, {"name": "duration", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
    {"name": "addDisbursement", "type": "function", "inputs": [{"name": "_recipient", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}, {"name": "_startTime", "type": "uint64", "internalType": "uint64"}, {"name": "_duration", "type": "uint64", "internalType": "uint64"}, {"name": "_note", "type": "string", "internalType": "string"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "addDisbursements", "type": "function", "inputs": [{"name": "_recipients", "type": "address[]", "internalType": "address[]"}, {"name": "_amounts", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_startTime", "type": "uint64", "internalType": "uint64"}, {"name": "_duration", "type": "uint64", "internalType": "uint64"}, {"name": "_note", "type": "string", "internalType": "string"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "claim", "type": "function", "inputs": [{"name": "_amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "disbursements", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "recipient", "type": "address", "internalType": "address"}, {"name": "note", "type": "string", "internalType": "string"}, {"name": "total", "type": "uint256", "internalType": "uint256"}, {"name": "claimed", "type": "uint256", "internalType": "uint256"}, {"name": "balance", "type": "uint256", "internalType": "uint256"}, {"name": "createdTime", "type": "uint64", "internalType": "uint64"}, {"name": "startTime", "type": "uint64", "internalType": "uint64"}, {"name": "duration", "type": "uint64", "internalType": "uint64"}], "stateMutability": "view"},
    {"name": "getDisbursementIds", "type": "function", "inputs": [{"name": "_recipient", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_tokenAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "reservedToken", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "totalClaimed", "type": "function", "inputs": [{"name": "_recipient", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "totalUnvested", "type": "function", "inputs": [{"name": "_recipient", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "totalVested", "type": "function", "inputs": [{"name": "_recipient", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "updateDisbursement", "type": "function", "inputs": [{"name": "_disbursementId", "type": "uint256", "internalType": "uint256"}, {"name": "_reduction", "type": "uint256", "internalType": "uint256"}, {"name": "_startTime", "type": "uint64", "internalType": "uint64"}, {"name": "_duration", "type": "uint64", "internalType": "uint64"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class TokenDisburse(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def add_disbursement(self, cred:Credentials, _recipient:address, _amount:uint256, _start_time:uint64, _duration:uint64, _note:string) -> TxReceipt:
        tx = self.contract.functions.addDisbursement(_recipient, _amount, _start_time, _duration, _note)
        return self.send_transaction(tx, cred)

    def add_disbursements(self, cred:Credentials, _recipients:Sequence[address], _amounts:Sequence[uint256], _start_time:uint64, _duration:uint64, _note:string) -> TxReceipt:
        tx = self.contract.functions.addDisbursements(_recipients, _amounts, _start_time, _duration, _note)
        return self.send_transaction(tx, cred)

    def claim(self, cred:Credentials, _amount:uint256) -> TxReceipt:
        tx = self.contract.functions.claim(_amount)
        return self.send_transaction(tx, cred)

    def disbursements(self, a:uint256) -> Tuple[uint256, address, string, uint256, uint256, uint256, uint64, uint64, uint64]:
        return self.contract.functions.disbursements(a).call()

    def get_disbursement_ids(self, _recipient:address) -> Sequence[uint256]:
        return self.contract.functions.getDisbursementIds(_recipient).call()

    def initialize(self, cred:Credentials, _token_address:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_token_address)
        return self.send_transaction(tx, cred)

    def reserved_token(self) -> uint256:
        return self.contract.functions.reservedToken().call()

    def total_claimed(self, _recipient:address) -> uint256:
        return self.contract.functions.totalClaimed(_recipient).call()

    def total_unvested(self, _recipient:address) -> uint256:
        return self.contract.functions.totalUnvested(_recipient).call()

    def total_vested(self, _recipient:address) -> uint256:
        return self.contract.functions.totalVested(_recipient).call()

    def update_disbursement(self, cred:Credentials, _disbursement_id:uint256, _reduction:uint256, _start_time:uint64, _duration:uint64) -> TxReceipt:
        tx = self.contract.functions.updateDisbursement(_disbursement_id, _reduction, _start_time, _duration)
        return self.send_transaction(tx, cred)