
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x8f1CeD3ABa6893E65DE59452C466B2CBb7Cd690b",
    "sd": "0x2dB164A65BB10BBbde7Aa441EAfDAED67AbE08EE"
}

ABI = """[
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "NameChange", "type": "event", "inputs": [{"name": "profileAddress", "type": "address", "indexed": false, "internalType": "address"}, {"name": "oldName", "type": "string", "indexed": false, "internalType": "string"}, {"name": "newName", "type": "string", "indexed": false, "internalType": "string"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "PicChange", "type": "event", "inputs": [{"name": "profileAddress", "type": "address", "indexed": false, "internalType": "address"}, {"name": "nftId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "collectionId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "changeName", "type": "function", "inputs": [{"name": "_name", "type": "string", "internalType": "string"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "changePic", "type": "function", "inputs": [{"name": "_nftId", "type": "uint256", "internalType": "uint256"}, {"name": "_collectionId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_profilesAddress", "type": "address", "internalType": "address"}, {"name": "_jewelTokenAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "jewelToken", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IJewelToken"}], "stateMutability": "view"},
    {"name": "nameChangeFee", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "picChangeFee", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "profilesContract", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IProfiles"}], "stateMutability": "view"},
    {"name": "setFees", "type": "function", "inputs": [{"name": "_feeAddresses", "type": "address[]", "internalType": "address[]"}, {"name": "_feePercents", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setNameChangeFee", "type": "function", "inputs": [{"name": "_fee", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setPicChangeFee", "type": "function", "inputs": [{"name": "_fee", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "togglePause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class Stylist(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def change_name(self, cred:Credentials, _name:string) -> TxReceipt:
        tx = self.contract.functions.changeName(_name)
        return self.send_transaction(tx, cred)

    def change_pic(self, cred:Credentials, _nft_id:uint256, _collection_id:uint256) -> TxReceipt:
        tx = self.contract.functions.changePic(_nft_id, _collection_id)
        return self.send_transaction(tx, cred)

    def initialize(self, cred:Credentials, _profiles_address:address, _jewel_token_address:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_profiles_address, _jewel_token_address)
        return self.send_transaction(tx, cred)

    def jewel_token(self) -> address:
        return self.contract.functions.jewelToken().call()

    def name_change_fee(self) -> uint256:
        return self.contract.functions.nameChangeFee().call()

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def pic_change_fee(self) -> uint256:
        return self.contract.functions.picChangeFee().call()

    def profiles_contract(self) -> address:
        return self.contract.functions.profilesContract().call()

    def set_fees(self, cred:Credentials, _fee_addresses:Sequence[address], _fee_percents:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.setFees(_fee_addresses, _fee_percents)
        return self.send_transaction(tx, cred)

    def set_name_change_fee(self, cred:Credentials, _fee:uint256) -> TxReceipt:
        tx = self.contract.functions.setNameChangeFee(_fee)
        return self.send_transaction(tx, cred)

    def set_pic_change_fee(self, cred:Credentials, _fee:uint256) -> TxReceipt:
        tx = self.contract.functions.setPicChangeFee(_fee)
        return self.send_transaction(tx, cred)

    def toggle_pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.togglePause()
        return self.send_transaction(tx, cred)