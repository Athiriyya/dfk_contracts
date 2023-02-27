
from ..abi_contract_wrapper import ABIContractWrapper
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x70908Fd7278aab183C7EfC4f3449184E98e2e305",
    "sd": "0x0000000000000000000000000000000000000000"
}

ABI = """[
    {"name": "CrystalAirdrop", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "crystalId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "createdBlock", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "CrystalDarkSummoned", "type": "event", "inputs": [{"name": "crystalId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "summonerId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "generation", "type": "uint16", "indexed": false, "internalType": "uint16"}, {"name": "createdBlock", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "summonerTears", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "assistantTears", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "enhancementStone", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "CrystalOpen", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "crystalId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "CrystalSummoned", "type": "event", "inputs": [{"name": "crystalId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "summonerId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "generation", "type": "uint16", "indexed": false, "internalType": "uint16"}, {"name": "createdBlock", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "summonerTears", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "assistantTears", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "enhancementStone", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "EnhancementStoneAdded", "type": "event", "inputs": [{"name": "atunementItemAddress", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "FeeAddressAdded", "type": "event", "inputs": [{"name": "feeAddress", "type": "address", "indexed": true, "internalType": "address"}, {"name": "feePercent", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "FeeDeferred", "type": "event", "inputs": [{"name": "source", "type": "address", "indexed": true, "internalType": "address"}, {"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "token", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "timestamp", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
    {"name": "FeeDisbursed", "type": "event", "inputs": [{"name": "source", "type": "address", "indexed": true, "internalType": "address"}, {"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "token", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "timestamp", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
    {"name": "FeeLockedBurned", "type": "event", "inputs": [{"name": "source", "type": "address", "indexed": true, "internalType": "address"}, {"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "token", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "timestamp", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
    {"name": "GlobalStartTimeSet", "type": "event", "inputs": [{"name": "startTime", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "RoleAdminChanged", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "previousAdminRole", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "newAdminRole", "type": "bytes32", "indexed": true, "internalType": "bytes32"}], "anonymous": false},
    {"name": "RoleGranted", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "account", "type": "address", "indexed": true, "internalType": "address"}, {"name": "sender", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "RoleRevoked", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "account", "type": "address", "indexed": true, "internalType": "address"}, {"name": "sender", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "DEFAULT_ADMIN_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "activeEnhancementStones", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "addEnhancementStone", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "baseCooldown", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "baseSummonFee", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "calculateRarityBonusCost", "type": "function", "inputs": [{"name": "_rarityBonusCharges", "type": "uint8", "internalType": "uint8"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "pure"},
    {"name": "calculateSummoningCost", "type": "function", "inputs": [{"name": "_hero", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}], "internalType": "struct SummoningInfo"}, {"name": "info", "type": "tuple", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}], "internalType": "struct HeroInfo"}, {"name": "state", "type": "tuple", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum HeroStatus"}], "internalType": "struct HeroState"}, {"name": "stats", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}], "internalType": "struct HeroStats"}, {"name": "primaryStatGrowth", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}], "internalType": "struct HeroStatGrowth"}, {"name": "secondaryStatGrowth", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}], "internalType": "struct HeroStatGrowth"}, {"name": "professions", "type": "tuple", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}], "internalType": "struct HeroProfessions"}], "internalType": "struct Hero"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "cooldownPerGen", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "feeAddresses", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "feePercents", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getRoleAdmin", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "grantRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "hasRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "increasePerGen", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "increasePerSummon", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_crystalCoreAddress", "type": "address", "internalType": "address"}, {"name": "_heroCoreAddress", "type": "address", "internalType": "address"}, {"name": "_powerTokenAddress", "type": "address", "internalType": "address"}, {"name": "_gaiaTearsAddress", "type": "address", "internalType": "address"}, {"name": "_statScienceAddress", "type": "address", "internalType": "address"}, {"name": "_graveyard", "type": "address", "internalType": "address"}, {"name": "_flagStorage", "type": "address", "internalType": "address"}, {"name": "_meditationCircle", "type": "address", "internalType": "address"}, {"name": "_assistingAuction", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "powerToken", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IPowerToken"}], "stateMutability": "view"},
    {"name": "removeEnhancementStone", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "renounceRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "revokeRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setFees", "type": "function", "inputs": [{"name": "_feeAddresses", "type": "address[]", "internalType": "address[]"}, {"name": "_feePercents", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setHeroCore", "type": "function", "inputs": [{"name": "_heroCoreAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setPowerToken", "type": "function", "inputs": [{"name": "_powerTokenAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setStatScience", "type": "function", "inputs": [{"name": "_statScienceAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setSummonFees", "type": "function", "inputs": [{"name": "_baseSummonFee", "type": "uint256", "internalType": "uint256"}, {"name": "_increasePerSummon", "type": "uint256", "internalType": "uint256"}, {"name": "_increasePerGen", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTears", "type": "function", "inputs": [{"name": "_tearsAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTokenUnlocker", "type": "function", "inputs": [{"name": "_tokenUnlockerAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "summonCrystal", "type": "function", "inputs": [{"name": "_summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "_assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "_summonerTears", "type": "uint16", "internalType": "uint16"}, {"name": "_assistantTears", "type": "uint16", "internalType": "uint16"}, {"name": "_enhancementStone", "type": "address", "internalType": "address"}, {"name": "_rarityBonusCharges", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "summonCrystalWithLocked", "type": "function", "inputs": [{"name": "_summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "_assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "_summonerTears", "type": "uint16", "internalType": "uint16"}, {"name": "_assistantTears", "type": "uint16", "internalType": "uint16"}, {"name": "_enhancementStone", "type": "address", "internalType": "address"}, {"name": "_rarityBonusCharges", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "supportsInterface", "type": "function", "inputs": [{"name": "interfaceId", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"}
]
"""     

