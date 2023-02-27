
from ..abi_contract_wrapper import ABIContractWrapper
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xBc36D18662Bb97F9e74B1EAA1B752aA7A44595A7",
    "sd": "0xb086584f476Ad21B40aF0672f385a67334A0b294"
}

ABI = """[
    {"name": "CrystalAirdrop", "type": "event", "inputs": [{"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "crystalId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "CrystalDarkSummoned", "type": "event", "inputs": [{"name": "crystalId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "summonerId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "assistantId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "generation", "type": "uint16", "internalType": "uint16", "indexed": false}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "summonerTears", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "assistantTears", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "enhancementStone", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "CrystalOpen", "type": "event", "inputs": [{"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "crystalId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "heroId", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "CrystalSummoned", "type": "event", "inputs": [{"name": "crystalId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "owner", "type": "address", "internalType": "address", "indexed": true}, {"name": "summonerId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "assistantId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "generation", "type": "uint16", "internalType": "uint16", "indexed": false}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "summonerTears", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "assistantTears", "type": "uint8", "internalType": "uint8", "indexed": false}, {"name": "enhancementStone", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "EnhancementStoneAdded", "type": "event", "inputs": [{"name": "atunementItemAddress", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "FeeAddressAdded", "type": "event", "inputs": [{"name": "feeAddress", "type": "address", "internalType": "address", "indexed": true}, {"name": "feePercent", "type": "uint256", "internalType": "uint256", "indexed": true}], "anonymous": false},
    {"name": "FeeDeferred", "type": "event", "inputs": [{"name": "source", "type": "address", "internalType": "address", "indexed": true}, {"name": "from", "type": "address", "internalType": "address", "indexed": true}, {"name": "to", "type": "address", "internalType": "address", "indexed": true}, {"name": "token", "type": "address", "internalType": "address", "indexed": false}, {"name": "amount", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "timestamp", "type": "uint64", "internalType": "uint64", "indexed": false}], "anonymous": false},
    {"name": "FeeDisbursed", "type": "event", "inputs": [{"name": "source", "type": "address", "internalType": "address", "indexed": true}, {"name": "from", "type": "address", "internalType": "address", "indexed": true}, {"name": "to", "type": "address", "internalType": "address", "indexed": true}, {"name": "token", "type": "address", "internalType": "address", "indexed": false}, {"name": "amount", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "timestamp", "type": "uint64", "internalType": "uint64", "indexed": false}], "anonymous": false},
    {"name": "FeeLockedBurned", "type": "event", "inputs": [{"name": "source", "type": "address", "internalType": "address", "indexed": true}, {"name": "from", "type": "address", "internalType": "address", "indexed": true}, {"name": "to", "type": "address", "internalType": "address", "indexed": true}, {"name": "token", "type": "address", "internalType": "address", "indexed": false}, {"name": "amount", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "timestamp", "type": "uint64", "internalType": "uint64", "indexed": false}], "anonymous": false},
    {"name": "GlobalStartTimeSet", "type": "event", "inputs": [{"name": "startTime", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "internalType": "uint8", "indexed": false}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "RoleAdminChanged", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "previousAdminRole", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "newAdminRole", "type": "bytes32", "internalType": "bytes32", "indexed": true}], "anonymous": false},
    {"name": "RoleGranted", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "account", "type": "address", "internalType": "address", "indexed": true}, {"name": "sender", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
    {"name": "RoleRevoked", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "account", "type": "address", "internalType": "address", "indexed": true}, {"name": "sender", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "DEFAULT_ADMIN_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "activeEnhancementStones", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "addEnhancementStone", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "approveAuctionSpending", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "baseCooldown", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "baseSummonFee", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "calculateSummoningCost", "type": "function", "inputs": [{"name": "_hero", "type": "tuple", "internalType": "struct Hero", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "internalType": "struct SummoningInfo", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}]}, {"name": "info", "type": "tuple", "internalType": "struct HeroInfo", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}]}, {"name": "state", "type": "tuple", "internalType": "struct HeroState", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum HeroStatus"}]}, {"name": "stats", "type": "tuple", "internalType": "struct HeroStats", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}]}, {"name": "primaryStatGrowth", "type": "tuple", "internalType": "struct HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "secondaryStatGrowth", "type": "tuple", "internalType": "struct HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "professions", "type": "tuple", "internalType": "struct HeroProfessions", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}]}]}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "cooldownPerGen", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "feeAddresses", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "feePercents", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getRoleAdmin", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "grantRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "hasRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "increasePerGen", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "increasePerSummon", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "lastLockedSummon", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "lockedSummonCooldown", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "powerToken", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IPowerToken"}], "stateMutability": "view"},
    {"name": "removeEnhancementStone", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "renounceRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "revokeRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setFees", "type": "function", "inputs": [{"name": "_feeAddresses", "type": "address[]", "internalType": "address[]"}, {"name": "_feePercents", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setHeroCore", "type": "function", "inputs": [{"name": "_heroCoreAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setLockedSummonCooldown", "type": "function", "inputs": [{"name": "_lockedSummonCooldown", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setPowerToken", "type": "function", "inputs": [{"name": "_powerTokenAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setStatScience", "type": "function", "inputs": [{"name": "_statScienceAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setSummonCooldowns", "type": "function", "inputs": [{"name": "_baseCooldown", "type": "uint256", "internalType": "uint256"}, {"name": "_cooldownPerGen", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setSummonFees", "type": "function", "inputs": [{"name": "_baseSummonFee", "type": "uint256", "internalType": "uint256"}, {"name": "_increasePerSummon", "type": "uint256", "internalType": "uint256"}, {"name": "_increasePerGen", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTears", "type": "function", "inputs": [{"name": "_tearsAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTokenUnlocker", "type": "function", "inputs": [{"name": "_tokenUnlockerAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "summonCrystal", "type": "function", "inputs": [{"name": "_summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "_assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "_summonerTears", "type": "uint16", "internalType": "uint16"}, {"name": "_assistantTears", "type": "uint16", "internalType": "uint16"}, {"name": "_enhancementStone", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "summonCrystalWithAuction", "type": "function", "inputs": [{"name": "_summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "_assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "_summonerTears", "type": "uint16", "internalType": "uint16"}, {"name": "_assistantTears", "type": "uint16", "internalType": "uint16"}, {"name": "_enhancementStone", "type": "address", "internalType": "address"}, {"name": "_assistingAuctionAddress", "type": "address", "internalType": "address"}, {"name": "_hireAmount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "summonCrystalWithAuctionWithLocked", "type": "function", "inputs": [{"name": "_summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "_assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "_summonerTears", "type": "uint16", "internalType": "uint16"}, {"name": "_assistantTears", "type": "uint16", "internalType": "uint16"}, {"name": "_enhancementStone", "type": "address", "internalType": "address"}, {"name": "_assistingAuctionAddress", "type": "address", "internalType": "address"}, {"name": "_hireAmount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "summonCrystalWithLocked", "type": "function", "inputs": [{"name": "_summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "_assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "_summonerTears", "type": "uint16", "internalType": "uint16"}, {"name": "_assistantTears", "type": "uint16", "internalType": "uint16"}, {"name": "_enhancementStone", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "supportsInterface", "type": "function", "inputs": [{"name": "interfaceId", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class HeroSummoning(ABIContractWrapper):
    def __init__(self, chain_key:str, rpc:str):
        contract_address = CONTRACT_ADDRESS[chain_key]
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def active_enhancement_stones(self, a:address, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.activeEnhancementStones(a).call(block_identifier=block_identifier)

    def add_enhancement_stone(self, cred:Credentials, _address:address) -> TxReceipt:
        tx = self.contract.functions.addEnhancementStone(_address)
        return self.send_transaction(tx, cred)

    def approve_auction_spending(self, cred:Credentials, _address:address, _amount:uint256) -> TxReceipt:
        tx = self.contract.functions.approveAuctionSpending(_address, _amount)
        return self.send_transaction(tx, cred)

    def base_cooldown(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.baseCooldown().call(block_identifier=block_identifier)

    def base_summon_fee(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.baseSummonFee().call(block_identifier=block_identifier)

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

    def last_locked_summon(self, a:address, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.lastLockedSummon(a).call(block_identifier=block_identifier)

    def locked_summon_cooldown(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.lockedSummonCooldown().call(block_identifier=block_identifier)

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
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

    def set_locked_summon_cooldown(self, cred:Credentials, _locked_summon_cooldown:uint256) -> TxReceipt:
        tx = self.contract.functions.setLockedSummonCooldown(_locked_summon_cooldown)
        return self.send_transaction(tx, cred)

    def set_power_token(self, cred:Credentials, _power_token_address:address) -> TxReceipt:
        tx = self.contract.functions.setPowerToken(_power_token_address)
        return self.send_transaction(tx, cred)

    def set_stat_science(self, cred:Credentials, _stat_science_address:address) -> TxReceipt:
        tx = self.contract.functions.setStatScience(_stat_science_address)
        return self.send_transaction(tx, cred)

    def set_summon_cooldowns(self, cred:Credentials, _base_cooldown:uint256, _cooldown_per_gen:uint256) -> TxReceipt:
        tx = self.contract.functions.setSummonCooldowns(_base_cooldown, _cooldown_per_gen)
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

    def summon_crystal(self, cred:Credentials, _summoner_id:uint256, _assistant_id:uint256, _summoner_tears:uint16, _assistant_tears:uint16, _enhancement_stone:address) -> TxReceipt:
        tx = self.contract.functions.summonCrystal(_summoner_id, _assistant_id, _summoner_tears, _assistant_tears, _enhancement_stone)
        return self.send_transaction(tx, cred)

    def summon_crystal_with_auction(self, cred:Credentials, _summoner_id:uint256, _assistant_id:uint256, _summoner_tears:uint16, _assistant_tears:uint16, _enhancement_stone:address, _assisting_auction_address:address, _hire_amount:uint256) -> TxReceipt:
        tx = self.contract.functions.summonCrystalWithAuction(_summoner_id, _assistant_id, _summoner_tears, _assistant_tears, _enhancement_stone, _assisting_auction_address, _hire_amount)
        return self.send_transaction(tx, cred)

    def summon_crystal_with_auction_with_locked(self, cred:Credentials, _summoner_id:uint256, _assistant_id:uint256, _summoner_tears:uint16, _assistant_tears:uint16, _enhancement_stone:address, _assisting_auction_address:address, _hire_amount:uint256) -> TxReceipt:
        tx = self.contract.functions.summonCrystalWithAuctionWithLocked(_summoner_id, _assistant_id, _summoner_tears, _assistant_tears, _enhancement_stone, _assisting_auction_address, _hire_amount)
        return self.send_transaction(tx, cred)

    def summon_crystal_with_locked(self, cred:Credentials, _summoner_id:uint256, _assistant_id:uint256, _summoner_tears:uint16, _assistant_tears:uint16, _enhancement_stone:address) -> TxReceipt:
        tx = self.contract.functions.summonCrystalWithLocked(_summoner_id, _assistant_id, _summoner_tears, _assistant_tears, _enhancement_stone)
        return self.send_transaction(tx, cred)

    def supports_interface(self, interface_id:bytes4, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.supportsInterface(interface_id).call(block_identifier=block_identifier)

    def unpause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unpause()
        return self.send_transaction(tx, cred)