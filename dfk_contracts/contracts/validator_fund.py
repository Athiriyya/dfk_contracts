
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xED6dC9FD092190C08e4afF8611496774Ded19D54",
    "sd": ""
}

ABI = """[
    {"name": "AddValidator", "type": "event", "inputs": [{"name": "validator", "type": "address", "indexed": false, "internalType": "address"}, {"name": "nodeID", "type": "string", "indexed": false, "internalType": "string"}], "anonymous": false},
    {"name": "Disbursement", "type": "event", "inputs": [{"name": "validator", "type": "address", "indexed": true, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Process", "type": "event", "inputs": [{"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "RemoveValidator", "type": "event", "inputs": [{"name": "validator", "type": "address", "indexed": false, "internalType": "address"}, {"name": "nodeID", "type": "string", "indexed": false, "internalType": "string"}], "anonymous": false},
    {"name": "Slash", "type": "event", "inputs": [{"name": "validator", "type": "address", "indexed": true, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Stake", "type": "event", "inputs": [{"name": "validator", "type": "address", "indexed": true, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "endTime", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Unstake", "type": "event", "inputs": [{"name": "validator", "type": "address", "indexed": true, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "INITIAL_MAX_STAKE_AMOUNT", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "INITIAL_MAX_STAKE_DURATION", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "INITIAL_MIN_STAKE_AMOUNT", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "INITIAL_MIN_STAKE_DURATION", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "addValidator", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}, {"name": "_nodeID", "type": "string", "internalType": "string"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "addressToValidator", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "nodeID", "type": "string", "internalType": "string"}, {"name": "rewardAddress", "type": "address", "internalType": "address"}, {"name": "stakeAmount", "type": "uint256", "internalType": "uint256"}, {"name": "stakeStartAt", "type": "uint256", "internalType": "uint256"}, {"name": "stakeEndAt", "type": "uint256", "internalType": "uint256"}, {"name": "balance", "type": "uint256", "internalType": "uint256"}, {"name": "lifetimeBalance", "type": "uint256", "internalType": "uint256"}, {"name": "exists", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "allocatedAmount", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "burnPercentage", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "claimBalance", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "fundAddress", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address payable"}], "stateMutability": "view"},
    {"name": "fundPercentage", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getValidator", "type": "function", "inputs": [{"name": "_validator", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "nodeID", "type": "string", "internalType": "string"}, {"name": "rewardAddress", "type": "address", "internalType": "address"}, {"name": "stakeAmount", "type": "uint256", "internalType": "uint256"}, {"name": "stakeStartAt", "type": "uint256", "internalType": "uint256"}, {"name": "stakeEndAt", "type": "uint256", "internalType": "uint256"}, {"name": "balance", "type": "uint256", "internalType": "uint256"}, {"name": "lifetimeBalance", "type": "uint256", "internalType": "uint256"}, {"name": "exists", "type": "bool", "internalType": "bool"}], "internalType": "struct ValidatorFund.Validator"}], "stateMutability": "view"},
    {"name": "getValidators", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "nodeID", "type": "string", "internalType": "string"}, {"name": "rewardAddress", "type": "address", "internalType": "address"}, {"name": "stakeAmount", "type": "uint256", "internalType": "uint256"}, {"name": "stakeStartAt", "type": "uint256", "internalType": "uint256"}, {"name": "stakeEndAt", "type": "uint256", "internalType": "uint256"}, {"name": "balance", "type": "uint256", "internalType": "uint256"}, {"name": "lifetimeBalance", "type": "uint256", "internalType": "uint256"}, {"name": "exists", "type": "bool", "internalType": "bool"}], "internalType": "struct ValidatorFund.Validator[]"}], "stateMutability": "view"},
    {"name": "govToken", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IERC20"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_burnPercentage", "type": "uint256", "internalType": "uint256"}, {"name": "_jewelFundPercentage", "type": "uint256", "internalType": "uint256"}, {"name": "_validatorFundPercentage", "type": "uint256", "internalType": "uint256"}, {"name": "_govTokenAddress", "type": "address", "internalType": "address"}, {"name": "_fundAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "lastDistribution", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "maxStakeAmount", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "maxStakeDuration", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "minStakeAmount", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "minStakeDuration", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "processFunds", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "removeValidator", "type": "function", "inputs": [{"name": "_validator", "type": "address", "internalType": "address"}, {"name": "_index", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "rewardPercentage", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "setPercentages", "type": "function", "inputs": [{"name": "_burnPercentage", "type": "uint256", "internalType": "uint256"}, {"name": "_fundPercentage", "type": "uint256", "internalType": "uint256"}, {"name": "_rewardPercentage", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setStakeAmounts", "type": "function", "inputs": [{"name": "_minStakeAmount", "type": "uint256", "internalType": "uint256"}, {"name": "_maxStakeAmount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setStakeDurations", "type": "function", "inputs": [{"name": "_minStakeDuration", "type": "uint256", "internalType": "uint256"}, {"name": "_maxStakeDuration", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "slash", "type": "function", "inputs": [{"name": "_validator", "type": "address", "internalType": "address"}, {"name": "_wei", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "stake", "type": "function", "inputs": [{"name": "_amount", "type": "uint256", "internalType": "uint256"}, {"name": "_duration", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "totalBurn", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "totalFund", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "totalReward", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "totalStake", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "unallocated", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "unstake", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "updateRewardAddress", "type": "function", "inputs": [{"name": "_rewardAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "validators", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"type": "receive", "stateMutability": "payable"}
]
"""     

