
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x947873092dc57C1A70704033c41cB110f4462a8B",
    "sd": ""
}

ABI = """[
    {"name": "Claimed", "type": "event", "inputs": [{"name": "recipient", "type": "address", "indexed": false, "internalType": "address"}, {"name": "token", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Dropped", "type": "event", "inputs": [{"name": "recipient", "type": "address", "indexed": false, "internalType": "address"}, {"name": "token", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Withdrawal", "type": "event", "inputs": [{"name": "tokenAddress", "type": "address", "indexed": false, "internalType": "address"}, {"name": "recipient", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "claimAirdrop", "type": "function", "inputs": [{"name": "_dropId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "deleteAirdrop", "type": "function", "inputs": [{"name": "player", "type": "address", "internalType": "address"}, {"name": "_dropId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "enabled", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setAirdrops", "type": "function", "inputs": [{"name": "_tokenAddress", "type": "address", "internalType": "address"}, {"name": "_recipients", "type": "address[]", "internalType": "address[]"}, {"name": "_amounts", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_note", "type": "string", "internalType": "string"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "toggleEnabled", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "tokenToPendingAmount", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "viewAirdrops", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "tokenAddress", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}, {"name": "time", "type": "uint256", "internalType": "uint256"}, {"name": "note", "type": "string", "internalType": "string"}], "internalType": "struct AirdropClaim.Drop[]"}], "stateMutability": "view"},
    {"name": "viewUserAirdrops", "type": "function", "inputs": [{"name": "player", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "tokenAddress", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}, {"name": "time", "type": "uint256", "internalType": "uint256"}, {"name": "note", "type": "string", "internalType": "string"}], "internalType": "struct AirdropClaim.Drop[]"}], "stateMutability": "view"},
    {"name": "withdrawTokens", "type": "function", "inputs": [{"name": "_tokenAddress", "type": "address", "internalType": "address"}, {"name": "_recipient", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class AirdropClaim(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def claim_airdrop(self, cred:Credentials, _drop_id:uint256) -> TxReceipt:
        tx = self.contract.functions.claimAirdrop(_drop_id)
        return self.send_transaction(tx, cred)

    def delete_airdrop(self, cred:Credentials, player:address, _drop_id:uint256) -> TxReceipt:
        tx = self.contract.functions.deleteAirdrop(player, _drop_id)
        return self.send_transaction(tx, cred)

    def enabled(self) -> bool:
        return self.contract.functions.enabled().call()

    def initialize(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.initialize()
        return self.send_transaction(tx, cred)

    def set_airdrops(self, cred:Credentials, _token_address:address, _recipients:Sequence[address], _amounts:Sequence[uint256], _note:string) -> TxReceipt:
        tx = self.contract.functions.setAirdrops(_token_address, _recipients, _amounts, _note)
        return self.send_transaction(tx, cred)

    def toggle_enabled(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.toggleEnabled()
        return self.send_transaction(tx, cred)

    def token_to_pending_amount(self, a:address) -> uint256:
        return self.contract.functions.tokenToPendingAmount(a).call()

    def view_airdrops(self) -> Sequence[tuple]:
        return self.contract.functions.viewAirdrops().call()

    def view_user_airdrops(self, player:address) -> Sequence[tuple]:
        return self.contract.functions.viewUserAirdrops(player).call()

    def withdraw_tokens(self, cred:Credentials, _token_address:address, _recipient:address, _amount:uint256) -> TxReceipt:
        tx = self.contract.functions.withdrawTokens(_token_address, _recipient, _amount)
        return self.send_transaction(tx, cred)