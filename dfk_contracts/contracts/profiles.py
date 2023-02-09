
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x6391F796D56201D279a42fD3141aDa7e26A3B4A5",
    "sd": "0xe1b8C354BE50357c2ab90A962254526d08aF0D2D"
}

ABI = """[
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "ProfileCreated", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": false, "internalType": "address"}, {"name": "name", "type": "string", "indexed": false, "internalType": "string"}, {"name": "created", "type": "uint64", "indexed": false, "internalType": "uint64"}, {"name": "nftId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "collectionId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "ProfileUpdated", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": false, "internalType": "address"}, {"name": "name", "type": "string", "indexed": false, "internalType": "string"}, {"name": "nftId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "collectionId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "MAX_CHAR", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "MAX_PIC", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "MIN_CHAR", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "addressToProfile", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "created", "type": "uint64", "internalType": "uint64"}, {"name": "nftId", "type": "uint256", "internalType": "uint256"}, {"name": "collectionId", "type": "uint256", "internalType": "uint256"}, {"name": "picUri", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "adminCreateProfile", "type": "function", "inputs": [{"name": "_owner", "type": "address", "internalType": "address"}, {"name": "_name", "type": "string", "internalType": "string"}, {"name": "_created", "type": "uint64", "internalType": "uint64"}, {"name": "_nftId", "type": "uint256", "internalType": "uint256"}, {"name": "_collectionId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "batchSetPicURI", "type": "function", "inputs": [{"name": "_uriArray", "type": "string[]", "internalType": "string[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "changeName", "type": "function", "inputs": [{"name": "_profileAddress", "type": "address", "internalType": "address"}, {"name": "_name", "type": "string", "internalType": "string"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "changePic", "type": "function", "inputs": [{"name": "_profileAddress", "type": "address", "internalType": "address"}, {"name": "_nftId", "type": "uint256", "internalType": "uint256"}, {"name": "_collectionId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "createProfile", "type": "function", "inputs": [{"name": "_name", "type": "string", "internalType": "string"}, {"name": "_nftId", "type": "uint256", "internalType": "uint256"}, {"name": "_collectionId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getProfile", "type": "function", "inputs": [{"name": "_profileAddress", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "created", "type": "uint64", "internalType": "uint64"}, {"name": "nftId", "type": "uint256", "internalType": "uint256"}, {"name": "collectionId", "type": "uint256", "internalType": "uint256"}, {"name": "picUri", "type": "string", "internalType": "string"}], "internalType": "struct ProfileTypes.Profile"}], "stateMutability": "view"},
    {"name": "getProfileByAddress", "type": "function", "inputs": [{"name": "_profileAddress", "type": "address", "internalType": "address"}], "outputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}, {"name": "_owner", "type": "address", "internalType": "address"}, {"name": "_name", "type": "string", "internalType": "string"}, {"name": "_created", "type": "uint64", "internalType": "uint64"}, {"name": "_picId", "type": "uint8", "internalType": "uint8"}, {"name": "_heroId", "type": "uint256", "internalType": "uint256"}, {"name": "_points", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getProfileByName", "type": "function", "inputs": [{"name": "_name", "type": "string", "internalType": "string"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "created", "type": "uint64", "internalType": "uint64"}, {"name": "nftId", "type": "uint256", "internalType": "uint256"}, {"name": "collectionId", "type": "uint256", "internalType": "uint256"}, {"name": "picUri", "type": "string", "internalType": "string"}], "internalType": "struct ProfileTypes.Profile"}], "stateMutability": "view"},
    {"name": "getTokenUrisHeldByAddress", "type": "function", "inputs": [{"name": "_profileAddress", "type": "address", "internalType": "address"}, {"name": "_collectionId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "string[]", "internalType": "string[]"}], "stateMutability": "view"},
    {"name": "heroesNftContract", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IHeroCore"}], "stateMutability": "view"},
    {"name": "identityTokenRouter", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IIdentityTokenRouter"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_heroCoreAddress", "type": "address", "internalType": "address"}, {"name": "_identityTokenRouter", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "maxChar", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "maxPic", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "minChar", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "nameToAddress", "type": "function", "inputs": [{"name": "", "type": "string", "internalType": "string"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "picUris", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "setHeroes", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setIdentityTokenRouter", "type": "function", "inputs": [{"name": "_identityTokenRouter", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setNameLengths", "type": "function", "inputs": [{"name": "_min", "type": "uint8", "internalType": "uint8"}, {"name": "_max", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setPicMax", "type": "function", "inputs": [{"name": "_max", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setPicURI", "type": "function", "inputs": [{"name": "_picId", "type": "uint256", "internalType": "uint256"}, {"name": "_picUri", "type": "string", "internalType": "string"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class Profiles(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def max_char(self) -> uint8:
        return self.contract.functions.MAX_CHAR().call()

    def max_pic(self) -> uint8:
        return self.contract.functions.MAX_PIC().call()

    def min_char(self) -> uint8:
        return self.contract.functions.MIN_CHAR().call()

    def address_to_profile(self, a:address) -> Tuple[address, string, uint64, uint256, uint256, string]:
        return self.contract.functions.addressToProfile(a).call()

    def admin_create_profile(self, cred:Credentials, _owner:address, _name:string, _created:uint64, _nft_id:uint256, _collection_id:uint256) -> TxReceipt:
        tx = self.contract.functions.adminCreateProfile(_owner, _name, _created, _nft_id, _collection_id)
        return self.send_transaction(tx, cred)

    def batch_set_pic_uri(self, cred:Credentials, _uri_array:Sequence[string]) -> TxReceipt:
        tx = self.contract.functions.batchSetPicURI(_uri_array)
        return self.send_transaction(tx, cred)

    def change_name(self, cred:Credentials, _profile_address:address, _name:string) -> TxReceipt:
        tx = self.contract.functions.changeName(_profile_address, _name)
        return self.send_transaction(tx, cred)

    def change_pic(self, cred:Credentials, _profile_address:address, _nft_id:uint256, _collection_id:uint256) -> TxReceipt:
        tx = self.contract.functions.changePic(_profile_address, _nft_id, _collection_id)
        return self.send_transaction(tx, cred)

    def create_profile(self, cred:Credentials, _name:string, _nft_id:uint256, _collection_id:uint256) -> TxReceipt:
        tx = self.contract.functions.createProfile(_name, _nft_id, _collection_id)
        return self.send_transaction(tx, cred)

    def get_profile(self, _profile_address:address) -> tuple:
        return self.contract.functions.getProfile(_profile_address).call()

    def get_profile_by_address(self, _profile_address:address) -> Tuple[uint256, address, string, uint64, uint8, uint256, uint256]:
        return self.contract.functions.getProfileByAddress(_profile_address).call()

    def get_profile_by_name(self, _name:string) -> tuple:
        return self.contract.functions.getProfileByName(_name).call()

    def get_token_uris_held_by_address(self, _profile_address:address, _collection_id:uint256) -> Sequence[string]:
        return self.contract.functions.getTokenUrisHeldByAddress(_profile_address, _collection_id).call()

    def heroes_nft_contract(self) -> address:
        return self.contract.functions.heroesNftContract().call()

    def identity_token_router(self) -> address:
        return self.contract.functions.identityTokenRouter().call()

    def initialize(self, cred:Credentials, _hero_core_address:address, _identity_token_router:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_hero_core_address, _identity_token_router)
        return self.send_transaction(tx, cred)

    def max_char(self) -> uint8:
        return self.contract.functions.maxChar().call()

    def max_pic(self) -> uint8:
        return self.contract.functions.maxPic().call()

    def min_char(self) -> uint8:
        return self.contract.functions.minChar().call()

    def name_to_address(self, a:string) -> address:
        return self.contract.functions.nameToAddress(a).call()

    def pic_uris(self, a:uint256) -> string:
        return self.contract.functions.picUris(a).call()

    def set_heroes(self, cred:Credentials, _address:address) -> TxReceipt:
        tx = self.contract.functions.setHeroes(_address)
        return self.send_transaction(tx, cred)

    def set_identity_token_router(self, cred:Credentials, _identity_token_router:address) -> TxReceipt:
        tx = self.contract.functions.setIdentityTokenRouter(_identity_token_router)
        return self.send_transaction(tx, cred)

    def set_name_lengths(self, cred:Credentials, _min:uint8, _max:uint8) -> TxReceipt:
        tx = self.contract.functions.setNameLengths(_min, _max)
        return self.send_transaction(tx, cred)

    def set_pic_max(self, cred:Credentials, _max:uint8) -> TxReceipt:
        tx = self.contract.functions.setPicMax(_max)
        return self.send_transaction(tx, cred)

    def set_pic_uri(self, cred:Credentials, _pic_id:uint256, _pic_uri:string) -> TxReceipt:
        tx = self.contract.functions.setPicURI(_pic_id, _pic_uri)
        return self.send_transaction(tx, cred)