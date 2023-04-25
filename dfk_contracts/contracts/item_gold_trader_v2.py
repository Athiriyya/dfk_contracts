
from ..abi_contract_wrapper import ABIContractWrapper
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x0f85fdf6c561C42d6b46d0E27ea6Aa9Bf9476B3f",
    "sd": "0x3Eab8a8F71dDA3e6c907C74302B734805C4f3278"
}

ABI = """[
    {"name": "ItemAdded", "type": "event", "inputs": [{"name": "item", "type": "address", "internalType": "address", "indexed": true}, {"name": "startingPrice", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "playerSellPrice", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "minPrice", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "deltaPriceIncrease", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "decreaseRate", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "priceIncreaseDecay", "type": "uint64", "internalType": "uint64", "indexed": false}], "anonymous": false},
    {"name": "ItemTraded", "type": "event", "inputs": [{"name": "player", "type": "address", "internalType": "address", "indexed": true}, {"name": "boughtItem", "type": "address", "internalType": "address", "indexed": false}, {"name": "boughtQty", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "soldItem", "type": "address", "internalType": "address", "indexed": false}, {"name": "soldQty", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "ItemUpdated", "type": "event", "inputs": [{"name": "item", "type": "address", "internalType": "address", "indexed": true}, {"name": "currentPrice", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "playerSellPrice", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "minPrice", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "deltaPriceIncrease", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "decreaseRate", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "priceIncreaseDecay", "type": "uint64", "internalType": "uint64", "indexed": false}, {"name": "status", "type": "uint8", "internalType": "uint8", "indexed": false}], "anonymous": false},
    {"name": "addTradeItem", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_startingPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_sellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_minPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_deltaPriceIncrease", "type": "uint256", "internalType": "uint256"}, {"name": "_decreaseRate", "type": "uint256", "internalType": "uint256"}, {"name": "_priceIncreaseDecay", "type": "uint64", "internalType": "uint64"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "addressToTradeItemId", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "buyItem", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_quantity", "type": "uint256", "internalType": "uint256"}, {"name": "_maxPrice", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getNextPrice", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_quantity", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getTradeItem", "type": "function", "inputs": [{"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "item", "type": "address", "internalType": "address"}, {"name": "currentPrice", "type": "uint256", "internalType": "uint256"}, {"name": "playerSellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "minPrice", "type": "uint256", "internalType": "uint256"}, {"name": "deltaPriceIncrease", "type": "uint256", "internalType": "uint256"}, {"name": "decreaseRate", "type": "uint256", "internalType": "uint256"}, {"name": "priceIncreaseDecay", "type": "uint64", "internalType": "uint64"}, {"name": "lastPurchaseTimestamp", "type": "uint64", "internalType": "uint64"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "internalType": "struct TraderTypes.TradeItem"}], "stateMutability": "view"},
    {"name": "getTradeItemByAddress", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "item", "type": "address", "internalType": "address"}, {"name": "currentPrice", "type": "uint256", "internalType": "uint256"}, {"name": "playerSellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "minPrice", "type": "uint256", "internalType": "uint256"}, {"name": "deltaPriceIncrease", "type": "uint256", "internalType": "uint256"}, {"name": "decreaseRate", "type": "uint256", "internalType": "uint256"}, {"name": "priceIncreaseDecay", "type": "uint64", "internalType": "uint64"}, {"name": "lastPurchaseTimestamp", "type": "uint64", "internalType": "uint64"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "internalType": "struct TraderTypes.TradeItem"}], "stateMutability": "view"},
    {"name": "getTradeItems", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "item", "type": "address", "internalType": "address"}, {"name": "currentPrice", "type": "uint256", "internalType": "uint256"}, {"name": "playerSellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "minPrice", "type": "uint256", "internalType": "uint256"}, {"name": "deltaPriceIncrease", "type": "uint256", "internalType": "uint256"}, {"name": "decreaseRate", "type": "uint256", "internalType": "uint256"}, {"name": "priceIncreaseDecay", "type": "uint64", "internalType": "uint64"}, {"name": "lastPurchaseTimestamp", "type": "uint64", "internalType": "uint64"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "internalType": "struct TraderTypes.TradeItem[]"}], "stateMutability": "view"},
    {"name": "sellItem", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_quantity", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "tradeItems", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "item", "type": "address", "internalType": "address"}, {"name": "currentPrice", "type": "uint256", "internalType": "uint256"}, {"name": "playerSellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "minPrice", "type": "uint256", "internalType": "uint256"}, {"name": "deltaPriceIncrease", "type": "uint256", "internalType": "uint256"}, {"name": "decreaseRate", "type": "uint256", "internalType": "uint256"}, {"name": "priceIncreaseDecay", "type": "uint64", "internalType": "uint64"}, {"name": "lastPurchaseTimestamp", "type": "uint64", "internalType": "uint64"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "updateTradeItem", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_currentPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_sellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_minPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_deltaPriceIncrease", "type": "uint256", "internalType": "uint256"}, {"name": "_decreaseRate", "type": "uint256", "internalType": "uint256"}, {"name": "_priceIncreaseDecay", "type": "uint64", "internalType": "uint64"}, {"name": "_status", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class ItemGoldTraderV2(ABIContractWrapper):
    def __init__(self, chain_key:str, rpc:str):
        contract_address = CONTRACT_ADDRESS[chain_key]
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def add_trade_item(self, cred:Credentials, _item_address:address, _starting_price:uint256, _sell_price:uint256, _min_price:uint256, _delta_price_increase:uint256, _decrease_rate:uint256, _price_increase_decay:uint64) -> TxReceipt:
        tx = self.contract.functions.addTradeItem(_item_address, _starting_price, _sell_price, _min_price, _delta_price_increase, _decrease_rate, _price_increase_decay)
        return self.send_transaction(tx, cred)

    def address_to_trade_item_id(self, a:address, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.addressToTradeItemId(a).call(block_identifier=block_identifier)

    def buy_item(self, cred:Credentials, _item_address:address, _quantity:uint256, _max_price:uint256) -> TxReceipt:
        tx = self.contract.functions.buyItem(_item_address, _quantity, _max_price)
        return self.send_transaction(tx, cred)

    def get_next_price(self, _item_address:address, _quantity:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.getNextPrice(_item_address, _quantity).call(block_identifier=block_identifier)

    def get_trade_item(self, _id:uint256, block_identifier:BlockIdentifier = 'latest') -> tuple:
        return self.contract.functions.getTradeItem(_id).call(block_identifier=block_identifier)

    def get_trade_item_by_address(self, _item_address:address, block_identifier:BlockIdentifier = 'latest') -> tuple:
        return self.contract.functions.getTradeItemByAddress(_item_address).call(block_identifier=block_identifier)

    def get_trade_items(self, block_identifier:BlockIdentifier = 'latest') -> List[tuple]:
        return self.contract.functions.getTradeItems().call(block_identifier=block_identifier)

    def sell_item(self, cred:Credentials, _item_address:address, _quantity:uint256) -> TxReceipt:
        tx = self.contract.functions.sellItem(_item_address, _quantity)
        return self.send_transaction(tx, cred)

    def trade_items(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> Tuple[uint256, address, uint256, uint256, uint256, uint256, uint256, uint64, uint64, uint8]:
        return self.contract.functions.tradeItems(a).call(block_identifier=block_identifier)

    def update_trade_item(self, cred:Credentials, _item_address:address, _current_price:uint256, _sell_price:uint256, _min_price:uint256, _delta_price_increase:uint256, _decrease_rate:uint256, _price_increase_decay:uint64, _status:uint8) -> TxReceipt:
        tx = self.contract.functions.updateTradeItem(_item_address, _current_price, _sell_price, _min_price, _delta_price_increase, _decrease_rate, _price_increase_decay, _status)
        return self.send_transaction(tx, cred)