
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xeaF833A0Ae97897f6F69a728C9c17916296cecCA",
    "sd": "0xe5D563F7e4144955FCFa8b90da45825426a05bD4"
}

ABI = """[
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "PetExchangeCompleted", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "eggId1", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "eggId2", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "eggTypeRecieved", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "PetExchangeStarted", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "eggId1", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "eggId2", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "completeExchange", "type": "function", "inputs": [{"name": "_exchangeId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "eggs", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "getPetExchange", "type": "function", "inputs": [{"name": "_exchangeId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "owner", "type": "address", "internalType": "address"}, {"name": "petId1", "type": "uint256", "internalType": "uint256"}, {"name": "petId2", "type": "uint256", "internalType": "uint256"}, {"name": "seedblock", "type": "uint256", "internalType": "uint256"}, {"name": "finishTime", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "enum PetExchangeStatus"}], "internalType": "struct PetExchangeData"}], "stateMutability": "view"},
    {"name": "getUserPetExchanges", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "owner", "type": "address", "internalType": "address"}, {"name": "petId1", "type": "uint256", "internalType": "uint256"}, {"name": "petId2", "type": "uint256", "internalType": "uint256"}, {"name": "seedblock", "type": "uint256", "internalType": "uint256"}, {"name": "finishTime", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "enum PetExchangeStatus"}], "internalType": "struct PetExchangeData[]"}], "stateMutability": "view"},
    {"name": "idToPetExchange", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "owner", "type": "address", "internalType": "address"}, {"name": "petId1", "type": "uint256", "internalType": "uint256"}, {"name": "petId2", "type": "uint256", "internalType": "uint256"}, {"name": "seedblock", "type": "uint256", "internalType": "uint256"}, {"name": "finishTime", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "enum PetExchangeStatus"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_petCoreAddress", "type": "address", "internalType": "address"}, {"name": "_pastureAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "profileExchangedPets", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "owner", "type": "address", "internalType": "address"}, {"name": "petId1", "type": "uint256", "internalType": "uint256"}, {"name": "petId2", "type": "uint256", "internalType": "uint256"}, {"name": "seedblock", "type": "uint256", "internalType": "uint256"}, {"name": "finishTime", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "enum PetExchangeStatus"}], "stateMutability": "view"},
    {"name": "setEgg", "type": "function", "inputs": [{"name": "_index", "type": "uint8", "internalType": "uint8"}, {"name": "_eggAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setPasture", "type": "function", "inputs": [{"name": "_pastureAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setPetCore", "type": "function", "inputs": [{"name": "_petCoreAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "startExchange", "type": "function", "inputs": [{"name": "_petId1", "type": "uint256", "internalType": "uint256"}, {"name": "_petId2", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "totalExchanges", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class PetExchange(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def complete_exchange(self, cred:Credentials, _exchange_id:uint256) -> TxReceipt:
        tx = self.contract.functions.completeExchange(_exchange_id)
        return self.send_transaction(tx, cred)

    def eggs(self, a:uint256) -> address:
        return self.contract.functions.eggs(a).call()

    def get_pet_exchange(self, _exchange_id:uint256) -> tuple:
        return self.contract.functions.getPetExchange(_exchange_id).call()

    def get_user_pet_exchanges(self, _address:address) -> Sequence[tuple]:
        return self.contract.functions.getUserPetExchanges(_address).call()

    def id_to_pet_exchange(self, a:uint256) -> Tuple[uint256, address, uint256, uint256, uint256, uint256, uint8]:
        return self.contract.functions.idToPetExchange(a).call()

    def initialize(self, cred:Credentials, _pet_core_address:address, _pasture_address:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_pet_core_address, _pasture_address)
        return self.send_transaction(tx, cred)

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
        return self.send_transaction(tx, cred)

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def profile_exchanged_pets(self, a:address, b:uint256) -> Tuple[uint256, address, uint256, uint256, uint256, uint256, uint8]:
        return self.contract.functions.profileExchangedPets(a, b).call()

    def set_egg(self, cred:Credentials, _index:uint8, _egg_address:address) -> TxReceipt:
        tx = self.contract.functions.setEgg(_index, _egg_address)
        return self.send_transaction(tx, cred)

    def set_pasture(self, cred:Credentials, _pasture_address:address) -> TxReceipt:
        tx = self.contract.functions.setPasture(_pasture_address)
        return self.send_transaction(tx, cred)

    def set_pet_core(self, cred:Credentials, _pet_core_address:address) -> TxReceipt:
        tx = self.contract.functions.setPetCore(_pet_core_address)
        return self.send_transaction(tx, cred)

    def start_exchange(self, cred:Credentials, _pet_id1:uint256, _pet_id2:uint256) -> TxReceipt:
        tx = self.contract.functions.startExchange(_pet_id1, _pet_id2)
        return self.send_transaction(tx, cred)

    def total_exchanges(self) -> uint256:
        return self.contract.functions.totalExchanges().call()

    def unpause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unpause()
        return self.send_transaction(tx, cred)