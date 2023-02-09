
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x57Dec9cC7f492d6583c773e2E7ad66dcDc6940Fb",
    "sd": "0xad2ea7b7e49be15918E4917736E86ff7feA57a6A"
}

ABI = """[
    {"name": "DiamondCut", "type": "event", "inputs": [{"name": "_diamondCut", "type": "tuple[]", "indexed": false, "internalType": "struct IDiamondCut.FacetCut[]", "components": [{"name": "facetAddress", "type": "address", "internalType": "address"}, {"name": "action", "type": "uint8", "internalType": "enum IDiamondCut.FacetCutAction"}, {"name": "functionSelectors", "type": "bytes4[]", "internalType": "bytes4[]"}]}, {"name": "_init", "type": "address", "indexed": false, "internalType": "address"}, {"name": "_calldata", "type": "bytes", "indexed": false, "internalType": "bytes"}], "anonymous": false},
    {"name": "diamondCut", "type": "function", "inputs": [{"name": "_diamondCut", "type": "tuple[]", "internalType": "struct IDiamondCut.FacetCut[]", "components": [{"name": "facetAddress", "type": "address", "internalType": "address"}, {"name": "action", "type": "uint8", "internalType": "enum IDiamondCut.FacetCutAction"}, {"name": "functionSelectors", "type": "bytes4[]", "internalType": "bytes4[]"}]}, {"name": "_init", "type": "address", "internalType": "address"}, {"name": "_calldata", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "facetAddress", "type": "function", "inputs": [{"name": "_functionSelector", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "facetAddress_", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "facetAddresses", "type": "function", "inputs": [], "outputs": [{"name": "facetAddresses_", "type": "address[]", "internalType": "address[]"}], "stateMutability": "view"},
    {"name": "facetFunctionSelectors", "type": "function", "inputs": [{"name": "_facet", "type": "address", "internalType": "address"}], "outputs": [{"name": "facetFunctionSelectors_", "type": "bytes4[]", "internalType": "bytes4[]"}], "stateMutability": "view"},
    {"name": "facets", "type": "function", "inputs": [], "outputs": [{"name": "facets_", "type": "tuple[]", "internalType": "struct IDiamondLoupe.Facet[]", "components": [{"name": "facetAddress", "type": "address", "internalType": "address"}, {"name": "functionSelectors", "type": "bytes4[]", "internalType": "bytes4[]"}]}], "stateMutability": "view"},
    {"name": "supportsInterface", "type": "function", "inputs": [{"name": "_interfaceId", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "OwnershipTransferred", "type": "event", "inputs": [{"name": "previousOwner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "newOwner", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "owner", "type": "function", "inputs": [], "outputs": [{"name": "owner_", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "transferOwnership", "type": "function", "inputs": [{"name": "_newOwner", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "addAttunementCrystal", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "adminRemove", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "removeAttunementCrystal", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setFlagStorage", "type": "function", "inputs": [{"name": "_flagStorageAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setPowerToken", "type": "function", "inputs": [{"name": "_powerTokenAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setRune", "type": "function", "inputs": [{"name": "_index", "type": "uint8", "internalType": "uint8"}, {"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setStatScienceAddress", "type": "function", "inputs": [{"name": "_statScienceAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTokenUnlocker", "type": "function", "inputs": [{"name": "_tokenUnlockerAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "AttunementCrystalAdded", "type": "event", "inputs": [{"name": "atunementItemAddress", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "FeeAddressAdded", "type": "event", "inputs": [{"name": "feeAddress", "type": "address", "indexed": true, "internalType": "address"}, {"name": "feePercent", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "FeeDeferred", "type": "event", "inputs": [{"name": "source", "type": "address", "indexed": true, "internalType": "address"}, {"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "token", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "timestamp", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
    {"name": "FeeDisbursed", "type": "event", "inputs": [{"name": "source", "type": "address", "indexed": true, "internalType": "address"}, {"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "token", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "timestamp", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
    {"name": "FeeLockedBurned", "type": "event", "inputs": [{"name": "source", "type": "address", "indexed": true, "internalType": "address"}, {"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "token", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "timestamp", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "LevelUp", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "hero", "type": "tuple", "indexed": false, "internalType": "struct Hero", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "internalType": "struct SummoningInfo", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}]}, {"name": "info", "type": "tuple", "internalType": "struct HeroInfo", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}]}, {"name": "state", "type": "tuple", "internalType": "struct HeroState", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum HeroStatus"}]}, {"name": "stats", "type": "tuple", "internalType": "struct HeroStats", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}]}, {"name": "primaryStatGrowth", "type": "tuple", "internalType": "struct HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "secondaryStatGrowth", "type": "tuple", "internalType": "struct HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "professions", "type": "tuple", "internalType": "struct HeroProfessions", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}]}]}, {"name": "oldHero", "type": "tuple", "indexed": false, "internalType": "struct Hero", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "internalType": "struct SummoningInfo", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}]}, {"name": "info", "type": "tuple", "internalType": "struct HeroInfo", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}]}, {"name": "state", "type": "tuple", "internalType": "struct HeroState", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum HeroStatus"}]}, {"name": "stats", "type": "tuple", "internalType": "struct HeroStats", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}]}, {"name": "primaryStatGrowth", "type": "tuple", "internalType": "struct HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "secondaryStatGrowth", "type": "tuple", "internalType": "struct HeroStatGrowth", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}]}, {"name": "professions", "type": "tuple", "internalType": "struct HeroProfessions", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}]}]}], "anonymous": false},
    {"name": "MeditationBegun", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "meditationId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "primaryStat", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "secondaryStat", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "tertiaryStat", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "attunementCrystal", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "MeditationBegunWithLevel", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "meditationId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "primaryStat", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "secondaryStat", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "tertiaryStat", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "attunementCrystal", "type": "address", "indexed": false, "internalType": "address"}, {"name": "toLevel", "type": "uint16", "indexed": false, "internalType": "uint16"}], "anonymous": false},
    {"name": "MeditationCompleted", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "meditationId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "RoleAdminChanged", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "previousAdminRole", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "newAdminRole", "type": "bytes32", "indexed": true, "internalType": "bytes32"}], "anonymous": false},
    {"name": "RoleGranted", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "account", "type": "address", "indexed": true, "internalType": "address"}, {"name": "sender", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "RoleRevoked", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "account", "type": "address", "indexed": true, "internalType": "address"}, {"name": "sender", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "StatUp", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "stat", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "increase", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "updateType", "type": "uint8", "indexed": false, "internalType": "enum UpdateType"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "DEFAULT_ADMIN_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "activeAttunementCrystals", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "heroToMeditation", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "profileActiveMeditations", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "primaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "secondaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "tertiaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "attunementCrystal", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "runes", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "contract IInventoryItem"}], "stateMutability": "view"},
    {"name": "tokenUnlockerAddress", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "completeMeditation", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getActiveMeditations", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[]", "internalType": "struct Meditation[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "primaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "secondaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "tertiaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "attunementCrystal", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "uint8"}]}], "stateMutability": "view"},
    {"name": "getHeroMeditation", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "internalType": "struct Meditation", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "primaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "secondaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "tertiaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "attunementCrystal", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "uint8"}]}], "stateMutability": "view"},
    {"name": "getMeditation", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "internalType": "struct Meditation", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "primaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "secondaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "tertiaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "attunementCrystal", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "uint8"}]}], "stateMutability": "view"},
    {"name": "getRoleAdmin", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "grantRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "hasRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "renounceRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "revokeRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setFees", "type": "function", "inputs": [{"name": "_feeAddresses", "type": "address[]", "internalType": "address[]"}, {"name": "_feePercents", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "_getRequiredRunes", "type": "function", "inputs": [{"name": "_level", "type": "uint16", "internalType": "uint16"}], "outputs": [{"name": "", "type": "uint16[10]", "internalType": "uint16[10]"}], "stateMutability": "pure"},
    {"name": "startMeditation", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}, {"name": "_primaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "_secondaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "_tertiaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "_attunementCrystal", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "startMeditationWithLocked", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}, {"name": "_primaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "_secondaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "_tertiaryStat", "type": "uint8", "internalType": "uint8"}, {"name": "_attunementCrystal", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class MasterGardener(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def diamond_cut(self, cred:Credentials, _diamond_cut:Sequence[tuple], _init:address, _calldata:bytes) -> TxReceipt:
        tx = self.contract.functions.diamondCut(_diamond_cut, _init, _calldata)
        return self.send_transaction(tx, cred)

    def facet_address(self, _function_selector:bytes4) -> address:
        return self.contract.functions.facetAddress(_function_selector).call()

    def facet_addresses(self) -> Sequence[address]:
        return self.contract.functions.facetAddresses().call()

    def facet_function_selectors(self, _facet:address) -> Sequence[bytes4]:
        return self.contract.functions.facetFunctionSelectors(_facet).call()

    def facets(self) -> Sequence[tuple]:
        return self.contract.functions.facets().call()

    def supports_interface(self, _interface_id:bytes4) -> bool:
        return self.contract.functions.supportsInterface(_interface_id).call()

    def owner(self) -> address:
        return self.contract.functions.owner().call()

    def transfer_ownership(self, cred:Credentials, _new_owner:address) -> TxReceipt:
        tx = self.contract.functions.transferOwnership(_new_owner)
        return self.send_transaction(tx, cred)

    def add_attunement_crystal(self, cred:Credentials, _address:address) -> TxReceipt:
        tx = self.contract.functions.addAttunementCrystal(_address)
        return self.send_transaction(tx, cred)

    def admin_remove(self, cred:Credentials, _hero_id:uint256) -> TxReceipt:
        tx = self.contract.functions.adminRemove(_hero_id)
        return self.send_transaction(tx, cred)

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
        return self.send_transaction(tx, cred)

    def remove_attunement_crystal(self, cred:Credentials, _address:address) -> TxReceipt:
        tx = self.contract.functions.removeAttunementCrystal(_address)
        return self.send_transaction(tx, cred)

    def set_flag_storage(self, cred:Credentials, _flag_storage_address:address) -> TxReceipt:
        tx = self.contract.functions.setFlagStorage(_flag_storage_address)
        return self.send_transaction(tx, cred)

    def set_power_token(self, cred:Credentials, _power_token_address:address) -> TxReceipt:
        tx = self.contract.functions.setPowerToken(_power_token_address)
        return self.send_transaction(tx, cred)

    def set_rune(self, cred:Credentials, _index:uint8, _address:address) -> TxReceipt:
        tx = self.contract.functions.setRune(_index, _address)
        return self.send_transaction(tx, cred)

    def set_stat_science_address(self, cred:Credentials, _stat_science_address:address) -> TxReceipt:
        tx = self.contract.functions.setStatScienceAddress(_stat_science_address)
        return self.send_transaction(tx, cred)

    def set_token_unlocker(self, cred:Credentials, _token_unlocker_address:address) -> TxReceipt:
        tx = self.contract.functions.setTokenUnlocker(_token_unlocker_address)
        return self.send_transaction(tx, cred)

    def unpause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unpause()
        return self.send_transaction(tx, cred)

    def active_attunement_crystals(self, a:address) -> bool:
        return self.contract.functions.activeAttunementCrystals(a).call()

    def hero_to_meditation(self, a:uint256) -> uint256:
        return self.contract.functions.heroToMeditation(a).call()

    def profile_active_meditations(self, a:address, b:uint256) -> Tuple[uint256, address, uint256, uint8, uint8, uint8, address, uint256, uint8]:
        return self.contract.functions.profileActiveMeditations(a, b).call()

    def runes(self, a:uint256) -> address:
        return self.contract.functions.runes(a).call()

    def token_unlocker_address(self) -> address:
        return self.contract.functions.tokenUnlockerAddress().call()

    def complete_meditation(self, cred:Credentials, _hero_id:uint256) -> TxReceipt:
        tx = self.contract.functions.completeMeditation(_hero_id)
        return self.send_transaction(tx, cred)

    def get_active_meditations(self, _address:address) -> Sequence[tuple]:
        return self.contract.functions.getActiveMeditations(_address).call()

    def get_hero_meditation(self, _hero_id:uint256) -> tuple:
        return self.contract.functions.getHeroMeditation(_hero_id).call()

    def get_meditation(self, _id:uint256) -> tuple:
        return self.contract.functions.getMeditation(_id).call()

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def set_fees(self, cred:Credentials, _fee_addresses:Sequence[address], _fee_percents:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.setFees(_fee_addresses, _fee_percents)
        return self.send_transaction(tx, cred)

    def _get_required_runes(self, _level:uint16) -> Sequence[uint16]:
        return self.contract.functions._getRequiredRunes(_level).call()

    def start_meditation(self, cred:Credentials, _hero_id:uint256, _primary_stat:uint8, _secondary_stat:uint8, _tertiary_stat:uint8, _attunement_crystal:address) -> TxReceipt:
        tx = self.contract.functions.startMeditation(_hero_id, _primary_stat, _secondary_stat, _tertiary_stat, _attunement_crystal)
        return self.send_transaction(tx, cred)

    def start_meditation_with_locked(self, cred:Credentials, _hero_id:uint256, _primary_stat:uint8, _secondary_stat:uint8, _tertiary_stat:uint8, _attunement_crystal:address) -> TxReceipt:
        tx = self.contract.functions.startMeditationWithLocked(_hero_id, _primary_stat, _secondary_stat, _tertiary_stat, _attunement_crystal)
        return self.send_transaction(tx, cred)