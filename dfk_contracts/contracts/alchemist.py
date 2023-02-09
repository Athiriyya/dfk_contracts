
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x87CBa8F998F902f2fff990efFa1E261F35932e57",
    "sd": "0x696BECc6ddD5589a9a3Bb93fAc3A53D26b7cb819"
}

ABI = """[
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "PotionAdded", "type": "event", "inputs": [{"name": "potionAddress", "type": "address", "indexed": true, "internalType": "address"}, {"name": "requiredResources", "type": "address[]", "indexed": false, "internalType": "address[]"}, {"name": "requiredQuantities", "type": "uint32[]", "indexed": false, "internalType": "uint32[]"}], "anonymous": false},
    {"name": "PotionCreated", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "potionAddress", "type": "address", "indexed": false, "internalType": "address"}, {"name": "quantity", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "requiredResources", "type": "address[]", "indexed": false, "internalType": "address[]"}, {"name": "requiredQuantities", "type": "uint32[]", "indexed": false, "internalType": "uint32[]"}], "anonymous": false},
    {"name": "PotionUpdated", "type": "event", "inputs": [{"name": "potionAddress", "type": "address", "indexed": true, "internalType": "address"}, {"name": "requiredResources", "type": "address[]", "indexed": false, "internalType": "address[]"}, {"name": "requiredQuantities", "type": "uint32[]", "indexed": false, "internalType": "uint32[]"}, {"name": "status", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "addPotion", "type": "function", "inputs": [{"name": "_potionAddress", "type": "address", "internalType": "address"}, {"name": "_requiredResources", "type": "address[]", "internalType": "address[]"}, {"name": "_requiredQuantities", "type": "uint32[]", "internalType": "uint32[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "addressToPotionId", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "createPotion", "type": "function", "inputs": [{"name": "_potionAddress", "type": "address", "internalType": "address"}, {"name": "_quantity", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getPotion", "type": "function", "inputs": [{"name": "_potionAddress", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "potionAddress", "type": "address", "internalType": "address"}, {"name": "requiredResources", "type": "address[]", "internalType": "address[]"}, {"name": "requiredQuantities", "type": "uint32[]", "internalType": "uint32[]"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "internalType": "struct Alchemist.Potion"}], "stateMutability": "view"},
    {"name": "getPotions", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "potionAddress", "type": "address", "internalType": "address"}, {"name": "requiredResources", "type": "address[]", "internalType": "address[]"}, {"name": "requiredQuantities", "type": "uint32[]", "internalType": "uint32[]"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "internalType": "struct Alchemist.Potion[]"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_dfkGoldAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "potions", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "potionAddress", "type": "address", "internalType": "address"}, {"name": "status", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "removePotion", "type": "function", "inputs": [{"name": "_potionAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "togglePause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "updatePotion", "type": "function", "inputs": [{"name": "_potionAddress", "type": "address", "internalType": "address"}, {"name": "_requiredResources", "type": "address[]", "internalType": "address[]"}, {"name": "_requiredQuantities", "type": "uint32[]", "internalType": "uint32[]"}, {"name": "_status", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class Alchemist(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def add_potion(self, cred:Credentials, _potion_address:address, _required_resources:Sequence[address], _required_quantities:Sequence[uint32]) -> TxReceipt:
        tx = self.contract.functions.addPotion(_potion_address, _required_resources, _required_quantities)
        return self.send_transaction(tx, cred)

    def address_to_potion_id(self, a:address) -> uint256:
        return self.contract.functions.addressToPotionId(a).call()

    def create_potion(self, cred:Credentials, _potion_address:address, _quantity:uint256) -> TxReceipt:
        tx = self.contract.functions.createPotion(_potion_address, _quantity)
        return self.send_transaction(tx, cred)

    def get_potion(self, _potion_address:address) -> tuple:
        return self.contract.functions.getPotion(_potion_address).call()

    def get_potions(self) -> Sequence[tuple]:
        return self.contract.functions.getPotions().call()

    def initialize(self, cred:Credentials, _dfk_gold_address:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_dfk_gold_address)
        return self.send_transaction(tx, cred)

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def potions(self, a:uint256) -> Tuple[address, uint8]:
        return self.contract.functions.potions(a).call()

    def remove_potion(self, cred:Credentials, _potion_address:address) -> TxReceipt:
        tx = self.contract.functions.removePotion(_potion_address)
        return self.send_transaction(tx, cred)

    def toggle_pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.togglePause()
        return self.send_transaction(tx, cred)

    def update_potion(self, cred:Credentials, _potion_address:address, _required_resources:Sequence[address], _required_quantities:Sequence[uint32], _status:uint8) -> TxReceipt:
        tx = self.contract.functions.updatePotion(_potion_address, _required_resources, _required_quantities, _status)
        return self.send_transaction(tx, cred)