class DarkSummoning(ABIContractWrapper):
    def __init__(self, chain_key:str, rpc:str):
        contract_address = CONTRACT_ADDRESS[chain_key]
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def active_enhancement_stones(self, a:address, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.activeEnhancementStones(a).call(block_identifier=block_identifier)

    def add_enhancement_stone(self, cred:Credentials, _address:address) -> TxReceipt:
        tx = self.contract.functions.addEnhancementStone(_address)
        return self.send_transaction(tx, cred)

    def base_cooldown(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.baseCooldown().call(block_identifier=block_identifier)

    def base_summon_fee(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.baseSummonFee().call(block_identifier=block_identifier)

    def calculate_rarity_bonus_cost(self, _rarity_bonus_charges:uint8, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.calculateRarityBonusCost(_rarity_bonus_charges).call(block_identifier=block_identifier)

    def calculate_summoning_cost(self, _hero:tuple, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.calculateSummoningCost(_hero).call(block_identifier=block_identifier)

    def cooldown_per_gen(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.cooldownPerGen().call(block_identifier=block_identifier)

    def fee_addresses(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.feeAddresses(a).call(block_identifier=block_identifier)

    def fee_percents(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.feePercents(a).call(block_identifier=block_identifier)

    def increase_per_gen(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.increasePerGen().call(block_identifier=block_identifier)

    def increase_per_summon(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.increasePerSummon().call(block_identifier=block_identifier)

    def initialize(self, cred:Credentials, _crystal_core_address:address, _hero_core_address:address, _power_token_address:address, _gaia_tears_address:address, _stat_science_address:address, _graveyard:address, _flag_storage:address, _meditation_circle:address, _assisting_auction:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_crystal_core_address, _hero_core_address, _power_token_address, _gaia_tears_address, _stat_science_address, _graveyard, _flag_storage, _meditation_circle, _assisting_auction)
        return self.send_transaction(tx, cred)

    def paused(self, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.paused().call(block_identifier=block_identifier)

    def power_token(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.powerToken().call(block_identifier=block_identifier)

    def remove_enhancement_stone(self, cred:Credentials, _address:address) -> TxReceipt:
        tx = self.contract.functions.removeEnhancementStone(_address)
        return self.send_transaction(tx, cred)

    def set_fees(self, cred:Credentials, _fee_addresses:Sequence[address], _fee_percents:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.setFees(_fee_addresses, _fee_percents)
        return self.send_transaction(tx, cred)

    def set_hero_core(self, cred:Credentials, _hero_core_address:address) -> TxReceipt:
        tx = self.contract.functions.setHeroCore(_hero_core_address)
        return self.send_transaction(tx, cred)

    def set_power_token(self, cred:Credentials, _power_token_address:address) -> TxReceipt:
        tx = self.contract.functions.setPowerToken(_power_token_address)
        return self.send_transaction(tx, cred)

    def set_stat_science(self, cred:Credentials, _stat_science_address:address) -> TxReceipt:
        tx = self.contract.functions.setStatScience(_stat_science_address)
        return self.send_transaction(tx, cred)

    def set_summon_fees(self, cred:Credentials, _base_summon_fee:uint256, _increase_per_summon:uint256, _increase_per_gen:uint256) -> TxReceipt:
        tx = self.contract.functions.setSummonFees(_base_summon_fee, _increase_per_summon, _increase_per_gen)
        return self.send_transaction(tx, cred)

    def set_tears(self, cred:Credentials, _tears_address:address) -> TxReceipt:
        tx = self.contract.functions.setTears(_tears_address)
        return self.send_transaction(tx, cred)

    def set_token_unlocker(self, cred:Credentials, _token_unlocker_address:address) -> TxReceipt:
        tx = self.contract.functions.setTokenUnlocker(_token_unlocker_address)
        return self.send_transaction(tx, cred)

    def summon_crystal(self, cred:Credentials, _summoner_id:uint256, _assistant_id:uint256, _summoner_tears:uint16, _assistant_tears:uint16, _enhancement_stone:address, _rarity_bonus_charges:uint8) -> TxReceipt:
        tx = self.contract.functions.summonCrystal(_summoner_id, _assistant_id, _summoner_tears, _assistant_tears, _enhancement_stone, _rarity_bonus_charges)
        return self.send_transaction(tx, cred)

    def summon_crystal_with_locked(self, cred:Credentials, _summoner_id:uint256, _assistant_id:uint256, _summoner_tears:uint16, _assistant_tears:uint16, _enhancement_stone:address, _rarity_bonus_charges:uint8) -> TxReceipt:
        tx = self.contract.functions.summonCrystalWithLocked(_summoner_id, _assistant_id, _summoner_tears, _assistant_tears, _enhancement_stone, _rarity_bonus_charges)
        return self.send_transaction(tx, cred)

    def supports_interface(self, interface_id:bytes4, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.supportsInterface(interface_id).call(block_identifier=block_identifier)