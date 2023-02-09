
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x6a56222A67df18FC282CD58dCDF12e61Be812f97",
    "sd": ""
}

ABI = """[
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "RaffleClosed", "type": "event", "inputs": [{"name": "raffleId", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "RaffleDrawn", "type": "event", "inputs": [{"name": "raffleId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "winner", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "RaffleEntered", "type": "event", "inputs": [{"name": "user", "type": "address", "indexed": true, "internalType": "address"}, {"name": "raffleId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "tickets", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "RaffleStarted", "type": "event", "inputs": [{"name": "raffleId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "raffleType", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "rewards", "type": "address[]", "internalType": "address[]"}, {"name": "rewardAmounts", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "maxWinners", "type": "uint256", "internalType": "uint256"}, {"name": "duration", "type": "uint64", "internalType": "uint64"}], "indexed": false, "internalType": "struct RaffleMaster.RaffleType"}], "anonymous": false},
    {"name": "RaffleTypeActivated", "type": "event", "inputs": [{"name": "raffleTypeId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "bucket", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "RaffleTypeAdded", "type": "event", "inputs": [{"name": "id", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "raffleType", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "rewards", "type": "address[]", "internalType": "address[]"}, {"name": "rewardAmounts", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "maxWinners", "type": "uint256", "internalType": "uint256"}, {"name": "duration", "type": "uint64", "internalType": "uint64"}], "indexed": false, "internalType": "struct RaffleMaster.RaffleType"}], "anonymous": false},
    {"name": "RaffleTypeDeactivated", "type": "event", "inputs": [{"name": "raffleTypeId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "bucket", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "activeRaffleTypes", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "addActiveRaffleType", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}, {"name": "_bucket", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "addAndActivateRaffleType", "type": "function", "inputs": [{"name": "_rewards", "type": "address[]", "internalType": "address[]"}, {"name": "_rewardAmounts", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_maxWinners", "type": "uint256", "internalType": "uint256"}, {"name": "_duration", "type": "uint64", "internalType": "uint64"}, {"name": "_buckets", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "addRaffleType", "type": "function", "inputs": [{"name": "_rewards", "type": "address[]", "internalType": "address[]"}, {"name": "_rewardAmounts", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_maxWinners", "type": "uint256", "internalType": "uint256"}, {"name": "_duration", "type": "uint64", "internalType": "uint64"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "closeRaffles", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "createRaffle", "type": "function", "inputs": [{"name": "_raffleTypeId", "type": "uint256", "internalType": "uint256"}, {"name": "_bucket", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "currentRaffleBuckets", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "drawWinners", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "enterRaffle", "type": "function", "inputs": [{"name": "_raffleId", "type": "uint256", "internalType": "uint256"}, {"name": "_tickets", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "entries", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "getCurrentRaffleBuckets", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "getCurrentRaffleData", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "raffleType", "type": "uint256", "internalType": "uint256"}, {"name": "startTime", "type": "uint256", "internalType": "uint256"}, {"name": "totalEntries", "type": "uint256", "internalType": "uint256"}, {"name": "endTime", "type": "uint256", "internalType": "uint256"}, {"name": "closedBlock", "type": "uint256", "internalType": "uint256"}, {"name": "winners", "type": "address[]", "internalType": "address[]"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "internalType": "struct RaffleMaster.Raffle[]"}, {"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "rewards", "type": "address[]", "internalType": "address[]"}, {"name": "rewardAmounts", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "maxWinners", "type": "uint256", "internalType": "uint256"}, {"name": "duration", "type": "uint64", "internalType": "uint64"}], "internalType": "struct RaffleMaster.RaffleType[]"}, {"name": "", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "getLastRaffleBuckets", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "getPreviousRaffleData", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "raffleType", "type": "uint256", "internalType": "uint256"}, {"name": "startTime", "type": "uint256", "internalType": "uint256"}, {"name": "totalEntries", "type": "uint256", "internalType": "uint256"}, {"name": "endTime", "type": "uint256", "internalType": "uint256"}, {"name": "closedBlock", "type": "uint256", "internalType": "uint256"}, {"name": "winners", "type": "address[]", "internalType": "address[]"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "internalType": "struct RaffleMaster.Raffle[]"}, {"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "rewards", "type": "address[]", "internalType": "address[]"}, {"name": "rewardAmounts", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "maxWinners", "type": "uint256", "internalType": "uint256"}, {"name": "duration", "type": "uint64", "internalType": "uint64"}], "internalType": "struct RaffleMaster.RaffleType[]"}, {"name": "", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "getRaffleList", "type": "function", "inputs": [{"name": "_raffleBuckets", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "raffleType", "type": "uint256", "internalType": "uint256"}, {"name": "startTime", "type": "uint256", "internalType": "uint256"}, {"name": "totalEntries", "type": "uint256", "internalType": "uint256"}, {"name": "endTime", "type": "uint256", "internalType": "uint256"}, {"name": "closedBlock", "type": "uint256", "internalType": "uint256"}, {"name": "winners", "type": "address[]", "internalType": "address[]"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "internalType": "struct RaffleMaster.Raffle[]"}], "stateMutability": "view"},
    {"name": "getRaffleTicketsAllowanceList", "type": "function", "inputs": [{"name": "_raffleBuckets", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "getRaffleTicketsList", "type": "function", "inputs": [{"name": "_raffleBuckets", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "getRaffleTypesList", "type": "function", "inputs": [{"name": "_raffleBuckets", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "rewards", "type": "address[]", "internalType": "address[]"}, {"name": "rewardAmounts", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "maxWinners", "type": "uint256", "internalType": "uint256"}, {"name": "duration", "type": "uint64", "internalType": "uint64"}], "internalType": "struct RaffleMaster.RaffleType[]"}], "stateMutability": "view"},
    {"name": "getTicketAllowance", "type": "function", "inputs": [{"name": "_user", "type": "address", "internalType": "address"}, {"name": "_raffleId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "initRaffleBuckets", "type": "function", "inputs": [{"name": "_buckets", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_raffleTickets", "type": "address", "internalType": "address"}, {"name": "_airdropClaim", "type": "address", "internalType": "address"}, {"name": "_itemMinter", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "lastRaffleBuckets", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "playerEntries", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}, {"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "raffleTypes", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "maxWinners", "type": "uint256", "internalType": "uint256"}, {"name": "duration", "type": "uint64", "internalType": "uint64"}], "stateMutability": "view"},
    {"name": "raffles", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "raffleType", "type": "uint256", "internalType": "uint256"}, {"name": "startTime", "type": "uint256", "internalType": "uint256"}, {"name": "totalEntries", "type": "uint256", "internalType": "uint256"}, {"name": "endTime", "type": "uint256", "internalType": "uint256"}, {"name": "closedBlock", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "removeActiveRaffleType", "type": "function", "inputs": [{"name": "_index", "type": "uint256", "internalType": "uint256"}, {"name": "_bucket", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setRaffleType", "type": "function", "inputs": [{"name": "_raffleTypeId", "type": "uint256", "internalType": "uint256"}, {"name": "_rewards", "type": "address[]", "internalType": "address[]"}, {"name": "_rewardAmounts", "type": "uint256[]", "internalType": "uint256[]"}, {"name": "_maxWinners", "type": "uint256", "internalType": "uint256"}, {"name": "_duration", "type": "uint64", "internalType": "uint64"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "startRandomRaffle", "type": "function", "inputs": [{"name": "_bucket", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "startRandomRaffles", "type": "function", "inputs": [{"name": "_buckets", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "timePerTicket", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "totalRaffleTypes", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "totalRaffles", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class RaffleMaster(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def active_raffle_types(self, a:uint256, b:uint256) -> uint256:
        return self.contract.functions.activeRaffleTypes(a, b).call()

    def add_active_raffle_type(self, cred:Credentials, _id:uint256, _bucket:uint256) -> TxReceipt:
        tx = self.contract.functions.addActiveRaffleType(_id, _bucket)
        return self.send_transaction(tx, cred)

    def add_and_activate_raffle_type(self, cred:Credentials, _rewards:Sequence[address], _reward_amounts:Sequence[uint256], _max_winners:uint256, _duration:uint64, _buckets:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.addAndActivateRaffleType(_rewards, _reward_amounts, _max_winners, _duration, _buckets)
        return self.send_transaction(tx, cred)

    def add_raffle_type(self, cred:Credentials, _rewards:Sequence[address], _reward_amounts:Sequence[uint256], _max_winners:uint256, _duration:uint64) -> TxReceipt:
        tx = self.contract.functions.addRaffleType(_rewards, _reward_amounts, _max_winners, _duration)
        return self.send_transaction(tx, cred)

    def close_raffles(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.closeRaffles()
        return self.send_transaction(tx, cred)

    def create_raffle(self, cred:Credentials, _raffle_type_id:uint256, _bucket:uint256) -> TxReceipt:
        tx = self.contract.functions.createRaffle(_raffle_type_id, _bucket)
        return self.send_transaction(tx, cred)

    def current_raffle_buckets(self, a:uint256) -> uint256:
        return self.contract.functions.currentRaffleBuckets(a).call()

    def draw_winners(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.drawWinners()
        return self.send_transaction(tx, cred)

    def enter_raffle(self, cred:Credentials, _raffle_id:uint256, _tickets:uint256) -> TxReceipt:
        tx = self.contract.functions.enterRaffle(_raffle_id, _tickets)
        return self.send_transaction(tx, cred)

    def entries(self, a:uint256, b:uint256) -> address:
        return self.contract.functions.entries(a, b).call()

    def get_current_raffle_buckets(self) -> Sequence[uint256]:
        return self.contract.functions.getCurrentRaffleBuckets().call()

    def get_current_raffle_data(self) -> Tuple[Sequence[tuple], Sequence[tuple], Sequence[uint256], Sequence[uint256]]:
        return self.contract.functions.getCurrentRaffleData().call()

    def get_last_raffle_buckets(self) -> Sequence[uint256]:
        return self.contract.functions.getLastRaffleBuckets().call()

    def get_previous_raffle_data(self) -> Tuple[Sequence[tuple], Sequence[tuple], Sequence[uint256], Sequence[uint256]]:
        return self.contract.functions.getPreviousRaffleData().call()

    def get_raffle_list(self, _raffle_buckets:Sequence[uint256]) -> Sequence[tuple]:
        return self.contract.functions.getRaffleList(_raffle_buckets).call()

    def get_raffle_tickets_allowance_list(self, _raffle_buckets:Sequence[uint256]) -> Sequence[uint256]:
        return self.contract.functions.getRaffleTicketsAllowanceList(_raffle_buckets).call()

    def get_raffle_tickets_list(self, _raffle_buckets:Sequence[uint256]) -> Sequence[uint256]:
        return self.contract.functions.getRaffleTicketsList(_raffle_buckets).call()

    def get_raffle_types_list(self, _raffle_buckets:Sequence[uint256]) -> Sequence[tuple]:
        return self.contract.functions.getRaffleTypesList(_raffle_buckets).call()

    def get_ticket_allowance(self, _user:address, _raffle_id:uint256) -> uint256:
        return self.contract.functions.getTicketAllowance(_user, _raffle_id).call()

    def init_raffle_buckets(self, cred:Credentials, _buckets:uint256) -> TxReceipt:
        tx = self.contract.functions.initRaffleBuckets(_buckets)
        return self.send_transaction(tx, cred)

    def initialize(self, cred:Credentials, _raffle_tickets:address, _airdrop_claim:address, _item_minter:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_raffle_tickets, _airdrop_claim, _item_minter)
        return self.send_transaction(tx, cred)

    def last_raffle_buckets(self, a:uint256) -> uint256:
        return self.contract.functions.lastRaffleBuckets(a).call()

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
        return self.send_transaction(tx, cred)

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def player_entries(self, a:uint256, b:address) -> uint256:
        return self.contract.functions.playerEntries(a, b).call()

    def raffle_types(self, a:uint256) -> Tuple[uint256, uint256, uint64]:
        return self.contract.functions.raffleTypes(a).call()

    def raffles(self, a:uint256) -> Tuple[uint256, uint256, uint256, uint256, uint256, uint256, uint8]:
        return self.contract.functions.raffles(a).call()

    def remove_active_raffle_type(self, cred:Credentials, _index:uint256, _bucket:uint256) -> TxReceipt:
        tx = self.contract.functions.removeActiveRaffleType(_index, _bucket)
        return self.send_transaction(tx, cred)

    def set_raffle_type(self, cred:Credentials, _raffle_type_id:uint256, _rewards:Sequence[address], _reward_amounts:Sequence[uint256], _max_winners:uint256, _duration:uint64) -> TxReceipt:
        tx = self.contract.functions.setRaffleType(_raffle_type_id, _rewards, _reward_amounts, _max_winners, _duration)
        return self.send_transaction(tx, cred)

    def start_random_raffle(self, cred:Credentials, _bucket:uint256) -> TxReceipt:
        tx = self.contract.functions.startRandomRaffle(_bucket)
        return self.send_transaction(tx, cred)

    def start_random_raffles(self, cred:Credentials, _buckets:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.startRandomRaffles(_buckets)
        return self.send_transaction(tx, cred)

    def time_per_ticket(self) -> uint256:
        return self.contract.functions.timePerTicket().call()

    def total_raffle_types(self) -> uint256:
        return self.contract.functions.totalRaffleTypes().call()

    def total_raffles(self) -> uint256:
        return self.contract.functions.totalRaffles().call()

    def unpause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unpause()
        return self.send_transaction(tx, cred)