class ValidatorFund(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def initial_max_stake_amount(self) -> uint256:
        return self.contract.functions.INITIAL_MAX_STAKE_AMOUNT().call()

    def initial_max_stake_duration(self) -> uint256:
        return self.contract.functions.INITIAL_MAX_STAKE_DURATION().call()

    def initial_min_stake_amount(self) -> uint256:
        return self.contract.functions.INITIAL_MIN_STAKE_AMOUNT().call()

    def initial_min_stake_duration(self) -> uint256:
        return self.contract.functions.INITIAL_MIN_STAKE_DURATION().call()

    def add_validator(self, cred:Credentials, _address:address, _node_id:string) -> TxReceipt:
        tx = self.contract.functions.addValidator(_address, _node_id)
        return self.send_transaction(tx, cred)

    def address_to_validator(self, a:address) -> Tuple[address, string, address, uint256, uint256, uint256, uint256, uint256, bool]:
        return self.contract.functions.addressToValidator(a).call()

    def allocated_amount(self) -> uint256:
        return self.contract.functions.allocatedAmount().call()

    def burn_percentage(self) -> uint256:
        return self.contract.functions.burnPercentage().call()

    def claim_balance(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.claimBalance()
        return self.send_transaction(tx, cred)

    def fund_address(self) -> address:
        return self.contract.functions.fundAddress().call()

    def fund_percentage(self) -> uint256:
        return self.contract.functions.fundPercentage().call()

    def get_validator(self, _validator:address) -> tuple:
        return self.contract.functions.getValidator(_validator).call()

    def get_validators(self) -> Sequence[tuple]:
        return self.contract.functions.getValidators().call()

    def gov_token(self) -> address:
        return self.contract.functions.govToken().call()

    def initialize(self, cred:Credentials, _burn_percentage:uint256, _jewel_fund_percentage:uint256, _validator_fund_percentage:uint256, _gov_token_address:address, _fund_address:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_burn_percentage, _jewel_fund_percentage, _validator_fund_percentage, _gov_token_address, _fund_address)
        return self.send_transaction(tx, cred)

    def last_distribution(self) -> uint256:
        return self.contract.functions.lastDistribution().call()

    def max_stake_amount(self) -> uint256:
        return self.contract.functions.maxStakeAmount().call()

    def max_stake_duration(self) -> uint256:
        return self.contract.functions.maxStakeDuration().call()

    def min_stake_amount(self) -> uint256:
        return self.contract.functions.minStakeAmount().call()

    def min_stake_duration(self) -> uint256:
        return self.contract.functions.minStakeDuration().call()

    def process_funds(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.processFunds()
        return self.send_transaction(tx, cred)

    def remove_validator(self, cred:Credentials, _validator:address, _index:uint256) -> TxReceipt:
        tx = self.contract.functions.removeValidator(_validator, _index)
        return self.send_transaction(tx, cred)

    def reward_percentage(self) -> uint256:
        return self.contract.functions.rewardPercentage().call()

    def set_percentages(self, cred:Credentials, _burn_percentage:uint256, _fund_percentage:uint256, _reward_percentage:uint256) -> TxReceipt:
        tx = self.contract.functions.setPercentages(_burn_percentage, _fund_percentage, _reward_percentage)
        return self.send_transaction(tx, cred)

    def set_stake_amounts(self, cred:Credentials, _min_stake_amount:uint256, _max_stake_amount:uint256) -> TxReceipt:
        tx = self.contract.functions.setStakeAmounts(_min_stake_amount, _max_stake_amount)
        return self.send_transaction(tx, cred)

    def set_stake_durations(self, cred:Credentials, _min_stake_duration:uint256, _max_stake_duration:uint256) -> TxReceipt:
        tx = self.contract.functions.setStakeDurations(_min_stake_duration, _max_stake_duration)
        return self.send_transaction(tx, cred)

    def slash(self, cred:Credentials, _validator:address, _wei:uint256) -> TxReceipt:
        tx = self.contract.functions.slash(_validator, _wei)
        return self.send_transaction(tx, cred)

    def stake(self, cred:Credentials, _amount:uint256, _duration:uint256) -> TxReceipt:
        tx = self.contract.functions.stake(_amount, _duration)
        return self.send_transaction(tx, cred)

    def total_burn(self) -> uint256:
        return self.contract.functions.totalBurn().call()

    def total_fund(self) -> uint256:
        return self.contract.functions.totalFund().call()

    def total_reward(self) -> uint256:
        return self.contract.functions.totalReward().call()

    def total_stake(self) -> uint256:
        return self.contract.functions.totalStake().call()

    def unallocated(self) -> uint256:
        return self.contract.functions.unallocated().call()

    def unstake(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unstake()
        return self.send_transaction(tx, cred)

    def update_reward_address(self, cred:Credentials, _reward_address:address) -> TxReceipt:
        tx = self.contract.functions.updateRewardAddress(_reward_address)
        return self.send_transaction(tx, cred)

    def validators(self, a:uint256) -> address:
        return self.contract.functions.validators(a).call()