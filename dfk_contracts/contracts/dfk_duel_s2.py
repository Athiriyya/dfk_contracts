
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x9EEaBBcf42F0c4900d302544Cce599811C2De2b9",
    "sd": ""
}

ABI = """[
    {"name": "cancelDuelEntry", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setDuelCompleteBlocks", "type": "function", "inputs": [{"name": "_blocks", "type": "uint16", "internalType": "uint16"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setGoldPot", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setLoseWinThresholds", "type": "function", "inputs": [{"name": "_lose", "type": "uint64", "internalType": "uint64"}, {"name": "_win", "type": "uint64", "internalType": "uint64"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setMatchLimit", "type": "function", "inputs": [{"name": "_limit", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setMatchMaker", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}, {"name": "_access", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setMatchThreshold", "type": "function", "inputs": [{"name": "_lobby", "type": "uint256", "internalType": "uint256"}, {"name": "_threshold", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setModerator", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}, {"name": "_access", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setOpenMatchmaking", "type": "function", "inputs": [{"name": "_open", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setScore", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}, {"name": "_type", "type": "uint256", "internalType": "uint256"}, {"name": "_score", "type": "uint64", "internalType": "uint64"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setSeasonStartAndDuration", "type": "function", "inputs": [{"name": "_start", "type": "uint256", "internalType": "uint256"}, {"name": "_duration", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setStatScienceAddress", "type": "function", "inputs": [{"name": "_statScienceAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTimeoutThreshold", "type": "function", "inputs": [{"name": "_threshold", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTypeAllowed", "type": "function", "inputs": [{"name": "_lobby", "type": "uint256", "internalType": "uint256"}, {"name": "_allowed", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "completeDuel", "type": "function", "inputs": [{"name": "_duelId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getCurrentClassBonuses", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8[6][2]", "internalType": "uint8[6][2]"}], "stateMutability": "view"},
    {"name": "completeDuelAdmin", "type": "function", "inputs": [{"name": "_duelId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getKeyExists", "type": "function", "inputs": [{"name": "_type", "type": "uint256", "internalType": "uint256"}, {"name": "_key", "type": "uint256", "internalType": "uint256"}, {"name": "_value", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "enterDuelLobby", "type": "function", "inputs": [{"name": "_type", "type": "uint256", "internalType": "uint256"}, {"name": "_heroIds", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_tokenFee", "type": "uint256", "internalType": "uint256"}, {"name": "_background", "type": "uint8", "internalType": "uint8"}, {"name": "_stat", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "DuelCompleted", "type": "event", "inputs": [{"name": "duelId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player1", "type": "address", "indexed": true, "internalType": "address"}, {"name": "player2", "type": "address", "indexed": true, "internalType": "address"}, {"name": "duel", "type": "tuple", "indexed": false, "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player1", "type": "address", "internalType": "address"}, {"name": "player2", "type": "address", "internalType": "address"}, {"name": "player1DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "player2DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "winner", "type": "address", "internalType": "address"}, {"name": "player1Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player2Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "player1ScoreChange", "type": "tuple", "components": [{"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "base", "type": "uint16", "internalType": "uint16"}, {"name": "streakBonus", "type": "uint32", "internalType": "uint32"}, {"name": "miscBonus", "type": "uint16", "internalType": "uint16"}, {"name": "diffBonus", "type": "uint32", "internalType": "uint32"}, {"name": "scoreBefore", "type": "uint64", "internalType": "uint64"}, {"name": "scoreAfter", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.PlayerScoreChange"}], "internalType": "struct IDuelS2Types.Duel"}], "anonymous": false},
    {"name": "DuelCreated", "type": "event", "inputs": [{"name": "duelId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player1", "type": "address", "indexed": true, "internalType": "address"}, {"name": "player2", "type": "address", "indexed": true, "internalType": "address"}, {"name": "duel", "type": "tuple", "indexed": false, "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player1", "type": "address", "internalType": "address"}, {"name": "player2", "type": "address", "internalType": "address"}, {"name": "player1DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "player2DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "winner", "type": "address", "internalType": "address"}, {"name": "player1Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player2Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "player1ScoreChange", "type": "tuple", "components": [{"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "base", "type": "uint16", "internalType": "uint16"}, {"name": "streakBonus", "type": "uint32", "internalType": "uint32"}, {"name": "miscBonus", "type": "uint16", "internalType": "uint16"}, {"name": "diffBonus", "type": "uint32", "internalType": "uint32"}, {"name": "scoreBefore", "type": "uint64", "internalType": "uint64"}, {"name": "scoreAfter", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.PlayerScoreChange"}], "internalType": "struct IDuelS2Types.Duel"}], "anonymous": false},
    {"name": "DuelEntryCreated", "type": "event", "inputs": [{"name": "id", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroIds", "type": "uint256[]", "indexed": false, "internalType": "uint256[]"}], "anonymous": false},
    {"name": "DuelEntryMatched", "type": "event", "inputs": [{"name": "duelId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "duelEntryId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player1", "type": "address", "indexed": true, "internalType": "address"}, {"name": "player2", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "PlayerScoreChanged", "type": "event", "inputs": [{"name": "duelId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "playerScoreChange", "type": "tuple", "indexed": false, "components": [{"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "base", "type": "uint16", "internalType": "uint16"}, {"name": "streakBonus", "type": "uint32", "internalType": "uint32"}, {"name": "miscBonus", "type": "uint16", "internalType": "uint16"}, {"name": "diffBonus", "type": "uint32", "internalType": "uint32"}, {"name": "scoreBefore", "type": "uint64", "internalType": "uint64"}, {"name": "scoreAfter", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.PlayerScoreChange"}], "anonymous": false},
    {"name": "TurnOutcome", "type": "event", "inputs": [{"name": "duelId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player1HeroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player2HeroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "turnResult", "type": "tuple", "indexed": false, "components": [{"name": "turn", "type": "uint16", "internalType": "uint16"}, {"name": "player1HeroId", "type": "uint256", "internalType": "uint256"}, {"name": "player2HeroId", "type": "uint256", "internalType": "uint256"}, {"name": "stat", "type": "uint8", "internalType": "uint8"}, {"name": "background", "type": "uint8", "internalType": "uint8"}, {"name": "hero1Score", "type": "tuple", "components": [{"name": "roll", "type": "uint8", "internalType": "uint8"}, {"name": "elementBonus", "type": "uint16", "internalType": "uint16"}, {"name": "statValue", "type": "uint16", "internalType": "uint16"}, {"name": "backgroundBonus", "type": "uint16", "internalType": "uint16"}, {"name": "classBonus", "type": "uint16", "internalType": "uint16"}, {"name": "subclassBonus", "type": "uint16", "internalType": "uint16"}, {"name": "total", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IDuelS2Types.HeroTurnScore"}, {"name": "hero2Score", "type": "tuple", "components": [{"name": "roll", "type": "uint8", "internalType": "uint8"}, {"name": "elementBonus", "type": "uint16", "internalType": "uint16"}, {"name": "statValue", "type": "uint16", "internalType": "uint16"}, {"name": "backgroundBonus", "type": "uint16", "internalType": "uint16"}, {"name": "classBonus", "type": "uint16", "internalType": "uint16"}, {"name": "subclassBonus", "type": "uint16", "internalType": "uint16"}, {"name": "total", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IDuelS2Types.HeroTurnScore"}, {"name": "winnerHeroId", "type": "uint256", "internalType": "uint256"}, {"name": "winnerPlayer", "type": "address", "internalType": "address"}], "internalType": "struct IDuelS2Types.TurnResult"}], "anonymous": false},
    {"name": "getActiveDuels", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player1", "type": "address", "internalType": "address"}, {"name": "player2", "type": "address", "internalType": "address"}, {"name": "player1DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "player2DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "winner", "type": "address", "internalType": "address"}, {"name": "player1Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player2Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "player1ScoreChange", "type": "tuple", "components": [{"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "base", "type": "uint16", "internalType": "uint16"}, {"name": "streakBonus", "type": "uint32", "internalType": "uint32"}, {"name": "miscBonus", "type": "uint16", "internalType": "uint16"}, {"name": "diffBonus", "type": "uint32", "internalType": "uint32"}, {"name": "scoreBefore", "type": "uint64", "internalType": "uint64"}, {"name": "scoreAfter", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.PlayerScoreChange"}], "internalType": "struct IDuelS2Types.Duel[]"}], "stateMutability": "view"},
    {"name": "getChallenges", "type": "function", "inputs": [{"name": "_profile", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player1", "type": "address", "internalType": "address"}, {"name": "player2", "type": "address", "internalType": "address"}, {"name": "player1DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "player2DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "winner", "type": "address", "internalType": "address"}, {"name": "player1Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player2Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "player1ScoreChange", "type": "tuple", "components": [{"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "base", "type": "uint16", "internalType": "uint16"}, {"name": "streakBonus", "type": "uint32", "internalType": "uint32"}, {"name": "miscBonus", "type": "uint16", "internalType": "uint16"}, {"name": "diffBonus", "type": "uint32", "internalType": "uint32"}, {"name": "scoreBefore", "type": "uint64", "internalType": "uint64"}, {"name": "scoreAfter", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.PlayerScoreChange"}], "internalType": "struct IDuelS2Types.Duel[]"}], "stateMutability": "view"},
    {"name": "getCurrentHeroScoreDuelId", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getDuel", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player1", "type": "address", "internalType": "address"}, {"name": "player2", "type": "address", "internalType": "address"}, {"name": "player1DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "player2DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "winner", "type": "address", "internalType": "address"}, {"name": "player1Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player2Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "player1ScoreChange", "type": "tuple", "components": [{"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "base", "type": "uint16", "internalType": "uint16"}, {"name": "streakBonus", "type": "uint32", "internalType": "uint32"}, {"name": "miscBonus", "type": "uint16", "internalType": "uint16"}, {"name": "diffBonus", "type": "uint32", "internalType": "uint32"}, {"name": "scoreBefore", "type": "uint64", "internalType": "uint64"}, {"name": "scoreAfter", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.PlayerScoreChange"}], "internalType": "struct IDuelS2Types.Duel"}], "stateMutability": "view"},
    {"name": "getDuelEntry", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroPower", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint256", "internalType": "uint256"}, {"name": "scoreAfter", "type": "uint256", "internalType": "uint256"}, {"name": "tokenFee", "type": "uint256", "internalType": "uint256"}, {"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "custom1", "type": "uint256", "internalType": "uint256"}, {"name": "custom2", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "winStreak", "type": "uint64", "internalType": "uint64"}, {"name": "loseStreak", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.DuelEntry"}], "stateMutability": "view"},
    {"name": "getDuelHistory", "type": "function", "inputs": [{"name": "_profile", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[100]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player1", "type": "address", "internalType": "address"}, {"name": "player2", "type": "address", "internalType": "address"}, {"name": "player1DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "player2DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "winner", "type": "address", "internalType": "address"}, {"name": "player1Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player2Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "player1ScoreChange", "type": "tuple", "components": [{"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "base", "type": "uint16", "internalType": "uint16"}, {"name": "streakBonus", "type": "uint32", "internalType": "uint32"}, {"name": "miscBonus", "type": "uint16", "internalType": "uint16"}, {"name": "diffBonus", "type": "uint32", "internalType": "uint32"}, {"name": "scoreBefore", "type": "uint64", "internalType": "uint64"}, {"name": "scoreAfter", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.PlayerScoreChange"}], "internalType": "struct IDuelS2Types.Duel[100]"}], "stateMutability": "view"},
    {"name": "getDuelIndexP1", "type": "function", "inputs": [{"name": "_duelId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getDuelRewards", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "item", "type": "address", "internalType": "address"}, {"name": "recipient", "type": "address", "internalType": "address"}, {"name": "qty", "type": "uint256", "internalType": "uint256"}], "internalType": "struct IDuelS2Types.DuelReward[]"}], "stateMutability": "view"},
    {"name": "getDuelTurns", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "turn", "type": "uint16", "internalType": "uint16"}, {"name": "player1HeroId", "type": "uint256", "internalType": "uint256"}, {"name": "player2HeroId", "type": "uint256", "internalType": "uint256"}, {"name": "stat", "type": "uint8", "internalType": "uint8"}, {"name": "background", "type": "uint8", "internalType": "uint8"}, {"name": "hero1Score", "type": "tuple", "components": [{"name": "roll", "type": "uint8", "internalType": "uint8"}, {"name": "elementBonus", "type": "uint16", "internalType": "uint16"}, {"name": "statValue", "type": "uint16", "internalType": "uint16"}, {"name": "backgroundBonus", "type": "uint16", "internalType": "uint16"}, {"name": "classBonus", "type": "uint16", "internalType": "uint16"}, {"name": "subclassBonus", "type": "uint16", "internalType": "uint16"}, {"name": "total", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IDuelS2Types.HeroTurnScore"}, {"name": "hero2Score", "type": "tuple", "components": [{"name": "roll", "type": "uint8", "internalType": "uint8"}, {"name": "elementBonus", "type": "uint16", "internalType": "uint16"}, {"name": "statValue", "type": "uint16", "internalType": "uint16"}, {"name": "backgroundBonus", "type": "uint16", "internalType": "uint16"}, {"name": "classBonus", "type": "uint16", "internalType": "uint16"}, {"name": "subclassBonus", "type": "uint16", "internalType": "uint16"}, {"name": "total", "type": "uint16", "internalType": "uint16"}], "internalType": "struct IDuelS2Types.HeroTurnScore"}, {"name": "winnerHeroId", "type": "uint256", "internalType": "uint256"}, {"name": "winnerPlayer", "type": "address", "internalType": "address"}], "internalType": "struct IDuelS2Types.TurnResult[]"}], "stateMutability": "view"},
    {"name": "getHeroDuel", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player1", "type": "address", "internalType": "address"}, {"name": "player2", "type": "address", "internalType": "address"}, {"name": "player1DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "player2DuelEntry", "type": "uint256", "internalType": "uint256"}, {"name": "winner", "type": "address", "internalType": "address"}, {"name": "player1Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player2Heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "player1ScoreChange", "type": "tuple", "components": [{"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "base", "type": "uint16", "internalType": "uint16"}, {"name": "streakBonus", "type": "uint32", "internalType": "uint32"}, {"name": "miscBonus", "type": "uint16", "internalType": "uint16"}, {"name": "diffBonus", "type": "uint32", "internalType": "uint32"}, {"name": "scoreBefore", "type": "uint64", "internalType": "uint64"}, {"name": "scoreAfter", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.PlayerScoreChange"}], "internalType": "struct IDuelS2Types.Duel"}], "stateMutability": "view"},
    {"name": "getHeroDuelCountForDay", "type": "function", "inputs": [{"name": "_heroIds", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_duelType", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "getHeroDuelEntry", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroPower", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint256", "internalType": "uint256"}, {"name": "scoreAfter", "type": "uint256", "internalType": "uint256"}, {"name": "tokenFee", "type": "uint256", "internalType": "uint256"}, {"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "custom1", "type": "uint256", "internalType": "uint256"}, {"name": "custom2", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "winStreak", "type": "uint64", "internalType": "uint64"}, {"name": "loseStreak", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.DuelEntry"}], "stateMutability": "view"},
    {"name": "getHeroLastTimePlayed", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getHighestScore", "type": "function", "inputs": [{"name": "_type", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint64", "internalType": "uint64"}], "stateMutability": "view"},
    {"name": "getNumRanks", "type": "function", "inputs": [{"name": "_type", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "pure"},
    {"name": "getPlayerDuelEntries", "type": "function", "inputs": [{"name": "_profile", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroPower", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint256", "internalType": "uint256"}, {"name": "scoreAfter", "type": "uint256", "internalType": "uint256"}, {"name": "tokenFee", "type": "uint256", "internalType": "uint256"}, {"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "custom1", "type": "uint256", "internalType": "uint256"}, {"name": "custom2", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "winStreak", "type": "uint64", "internalType": "uint64"}, {"name": "loseStreak", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.DuelEntry[]"}], "stateMutability": "view"},
    {"name": "getPlayerRank", "type": "function", "inputs": [{"name": "_profile", "type": "address", "internalType": "address"}, {"name": "_type", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getPlayerScore", "type": "function", "inputs": [{"name": "_profile", "type": "address", "internalType": "address"}, {"name": "_type", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint64", "internalType": "uint64"}], "stateMutability": "view"},
    {"name": "getPracticeEntry", "type": "function", "inputs": [{"name": "_type", "type": "uint256", "internalType": "uint256"}, {"name": "_rank", "type": "uint8", "internalType": "uint8"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroPower", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint256", "internalType": "uint256"}, {"name": "scoreAfter", "type": "uint256", "internalType": "uint256"}, {"name": "tokenFee", "type": "uint256", "internalType": "uint256"}, {"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "custom1", "type": "uint256", "internalType": "uint256"}, {"name": "custom2", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "winStreak", "type": "uint64", "internalType": "uint64"}, {"name": "loseStreak", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.DuelEntry"}], "stateMutability": "view"},
    {"name": "getRankLevels", "type": "function", "inputs": [{"name": "_type", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint16[]", "internalType": "uint16[]"}], "stateMutability": "pure"},
    {"name": "getSeasonInfo", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getTotalDuelEntries", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getTotalDuels", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getTotalOpenDuelEntries", "type": "function", "inputs": [{"name": "_lobby", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getTotalPlayerDuels", "type": "function", "inputs": [{"name": "_profile", "type": "address", "internalType": "address"}, {"name": "_type", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint64", "internalType": "uint64"}], "stateMutability": "view"},
    {"name": "getTotalPlayerWins", "type": "function", "inputs": [{"name": "_profile", "type": "address", "internalType": "address"}, {"name": "_type", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint64", "internalType": "uint64"}], "stateMutability": "view"},
    {"name": "getWinStreaks", "type": "function", "inputs": [{"name": "_player", "type": "address", "internalType": "address"}, {"name": "_type", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getDuelEntryMatch", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}, {"name": "_randomDistance", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroPower", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint256", "internalType": "uint256"}, {"name": "scoreAfter", "type": "uint256", "internalType": "uint256"}, {"name": "tokenFee", "type": "uint256", "internalType": "uint256"}, {"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "custom1", "type": "uint256", "internalType": "uint256"}, {"name": "custom2", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "winStreak", "type": "uint64", "internalType": "uint64"}, {"name": "loseStreak", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.DuelEntry"}], "stateMutability": "view"},
    {"name": "getFirstOpenEntry", "type": "function", "inputs": [{"name": "_lobby", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroPower", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint256", "internalType": "uint256"}, {"name": "scoreAfter", "type": "uint256", "internalType": "uint256"}, {"name": "tokenFee", "type": "uint256", "internalType": "uint256"}, {"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "custom1", "type": "uint256", "internalType": "uint256"}, {"name": "custom2", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "winStreak", "type": "uint64", "internalType": "uint64"}, {"name": "loseStreak", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.DuelEntry"}], "stateMutability": "view"},
    {"name": "getNextDuelEntryMatch", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroPower", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint256", "internalType": "uint256"}, {"name": "scoreAfter", "type": "uint256", "internalType": "uint256"}, {"name": "tokenFee", "type": "uint256", "internalType": "uint256"}, {"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "custom1", "type": "uint256", "internalType": "uint256"}, {"name": "custom2", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "winStreak", "type": "uint64", "internalType": "uint64"}, {"name": "loseStreak", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.DuelEntry"}], "stateMutability": "view"},
    {"name": "getPrevDuelEntryMatch", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroPower", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint256", "internalType": "uint256"}, {"name": "scoreAfter", "type": "uint256", "internalType": "uint256"}, {"name": "tokenFee", "type": "uint256", "internalType": "uint256"}, {"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "custom1", "type": "uint256", "internalType": "uint256"}, {"name": "custom2", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "winStreak", "type": "uint64", "internalType": "uint64"}, {"name": "loseStreak", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.DuelEntry"}], "stateMutability": "view"},
    {"name": "getTreeNode", "type": "function", "inputs": [{"name": "_type", "type": "uint256", "internalType": "uint256"}, {"name": "_value", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "_parent", "type": "uint256", "internalType": "uint256"}, {"name": "_left", "type": "uint256", "internalType": "uint256"}, {"name": "_right", "type": "uint256", "internalType": "uint256"}, {"name": "_red", "type": "bool", "internalType": "bool"}, {"name": "_keyCount", "type": "uint256", "internalType": "uint256"}, {"name": "_count", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getTreePrev", "type": "function", "inputs": [{"name": "_type", "type": "uint256", "internalType": "uint256"}, {"name": "_key", "type": "uint256", "internalType": "uint256"}, {"name": "_value", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroPower", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint256", "internalType": "uint256"}, {"name": "scoreAfter", "type": "uint256", "internalType": "uint256"}, {"name": "tokenFee", "type": "uint256", "internalType": "uint256"}, {"name": "duelId", "type": "uint256", "internalType": "uint256"}, {"name": "custom1", "type": "uint256", "internalType": "uint256"}, {"name": "custom2", "type": "uint256", "internalType": "uint256"}, {"name": "duelType", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "uint8"}, {"name": "winStreak", "type": "uint64", "internalType": "uint64"}, {"name": "loseStreak", "type": "uint64", "internalType": "uint64"}], "internalType": "struct IDuelS2Types.DuelEntry"}], "stateMutability": "view"},
    {"name": "getTreeValue", "type": "function", "inputs": [{"name": "_type", "type": "uint256", "internalType": "uint256"}, {"name": "_value", "type": "uint256", "internalType": "uint256"}, {"name": "_index", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "_key", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getTreeValueIndex", "type": "function", "inputs": [{"name": "_type", "type": "uint256", "internalType": "uint256"}, {"name": "_key", "type": "uint256", "internalType": "uint256"}, {"name": "_value", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "matchDuelEntry", "type": "function", "inputs": [{"name": "_duelEntry1ID", "type": "uint256", "internalType": "uint256"}, {"name": "_duelEntry2ID", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "matchMake", "type": "function", "inputs": [{"name": "_lobby", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "matchMakeAdmin", "type": "function", "inputs": [{"name": "_lobby", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "acceptChallenge", "type": "function", "inputs": [{"name": "_duelId", "type": "uint256", "internalType": "uint256"}, {"name": "_heroIds", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_background", "type": "uint8", "internalType": "uint8"}, {"name": "_stat", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "startPracticeDuel", "type": "function", "inputs": [{"name": "_type", "type": "uint256", "internalType": "uint256"}, {"name": "_heroIds", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_rank", "type": "uint8", "internalType": "uint8"}, {"name": "_background", "type": "uint8", "internalType": "uint8"}, {"name": "_stat", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "startPrivateDuel", "type": "function", "inputs": [{"name": "_type", "type": "uint256", "internalType": "uint256"}, {"name": "_heroIds", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_opponent", "type": "address", "internalType": "address"}, {"name": "_background", "type": "uint8", "internalType": "uint8"}, {"name": "_stat", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "init", "type": "function", "inputs": [{"name": "_heroCoreAddress", "type": "address", "internalType": "address"}, {"name": "_statScienceAddress", "type": "address", "internalType": "address"}, {"name": "_raffleWholesale", "type": "address", "internalType": "address"}, {"name": "_dfkGold", "type": "address", "internalType": "address"}, {"name": "_powerToken", "type": "address", "internalType": "address"}, {"name": "_goldPot", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class DFKDuelS2(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def cancel_duel_entry(self, cred:Credentials, _id:uint256) -> TxReceipt:
        tx = self.contract.functions.cancelDuelEntry(_id)
        return self.send_transaction(tx, cred)

    def set_duel_complete_blocks(self, cred:Credentials, _blocks:uint16) -> TxReceipt:
        tx = self.contract.functions.setDuelCompleteBlocks(_blocks)
        return self.send_transaction(tx, cred)

    def set_gold_pot(self, cred:Credentials, _address:address) -> TxReceipt:
        tx = self.contract.functions.setGoldPot(_address)
        return self.send_transaction(tx, cred)

    def set_lose_win_thresholds(self, cred:Credentials, _lose:uint64, _win:uint64) -> TxReceipt:
        tx = self.contract.functions.setLoseWinThresholds(_lose, _win)
        return self.send_transaction(tx, cred)

    def set_match_limit(self, cred:Credentials, _limit:uint256) -> TxReceipt:
        tx = self.contract.functions.setMatchLimit(_limit)
        return self.send_transaction(tx, cred)

    def set_match_maker(self, cred:Credentials, _address:address, _access:bool) -> TxReceipt:
        tx = self.contract.functions.setMatchMaker(_address, _access)
        return self.send_transaction(tx, cred)

    def set_match_threshold(self, cred:Credentials, _lobby:uint256, _threshold:uint256) -> TxReceipt:
        tx = self.contract.functions.setMatchThreshold(_lobby, _threshold)
        return self.send_transaction(tx, cred)

    def set_moderator(self, cred:Credentials, _address:address, _access:bool) -> TxReceipt:
        tx = self.contract.functions.setModerator(_address, _access)
        return self.send_transaction(tx, cred)

    def set_open_matchmaking(self, cred:Credentials, _open:bool) -> TxReceipt:
        tx = self.contract.functions.setOpenMatchmaking(_open)
        return self.send_transaction(tx, cred)

    def set_score(self, cred:Credentials, _address:address, _type:uint256, _score:uint64) -> TxReceipt:
        tx = self.contract.functions.setScore(_address, _type, _score)
        return self.send_transaction(tx, cred)

    def set_season_start_and_duration(self, cred:Credentials, _start:uint256, _duration:uint256) -> TxReceipt:
        tx = self.contract.functions.setSeasonStartAndDuration(_start, _duration)
        return self.send_transaction(tx, cred)

    def set_stat_science_address(self, cred:Credentials, _stat_science_address:address) -> TxReceipt:
        tx = self.contract.functions.setStatScienceAddress(_stat_science_address)
        return self.send_transaction(tx, cred)

    def set_timeout_threshold(self, cred:Credentials, _threshold:uint256) -> TxReceipt:
        tx = self.contract.functions.setTimeoutThreshold(_threshold)
        return self.send_transaction(tx, cred)

    def set_type_allowed(self, cred:Credentials, _lobby:uint256, _allowed:bool) -> TxReceipt:
        tx = self.contract.functions.setTypeAllowed(_lobby, _allowed)
        return self.send_transaction(tx, cred)

    def complete_duel(self, cred:Credentials, _duel_id:uint256) -> TxReceipt:
        tx = self.contract.functions.completeDuel(_duel_id)
        return self.send_transaction(tx, cred)

    def get_current_class_bonuses(self) -> Sequence[Sequence[uint8]]:
        return self.contract.functions.getCurrentClassBonuses().call()

    def complete_duel_admin(self, cred:Credentials, _duel_id:uint256) -> TxReceipt:
        tx = self.contract.functions.completeDuelAdmin(_duel_id)
        return self.send_transaction(tx, cred)

    def get_key_exists(self, _type:uint256, _key:uint256, _value:uint256) -> bool:
        return self.contract.functions.getKeyExists(_type, _key, _value).call()

    def enter_duel_lobby(self, cred:Credentials, _type:uint256, _hero_ids:Sequence[uint256], _token_fee:uint256, _background:uint8, _stat:uint8) -> TxReceipt:
        tx = self.contract.functions.enterDuelLobby(_type, _hero_ids, _token_fee, _background, _stat)
        return self.send_transaction(tx, cred)

    def get_active_duels(self, _address:address) -> Sequence[tuple]:
        return self.contract.functions.getActiveDuels(_address).call()

    def get_challenges(self, _profile:address) -> Sequence[tuple]:
        return self.contract.functions.getChallenges(_profile).call()

    def get_current_hero_score_duel_id(self, _hero_id:uint256) -> uint256:
        return self.contract.functions.getCurrentHeroScoreDuelId(_hero_id).call()

    def get_duel(self, _id:uint256) -> tuple:
        return self.contract.functions.getDuel(_id).call()

    def get_duel_entry(self, _id:uint256) -> tuple:
        return self.contract.functions.getDuelEntry(_id).call()

    def get_duel_history(self, _profile:address) -> Sequence[tuple]:
        return self.contract.functions.getDuelHistory(_profile).call()

    def get_duel_index_p1(self, _duel_id:uint256) -> uint256:
        return self.contract.functions.getDuelIndexP1(_duel_id).call()

    def get_duel_rewards(self, _id:uint256) -> Sequence[tuple]:
        return self.contract.functions.getDuelRewards(_id).call()

    def get_duel_turns(self, _id:uint256) -> Sequence[tuple]:
        return self.contract.functions.getDuelTurns(_id).call()

    def get_hero_duel(self, _hero_id:uint256) -> tuple:
        return self.contract.functions.getHeroDuel(_hero_id).call()

    def get_hero_duel_count_for_day(self, _hero_ids:Sequence[uint256], _duel_type:uint256) -> Sequence[uint256]:
        return self.contract.functions.getHeroDuelCountForDay(_hero_ids, _duel_type).call()

    def get_hero_duel_entry(self, _hero_id:uint256) -> tuple:
        return self.contract.functions.getHeroDuelEntry(_hero_id).call()

    def get_hero_last_time_played(self, _hero_id:uint256) -> uint256:
        return self.contract.functions.getHeroLastTimePlayed(_hero_id).call()

    def get_highest_score(self, _type:uint256) -> uint64:
        return self.contract.functions.getHighestScore(_type).call()

    def get_num_ranks(self, _type:uint256) -> uint256:
        return self.contract.functions.getNumRanks(_type).call()

    def get_player_duel_entries(self, _profile:address) -> Sequence[tuple]:
        return self.contract.functions.getPlayerDuelEntries(_profile).call()

    def get_player_rank(self, _profile:address, _type:uint256) -> uint256:
        return self.contract.functions.getPlayerRank(_profile, _type).call()

    def get_player_score(self, _profile:address, _type:uint256) -> uint64:
        return self.contract.functions.getPlayerScore(_profile, _type).call()

    def get_practice_entry(self, _type:uint256, _rank:uint8) -> tuple:
        return self.contract.functions.getPracticeEntry(_type, _rank).call()

    def get_rank_levels(self, _type:uint256) -> Sequence[uint16]:
        return self.contract.functions.getRankLevels(_type).call()

    def get_season_info(self) -> Tuple[uint256, uint256]:
        return self.contract.functions.getSeasonInfo().call()

    def get_total_duel_entries(self) -> uint256:
        return self.contract.functions.getTotalDuelEntries().call()

    def get_total_duels(self) -> uint256:
        return self.contract.functions.getTotalDuels().call()

    def get_total_open_duel_entries(self, _lobby:uint256) -> uint256:
        return self.contract.functions.getTotalOpenDuelEntries(_lobby).call()

    def get_total_player_duels(self, _profile:address, _type:uint256) -> uint64:
        return self.contract.functions.getTotalPlayerDuels(_profile, _type).call()

    def get_total_player_wins(self, _profile:address, _type:uint256) -> uint64:
        return self.contract.functions.getTotalPlayerWins(_profile, _type).call()

    def get_win_streaks(self, _player:address, _type:uint256) -> uint256:
        return self.contract.functions.getWinStreaks(_player, _type).call()

    def get_duel_entry_match(self, _id:uint256, _random_distance:uint256) -> tuple:
        return self.contract.functions.getDuelEntryMatch(_id, _random_distance).call()

    def get_first_open_entry(self, _lobby:uint256) -> tuple:
        return self.contract.functions.getFirstOpenEntry(_lobby).call()

    def get_next_duel_entry_match(self, _id:uint256) -> tuple:
        return self.contract.functions.getNextDuelEntryMatch(_id).call()

    def get_prev_duel_entry_match(self, _id:uint256) -> tuple:
        return self.contract.functions.getPrevDuelEntryMatch(_id).call()

    def get_tree_node(self, _type:uint256, _value:uint256) -> Tuple[uint256, uint256, uint256, bool, uint256, uint256]:
        return self.contract.functions.getTreeNode(_type, _value).call()

    def get_tree_prev(self, _type:uint256, _key:uint256, _value:uint256) -> tuple:
        return self.contract.functions.getTreePrev(_type, _key, _value).call()

    def get_tree_value(self, _type:uint256, _value:uint256, _index:uint256) -> uint256:
        return self.contract.functions.getTreeValue(_type, _value, _index).call()

    def get_tree_value_index(self, _type:uint256, _key:uint256, _value:uint256) -> uint256:
        return self.contract.functions.getTreeValueIndex(_type, _key, _value).call()

    def match_duel_entry(self, cred:Credentials, _duel_entry1_id:uint256, _duel_entry2_id:uint256) -> TxReceipt:
        tx = self.contract.functions.matchDuelEntry(_duel_entry1_id, _duel_entry2_id)
        return self.send_transaction(tx, cred)

    def match_make(self, cred:Credentials, _lobby:uint256) -> TxReceipt:
        tx = self.contract.functions.matchMake(_lobby)
        return self.send_transaction(tx, cred)

    def match_make_admin(self, cred:Credentials, _lobby:uint256) -> TxReceipt:
        tx = self.contract.functions.matchMakeAdmin(_lobby)
        return self.send_transaction(tx, cred)

    def accept_challenge(self, cred:Credentials, _duel_id:uint256, _hero_ids:Sequence[uint256], _background:uint8, _stat:uint8) -> TxReceipt:
        tx = self.contract.functions.acceptChallenge(_duel_id, _hero_ids, _background, _stat)
        return self.send_transaction(tx, cred)

    def start_practice_duel(self, cred:Credentials, _type:uint256, _hero_ids:Sequence[uint256], _rank:uint8, _background:uint8, _stat:uint8) -> TxReceipt:
        tx = self.contract.functions.startPracticeDuel(_type, _hero_ids, _rank, _background, _stat)
        return self.send_transaction(tx, cred)

    def start_private_duel(self, cred:Credentials, _type:uint256, _hero_ids:Sequence[uint256], _opponent:address, _background:uint8, _stat:uint8) -> TxReceipt:
        tx = self.contract.functions.startPrivateDuel(_type, _hero_ids, _opponent, _background, _stat)
        return self.send_transaction(tx, cred)

    def init(self, cred:Credentials, _hero_core_address:address, _stat_science_address:address, _raffle_wholesale:address, _dfk_gold:address, _power_token:address, _gold_pot:address) -> TxReceipt:
        tx = self.contract.functions.init(_hero_core_address, _stat_science_address, _raffle_wholesale, _dfk_gold, _power_token, _gold_pot)
        return self.send_transaction(tx, cred)