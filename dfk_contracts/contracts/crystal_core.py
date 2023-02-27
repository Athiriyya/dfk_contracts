
from ..abi_contract_wrapper import ABIContractWrapper
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x68f6C64786cfCb35108986041D1009c9d27bde22",
    "sd": "0x13cE9c99E8E2fcDe1632adA7B69b2eCf5BE8ED45"
}

ABI = """[
    {"name": "CrystalAirdrop", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "crystalId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "createdBlock", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "CrystalOpen", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "crystalId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "CrystalSummoned", "type": "event", "inputs": [{"name": "crystalId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "summonerId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "generation", "type": "uint16", "indexed": false, "internalType": "uint16"}, {"name": "createdBlock", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "summonerTears", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "assistantTears", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "enhancementStone", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "EnhancementStoneAdded", "type": "event", "inputs": [{"name": "atunementItemAddress", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "RoleAdminChanged", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "previousAdminRole", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "newAdminRole", "type": "bytes32", "indexed": true, "internalType": "bytes32"}], "anonymous": false},
    {"name": "RoleGranted", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "account", "type": "address", "indexed": true, "internalType": "address"}, {"name": "sender", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "RoleRevoked", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "account", "type": "address", "indexed": true, "internalType": "address"}, {"name": "sender", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "CRYSTAL_MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "DEFAULT_ADMIN_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "airdropCrystal", "type": "function", "inputs": [{"name": "_recipient", "type": "address", "internalType": "address"}, {"name": "_isShiny", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "createCrystal", "type": "function", "inputs": [{"name": "_owner", "type": "address", "internalType": "address"}, {"name": "_summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "_assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "_generation", "type": "uint16", "internalType": "uint16"}, {"name": "_summonerBonusTears", "type": "uint8", "internalType": "uint8"}, {"name": "_assistantBonusTears", "type": "uint8", "internalType": "uint8"}, {"name": "_enhancementStone", "type": "address", "internalType": "address"}, {"name": "_maxSummons", "type": "uint32", "internalType": "uint32"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getCrystal", "type": "function", "inputs": [{"name": "_crystalId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "internalType": "struct HeroCrystal", "components": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "summonerTears", "type": "uint8", "internalType": "uint8"}, {"name": "assistantTears", "type": "uint8", "internalType": "uint8"}, {"name": "enhancementStone", "type": "address", "internalType": "address"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}]}], "stateMutability": "view"},
    {"name": "getRoleAdmin", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "getUserCrystals", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "grantRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "hasRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_heroCoreAddress", "type": "address", "internalType": "address"}, {"name": "_statScienceAddress", "type": "address", "internalType": "address"}, {"name": "_randomGeneratorAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "newSummonCooldown", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "open", "type": "function", "inputs": [{"name": "_crystalId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "renounceRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "revokeRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setHeroCore", "type": "function", "inputs": [{"name": "_heroCoreAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setStatScience", "type": "function", "inputs": [{"name": "_statScienceAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setWaitBlocks", "type": "function", "inputs": [{"name": "_waitBlocks", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "supportsInterface", "type": "function", "inputs": [{"name": "interfaceId", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "totalCrystals", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "waitBlocks", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"}
]
"""     

class CrystalCore(ABIContractWrapper):
    def __init__(self, chain_key:str, rpc:str):
        contract_address = CONTRACT_ADDRESS[chain_key]
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def airdrop_crystal(self, cred:Credentials, _recipient:address, _is_shiny:bool) -> TxReceipt:
        tx = self.contract.functions.airdropCrystal(_recipient, _is_shiny)
        return self.send_transaction(tx, cred)

    def create_crystal(self, cred:Credentials, _owner:address, _summoner_id:uint256, _assistant_id:uint256, _generation:uint16, _summoner_bonus_tears:uint8, _assistant_bonus_tears:uint8, _enhancement_stone:address, _max_summons:uint32) -> TxReceipt:
        tx = self.contract.functions.createCrystal(_owner, _summoner_id, _assistant_id, _generation, _summoner_bonus_tears, _assistant_bonus_tears, _enhancement_stone, _max_summons)
        return self.send_transaction(tx, cred)

    def get_crystal(self, _crystal_id:uint256, block_identifier:BlockIdentifier = 'latest') -> tuple:
        return self.contract.functions.getCrystal(_crystal_id).call(block_identifier=block_identifier)

    def get_user_crystals(self, _address:address, block_identifier:BlockIdentifier = 'latest') -> List[uint256]:
        return self.contract.functions.getUserCrystals(_address).call(block_identifier=block_identifier)

    def initialize(self, cred:Credentials, _hero_core_address:address, _stat_science_address:address, _random_generator_address:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_hero_core_address, _stat_science_address, _random_generator_address)
        return self.send_transaction(tx, cred)

    def new_summon_cooldown(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.newSummonCooldown().call(block_identifier=block_identifier)

    def open(self, cred:Credentials, _crystal_id:uint256) -> TxReceipt:
        tx = self.contract.functions.open(_crystal_id)
        return self.send_transaction(tx, cred)

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
        return self.send_transaction(tx, cred)

    def paused(self, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.paused().call(block_identifier=block_identifier)

    def set_hero_core(self, cred:Credentials, _hero_core_address:address) -> TxReceipt:
        tx = self.contract.functions.setHeroCore(_hero_core_address)
        return self.send_transaction(tx, cred)

    def set_stat_science(self, cred:Credentials, _stat_science_address:address) -> TxReceipt:
        tx = self.contract.functions.setStatScience(_stat_science_address)
        return self.send_transaction(tx, cred)

    def set_wait_blocks(self, cred:Credentials, _wait_blocks:uint256) -> TxReceipt:
        tx = self.contract.functions.setWaitBlocks(_wait_blocks)
        return self.send_transaction(tx, cred)

    def supports_interface(self, interface_id:bytes4, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.supportsInterface(interface_id).call(block_identifier=block_identifier)

    def total_crystals(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.totalCrystals().call(block_identifier=block_identifier)

    def unpause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unpause()
        return self.send_transaction(tx, cred)

    def wait_blocks(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.waitBlocks().call(block_identifier=block_identifier)