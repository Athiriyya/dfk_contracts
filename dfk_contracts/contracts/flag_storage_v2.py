
from ..abi_contract_wrapper import ABIContractWrapper
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x75d8ba2E4725633FcdcC165332dCA04c107915cA",
    "sd": "0xeb9ff38209dCC4236DBFb3C275c0AAeEBf0B92Cf"
}

ABI = """[
    {"name": "DarkSummoningStorageSet", "type": "event", "inputs": [{"name": "heroId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "values", "type": "tuple", "internalType": "struct DarkSummoning", "components": [{"name": "levelCarryover", "type": "uint32", "internalType": "uint32"}], "indexed": false}], "anonymous": false},
    {"name": "Gen0RerollSDStorageSet", "type": "event", "inputs": [{"name": "heroId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "values", "type": "tuple", "internalType": "struct Gen0RerollSD", "components": [{"name": "player", "type": "address", "internalType": "address"}, {"name": "summonRecord", "type": "uint32", "internalType": "uint32"}, {"name": "rerolledGameGenes", "type": "bool", "internalType": "bool"}, {"name": "rerolledAppearanceGenes", "type": "bool", "internalType": "bool"}], "indexed": false}], "anonymous": false},
    {"name": "OwnershipTransferred", "type": "event", "inputs": [{"name": "previousOwner", "type": "address", "internalType": "address", "indexed": true}, {"name": "newOwner", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
    {"name": "owner", "type": "function", "inputs": [], "outputs": [{"name": "owner_", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "transferOwnership", "type": "function", "inputs": [{"name": "_newOwner", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setModerator", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}, {"name": "_access", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setUpdater", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}, {"name": "_access", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getDarkSummoningStorage", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "internalType": "struct DarkSummoning", "components": [{"name": "levelCarryover", "type": "uint32", "internalType": "uint32"}]}], "stateMutability": "view"},
    {"name": "setLevelCarryover", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}, {"name": "_value", "type": "uint32", "internalType": "uint32"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getGen0RerollSDStorage", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "internalType": "struct Gen0RerollSD", "components": [{"name": "player", "type": "address", "internalType": "address"}, {"name": "summonRecord", "type": "uint32", "internalType": "uint32"}, {"name": "rerolledGameGenes", "type": "bool", "internalType": "bool"}, {"name": "rerolledAppearanceGenes", "type": "bool", "internalType": "bool"}]}], "stateMutability": "view"},
    {"name": "setGen0RerollSDStorage", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}, {"name": "_reroll", "type": "tuple", "internalType": "struct Gen0RerollSD", "components": [{"name": "player", "type": "address", "internalType": "address"}, {"name": "summonRecord", "type": "uint32", "internalType": "uint32"}, {"name": "rerolledGameGenes", "type": "bool", "internalType": "bool"}, {"name": "rerolledAppearanceGenes", "type": "bool", "internalType": "bool"}]}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class FlagStorageV2(ABIContractWrapper):
    def __init__(self, chain_key:str, rpc:str):
        contract_address = CONTRACT_ADDRESS[chain_key]
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def owner(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.owner().call(block_identifier=block_identifier)

    def transfer_ownership(self, cred:Credentials, _new_owner:address) -> TxReceipt:
        tx = self.contract.functions.transferOwnership(_new_owner)
        return self.send_transaction(tx, cred)

    def set_moderator(self, cred:Credentials, _address:address, _access:bool) -> TxReceipt:
        tx = self.contract.functions.setModerator(_address, _access)
        return self.send_transaction(tx, cred)

    def set_updater(self, cred:Credentials, _address:address, _access:bool) -> TxReceipt:
        tx = self.contract.functions.setUpdater(_address, _access)
        return self.send_transaction(tx, cred)

    def get_dark_summoning_storage(self, _hero_id:uint256, block_identifier:BlockIdentifier = 'latest') -> tuple:
        return self.contract.functions.getDarkSummoningStorage(_hero_id).call(block_identifier=block_identifier)

    def set_level_carryover(self, cred:Credentials, _hero_id:uint256, _value:uint32) -> TxReceipt:
        tx = self.contract.functions.setLevelCarryover(_hero_id, _value)
        return self.send_transaction(tx, cred)

    def get_gen0_reroll_sd_storage(self, _hero_id:uint256, block_identifier:BlockIdentifier = 'latest') -> tuple:
        return self.contract.functions.getGen0RerollSDStorage(_hero_id).call(block_identifier=block_identifier)

    def set_gen0_reroll_sd_storage(self, cred:Credentials, _hero_id:uint256, _reroll:tuple) -> TxReceipt:
        tx = self.contract.functions.setGen0RerollSDStorage(_hero_id, _reroll)
        return self.send_transaction(tx, cred)