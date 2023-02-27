
from ..abi_contract_wrapper import ABIContractWrapper
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x57Dec9cC7f492d6583c773e2E7ad66dcDc6940Fb",
    "sd": "0xad2ea7b7e49be15918E4917736E86ff7feA57a6A"
}

ABI = """[
    {"type": "constructor", "inputs": [{"name": "_govToken", "type": "address", "internalType": "contract ICrystalToken"}, {"name": "_devaddr", "type": "address", "internalType": "address"}, {"name": "_liquidityaddr", "type": "address", "internalType": "address"}, {"name": "_comfundaddr", "type": "address", "internalType": "address"}, {"name": "_founderaddr", "type": "address", "internalType": "address"}, {"name": "_rewardPerSecond", "type": "uint256", "internalType": "uint256"}, {"name": "_startTimestamp", "type": "uint256", "internalType": "uint256"}, {"name": "_halvingAfterTimestamp", "type": "uint256", "internalType": "uint256"}, {"name": "_rewardMultiplier", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_timeDeltaStartStage", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_timeDeltaEndStage", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_userFeeStage", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_devFeeStage", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "nonpayable"},
    {"name": "Deposit", "type": "event", "inputs": [{"name": "user", "type": "address", "indexed": true, "internalType": "address"}, {"name": "pid", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "EmergencyWithdraw", "type": "event", "inputs": [{"name": "user", "type": "address", "indexed": true, "internalType": "address"}, {"name": "pid", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "OwnershipTransferred", "type": "event", "inputs": [{"name": "previousOwner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "newOwner", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "SendGovernanceTokenReward", "type": "event", "inputs": [{"name": "user", "type": "address", "indexed": true, "internalType": "address"}, {"name": "pid", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "lockAmount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Withdraw", "type": "event", "inputs": [{"name": "user", "type": "address", "indexed": true, "internalType": "address"}, {"name": "pid", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "FINISH_BONUS_AT_TIMESTAMP", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "HALVING_AT_TIMESTAMP", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "PERCENT_FOR_COM", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "PERCENT_FOR_DEV", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "PERCENT_FOR_FOUNDERS", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "PERCENT_FOR_LP", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "PERCENT_LOCK_BONUS_REWARD", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "REWARD_MULTIPLIER", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "REWARD_PER_SECOND", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "START_TIMESTAMP", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "add", "type": "function", "inputs": [{"name": "_allocPoint", "type": "uint256", "internalType": "uint256"}, {"name": "_lpToken", "type": "address", "internalType": "contract IERC20"}, {"name": "_withUpdate", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "addAuthorized", "type": "function", "inputs": [{"name": "_toAdd", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "authorized", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "bonusFinishUpdate", "type": "function", "inputs": [{"name": "_newFinish", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "claimReward", "type": "function", "inputs": [{"name": "_pid", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "claimRewards", "type": "function", "inputs": [{"name": "_pids", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "comUpdate", "type": "function", "inputs": [{"name": "_newCom", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "comfundaddr", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "deposit", "type": "function", "inputs": [{"name": "_pid", "type": "uint256", "internalType": "uint256"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "dev", "type": "function", "inputs": [{"name": "_devaddr", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "devFeeStage", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "devaddr", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "emergencyWithdraw", "type": "function", "inputs": [{"name": "_pid", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "founderUpdate", "type": "function", "inputs": [{"name": "_newFounder", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "founderaddr", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "getLockPercentage", "type": "function", "inputs": [{"name": "_from", "type": "uint256", "internalType": "uint256"}, {"name": "_to", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getMultiplier", "type": "function", "inputs": [{"name": "_from", "type": "uint256", "internalType": "uint256"}, {"name": "_to", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getNewRewardPerSecond", "type": "function", "inputs": [{"name": "pid1", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getPoolReward", "type": "function", "inputs": [{"name": "_from", "type": "uint256", "internalType": "uint256"}, {"name": "_to", "type": "uint256", "internalType": "uint256"}, {"name": "_allocPoint", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "forDev", "type": "uint256", "internalType": "uint256"}, {"name": "forFarmer", "type": "uint256", "internalType": "uint256"}, {"name": "forLP", "type": "uint256", "internalType": "uint256"}, {"name": "forCom", "type": "uint256", "internalType": "uint256"}, {"name": "forFounders", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "govToken", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract ICrystalToken"}], "stateMutability": "view"},
    {"name": "halvingUpdate", "type": "function", "inputs": [{"name": "_newHalving", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "liquidityaddr", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "lockUpdate", "type": "function", "inputs": [{"name": "_newlock", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "lockcomUpdate", "type": "function", "inputs": [{"name": "_newcomlock", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "lockdevUpdate", "type": "function", "inputs": [{"name": "_newdevlock", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "lockfounderUpdate", "type": "function", "inputs": [{"name": "_newfounderlock", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "locklpUpdate", "type": "function", "inputs": [{"name": "_newlplock", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "lpUpdate", "type": "function", "inputs": [{"name": "_newLP", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "massUpdatePools", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "owner", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "pendingReward", "type": "function", "inputs": [{"name": "_pid", "type": "uint256", "internalType": "uint256"}, {"name": "_user", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "poolExistence", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "contract IERC20"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "poolId1", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "poolInfo", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "lpToken", "type": "address", "internalType": "contract IERC20"}, {"name": "allocPoint", "type": "uint256", "internalType": "uint256"}, {"name": "lastRewardTimestamp", "type": "uint256", "internalType": "uint256"}, {"name": "accGovTokenPerShare", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "poolLength", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "reclaimTokenOwnership", "type": "function", "inputs": [{"name": "_newOwner", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "removeAuthorized", "type": "function", "inputs": [{"name": "_toRemove", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "renounceOwnership", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "rewardMulUpdate", "type": "function", "inputs": [{"name": "_newMulReward", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "rewardUpdate", "type": "function", "inputs": [{"name": "_newReward", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "set", "type": "function", "inputs": [{"name": "_pid", "type": "uint256", "internalType": "uint256"}, {"name": "_allocPoint", "type": "uint256", "internalType": "uint256"}, {"name": "_withUpdate", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setDevFeeStage", "type": "function", "inputs": [{"name": "_devFees", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setStageEnds", "type": "function", "inputs": [{"name": "_timeEnds", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setStageStarts", "type": "function", "inputs": [{"name": "_timeStarts", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setUserFeeStage", "type": "function", "inputs": [{"name": "_userFees", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "startTimestampUpdate", "type": "function", "inputs": [{"name": "_newstarttimestamp", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "timeDeltaEndStage", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "timeDeltaStartStage", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "totalAllocPoint", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "transferOwnership", "type": "function", "inputs": [{"name": "newOwner", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "updatePool", "type": "function", "inputs": [{"name": "_pid", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "usdOracle", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "userDelta", "type": "function", "inputs": [{"name": "_pid", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "userFeeStage", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "userInfo", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}, {"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "amount", "type": "uint256", "internalType": "uint256"}, {"name": "rewardDebt", "type": "uint256", "internalType": "uint256"}, {"name": "rewardDebtAtTimestamp", "type": "uint256", "internalType": "uint256"}, {"name": "lastWithdrawTimestamp", "type": "uint256", "internalType": "uint256"}, {"name": "firstDepositTimestamp", "type": "uint256", "internalType": "uint256"}, {"name": "timeDelta", "type": "uint256", "internalType": "uint256"}, {"name": "lastDepositTimestamp", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "withdraw", "type": "function", "inputs": [{"name": "_pid", "type": "uint256", "internalType": "uint256"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class MasterGardener(ABIContractWrapper):
    def __init__(self, chain_key:str, rpc:str):
        contract_address = CONTRACT_ADDRESS[chain_key]
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def finish_bonus_at_timestamp(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.FINISH_BONUS_AT_TIMESTAMP().call(block_identifier=block_identifier)

    def halving_at_timestamp(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.HALVING_AT_TIMESTAMP(a).call(block_identifier=block_identifier)

    def percent_for_com(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.PERCENT_FOR_COM().call(block_identifier=block_identifier)

    def percent_for_dev(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.PERCENT_FOR_DEV().call(block_identifier=block_identifier)

    def percent_for_founders(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.PERCENT_FOR_FOUNDERS().call(block_identifier=block_identifier)

    def percent_for_lp(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.PERCENT_FOR_LP().call(block_identifier=block_identifier)

    def percent_lock_bonus_reward(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.PERCENT_LOCK_BONUS_REWARD(a).call(block_identifier=block_identifier)

    def reward_multiplier(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.REWARD_MULTIPLIER(a).call(block_identifier=block_identifier)

    def reward_per_second(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.REWARD_PER_SECOND().call(block_identifier=block_identifier)

    def start_timestamp(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.START_TIMESTAMP().call(block_identifier=block_identifier)

    def add(self, cred:Credentials, _alloc_point:uint256, _lp_token:address, _with_update:bool) -> TxReceipt:
        tx = self.contract.functions.add(_alloc_point, _lp_token, _with_update)
        return self.send_transaction(tx, cred)

    def add_authorized(self, cred:Credentials, _to_add:address) -> TxReceipt:
        tx = self.contract.functions.addAuthorized(_to_add)
        return self.send_transaction(tx, cred)

    def authorized(self, a:address, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.authorized(a).call(block_identifier=block_identifier)

    def bonus_finish_update(self, cred:Credentials, _new_finish:uint256) -> TxReceipt:
        tx = self.contract.functions.bonusFinishUpdate(_new_finish)
        return self.send_transaction(tx, cred)

    def claim_reward(self, cred:Credentials, _pid:uint256) -> TxReceipt:
        tx = self.contract.functions.claimReward(_pid)
        return self.send_transaction(tx, cred)

    def claim_rewards(self, cred:Credentials, _pids:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.claimRewards(_pids)
        return self.send_transaction(tx, cred)

    def com_update(self, cred:Credentials, _new_com:address) -> TxReceipt:
        tx = self.contract.functions.comUpdate(_new_com)
        return self.send_transaction(tx, cred)

    def comfundaddr(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.comfundaddr().call(block_identifier=block_identifier)

    def deposit(self, cred:Credentials, _pid:uint256, _amount:uint256) -> TxReceipt:
        tx = self.contract.functions.deposit(_pid, _amount)
        return self.send_transaction(tx, cred)

    def dev(self, cred:Credentials, _devaddr:address) -> TxReceipt:
        tx = self.contract.functions.dev(_devaddr)
        return self.send_transaction(tx, cred)

    def dev_fee_stage(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.devFeeStage(a).call(block_identifier=block_identifier)

    def devaddr(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.devaddr().call(block_identifier=block_identifier)

    def emergency_withdraw(self, cred:Credentials, _pid:uint256) -> TxReceipt:
        tx = self.contract.functions.emergencyWithdraw(_pid)
        return self.send_transaction(tx, cred)

    def founder_update(self, cred:Credentials, _new_founder:address) -> TxReceipt:
        tx = self.contract.functions.founderUpdate(_new_founder)
        return self.send_transaction(tx, cred)

    def founderaddr(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.founderaddr().call(block_identifier=block_identifier)

    def get_lock_percentage(self, _from:uint256, _to:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.getLockPercentage(_from, _to).call(block_identifier=block_identifier)

    def get_multiplier(self, _from:uint256, _to:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.getMultiplier(_from, _to).call(block_identifier=block_identifier)

    def get_new_reward_per_second(self, pid1:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.getNewRewardPerSecond(pid1).call(block_identifier=block_identifier)

    def get_pool_reward(self, _from:uint256, _to:uint256, _alloc_point:uint256, block_identifier:BlockIdentifier = 'latest') -> Tuple[uint256, uint256, uint256, uint256, uint256]:
        return self.contract.functions.getPoolReward(_from, _to, _alloc_point).call(block_identifier=block_identifier)

    def gov_token(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.govToken().call(block_identifier=block_identifier)

    def halving_update(self, cred:Credentials, _new_halving:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.halvingUpdate(_new_halving)
        return self.send_transaction(tx, cred)

    def liquidityaddr(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.liquidityaddr().call(block_identifier=block_identifier)

    def lock_update(self, cred:Credentials, _newlock:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.lockUpdate(_newlock)
        return self.send_transaction(tx, cred)

    def lockcom_update(self, cred:Credentials, _newcomlock:uint256) -> TxReceipt:
        tx = self.contract.functions.lockcomUpdate(_newcomlock)
        return self.send_transaction(tx, cred)

    def lockdev_update(self, cred:Credentials, _newdevlock:uint256) -> TxReceipt:
        tx = self.contract.functions.lockdevUpdate(_newdevlock)
        return self.send_transaction(tx, cred)

    def lockfounder_update(self, cred:Credentials, _newfounderlock:uint256) -> TxReceipt:
        tx = self.contract.functions.lockfounderUpdate(_newfounderlock)
        return self.send_transaction(tx, cred)

    def locklp_update(self, cred:Credentials, _newlplock:uint256) -> TxReceipt:
        tx = self.contract.functions.locklpUpdate(_newlplock)
        return self.send_transaction(tx, cred)

    def lp_update(self, cred:Credentials, _new_lp:address) -> TxReceipt:
        tx = self.contract.functions.lpUpdate(_new_lp)
        return self.send_transaction(tx, cred)

    def mass_update_pools(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.massUpdatePools()
        return self.send_transaction(tx, cred)

    def owner(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.owner().call(block_identifier=block_identifier)

    def pending_reward(self, _pid:uint256, _user:address, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.pendingReward(_pid, _user).call(block_identifier=block_identifier)

    def pool_existence(self, a:address, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.poolExistence(a).call(block_identifier=block_identifier)

    def pool_id1(self, a:address, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.poolId1(a).call(block_identifier=block_identifier)

    def pool_info(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> Tuple[address, uint256, uint256, uint256]:
        return self.contract.functions.poolInfo(a).call(block_identifier=block_identifier)

    def pool_length(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.poolLength().call(block_identifier=block_identifier)

    def reclaim_token_ownership(self, cred:Credentials, _new_owner:address) -> TxReceipt:
        tx = self.contract.functions.reclaimTokenOwnership(_new_owner)
        return self.send_transaction(tx, cred)

    def remove_authorized(self, cred:Credentials, _to_remove:address) -> TxReceipt:
        tx = self.contract.functions.removeAuthorized(_to_remove)
        return self.send_transaction(tx, cred)

    def renounce_ownership(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.renounceOwnership()
        return self.send_transaction(tx, cred)

    def reward_mul_update(self, cred:Credentials, _new_mul_reward:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.rewardMulUpdate(_new_mul_reward)
        return self.send_transaction(tx, cred)

    def reward_update(self, cred:Credentials, _new_reward:uint256) -> TxReceipt:
        tx = self.contract.functions.rewardUpdate(_new_reward)
        return self.send_transaction(tx, cred)

    def set(self, cred:Credentials, _pid:uint256, _alloc_point:uint256, _with_update:bool) -> TxReceipt:
        tx = self.contract.functions.set(_pid, _alloc_point, _with_update)
        return self.send_transaction(tx, cred)

    def set_dev_fee_stage(self, cred:Credentials, _dev_fees:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.setDevFeeStage(_dev_fees)
        return self.send_transaction(tx, cred)

    def set_stage_ends(self, cred:Credentials, _time_ends:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.setStageEnds(_time_ends)
        return self.send_transaction(tx, cred)

    def set_stage_starts(self, cred:Credentials, _time_starts:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.setStageStarts(_time_starts)
        return self.send_transaction(tx, cred)

    def set_user_fee_stage(self, cred:Credentials, _user_fees:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.setUserFeeStage(_user_fees)
        return self.send_transaction(tx, cred)

    def start_timestamp_update(self, cred:Credentials, _newstarttimestamp:uint256) -> TxReceipt:
        tx = self.contract.functions.startTimestampUpdate(_newstarttimestamp)
        return self.send_transaction(tx, cred)

    def time_delta_end_stage(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.timeDeltaEndStage(a).call(block_identifier=block_identifier)

    def time_delta_start_stage(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.timeDeltaStartStage(a).call(block_identifier=block_identifier)

    def total_alloc_point(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.totalAllocPoint().call(block_identifier=block_identifier)

    def transfer_ownership(self, cred:Credentials, new_owner:address) -> TxReceipt:
        tx = self.contract.functions.transferOwnership(new_owner)
        return self.send_transaction(tx, cred)

    def update_pool(self, cred:Credentials, _pid:uint256) -> TxReceipt:
        tx = self.contract.functions.updatePool(_pid)
        return self.send_transaction(tx, cred)

    def usd_oracle(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.usdOracle().call(block_identifier=block_identifier)

    def user_delta(self, _pid:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.userDelta(_pid).call(block_identifier=block_identifier)

    def user_fee_stage(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.userFeeStage(a).call(block_identifier=block_identifier)

    def user_info(self, a:uint256, b:address, block_identifier:BlockIdentifier = 'latest') -> Tuple[uint256, uint256, uint256, uint256, uint256, uint256, uint256]:
        return self.contract.functions.userInfo(a, b).call(block_identifier=block_identifier)

    def withdraw(self, cred:Credentials, _pid:uint256, _amount:uint256) -> TxReceipt:
        tx = self.contract.functions.withdraw(_pid, _amount)
        return self.send_transaction(tx, cred)