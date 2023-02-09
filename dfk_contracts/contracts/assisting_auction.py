
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x8101CfFBec8E045c3FAdC3877a1D30f97d301209",
    "sd": "0xA2cef1763e59198025259d76Ce8F9E60d27B17B5"
}

ABI = """[
    {"type": "constructor", "inputs": [{"name": "_heroCoreAddress", "type": "address", "internalType": "address"}, {"name": "_jewelAddress", "type": "address", "internalType": "address"}, {"name": "_cut", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "AuctionCancelled", "type": "event", "inputs": [{"name": "auctionId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "tokenId", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "AuctionCreated", "type": "event", "inputs": [{"name": "auctionId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "tokenId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "startingPrice", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "endingPrice", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "duration", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "winner", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "AuctionSuccessful", "type": "event", "inputs": [{"name": "auctionId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "tokenId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "totalPrice", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "winner", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "OwnershipTransferred", "type": "event", "inputs": [{"name": "previousOwner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "newOwner", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "auctionHeroCore", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IHeroCore"}], "stateMutability": "view"},
    {"name": "bid", "type": "function", "inputs": [{"name": "_tokenId", "type": "uint256", "internalType": "uint256"}, {"name": "_bidAmount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "cancelAuction", "type": "function", "inputs": [{"name": "_tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "cancelAuctionWhenPaused", "type": "function", "inputs": [{"name": "_tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "createAuction", "type": "function", "inputs": [{"name": "_tokenId", "type": "uint256", "internalType": "uint256"}, {"name": "_startingPrice", "type": "uint128", "internalType": "uint128"}, {"name": "_endingPrice", "type": "uint128", "internalType": "uint128"}, {"name": "_duration", "type": "uint64", "internalType": "uint64"}, {"name": "_winner", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getAuction", "type": "function", "inputs": [{"name": "_tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "auctionId", "type": "uint256", "internalType": "uint256"}, {"name": "seller", "type": "address", "internalType": "address"}, {"name": "startingPrice", "type": "uint256", "internalType": "uint256"}, {"name": "endingPrice", "type": "uint256", "internalType": "uint256"}, {"name": "duration", "type": "uint256", "internalType": "uint256"}, {"name": "startedAt", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getCurrentPrice", "type": "function", "inputs": [{"name": "_tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getUserAuctions", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "isOnAuction", "type": "function", "inputs": [{"name": "_tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "jewelToken", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IJewelToken"}], "stateMutability": "view"},
    {"name": "maxPrice", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "minPrice", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "owner", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "ownerCut", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "renounceOwnership", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setFees", "type": "function", "inputs": [{"name": "_feeAddresses", "type": "address[]", "internalType": "address[]"}, {"name": "_feePercents", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setLimits", "type": "function", "inputs": [{"name": "_min", "type": "uint256", "internalType": "uint256"}, {"name": "_max", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "transferOwnership", "type": "function", "inputs": [{"name": "newOwner", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "userAuctions", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"}
]
"""     

class AssistingAuction(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def auction_hero_core(self) -> address:
        return self.contract.functions.auctionHeroCore().call()

    def bid(self, cred:Credentials, _token_id:uint256, _bid_amount:uint256) -> TxReceipt:
        tx = self.contract.functions.bid(_token_id, _bid_amount)
        return self.send_transaction(tx, cred)

    def cancel_auction(self, cred:Credentials, _token_id:uint256) -> TxReceipt:
        tx = self.contract.functions.cancelAuction(_token_id)
        return self.send_transaction(tx, cred)

    def cancel_auction_when_paused(self, cred:Credentials, _token_id:uint256) -> TxReceipt:
        tx = self.contract.functions.cancelAuctionWhenPaused(_token_id)
        return self.send_transaction(tx, cred)

    def create_auction(self, cred:Credentials, _token_id:uint256, _starting_price:uint128, _ending_price:uint128, _duration:uint64, _winner:address) -> TxReceipt:
        tx = self.contract.functions.createAuction(_token_id, _starting_price, _ending_price, _duration, _winner)
        return self.send_transaction(tx, cred)

    def get_auction(self, _token_id:uint256) -> Tuple[uint256, address, uint256, uint256, uint256, uint256]:
        return self.contract.functions.getAuction(_token_id).call()

    def get_current_price(self, _token_id:uint256) -> uint256:
        return self.contract.functions.getCurrentPrice(_token_id).call()

    def get_user_auctions(self, _address:address) -> Sequence[uint256]:
        return self.contract.functions.getUserAuctions(_address).call()

    def is_on_auction(self, _token_id:uint256) -> bool:
        return self.contract.functions.isOnAuction(_token_id).call()

    def jewel_token(self) -> address:
        return self.contract.functions.jewelToken().call()

    def max_price(self) -> uint256:
        return self.contract.functions.maxPrice().call()

    def min_price(self) -> uint256:
        return self.contract.functions.minPrice().call()

    def owner(self) -> address:
        return self.contract.functions.owner().call()

    def owner_cut(self) -> uint256:
        return self.contract.functions.ownerCut().call()

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def renounce_ownership(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.renounceOwnership()
        return self.send_transaction(tx, cred)

    def set_fees(self, cred:Credentials, _fee_addresses:Sequence[address], _fee_percents:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.setFees(_fee_addresses, _fee_percents)
        return self.send_transaction(tx, cred)

    def set_limits(self, cred:Credentials, _min:uint256, _max:uint256) -> TxReceipt:
        tx = self.contract.functions.setLimits(_min, _max)
        return self.send_transaction(tx, cred)

    def transfer_ownership(self, cred:Credentials, new_owner:address) -> TxReceipt:
        tx = self.contract.functions.transferOwnership(new_owner)
        return self.send_transaction(tx, cred)

    def user_auctions(self, a:address, b:uint256) -> uint256:
        return self.contract.functions.userAuctions(a, b).call()