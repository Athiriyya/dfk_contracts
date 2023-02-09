
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xEb9B61B145D6489Be575D3603F4a704810e143dF",
    "sd": "0x268CC8248FFB72Cd5F3e73A9a20Fa2FF40EfbA61"
}

ABI = """[
    {"name": "Approval", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "approved", "type": "address", "indexed": true, "internalType": "address"}, {"name": "tokenId", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "ApprovalForAll", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "operator", "type": "address", "indexed": true, "internalType": "address"}, {"name": "approved", "type": "bool", "indexed": false, "internalType": "bool"}], "anonymous": false},
    {"name": "HeroSummoned", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "statGenes", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "HeroUpdated", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "hero", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}], "internalType": "struct IHeroTypes.SummoningInfo"}, {"name": "info", "type": "tuple", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum IHeroTypes.Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}], "internalType": "struct IHeroTypes.HeroInfo"}, {"name": "state", "type": "tuple", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum IHeroTypes.HeroStatus"}], "internalType": "struct IHeroTypes.HeroState"}, {"name": "stats", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroStats"}, {"name": "primaryStatGrowth", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroStatGrowth"}, {"name": "secondaryStatGrowth", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroStatGrowth"}, {"name": "professions", "type": "tuple", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroProfessions"}], "indexed": false, "internalType": "struct IHeroTypes.Hero"}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "Transfer", "type": "event", "inputs": [{"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "tokenId", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "approve", "type": "function", "inputs": [{"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "balanceOf", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "bridgeMint", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}, {"name": "_to", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "burn", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "createHero", "type": "function", "inputs": [{"name": "_statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "_visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "_rarity", "type": "uint8", "internalType": "enum IHeroTypes.Rarity"}, {"name": "_shiny", "type": "bool", "internalType": "bool"}, {"name": "_crystal", "type": "tuple", "components": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "summonerTears", "type": "uint8", "internalType": "uint8"}, {"name": "assistantTears", "type": "uint8", "internalType": "uint8"}, {"name": "enhancementStone", "type": "address", "internalType": "address"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}], "internalType": "struct ICrystalTypes.HeroCrystal"}, {"name": "_crystalId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "getApproved", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "getHero", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}], "internalType": "struct IHeroTypes.SummoningInfo"}, {"name": "info", "type": "tuple", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum IHeroTypes.Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}], "internalType": "struct IHeroTypes.HeroInfo"}, {"name": "state", "type": "tuple", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum IHeroTypes.HeroStatus"}], "internalType": "struct IHeroTypes.HeroState"}, {"name": "stats", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroStats"}, {"name": "primaryStatGrowth", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroStatGrowth"}, {"name": "secondaryStatGrowth", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroStatGrowth"}, {"name": "professions", "type": "tuple", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroProfessions"}], "internalType": "struct IHeroTypes.Hero"}], "stateMutability": "view"},
    {"name": "getUserHeroes", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_name", "type": "string", "internalType": "string"}, {"name": "_symbol", "type": "string", "internalType": "string"}, {"name": "_url", "type": "string", "internalType": "string"}, {"name": "_statScienceAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "name", "type": "string", "internalType": "string"}, {"name": "symbol", "type": "string", "internalType": "string"}, {"name": "baseTokenURI", "type": "string", "internalType": "string"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "isApprovedForAll", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "operator", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "mint", "type": "function", "inputs": [{"name": "to", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "name", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "ownerOf", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "postInit", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "safeTransferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setApprovalForAll", "type": "function", "inputs": [{"name": "operator", "type": "address", "internalType": "address"}, {"name": "approved", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setStatScienceAddress", "type": "function", "inputs": [{"name": "_statScienceAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "symbol", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "tokenByIndex", "type": "function", "inputs": [{"name": "index", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "tokenOfOwnerByIndex", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "index", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "tokenURI", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "totalSupply", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "transferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "updateHero", "type": "function", "inputs": [{"name": "_hero", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "summoningInfo", "type": "tuple", "components": [{"name": "summonedTime", "type": "uint256", "internalType": "uint256"}, {"name": "nextSummonTime", "type": "uint256", "internalType": "uint256"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "summons", "type": "uint32", "internalType": "uint32"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}], "internalType": "struct IHeroTypes.SummoningInfo"}, {"name": "info", "type": "tuple", "components": [{"name": "statGenes", "type": "uint256", "internalType": "uint256"}, {"name": "visualGenes", "type": "uint256", "internalType": "uint256"}, {"name": "rarity", "type": "uint8", "internalType": "enum IHeroTypes.Rarity"}, {"name": "shiny", "type": "bool", "internalType": "bool"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}, {"name": "class", "type": "uint8", "internalType": "uint8"}, {"name": "subClass", "type": "uint8", "internalType": "uint8"}], "internalType": "struct IHeroTypes.HeroInfo"}, {"name": "state", "type": "tuple", "components": [{"name": "staminaFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "hpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "mpFullAt", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint16", "internalType": "uint16"}, {"name": "xp", "type": "uint64", "internalType": "uint64"}, {"name": "currentQuest", "type": "address", "internalType": "address"}, {"name": "sp", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum IHeroTypes.HeroStatus"}], "internalType": "struct IHeroTypes.HeroState"}, {"name": "stats", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hp", "type": "uint16", "internalType": "uint16"}, {"name": "mp", "type": "uint16", "internalType": "uint16"}, {"name": "stamina", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroStats"}, {"name": "primaryStatGrowth", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroStatGrowth"}, {"name": "secondaryStatGrowth", "type": "tuple", "components": [{"name": "strength", "type": "uint16", "internalType": "uint16"}, {"name": "intelligence", "type": "uint16", "internalType": "uint16"}, {"name": "wisdom", "type": "uint16", "internalType": "uint16"}, {"name": "luck", "type": "uint16", "internalType": "uint16"}, {"name": "agility", "type": "uint16", "internalType": "uint16"}, {"name": "vitality", "type": "uint16", "internalType": "uint16"}, {"name": "endurance", "type": "uint16", "internalType": "uint16"}, {"name": "dexterity", "type": "uint16", "internalType": "uint16"}, {"name": "hpSm", "type": "uint16", "internalType": "uint16"}, {"name": "hpRg", "type": "uint16", "internalType": "uint16"}, {"name": "hpLg", "type": "uint16", "internalType": "uint16"}, {"name": "mpSm", "type": "uint16", "internalType": "uint16"}, {"name": "mpRg", "type": "uint16", "internalType": "uint16"}, {"name": "mpLg", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroStatGrowth"}, {"name": "professions", "type": "tuple", "components": [{"name": "mining", "type": "uint16", "internalType": "uint16"}, {"name": "gardening", "type": "uint16", "internalType": "uint16"}, {"name": "foraging", "type": "uint16", "internalType": "uint16"}, {"name": "fishing", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IHeroTypes.HeroProfessions"}], "internalType": "struct IHeroTypes.Hero"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class HeroCore(ABIWrapperContract):

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

    def burn(self, cred:Credentials, token_id:uint256) -> TxReceipt:
        tx = self.contract.functions.burn(token_id)
        return self.send_transaction(tx, cred)

    def create_hero(self, cred:Credentials, _stat_genes:uint256, _visual_genes:uint256, _rarity:uint8, _shiny:bool, _crystal:tuple, _crystal_id:uint256) -> TxReceipt:
        tx = self.contract.functions.createHero(_stat_genes, _visual_genes, _rarity, _shiny, _crystal, _crystal_id)
        return self.send_transaction(tx, cred)

    def get_approved(self, token_id:uint256) -> address:
        return self.contract.functions.getApproved(token_id).call()

    def get_hero(self, _id:uint256) -> tuple:
        return self.contract.functions.getHero(_id).call()

    def get_user_heroes(self, _address:address) -> Sequence[uint256]:
        return self.contract.functions.getUserHeroes(_address).call()

    def initialize(self, cred:Credentials, _name:string, _symbol:string, _url:string, _stat_science_address:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_name, _symbol, _url, _stat_science_address)
        return self.send_transaction(tx, cred)

    def initialize(self, cred:Credentials, name:string, symbol:string, base_token_uri:string) -> TxReceipt:
        tx = self.contract.functions.initialize(name, symbol, base_token_uri)
        return self.send_transaction(tx, cred)

    def is_approved_for_all(self, owner:address, operator:address) -> bool:
        return self.contract.functions.isApprovedForAll(owner, operator).call()

    def mint(self, cred:Credentials, to:address) -> TxReceipt:
        tx = self.contract.functions.mint(to)
        return self.send_transaction(tx, cred)

    def name(self) -> string:
        return self.contract.functions.name().call()

    def owner_of(self, token_id:uint256) -> address:
        return self.contract.functions.ownerOf(token_id).call()

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
        return self.send_transaction(tx, cred)

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def post_init(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.postInit()
        return self.send_transaction(tx, cred)

    def safe_transfer_from(self, cred:Credentials, _from:address, to:address, token_id:uint256) -> TxReceipt:
        tx = self.contract.functions.safeTransferFrom(_from, to, token_id)
        return self.send_transaction(tx, cred)

    def set_approval_for_all(self, cred:Credentials, operator:address, approved:bool) -> TxReceipt:
        tx = self.contract.functions.setApprovalForAll(operator, approved)
        return self.send_transaction(tx, cred)

    def set_stat_science_address(self, cred:Credentials, _stat_science_address:address) -> TxReceipt:
        tx = self.contract.functions.setStatScienceAddress(_stat_science_address)
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

    def update_hero(self, cred:Credentials, _hero:tuple) -> TxReceipt:
        tx = self.contract.functions.updateHero(_hero)
        return self.send_transaction(tx, cred)