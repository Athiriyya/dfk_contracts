
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x0f85fdf6c561C42d6b46d0E27ea6Aa9Bf9476B3f",
    "sd": "0x3Eab8a8F71dDA3e6c907C74302B734805C4f3278"
}

ABI = """[
    {"name": "ItemAdded", "type": "event", "inputs": [{"name": "item", "type": "address", "indexed": true, "internalType": "address"}, {"name": "buyPrice", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "sellPrice", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "ItemTraded", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "boughtItem", "type": "address", "indexed": false, "internalType": "address"}, {"name": "boughtQty", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "soldItem", "type": "address", "indexed": false, "internalType": "address"}, {"name": "soldQty", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "ItemUpdated", "type": "event", "inputs": [{"name": "item", "type": "address", "indexed": true, "internalType": "address"}, {"name": "buyPrice", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "sellPrice", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "status", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "addTradeItem", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_buyPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_sellPrice", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "addressToTradeItemId", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "buyItem", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_quantity", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getTradeItems", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "item", "type": "address", "internalType": "contract IInventoryItem"}, {"name": "buyPrice", "type": "uint256", "internalType": "uint256"}, {"name": "sellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "internalType": "struct ItemGoldTrader.TradeItem[]"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_dfkGoldAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "sellItem", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_quantity", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "tradeItems", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "item", "type": "address", "internalType": "contract IInventoryItem"}, {"name": "buyPrice", "type": "uint256", "internalType": "uint256"}, {"name": "sellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "updateTradeItem", "type": "function", "inputs": [{"name": "_itemAddress", "type": "address", "internalType": "address"}, {"name": "_buyPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_sellPrice", "type": "uint256", "internalType": "uint256"}, {"name": "_status", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class ItemGoldTraderV2(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def add_trade_item(self, cred:Credentials, _item_address:address, _buy_price:uint256, _sell_price:uint256) -> TxReceipt:
        tx = self.contract.functions.addTradeItem(_item_address, _buy_price, _sell_price)
        return self.send_transaction(tx, cred)

    def address_to_trade_item_id(self, a:address) -> uint256:
        return self.contract.functions.addressToTradeItemId(a).call()

    def buy_item(self, cred:Credentials, _item_address:address, _quantity:uint256) -> TxReceipt:
        tx = self.contract.functions.buyItem(_item_address, _quantity)
        return self.send_transaction(tx, cred)

    def get_trade_items(self) -> Sequence[tuple]:
        return self.contract.functions.getTradeItems().call()

    def initialize(self, cred:Credentials, _dfk_gold_address:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_dfk_gold_address)
        return self.send_transaction(tx, cred)

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def sell_item(self, cred:Credentials, _item_address:address, _quantity:uint256) -> TxReceipt:
        tx = self.contract.functions.sellItem(_item_address, _quantity)
        return self.send_transaction(tx, cred)

    def trade_items(self, a:uint256) -> Tuple[uint256, address, uint256, uint256, uint8]:
        return self.contract.functions.tradeItems(a).call()

    def update_trade_item(self, cred:Credentials, _item_address:address, _buy_price:uint256, _sell_price:uint256, _status:uint8) -> TxReceipt:
        tx = self.contract.functions.updateTradeItem(_item_address, _buy_price, _sell_price, _status)
        return self.send_transaction(tx, cred)