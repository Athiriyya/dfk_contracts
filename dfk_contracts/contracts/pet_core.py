
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xAC9AFb5900C8A27B766bCad3A37423DC0F4C22d3",
    "sd": "0x6362b205b539afb5FC369277365441c1dC6fAa28"
}

ABI = """[
    {"name": "Approval", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "approved", "type": "address", "indexed": true, "internalType": "address"}, {"name": "tokenId", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "ApprovalForAll", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "operator", "type": "address", "indexed": true, "internalType": "address"}, {"name": "approved", "type": "bool", "indexed": false, "internalType": "bool"}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "PetHatched", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "petId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "pet", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "originId", "type": "uint8", "internalType": "uint8"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "season", "type": "uint8", "internalType": "uint8"}, {"name": "eggType", "type": "uint8", "internalType": "uint8"}, {"name": "rarity", "type": "uint8", "internalType": "uint8"}, {"name": "element", "type": "uint8", "internalType": "uint8"}, {"name": "bonusCount", "type": "uint8", "internalType": "uint8"}, {"name": "profBonus", "type": "uint8", "internalType": "uint8"}, {"name": "profBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "craftBonus", "type": "uint8", "internalType": "uint8"}, {"name": "craftBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "combatBonus", "type": "uint8", "internalType": "uint8"}, {"name": "combatBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "appearance", "type": "uint16", "internalType": "uint16"}, {"name": "background", "type": "uint8", "internalType": "uint8"}, {"name": "shiny", "type": "uint8", "internalType": "uint8"}, {"name": "hungryAt", "type": "uint64", "internalType": "uint64"}, {"name": "equippableAt", "type": "uint64", "internalType": "uint64"}, {"name": "equippedTo", "type": "uint256", "internalType": "uint256"}], "indexed": false, "internalType": "struct Pet"}], "anonymous": false},
    {"name": "PetUpdated", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "petId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "pet", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "originId", "type": "uint8", "internalType": "uint8"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "season", "type": "uint8", "internalType": "uint8"}, {"name": "eggType", "type": "uint8", "internalType": "uint8"}, {"name": "rarity", "type": "uint8", "internalType": "uint8"}, {"name": "element", "type": "uint8", "internalType": "uint8"}, {"name": "bonusCount", "type": "uint8", "internalType": "uint8"}, {"name": "profBonus", "type": "uint8", "internalType": "uint8"}, {"name": "profBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "craftBonus", "type": "uint8", "internalType": "uint8"}, {"name": "craftBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "combatBonus", "type": "uint8", "internalType": "uint8"}, {"name": "combatBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "appearance", "type": "uint16", "internalType": "uint16"}, {"name": "background", "type": "uint8", "internalType": "uint8"}, {"name": "shiny", "type": "uint8", "internalType": "uint8"}, {"name": "hungryAt", "type": "uint64", "internalType": "uint64"}, {"name": "equippableAt", "type": "uint64", "internalType": "uint64"}, {"name": "equippedTo", "type": "uint256", "internalType": "uint256"}], "indexed": false, "internalType": "struct Pet"}], "anonymous": false},
    {"name": "Transfer", "type": "event", "inputs": [{"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "tokenId", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "approve", "type": "function", "inputs": [{"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "balanceOf", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "bridgeMint", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}, {"name": "_to", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getApproved", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "getPet", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "originId", "type": "uint8", "internalType": "uint8"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "season", "type": "uint8", "internalType": "uint8"}, {"name": "eggType", "type": "uint8", "internalType": "uint8"}, {"name": "rarity", "type": "uint8", "internalType": "uint8"}, {"name": "element", "type": "uint8", "internalType": "uint8"}, {"name": "bonusCount", "type": "uint8", "internalType": "uint8"}, {"name": "profBonus", "type": "uint8", "internalType": "uint8"}, {"name": "profBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "craftBonus", "type": "uint8", "internalType": "uint8"}, {"name": "craftBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "combatBonus", "type": "uint8", "internalType": "uint8"}, {"name": "combatBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "appearance", "type": "uint16", "internalType": "uint16"}, {"name": "background", "type": "uint8", "internalType": "uint8"}, {"name": "shiny", "type": "uint8", "internalType": "uint8"}, {"name": "hungryAt", "type": "uint64", "internalType": "uint64"}, {"name": "equippableAt", "type": "uint64", "internalType": "uint64"}, {"name": "equippedTo", "type": "uint256", "internalType": "uint256"}], "internalType": "struct Pet"}], "stateMutability": "view"},
    {"name": "getUserPets", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "originId", "type": "uint8", "internalType": "uint8"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "season", "type": "uint8", "internalType": "uint8"}, {"name": "eggType", "type": "uint8", "internalType": "uint8"}, {"name": "rarity", "type": "uint8", "internalType": "uint8"}, {"name": "element", "type": "uint8", "internalType": "uint8"}, {"name": "bonusCount", "type": "uint8", "internalType": "uint8"}, {"name": "profBonus", "type": "uint8", "internalType": "uint8"}, {"name": "profBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "craftBonus", "type": "uint8", "internalType": "uint8"}, {"name": "craftBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "combatBonus", "type": "uint8", "internalType": "uint8"}, {"name": "combatBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "appearance", "type": "uint16", "internalType": "uint16"}, {"name": "background", "type": "uint8", "internalType": "uint8"}, {"name": "shiny", "type": "uint8", "internalType": "uint8"}, {"name": "hungryAt", "type": "uint64", "internalType": "uint64"}, {"name": "equippableAt", "type": "uint64", "internalType": "uint64"}, {"name": "equippedTo", "type": "uint256", "internalType": "uint256"}], "internalType": "struct Pet[]"}], "stateMutability": "view"},
    {"name": "hatchPet", "type": "function", "inputs": [{"name": "_petOptions", "type": "tuple", "components": [{"name": "originId", "type": "uint8", "internalType": "uint8"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "season", "type": "uint8", "internalType": "uint8"}, {"name": "eggType", "type": "uint8", "internalType": "uint8"}, {"name": "rarity", "type": "uint8", "internalType": "uint8"}, {"name": "element", "type": "uint8", "internalType": "uint8"}, {"name": "bonusCount", "type": "uint8", "internalType": "uint8"}, {"name": "profBonus", "type": "uint8", "internalType": "uint8"}, {"name": "profBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "craftBonus", "type": "uint8", "internalType": "uint8"}, {"name": "craftBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "combatBonus", "type": "uint8", "internalType": "uint8"}, {"name": "combatBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "appearance", "type": "uint16", "internalType": "uint16"}, {"name": "background", "type": "uint8", "internalType": "uint8"}, {"name": "shiny", "type": "uint8", "internalType": "uint8"}], "internalType": "struct PetOptions"}, {"name": "owner", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_name", "type": "string", "internalType": "string"}, {"name": "_symbol", "type": "string", "internalType": "string"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "isApprovedForAll", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "operator", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "name", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "nextPetId", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "ownerOf", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "safeTransferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "safeTransferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}, {"name": "_data", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setApprovalForAll", "type": "function", "inputs": [{"name": "operator", "type": "address", "internalType": "address"}, {"name": "approved", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "symbol", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "tokenByIndex", "type": "function", "inputs": [{"name": "index", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "tokenOfOwnerByIndex", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "index", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "tokenURI", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "totalSupply", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "transferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "updatePet", "type": "function", "inputs": [{"name": "_pet", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "originId", "type": "uint8", "internalType": "uint8"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "season", "type": "uint8", "internalType": "uint8"}, {"name": "eggType", "type": "uint8", "internalType": "uint8"}, {"name": "rarity", "type": "uint8", "internalType": "uint8"}, {"name": "element", "type": "uint8", "internalType": "uint8"}, {"name": "bonusCount", "type": "uint8", "internalType": "uint8"}, {"name": "profBonus", "type": "uint8", "internalType": "uint8"}, {"name": "profBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "craftBonus", "type": "uint8", "internalType": "uint8"}, {"name": "craftBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "combatBonus", "type": "uint8", "internalType": "uint8"}, {"name": "combatBonusScalar", "type": "uint8", "internalType": "uint8"}, {"name": "appearance", "type": "uint16", "internalType": "uint16"}, {"name": "background", "type": "uint8", "internalType": "uint8"}, {"name": "shiny", "type": "uint8", "internalType": "uint8"}, {"name": "hungryAt", "type": "uint64", "internalType": "uint64"}, {"name": "equippableAt", "type": "uint64", "internalType": "uint64"}, {"name": "equippedTo", "type": "uint256", "internalType": "uint256"}], "internalType": "struct Pet"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class PetCore(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def approve(self, cred:Credentials, to:address, token_id:uint256) -> TxReceipt:
        tx = self.contract.functions.approve(to, token_id)
        return self.send_transaction(tx, cred)

    def balance_of(self, owner:address) -> uint256:
        return self.contract.functions.balanceOf(owner).call()

    def bridge_mint(self, cred:Credentials, _id:uint256, _to:address) -> TxReceipt:
        tx = self.contract.functions.bridgeMint(_id, _to)
        return self.send_transaction(tx, cred)

    def get_approved(self, token_id:uint256) -> address:
        return self.contract.functions.getApproved(token_id).call()

    def get_pet(self, _id:uint256) -> tuple:
        return self.contract.functions.getPet(_id).call()

    def get_user_pets(self, _address:address) -> Sequence[tuple]:
        return self.contract.functions.getUserPets(_address).call()

    def hatch_pet(self, cred:Credentials, _pet_options:tuple, owner:address) -> TxReceipt:
        tx = self.contract.functions.hatchPet(_pet_options, owner)
        return self.send_transaction(tx, cred)

    def initialize(self, cred:Credentials, _name:string, _symbol:string) -> TxReceipt:
        tx = self.contract.functions.initialize(_name, _symbol)
        return self.send_transaction(tx, cred)

    def is_approved_for_all(self, owner:address, operator:address) -> bool:
        return self.contract.functions.isApprovedForAll(owner, operator).call()

    def name(self) -> string:
        return self.contract.functions.name().call()

    def next_pet_id(self) -> uint256:
        return self.contract.functions.nextPetId().call()

    def owner_of(self, token_id:uint256) -> address:
        return self.contract.functions.ownerOf(token_id).call()

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
        return self.send_transaction(tx, cred)

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def safe_transfer_from(self, cred:Credentials, _from:address, to:address, token_id:uint256) -> TxReceipt:
        tx = self.contract.functions.safeTransferFrom(_from, to, token_id)
        return self.send_transaction(tx, cred)

    def safe_transfer_from(self, cred:Credentials, _from:address, to:address, token_id:uint256, _data:bytes) -> TxReceipt:
        tx = self.contract.functions.safeTransferFrom(_from, to, token_id, _data)
        return self.send_transaction(tx, cred)

    def set_approval_for_all(self, cred:Credentials, operator:address, approved:bool) -> TxReceipt:
        tx = self.contract.functions.setApprovalForAll(operator, approved)
        return self.send_transaction(tx, cred)

    def symbol(self) -> string:
        return self.contract.functions.symbol().call()

    def token_by_index(self, index:uint256) -> uint256:
        return self.contract.functions.tokenByIndex(index).call()

    def token_of_owner_by_index(self, owner:address, index:uint256) -> uint256:
        return self.contract.functions.tokenOfOwnerByIndex(owner, index).call()

    def token_uri(self, token_id:uint256) -> string:
        return self.contract.functions.tokenURI(token_id).call()

    def total_supply(self) -> uint256:
        return self.contract.functions.totalSupply().call()

    def transfer_from(self, cred:Credentials, _from:address, to:address, token_id:uint256) -> TxReceipt:
        tx = self.contract.functions.transferFrom(_from, to, token_id)
        return self.send_transaction(tx, cred)

    def unpause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unpause()
        return self.send_transaction(tx, cred)

    def update_pet(self, cred:Credentials, _pet:tuple) -> TxReceipt:
        tx = self.contract.functions.updatePet(_pet)
        return self.send_transaction(tx, cred)