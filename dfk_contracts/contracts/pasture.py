
from ..abi_contract_wrapper import ABIContractWrapper
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xE959cbddB8616BDFFa5464279664CCbb9EA10317",
    "sd": "0x4aBb1cDe7a0C55850495E80E1806993b1B92F742"
}

ABI = """[
    {"type": "constructor", "inputs": [{"name": "_petCore", "type": "address", "internalType": "address"}], "stateMutability": "nonpayable"},
    {"name": "PetReleased", "type": "event", "inputs": [{"name": "petId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "releaseReason", "type": "string", "indexed": true, "internalType": "string"}, {"name": "releaseTime", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "getProfileReleasedPet", "type": "function", "inputs": [{"name": "_profile", "type": "address", "internalType": "address"}, {"name": "_index", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "petId", "type": "uint256", "internalType": "uint256"}, {"name": "releaseTime", "type": "uint64", "internalType": "uint64"}, {"name": "releaseReason", "type": "string", "internalType": "string"}, {"name": "previousOwner", "type": "address", "internalType": "address"}], "internalType": "struct ReleasedPet"}], "stateMutability": "view"},
    {"name": "getProfileReleasedPets", "type": "function", "inputs": [{"name": "_profile", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "petId", "type": "uint256", "internalType": "uint256"}, {"name": "releaseTime", "type": "uint64", "internalType": "uint64"}, {"name": "releaseReason", "type": "string", "internalType": "string"}, {"name": "previousOwner", "type": "address", "internalType": "address"}], "internalType": "struct ReleasedPet[]"}], "stateMutability": "view"},
    {"name": "getReleasedPet", "type": "function", "inputs": [{"name": "_petId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "petId", "type": "uint256", "internalType": "uint256"}, {"name": "releaseTime", "type": "uint64", "internalType": "uint64"}, {"name": "releaseReason", "type": "string", "internalType": "string"}, {"name": "previousOwner", "type": "address", "internalType": "address"}], "internalType": "struct ReleasedPet"}], "stateMutability": "view"},
    {"name": "getReleasedPets", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "petId", "type": "uint256", "internalType": "uint256"}, {"name": "releaseTime", "type": "uint64", "internalType": "uint64"}, {"name": "releaseReason", "type": "string", "internalType": "string"}, {"name": "previousOwner", "type": "address", "internalType": "address"}], "internalType": "struct ReleasedPet[]"}], "stateMutability": "view"},
    {"name": "petCore", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IPetCore"}], "stateMutability": "view"},
    {"name": "petToReleasedPet", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "profileReleasedPets", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "petId", "type": "uint256", "internalType": "uint256"}, {"name": "releaseTime", "type": "uint64", "internalType": "uint64"}, {"name": "releaseReason", "type": "string", "internalType": "string"}, {"name": "previousOwner", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "releasePet", "type": "function", "inputs": [{"name": "_holder", "type": "address", "internalType": "address"}, {"name": "_petId", "type": "uint256", "internalType": "uint256"}, {"name": "_releaseReason", "type": "string", "internalType": "string"}, {"name": "_previousOwner", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "releasedPets", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "petId", "type": "uint256", "internalType": "uint256"}, {"name": "releaseTime", "type": "uint64", "internalType": "uint64"}, {"name": "releaseReason", "type": "string", "internalType": "string"}, {"name": "previousOwner", "type": "address", "internalType": "address"}], "stateMutability": "view"}
]
"""     

class Pasture(ABIContractWrapper):
    def __init__(self, chain_key:str, rpc:str):
        contract_address = CONTRACT_ADDRESS[chain_key]
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def get_profile_released_pet(self, _profile:address, _index:uint256, block_identifier:BlockIdentifier = 'latest') -> tuple:
        return self.contract.functions.getProfileReleasedPet(_profile, _index).call(block_identifier=block_identifier)

    def get_profile_released_pets(self, _profile:address, block_identifier:BlockIdentifier = 'latest') -> List[tuple]:
        return self.contract.functions.getProfileReleasedPets(_profile).call(block_identifier=block_identifier)

    def get_released_pet(self, _pet_id:uint256, block_identifier:BlockIdentifier = 'latest') -> tuple:
        return self.contract.functions.getReleasedPet(_pet_id).call(block_identifier=block_identifier)

    def get_released_pets(self, block_identifier:BlockIdentifier = 'latest') -> List[tuple]:
        return self.contract.functions.getReleasedPets().call(block_identifier=block_identifier)

    def pet_core(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.petCore().call(block_identifier=block_identifier)

    def pet_to_released_pet(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.petToReleasedPet(a).call(block_identifier=block_identifier)

    def profile_released_pets(self, a:address, b:uint256, block_identifier:BlockIdentifier = 'latest') -> Tuple[uint256, uint256, uint64, string, address]:
        return self.contract.functions.profileReleasedPets(a, b).call(block_identifier=block_identifier)

    def release_pet(self, cred:Credentials, _holder:address, _pet_id:uint256, _release_reason:string, _previous_owner:address) -> TxReceipt:
        tx = self.contract.functions.releasePet(_holder, _pet_id, _release_reason, _previous_owner)
        return self.send_transaction(tx, cred)

    def released_pets(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> Tuple[uint256, uint256, uint64, string, address]:
        return self.contract.functions.releasedPets(a).call(block_identifier=block_identifier)