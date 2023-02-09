
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xE9AbfBC143d7cef74b5b793ec5907fa62ca53154",
    "sd": "0x8dc58d6327E1f65b18B82EDFb01A361f3AAEf624"
}

ABI = """[
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "QuestCanceled", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "quest", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "questAddress", "type": "address", "internalType": "address"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "startAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "attempts", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum QuestStatus"}], "indexed": false, "internalType": "struct Quest"}], "anonymous": false},
    {"name": "QuestCompleted", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "quest", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "questAddress", "type": "address", "internalType": "address"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "startAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "attempts", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum QuestStatus"}], "indexed": false, "internalType": "struct Quest"}], "anonymous": false},
    {"name": "QuestReward", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "rewardItem", "type": "address", "indexed": false, "internalType": "address"}, {"name": "itemQuantity", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "QuestSkillUp", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "profession", "type": "uint8", "indexed": false, "internalType": "uint8"}, {"name": "skillUp", "type": "uint16", "indexed": false, "internalType": "uint16"}], "anonymous": false},
    {"name": "QuestStaminaSpent", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "staminaFullAt", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "staminaSpent", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "QuestStarted", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "quest", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "questAddress", "type": "address", "internalType": "address"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "startAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "attempts", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum QuestStatus"}], "indexed": false, "internalType": "struct Quest"}, {"name": "startAtTime", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "QuestXP", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "xpEarned", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
    {"name": "RewardMinted", "type": "event", "inputs": [{"name": "questId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "reward", "type": "address", "indexed": true, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "data", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "TrainingAttemptDone", "type": "event", "inputs": [{"name": "success", "type": "bool", "indexed": false, "internalType": "bool"}, {"name": "attempt", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "TrainingSuccessRatio", "type": "event", "inputs": [{"name": "winCount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "attempts", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "activateQuest", "type": "function", "inputs": [{"name": "_questAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "activeAccountQuests", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "questAddress", "type": "address", "internalType": "address"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "startAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "attempts", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum QuestStatus"}], "stateMutability": "view"},
    {"name": "cancelQuest", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "clearActiveQuests", "type": "function", "inputs": [{"name": "_questAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "clearActiveQuestsAndHeroes", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "clearActiveQuestsAndHeroesWithOffset", "type": "function", "inputs": [{"name": "_offset", "type": "uint256", "internalType": "uint256"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "completeQuest", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getAccountActiveQuests", "type": "function", "inputs": [{"name": "_account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "questAddress", "type": "address", "internalType": "address"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "startAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "attempts", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum QuestStatus"}], "internalType": "struct Quest[]"}], "stateMutability": "view"},
    {"name": "getCurrentStamina", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getHeroQuest", "type": "function", "inputs": [{"name": "heroId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "questAddress", "type": "address", "internalType": "address"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "heroes", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "startAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "attempts", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum QuestStatus"}], "internalType": "struct Quest"}], "stateMutability": "view"},
    {"name": "getQuestContracts", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address[]", "internalType": "address[]"}], "stateMutability": "view"},
    {"name": "heroCore", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IHeroCoreUpgradeable"}], "stateMutability": "view"},
    {"name": "heroToQuest", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_heroCoreAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "isQuest", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "multiCompleteQuest", "type": "function", "inputs": [{"name": "_heroIds", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "multiStartQuest", "type": "function", "inputs": [{"name": "_questAddress", "type": "address[]", "internalType": "address[]"}, {"name": "_heroIds", "type": "uint256[][]", "internalType": "uint256[][]"}, {"name": "_attempts", "type": "uint8[]", "internalType": "uint8[]"}, {"name": "_level", "type": "uint8[]", "internalType": "uint8[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "questCounter", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "questRewarder", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "quests", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "questAddress", "type": "address", "internalType": "address"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "player", "type": "address", "internalType": "address"}, {"name": "startBlock", "type": "uint256", "internalType": "uint256"}, {"name": "startAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "completeAtTime", "type": "uint256", "internalType": "uint256"}, {"name": "attempts", "type": "uint8", "internalType": "uint8"}, {"name": "status", "type": "uint8", "internalType": "enum QuestStatus"}], "stateMutability": "view"},
    {"name": "setQuestRewarder", "type": "function", "inputs": [{"name": "_questRewarder", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTimePerStamina", "type": "function", "inputs": [{"name": "_timePerStamina", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "startQuest", "type": "function", "inputs": [{"name": "_heroIds", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_questAddress", "type": "address", "internalType": "address"}, {"name": "_attempts", "type": "uint8", "internalType": "uint8"}, {"name": "_level", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "timePerStamina", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"}
]
"""     

