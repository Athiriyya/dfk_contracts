
from ..abi_contract_wrapper import ABIContractWrapper
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x530fff22987E137e7C8D2aDcC4c15eb45b4FA752",
    "sd": "0x1Ac6Cd893EDdb6Cac15E5A9FC549335b8b449015"
}

ABI = """[
    {"name": "QuestCanceled", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "quest", "type": "tuple", "internalType": "struct Quest", "indexed": false, "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "questInstanceId", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "startAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "attempts", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum QuestStatus"}, {"name": "questType", "type": "uint8", "internalType": "uint8"}]}], "anonymous": false},
    {"name": "QuestCompleted", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "quest", "type": "tuple", "internalType": "struct Quest", "indexed": false, "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "questInstanceId", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "startAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "attempts", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum QuestStatus"}, {"name": "questType", "type": "uint8", "internalType": "uint8"}]}], "anonymous": false},
    {"name": "QuestReward", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "rewardItem", "type": "address", "indexed": false, "internalType": "address"}, {"name": "itemQuantity", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "QuestSkillUp", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "profession", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "skillUp", "type": "uint16", "indexed": false, "internalType": "uint16"}], "anonymous": false},
    {"name": "QuestStaminaSpent", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "staminaFullAt", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "staminaSpent", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "QuestStarted", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "quest", "type": "tuple", "internalType": "struct Quest", "indexed": false, "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "questInstanceId", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "startAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "attempts", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum QuestStatus"}, {"name": "questType", "type": "uint8", "internalType": "uint8"}]}, {"name": "startAtTime", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "QuestXP", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "xpEarned", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
    {"name": "QuickStudy", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "xpBefore", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "xpAfter", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "percentage", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "RewardMinted", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "reward", "type": "address", "indexed": true, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "data", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "TokenBonusAwarded", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "TrainingAttemptDone", "type": "event", "inputs": [{"name": "success", "type": "bool", "indexed": false, "internalType": "bool"}, {"name": "attempt", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "TrainingSuccessRatio", "type": "event", "inputs": [{"name": "winCount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "attempts", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "cancelQuest", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "clearActiveQuests", "type": "function", "inputs": [{"name": "_questInstanceId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "clearActiveQuestsAndHeroes", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "clearActiveQuestsAndHeroesWithOffset", "type": "function", "inputs": [{"name": "_offset", "type": "uint256", "internalType": "uint256"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "completeQuest", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getAccountActiveQuests", "type": "function", "inputs": [{"name": "_account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[]", "internalType": "struct Quest[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "questInstanceId", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "startAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "attempts", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum QuestStatus"}, {"name": "questType", "type": "uint8", "internalType": "uint8"}]}], "stateMutability": "view"},
    {"name": "getCurrentStamina", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getHeroQuest", "type": "function", "inputs": [{"name": "heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "internalType": "struct Quest", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "questInstanceId", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "startAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "attempts", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum QuestStatus"}, {"name": "questType", "type": "uint8", "internalType": "uint8"}]}], "stateMutability": "view"},
    {"name": "getQuestInstanceIds", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "heroToQuest", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "multiCompleteQuest", "type": "function", "inputs": [{"name": "_heroIds", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "multiStartQuest", "type": "function", "inputs": [{"name": "_heroIds", "type": "uint256[][]", "internalType": "uint256[][]"}, {"name": "_questInstanceId", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_attempts", "type": "uint8[]", "internalType": "uint8[]"}, {"name": "_level", "type": "uint8[]", "internalType": "uint8[]"}, {"name": "_type", "type": "uint8[]", "internalType": "uint8[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "questCounter", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "quests", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "internalType": "struct Quest", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "questInstanceId", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "startAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "attempts", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum QuestStatus"}, {"name": "questType", "type": "uint8", "internalType": "uint8"}]}], "stateMutability": "view"},
    {"name": "startQuest", "type": "function", "inputs": [{"name": "_heroIds", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_questInstanceId", "type": "uint256", "internalType": "uint256"}, {"name": "_attempts", "type": "uint8", "internalType": "uint8"}, {"name": "_level", "type": "uint8", "internalType": "uint8"}, {"name": "_type", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class QuestCoreV3(ABIContractWrapper):
    def __init__(self, chain_key:str, rpc:str):
        contract_address = CONTRACT_ADDRESS[chain_key]
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def cancel_quest(self, cred:Credentials, _hero_id:uint256) -> TxReceipt:
        tx = self.contract.functions.cancelQuest(_hero_id)
        return self.send_transaction(tx, cred)

    def clear_active_quests(self, cred:Credentials, _quest_instance_id:uint256) -> TxReceipt:
        tx = self.contract.functions.clearActiveQuests(_quest_instance_id)
        return self.send_transaction(tx, cred)

    def clear_active_quests_and_heroes(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.clearActiveQuestsAndHeroes()
        return self.send_transaction(tx, cred)

    def clear_active_quests_and_heroes_with_offset(self, cred:Credentials, _offset:uint256, _amount:uint256) -> TxReceipt:
        tx = self.contract.functions.clearActiveQuestsAndHeroesWithOffset(_offset, _amount)
        return self.send_transaction(tx, cred)

    def complete_quest(self, cred:Credentials, _hero_id:uint256) -> TxReceipt:
        tx = self.contract.functions.completeQuest(_hero_id)
        return self.send_transaction(tx, cred)

    def get_account_active_quests(self, _account:address, block_identifier:BlockIdentifier = 'latest') -> List[tuple]:
        return self.contract.functions.getAccountActiveQuests(_account).call(block_identifier=block_identifier)

    def get_current_stamina(self, _hero_id:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.getCurrentStamina(_hero_id).call(block_identifier=block_identifier)

    def get_hero_quest(self, hero_id:uint256, block_identifier:BlockIdentifier = 'latest') -> tuple:
        return self.contract.functions.getHeroQuest(hero_id).call(block_identifier=block_identifier)

    def get_quest_instance_ids(self, block_identifier:BlockIdentifier = 'latest') -> List[uint256]:
        return self.contract.functions.getQuestInstanceIds().call(block_identifier=block_identifier)

    def hero_to_quest(self, _hero_id:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.heroToQuest(_hero_id).call(block_identifier=block_identifier)

    def multi_complete_quest(self, cred:Credentials, _hero_ids:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.multiCompleteQuest(_hero_ids)
        return self.send_transaction(tx, cred)

    def multi_start_quest(self, cred:Credentials, _hero_ids:Sequence[Sequence[uint256]], _quest_instance_id:Sequence[uint256], _attempts:Sequence[uint8], _level:Sequence[uint8], _type:Sequence[uint8]) -> TxReceipt:
        tx = self.contract.functions.multiStartQuest(_hero_ids, _quest_instance_id, _attempts, _level, _type)
        return self.send_transaction(tx, cred)

    def quest_counter(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.questCounter().call(block_identifier=block_identifier)

    def quests(self, _id:uint256, block_identifier:BlockIdentifier = 'latest') -> tuple:
        return self.contract.functions.quests(_id).call(block_identifier=block_identifier)

    def start_quest(self, cred:Credentials, _hero_ids:Sequence[uint256], _quest_instance_id:uint256, _attempts:uint8, _level:uint8, _type:uint8) -> TxReceipt:
        tx = self.contract.functions.startQuest(_hero_ids, _quest_instance_id, _attempts, _level, _type)
        return self.send_transaction(tx, cred)