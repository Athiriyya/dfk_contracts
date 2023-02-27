
from ..abi_contract_wrapper import ABIContractWrapper
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xc20a268bc7c4dB28f1f6e1703676513Db06C1B93",
    "sd": "0xcd26DfD7EdAe42eD525266D9a53b466db4Ed4f7b"
}

ABI = """[
    {"name": "Canceled", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": false, "internalType": "address"}, {"name": "powerUpId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Deactivated", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": false, "internalType": "address"}, {"name": "powerUpId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Expired", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": false, "internalType": "address"}, {"name": "powerUpId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "HeroAssigned", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": false, "internalType": "address"}, {"name": "powerUpId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "HeroRemoved", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": false, "internalType": "address"}, {"name": "powerUpId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "IncreasedTier", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": false, "internalType": "address"}, {"name": "powerUpId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "userData", "type": "tuple", "indexed": false, "internalType": "struct PowerUpUserData", "components": [{"name": "isActivated", "type": "bool", "internalType": "bool"}, {"name": "emergencyWithdrawHappened", "type": "bool", "internalType": "bool"}, {"name": "tier", "type": "uint256", "internalType": "uint256"}, {"name": "openHeroSlots", "type": "uint256", "internalType": "uint256"}, {"name": "cancellationHeldSlots", "type": "uint256", "internalType": "uint256"}, {"name": "heldSlotExpiration", "type": "uint256", "internalType": "uint256"}, {"name": "govTokenHoldExpiration", "type": "uint256", "internalType": "uint256"}, {"name": "owner", "type": "address", "internalType": "address"}]}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "PowerUpAdded", "type": "event", "inputs": [{"name": "powerup", "type": "tuple", "indexed": false, "internalType": "struct PowerUp", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "powerUpType", "type": "uint256", "internalType": "uint256"}, {"name": "tiers", "type": "uint256", "internalType": "uint256"}, {"name": "heroesPerTier", "type": "uint256", "internalType": "uint256"}, {"name": "lockTimeRequiredToAcquire", "type": "uint256", "internalType": "uint256"}, {"name": "cancelDelay", "type": "uint256", "internalType": "uint256"}, {"name": "govTokenPerTier", "type": "uint256[]", "internalType": "uint256[]"}]}], "anonymous": false},
    {"name": "PowerUpRemoved", "type": "event", "inputs": [{"name": "powerup", "type": "tuple", "indexed": false, "internalType": "struct PowerUp", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "powerUpType", "type": "uint256", "internalType": "uint256"}, {"name": "tiers", "type": "uint256", "internalType": "uint256"}, {"name": "heroesPerTier", "type": "uint256", "internalType": "uint256"}, {"name": "lockTimeRequiredToAcquire", "type": "uint256", "internalType": "uint256"}, {"name": "cancelDelay", "type": "uint256", "internalType": "uint256"}, {"name": "govTokenPerTier", "type": "uint256[]", "internalType": "uint256[]"}]}], "anonymous": false},
    {"name": "PowerUpUpdated", "type": "event", "inputs": [{"name": "powerup", "type": "tuple", "indexed": false, "internalType": "struct PowerUp", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "powerUpType", "type": "uint256", "internalType": "uint256"}, {"name": "tiers", "type": "uint256", "internalType": "uint256"}, {"name": "heroesPerTier", "type": "uint256", "internalType": "uint256"}, {"name": "lockTimeRequiredToAcquire", "type": "uint256", "internalType": "uint256"}, {"name": "cancelDelay", "type": "uint256", "internalType": "uint256"}, {"name": "govTokenPerTier", "type": "uint256[]", "internalType": "uint256[]"}]}], "anonymous": false},
    {"name": "RoleAdminChanged", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "previousAdminRole", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "newAdminRole", "type": "bytes32", "indexed": true, "internalType": "bytes32"}], "anonymous": false},
    {"name": "RoleGranted", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "account", "type": "address", "indexed": true, "internalType": "address"}, {"name": "sender", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "RoleRevoked", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "account", "type": "address", "indexed": true, "internalType": "address"}, {"name": "sender", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "Subscribed", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": false, "internalType": "address"}, {"name": "powerUpId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "userData", "type": "tuple", "indexed": false, "internalType": "struct PowerUpUserData", "components": [{"name": "isActivated", "type": "bool", "internalType": "bool"}, {"name": "emergencyWithdrawHappened", "type": "bool", "internalType": "bool"}, {"name": "tier", "type": "uint256", "internalType": "uint256"}, {"name": "openHeroSlots", "type": "uint256", "internalType": "uint256"}, {"name": "cancellationHeldSlots", "type": "uint256", "internalType": "uint256"}, {"name": "heldSlotExpiration", "type": "uint256", "internalType": "uint256"}, {"name": "govTokenHoldExpiration", "type": "uint256", "internalType": "uint256"}, {"name": "owner", "type": "address", "internalType": "address"}]}], "anonymous": false},
    {"name": "CANCELER_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "DEFAULT_ADMIN_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "activePowerUps", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "addPowerUp", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}, {"name": "_name", "type": "string", "internalType": "string"}, {"name": "_type", "type": "uint256", "internalType": "uint256"}, {"name": "_tiers", "type": "uint256", "internalType": "uint256"}, {"name": "_heroesPerTier", "type": "uint256", "internalType": "uint256"}, {"name": "_lockTimeRequiredToAcquire", "type": "uint256", "internalType": "uint256"}, {"name": "_cancelHoldDelay", "type": "uint256", "internalType": "uint256"}, {"name": "_govTokenPerTier", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "assignHero", "type": "function", "inputs": [{"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}, {"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "assignHeroes", "type": "function", "inputs": [{"name": "_powerUpIds", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_heroIds", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "cancel", "type": "function", "inputs": [{"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "cleanUpHeroAssignments", "type": "function", "inputs": [{"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "deactivatePowerUps", "type": "function", "inputs": [{"name": "_user", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "emergencyCancelAll", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getActivePowerUps", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "powerUpType", "type": "uint256", "internalType": "uint256"}, {"name": "tiers", "type": "uint256", "internalType": "uint256"}, {"name": "heroesPerTier", "type": "uint256", "internalType": "uint256"}, {"name": "lockTimeRequiredToAcquire", "type": "uint256", "internalType": "uint256"}, {"name": "cancelDelay", "type": "uint256", "internalType": "uint256"}, {"name": "govTokenPerTier", "type": "uint256[]", "internalType": "uint256[]"}], "internalType": "struct PowerUp[]"}], "stateMutability": "view"},
    {"name": "getAssignedHeroIds", "type": "function", "inputs": [{"name": "_account", "type": "address", "internalType": "address"}, {"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "getAssignedHeroes", "type": "function", "inputs": [{"name": "_account", "type": "address", "internalType": "address"}, {"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}], "internalType": "struct SummoningInfo"}, {"name": "info", "type": "tuple", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}], "internalType": "struct HeroInfo"}, {"name": "state", "type": "tuple", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum HeroStatus"}], "internalType": "struct HeroState"}, {"name": "stats", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}], "internalType": "struct HeroStats"}, {"name": "primaryStatGrowth", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}], "internalType": "struct HeroStatGrowth"}, {"name": "secondaryStatGrowth", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}], "internalType": "struct HeroStatGrowth"}, {"name": "professions", "type": "tuple", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}], "internalType": "struct HeroProfessions"}], "internalType": "struct Hero[]"}], "stateMutability": "view"},
    {"name": "getPowerUpHeroData", "type": "function", "inputs": [{"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}, {"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "powerUpId", "type": "uint256", "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "assignedSlot", "type": "uint256", "internalType": "uint256"}, {"name": "owner", "type": "address", "internalType": "address"}], "internalType": "struct PowerUpHeroData"}], "stateMutability": "view"},
    {"name": "getRoleAdmin", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "getUserPowerUpData", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}, {"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "isActivated", "type": "bool", "internalType": "bool"}, {"name": "emergencyWithdrawHappened", "type": "bool", "internalType": "bool"}, {"name": "tier", "type": "uint256", "internalType": "uint256"}, {"name": "openHeroSlots", "type": "uint256", "internalType": "uint256"}, {"name": "cancellationHeldSlots", "type": "uint256", "internalType": "uint256"}, {"name": "heldSlotExpiration", "type": "uint256", "internalType": "uint256"}, {"name": "govTokenHoldExpiration", "type": "uint256", "internalType": "uint256"}, {"name": "owner", "type": "address", "internalType": "address"}], "internalType": "struct PowerUpUserData"}], "stateMutability": "view"},
    {"name": "getUserPowerUpDataForActivePowerUps", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "isActivated", "type": "bool", "internalType": "bool"}, {"name": "emergencyWithdrawHappened", "type": "bool", "internalType": "bool"}, {"name": "tier", "type": "uint256", "internalType": "uint256"}, {"name": "openHeroSlots", "type": "uint256", "internalType": "uint256"}, {"name": "cancellationHeldSlots", "type": "uint256", "internalType": "uint256"}, {"name": "heldSlotExpiration", "type": "uint256", "internalType": "uint256"}, {"name": "govTokenHoldExpiration", "type": "uint256", "internalType": "uint256"}, {"name": "owner", "type": "address", "internalType": "address"}], "internalType": "struct PowerUpUserData[]"}, {"name": "", "type": "tuple[]", "components": [{"name": "powerUpId", "type": "uint256", "internalType": "uint256"}, {"name": "govTokens", "type": "uint256", "internalType": "uint256"}, {"name": "end", "type": "uint256", "internalType": "uint256"}, {"name": "govTokenHoldExpiration", "type": "uint256", "internalType": "uint256"}, {"name": "usedBalance", "type": "uint256", "internalType": "uint256"}], "internalType": "struct PowerUpLock[]"}], "stateMutability": "view"},
    {"name": "grantRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "hasRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "increaseTier", "type": "function", "inputs": [{"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}, {"name": "_tier", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_voteEscrowRewardPoolAddress", "type": "address", "internalType": "address"}, {"name": "_heroCoreAddress", "type": "address", "internalType": "address"}, {"name": "_questCoreAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "isHeroPowerUpActive", "type": "function", "inputs": [{"name": "_user", "type": "address", "internalType": "address"}, {"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}, {"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "isUserPowerUpActive", "type": "function", "inputs": [{"name": "_user", "type": "address", "internalType": "address"}, {"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "powerUpHeroData", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "powerUpId", "type": "uint256", "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "assignedSlot", "type": "uint256", "internalType": "uint256"}, {"name": "owner", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "powerUpHeroesAssigned", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "uint256", "internalType": "uint256"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "powerUps", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "powerUpType", "type": "uint256", "internalType": "uint256"}, {"name": "tiers", "type": "uint256", "internalType": "uint256"}, {"name": "heroesPerTier", "type": "uint256", "internalType": "uint256"}, {"name": "lockTimeRequiredToAcquire", "type": "uint256", "internalType": "uint256"}, {"name": "cancelDelay", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "removeHero", "type": "function", "inputs": [{"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}, {"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "removeHeroFromAllType3", "type": "function", "inputs": [{"name": "_user", "type": "address", "internalType": "address"}, {"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "removeHeroFromAllType3ForSender", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "removeHeroes", "type": "function", "inputs": [{"name": "_powerUpIds", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_heroIds", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "renounceRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "revokeRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "subscribe", "type": "function", "inputs": [{"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}, {"name": "_tier", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "supportsInterface", "type": "function", "inputs": [{"name": "interfaceId", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "userPowerUpData", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "isActivated", "type": "bool", "internalType": "bool"}, {"name": "emergencyWithdrawHappened", "type": "bool", "internalType": "bool"}, {"name": "tier", "type": "uint256", "internalType": "uint256"}, {"name": "openHeroSlots", "type": "uint256", "internalType": "uint256"}, {"name": "cancellationHeldSlots", "type": "uint256", "internalType": "uint256"}, {"name": "heldSlotExpiration", "type": "uint256", "internalType": "uint256"}, {"name": "govTokenHoldExpiration", "type": "uint256", "internalType": "uint256"}, {"name": "owner", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "verifyAllPowerUps", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "verifyPowerUp", "type": "function", "inputs": [{"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "verifyPowerUpForUser", "type": "function", "inputs": [{"name": "_user", "type": "address", "internalType": "address"}, {"name": "_powerUpId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class PowerUpManager(ABIContractWrapper):
    def __init__(self, chain_key:str, rpc:str):
        contract_address = CONTRACT_ADDRESS[chain_key]
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def active_power_ups(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.activePowerUps(a).call(block_identifier=block_identifier)

    def add_power_up(self, cred:Credentials, _id:uint256, _name:string, _type:uint256, _tiers:uint256, _heroes_per_tier:uint256, _lock_time_required_to_acquire:uint256, _cancel_hold_delay:uint256, _gov_token_per_tier:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.addPowerUp(_id, _name, _type, _tiers, _heroes_per_tier, _lock_time_required_to_acquire, _cancel_hold_delay, _gov_token_per_tier)
        return self.send_transaction(tx, cred)

    def assign_hero(self, cred:Credentials, _power_up_id:uint256, _hero_id:uint256) -> TxReceipt:
        tx = self.contract.functions.assignHero(_power_up_id, _hero_id)
        return self.send_transaction(tx, cred)

    def assign_heroes(self, cred:Credentials, _power_up_ids:Sequence[uint256], _hero_ids:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.assignHeroes(_power_up_ids, _hero_ids)
        return self.send_transaction(tx, cred)

    def cancel(self, cred:Credentials, _power_up_id:uint256) -> TxReceipt:
        tx = self.contract.functions.cancel(_power_up_id)
        return self.send_transaction(tx, cred)

    def clean_up_hero_assignments(self, cred:Credentials, _power_up_id:uint256) -> TxReceipt:
        tx = self.contract.functions.cleanUpHeroAssignments(_power_up_id)
        return self.send_transaction(tx, cred)

    def deactivate_power_ups(self, cred:Credentials, _user:address) -> TxReceipt:
        tx = self.contract.functions.deactivatePowerUps(_user)
        return self.send_transaction(tx, cred)

    def emergency_cancel_all(self, cred:Credentials, _address:address) -> TxReceipt:
        tx = self.contract.functions.emergencyCancelAll(_address)
        return self.send_transaction(tx, cred)

    def get_active_power_ups(self, block_identifier:BlockIdentifier = 'latest') -> List[tuple]:
        return self.contract.functions.getActivePowerUps().call(block_identifier=block_identifier)

    def get_assigned_hero_ids(self, _account:address, _power_up_id:uint256, block_identifier:BlockIdentifier = 'latest') -> List[uint256]:
        return self.contract.functions.getAssignedHeroIds(_account, _power_up_id).call(block_identifier=block_identifier)

    def get_assigned_heroes(self, _account:address, _power_up_id:uint256, block_identifier:BlockIdentifier = 'latest') -> List[tuple]:
        return self.contract.functions.getAssignedHeroes(_account, _power_up_id).call(block_identifier=block_identifier)

    def get_power_up_hero_data(self, _power_up_id:uint256, _hero_id:uint256, block_identifier:BlockIdentifier = 'latest') -> tuple:
        return self.contract.functions.getPowerUpHeroData(_power_up_id, _hero_id).call(block_identifier=block_identifier)

    def get_user_power_up_data(self, _address:address, _power_up_id:uint256, block_identifier:BlockIdentifier = 'latest') -> tuple:
        return self.contract.functions.getUserPowerUpData(_address, _power_up_id).call(block_identifier=block_identifier)

    def get_user_power_up_data_for_active_power_ups(self, _address:address, block_identifier:BlockIdentifier = 'latest') -> Tuple[List[tuple], List[tuple]]:
        return self.contract.functions.getUserPowerUpDataForActivePowerUps(_address).call(block_identifier=block_identifier)

    def increase_tier(self, cred:Credentials, _power_up_id:uint256, _tier:uint256) -> TxReceipt:
        tx = self.contract.functions.increaseTier(_power_up_id, _tier)
        return self.send_transaction(tx, cred)

    def initialize(self, cred:Credentials, _vote_escrow_reward_pool_address:address, _hero_core_address:address, _quest_core_address:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_vote_escrow_reward_pool_address, _hero_core_address, _quest_core_address)
        return self.send_transaction(tx, cred)

    def is_hero_power_up_active(self, _user:address, _power_up_id:uint256, _hero_id:uint256, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.isHeroPowerUpActive(_user, _power_up_id, _hero_id).call(block_identifier=block_identifier)

    def is_user_power_up_active(self, _user:address, _power_up_id:uint256, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.isUserPowerUpActive(_user, _power_up_id).call(block_identifier=block_identifier)

    def power_up_hero_data(self, a:uint256, b:uint256, block_identifier:BlockIdentifier = 'latest') -> Tuple[uint256, uint256, uint256, address]:
        return self.contract.functions.powerUpHeroData(a, b).call(block_identifier=block_identifier)

    def power_up_heroes_assigned(self, a:address, b:uint256, c:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.powerUpHeroesAssigned(a, b, c).call(block_identifier=block_identifier)

    def power_ups(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> Tuple[uint256, string, uint256, uint256, uint256, uint256, uint256]:
        return self.contract.functions.powerUps(a).call(block_identifier=block_identifier)

    def remove_hero(self, cred:Credentials, _power_up_id:uint256, _hero_id:uint256) -> TxReceipt:
        tx = self.contract.functions.removeHero(_power_up_id, _hero_id)
        return self.send_transaction(tx, cred)

    def remove_hero_from_all_type3(self, cred:Credentials, _user:address, _hero_id:uint256) -> TxReceipt:
        tx = self.contract.functions.removeHeroFromAllType3(_user, _hero_id)
        return self.send_transaction(tx, cred)

    def remove_hero_from_all_type3_for_sender(self, cred:Credentials, _hero_id:uint256) -> TxReceipt:
        tx = self.contract.functions.removeHeroFromAllType3ForSender(_hero_id)
        return self.send_transaction(tx, cred)

    def remove_heroes(self, cred:Credentials, _power_up_ids:Sequence[uint256], _hero_ids:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.removeHeroes(_power_up_ids, _hero_ids)
        return self.send_transaction(tx, cred)

    def subscribe(self, cred:Credentials, _power_up_id:uint256, _tier:uint256) -> TxReceipt:
        tx = self.contract.functions.subscribe(_power_up_id, _tier)
        return self.send_transaction(tx, cred)

    def supports_interface(self, interface_id:bytes4, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.supportsInterface(interface_id).call(block_identifier=block_identifier)

    def user_power_up_data(self, a:address, b:uint256, block_identifier:BlockIdentifier = 'latest') -> Tuple[bool, bool, uint256, uint256, uint256, uint256, uint256, address]:
        return self.contract.functions.userPowerUpData(a, b).call(block_identifier=block_identifier)

    def verify_all_power_ups(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.verifyAllPowerUps()
        return self.send_transaction(tx, cred)

    def verify_power_up(self, cred:Credentials, _power_up_id:uint256) -> TxReceipt:
        tx = self.contract.functions.verifyPowerUp(_power_up_id)
        return self.send_transaction(tx, cred)

    def verify_power_up_for_user(self, cred:Credentials, _user:address, _power_up_id:uint256) -> TxReceipt:
        tx = self.contract.functions.verifyPowerUpForUser(_user, _power_up_id)
        return self.send_transaction(tx, cred)