class QuestCore(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def activate_quest(self, cred:Credentials, _quest_address:address) -> TxReceipt:
        tx = self.contract.functions.activateQuest(_quest_address)
        return self.send_transaction(tx, cred)

    def active_account_quests(self, a:address, b:address, c:uint256) -> Tuple[uint256, address, uint8, address, uint256, uint256, uint256, uint8, uint8]:
        return self.contract.functions.activeAccountQuests(a, b, c).call()

    def cancel_quest(self, cred:Credentials, _hero_id:uint256) -> TxReceipt:
        tx = self.contract.functions.cancelQuest(_hero_id)
        return self.send_transaction(tx, cred)

    def clear_active_quests(self, cred:Credentials, _quest_address:address) -> TxReceipt:
        tx = self.contract.functions.clearActiveQuests(_quest_address)
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

    def get_account_active_quests(self, _account:address) -> Sequence[tuple]:
        return self.contract.functions.getAccountActiveQuests(_account).call()

    def get_current_stamina(self, _hero_id:uint256) -> uint256:
        return self.contract.functions.getCurrentStamina(_hero_id).call()

    def get_hero_quest(self, hero_id:uint256) -> tuple:
        return self.contract.functions.getHeroQuest(hero_id).call()

    def get_quest_contracts(self) -> Sequence[address]:
        return self.contract.functions.getQuestContracts().call()

    def hero_core(self) -> address:
        return self.contract.functions.heroCore().call()

    def hero_to_quest(self, a:uint256) -> uint256:
        return self.contract.functions.heroToQuest(a).call()

    def initialize(self, cred:Credentials, _hero_core_address:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_hero_core_address)
        return self.send_transaction(tx, cred)

    def is_quest(self, a:address) -> bool:
        return self.contract.functions.isQuest(a).call()

    def multi_complete_quest(self, cred:Credentials, _hero_ids:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.multiCompleteQuest(_hero_ids)
        return self.send_transaction(tx, cred)

    def multi_start_quest(self, cred:Credentials, _quest_address:Sequence[address], _hero_ids:Sequence[Sequence[uint256]], _attempts:Sequence[uint8], _level:Sequence[uint8]) -> TxReceipt:
        tx = self.contract.functions.multiStartQuest(_quest_address, _hero_ids, _attempts, _level)
        return self.send_transaction(tx, cred)

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def quest_counter(self) -> uint256:
        return self.contract.functions.questCounter().call()

    def quest_rewarder(self) -> address:
        return self.contract.functions.questRewarder().call()

    def quests(self, a:uint256) -> Tuple[uint256, address, uint8, address, uint256, uint256, uint256, uint8, uint8]:
        return self.contract.functions.quests(a).call()

    def set_quest_rewarder(self, cred:Credentials, _quest_rewarder:address) -> TxReceipt:
        tx = self.contract.functions.setQuestRewarder(_quest_rewarder)
        return self.send_transaction(tx, cred)

    def set_time_per_stamina(self, cred:Credentials, _time_per_stamina:uint256) -> TxReceipt:
        tx = self.contract.functions.setTimePerStamina(_time_per_stamina)
        return self.send_transaction(tx, cred)

    def start_quest(self, cred:Credentials, _hero_ids:Sequence[uint256], _quest_address:address, _attempts:uint8, _level:uint8) -> TxReceipt:
        tx = self.contract.functions.startQuest(_hero_ids, _quest_address, _attempts, _level)
        return self.send_transaction(tx, cred)

    def time_per_stamina(self) -> uint256:
        return self.contract.functions.timePerStamina().call()