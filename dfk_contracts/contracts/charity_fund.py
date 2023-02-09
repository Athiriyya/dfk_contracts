
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xABABB0A2c42274D0e81417B824CABca464F5c16C",
    "sd": ""
}

ABI = """[
    {"name": "Donation", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": true, "internalType": "address"}, {"name": "token", "type": "address", "indexed": true, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "OwnershipTransferred", "type": "event", "inputs": [{"name": "previousOwner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "newOwner", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "Withdrawal", "type": "event", "inputs": [{"name": "token", "type": "address", "indexed": true, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"type": "fallback", "stateMutability": "payable"},
    {"name": "accepted", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "addToken", "type": "function", "inputs": [{"name": "_token", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "campaignId", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "disableToken", "type": "function", "inputs": [{"name": "_token", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "donateNativeToken", "type": "function", "inputs": [], "outputs": [], "stateMutability": "payable"},
    {"name": "donateToken", "type": "function", "inputs": [{"name": "_token", "type": "address", "internalType": "address"}, {"name": "_wei", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "donationTotals", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "enableToken", "type": "function", "inputs": [{"name": "_token", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getInfo", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "accepted", "type": "bool", "internalType": "bool"}, {"name": "token", "type": "address", "internalType": "address"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "symbol", "type": "string", "internalType": "string"}, {"name": "decimals", "type": "uint256", "internalType": "uint256"}, {"name": "total", "type": "uint256", "internalType": "uint256"}, {"name": "balance", "type": "uint256", "internalType": "uint256"}, {"name": "userDonation", "type": "uint256", "internalType": "uint256"}, {"name": "campaignDonationHistory", "type": "uint256", "internalType": "uint256"}], "internalType": "struct Structs.Info[]"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_multisig", "type": "address", "internalType": "address"}, {"name": "_flagStorageAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "multisig", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "owner", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "renounceOwnership", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setCampaignId", "type": "function", "inputs": [{"name": "_campaignId", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "tokens", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "transferOwnership", "type": "function", "inputs": [{"name": "newOwner", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "withdraw", "type": "function", "inputs": [{"name": "_token", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "withdrawAll", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "withdrawNative", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"type": "receive", "stateMutability": "payable"}
]
"""     

class CharityFund(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def accepted(self, a:address) -> bool:
        return self.contract.functions.accepted(a).call()

    def add_token(self, cred:Credentials, _token:address) -> TxReceipt:
        tx = self.contract.functions.addToken(_token)
        return self.send_transaction(tx, cred)

    def campaign_id(self) -> uint8:
        return self.contract.functions.campaignId().call()

    def disable_token(self, cred:Credentials, _token:address) -> TxReceipt:
        tx = self.contract.functions.disableToken(_token)
        return self.send_transaction(tx, cred)

    def donate_native_token(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.donateNativeToken()
        return self.send_transaction(tx, cred)

    def donate_token(self, cred:Credentials, _token:address, _wei:uint256) -> TxReceipt:
        tx = self.contract.functions.donateToken(_token, _wei)
        return self.send_transaction(tx, cred)

    def donation_totals(self, a:address) -> uint256:
        return self.contract.functions.donationTotals(a).call()

    def enable_token(self, cred:Credentials, _token:address) -> TxReceipt:
        tx = self.contract.functions.enableToken(_token)
        return self.send_transaction(tx, cred)

    def get_info(self) -> Sequence[tuple]:
        return self.contract.functions.getInfo().call()

    def initialize(self, cred:Credentials, _multisig:address, _flag_storage_address:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_multisig, _flag_storage_address)
        return self.send_transaction(tx, cred)

    def multisig(self) -> address:
        return self.contract.functions.multisig().call()

    def owner(self) -> address:
        return self.contract.functions.owner().call()

    def renounce_ownership(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.renounceOwnership()
        return self.send_transaction(tx, cred)

    def set_campaign_id(self, cred:Credentials, _campaign_id:uint8) -> TxReceipt:
        tx = self.contract.functions.setCampaignId(_campaign_id)
        return self.send_transaction(tx, cred)

    def tokens(self, a:uint256) -> address:
        return self.contract.functions.tokens(a).call()

    def transfer_ownership(self, cred:Credentials, new_owner:address) -> TxReceipt:
        tx = self.contract.functions.transferOwnership(new_owner)
        return self.send_transaction(tx, cred)

    def withdraw(self, cred:Credentials, _token:address) -> TxReceipt:
        tx = self.contract.functions.withdraw(_token)
        return self.send_transaction(tx, cred)

    def withdraw_all(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.withdrawAll()
        return self.send_transaction(tx, cred)

    def withdraw_native(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.withdrawNative()
        return self.send_transaction(tx, cred)