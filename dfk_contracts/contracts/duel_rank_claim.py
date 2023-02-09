
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x89789a580fdE00319493BdCdB6C65959DAB1e517",
    "sd": ""
}

ABI = """[
    {"name": "Claimed", "type": "event", "inputs": [{"name": "rankId", "type": "uint256", "internalType": "uint256", "indexed": true}, {"name": "recipient", "type": "address", "internalType": "address", "indexed": true}, {"name": "token", "type": "address", "internalType": "address", "indexed": false}, {"name": "amount", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "timestamp", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "internalType": "uint8", "indexed": false}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "RoleAdminChanged", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "previousAdminRole", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "newAdminRole", "type": "bytes32", "internalType": "bytes32", "indexed": true}], "anonymous": false},
    {"name": "RoleGranted", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "account", "type": "address", "internalType": "address", "indexed": true}, {"name": "sender", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
    {"name": "RoleRevoked", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32", "indexed": true}, {"name": "account", "type": "address", "internalType": "address", "indexed": true}, {"name": "sender", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
    {"name": "SetReward", "type": "event", "inputs": [{"name": "season", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "duelType", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "rank", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "rankId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "token", "type": "address", "internalType": "address", "indexed": false}, {"name": "amount", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "DEFAULT_ADMIN_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "_calculateRankId", "type": "function", "inputs": [{"name": "_season", "type": "uint256", "internalType": "uint256"}, {"name": "_duelType", "type": "uint256", "internalType": "uint256"}, {"name": "_rank", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "pure"},
    {"name": "claimReward", "type": "function", "inputs": [{"name": "_season", "type": "uint256", "internalType": "uint256"}, {"name": "_duelType", "type": "uint256", "internalType": "uint256"}, {"name": "_rank", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getClaimedRanks", "type": "function", "inputs": [{"name": "_season", "type": "uint256", "internalType": "uint256"}, {"name": "_duelType", "type": "uint256", "internalType": "uint256"}, {"name": "_user", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "getRewards", "type": "function", "inputs": [{"name": "_season", "type": "uint256", "internalType": "uint256"}, {"name": "_duelType", "type": "uint256", "internalType": "uint256"}, {"name": "_rank", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "tokenAddress", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "internalType": "struct DuelRankClaim.RankReward[]"}], "stateMutability": "view"},
    {"name": "getRewardsForSeasonAndDuelType", "type": "function", "inputs": [{"name": "_season", "type": "uint256", "internalType": "uint256"}, {"name": "_duelType", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple[][]", "components": [{"name": "tokenAddress", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "internalType": "struct DuelRankClaim.RankReward[][]"}], "stateMutability": "view"},
    {"name": "getRoleAdmin", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "getSeasonInfo", "type": "function", "inputs": [{"name": "_player", "type": "address", "internalType": "address"}, {"name": "_season", "type": "uint256", "internalType": "uint256"}, {"name": "_duelType", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "score", "type": "uint64", "internalType": "uint64"}, {"name": "rank", "type": "uint256", "internalType": "uint256"}, {"name": "ranks", "type": "uint16[]", "internalType": "uint16[]"}, {"name": "claimedRanks", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "rewards", "type": "tuple[][]", "components": [{"name": "tokenAddress", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "internalType": "struct DuelRankClaim.RankReward[][]"}, {"name": "startTime", "type": "uint256", "internalType": "uint256"}, {"name": "duration", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getSeasonRankRequirements", "type": "function", "inputs": [{"name": "_season", "type": "uint256", "internalType": "uint256"}, {"name": "_duelType", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint16[]", "internalType": "uint16[]"}], "stateMutability": "view"},
    {"name": "grantRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "hasRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_itemMinter", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "rankRewards", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "tokenAddress", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "renounceRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "revokeRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setDuelContract", "type": "function", "inputs": [{"name": "_season", "type": "uint256", "internalType": "uint256"}, {"name": "_duelContract", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setItemMinter", "type": "function", "inputs": [{"name": "_itemMinter", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setRankRewards", "type": "function", "inputs": [{"name": "_season", "type": "uint256", "internalType": "uint256"}, {"name": "_duelType", "type": "uint256", "internalType": "uint256"}, {"name": "_rank", "type": "uint256", "internalType": "uint256"}, {"name": "_tokenAddresses", "type": "address[]", "internalType": "address[]"}, {"name": "_amounts", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "supportsInterface", "type": "function", "inputs": [{"name": "interfaceId", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "userRankClaims", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}, {"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"}
]
"""     

class DuelRankClaim(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def _calculate_rank_id(self, _season:uint256, _duel_type:uint256, _rank:uint256) -> uint256:
        return self.contract.functions._calculateRankId(_season, _duel_type, _rank).call()

    def claim_reward(self, cred:Credentials, _season:uint256, _duel_type:uint256, _rank:uint256) -> TxReceipt:
        tx = self.contract.functions.claimReward(_season, _duel_type, _rank)
        return self.send_transaction(tx, cred)

    def get_claimed_ranks(self, _season:uint256, _duel_type:uint256, _user:address) -> Sequence[uint256]:
        return self.contract.functions.getClaimedRanks(_season, _duel_type, _user).call()

    def get_rewards(self, _season:uint256, _duel_type:uint256, _rank:uint256) -> Sequence[tuple]:
        return self.contract.functions.getRewards(_season, _duel_type, _rank).call()

    def get_rewards_for_season_and_duel_type(self, _season:uint256, _duel_type:uint256) -> Sequence[Sequence[tuple]]:
        return self.contract.functions.getRewardsForSeasonAndDuelType(_season, _duel_type).call()

    def get_season_info(self, _player:address, _season:uint256, _duel_type:uint256) -> Tuple[uint64, uint256, Sequence[uint16], Sequence[uint256], Sequence[Sequence[tuple]], uint256, uint256]:
        return self.contract.functions.getSeasonInfo(_player, _season, _duel_type).call()

    def get_season_rank_requirements(self, _season:uint256, _duel_type:uint256) -> Sequence[uint16]:
        return self.contract.functions.getSeasonRankRequirements(_season, _duel_type).call()

    def initialize(self, cred:Credentials, _item_minter:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_item_minter)
        return self.send_transaction(tx, cred)

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
        return self.send_transaction(tx, cred)

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def rank_rewards(self, a:uint256, b:uint256) -> Tuple[address, uint256]:
        return self.contract.functions.rankRewards(a, b).call()

    def set_duel_contract(self, cred:Credentials, _season:uint256, _duel_contract:address) -> TxReceipt:
        tx = self.contract.functions.setDuelContract(_season, _duel_contract)
        return self.send_transaction(tx, cred)

    def set_item_minter(self, cred:Credentials, _item_minter:address) -> TxReceipt:
        tx = self.contract.functions.setItemMinter(_item_minter)
        return self.send_transaction(tx, cred)

    def set_rank_rewards(self, cred:Credentials, _season:uint256, _duel_type:uint256, _rank:uint256, _token_addresses:Sequence[address], _amounts:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.setRankRewards(_season, _duel_type, _rank, _token_addresses, _amounts)
        return self.send_transaction(tx, cred)

    def supports_interface(self, interface_id:bytes4) -> bool:
        return self.contract.functions.supportsInterface(interface_id).call()

    def unpause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unpause()
        return self.send_transaction(tx, cred)

    def user_rank_claims(self, a:uint256, b:address) -> uint256:
        return self.contract.functions.userRankClaims(a, b).call()