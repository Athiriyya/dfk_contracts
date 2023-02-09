
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xc32A0e963e50AAAED273A75425fC39902b0d0b3b",
    "sd": ""
}

ABI = """[
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "RecipeSet", "type": "event", "inputs": [{"name": "stoneAddress", "type": "address", "indexed": true, "internalType": "address"}, {"name": "requiredResources", "type": "address[]", "indexed": false, "internalType": "address[]"}, {"name": "requiredQuantities", "type": "uint32[]", "indexed": false, "internalType": "uint32[]"}, {"name": "active", "type": "bool", "indexed": false, "internalType": "bool"}], "anonymous": false},
    {"name": "ShopSetUp", "type": "event", "inputs": [{"name": "workingUntil", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "awayUntil", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "StoneCarved", "type": "event", "inputs": [{"name": "player", "type": "address", "indexed": true, "internalType": "address"}, {"name": "stoneAddress", "type": "address", "indexed": false, "internalType": "address"}, {"name": "quantity", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "adminSetupShop", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "awayUntil", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "carveStone", "type": "function", "inputs": [{"name": "_stoneAddress", "type": "address", "internalType": "address"}, {"name": "_quantity", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getAvailability", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getRecipe", "type": "function", "inputs": [{"name": "stoneAddress", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "requiredResources", "type": "address[]", "internalType": "address[]"}, {"name": "requiredQuantities", "type": "uint32[]", "internalType": "uint32[]"}, {"name": "active", "type": "bool", "internalType": "bool"}], "internalType": "struct StoneCarver.Recipe"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "minClosedTime", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "minOpenTime", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "recipes", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "active", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "setRecipe", "type": "function", "inputs": [{"name": "_stoneAddress", "type": "address", "internalType": "address"}, {"name": "_requiredResources", "type": "address[]", "internalType": "address[]"}, {"name": "_requiredQuantities", "type": "uint32[]", "internalType": "uint32[]"}, {"name": "_active", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTimes", "type": "function", "inputs": [{"name": "_minOpenTime", "type": "uint256", "internalType": "uint256"}, {"name": "_varOpenTime", "type": "uint256", "internalType": "uint256"}, {"name": "_minClosedTime", "type": "uint256", "internalType": "uint256"}, {"name": "_varClosedTime", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setUpShop", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "varClosedTime", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "varOpenTime", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "workingUntil", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"}
]
"""     

class StoneCarver(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def admin_setup_shop(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.adminSetupShop()
        return self.send_transaction(tx, cred)

    def away_until(self) -> uint256:
        return self.contract.functions.awayUntil().call()

    def carve_stone(self, cred:Credentials, _stone_address:address, _quantity:uint256) -> TxReceipt:
        tx = self.contract.functions.carveStone(_stone_address, _quantity)
        return self.send_transaction(tx, cred)

    def get_availability(self) -> Tuple[uint256, uint256]:
        return self.contract.functions.getAvailability().call()

    def get_recipe(self, stone_address:address) -> tuple:
        return self.contract.functions.getRecipe(stone_address).call()

    def initialize(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.initialize()
        return self.send_transaction(tx, cred)

    def min_closed_time(self) -> uint256:
        return self.contract.functions.minClosedTime().call()

    def min_open_time(self) -> uint256:
        return self.contract.functions.minOpenTime().call()

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
        return self.send_transaction(tx, cred)

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def recipes(self, a:address) -> bool:
        return self.contract.functions.recipes(a).call()

    def set_recipe(self, cred:Credentials, _stone_address:address, _required_resources:Sequence[address], _required_quantities:Sequence[uint32], _active:bool) -> TxReceipt:
        tx = self.contract.functions.setRecipe(_stone_address, _required_resources, _required_quantities, _active)
        return self.send_transaction(tx, cred)

    def set_times(self, cred:Credentials, _min_open_time:uint256, _var_open_time:uint256, _min_closed_time:uint256, _var_closed_time:uint256) -> TxReceipt:
        tx = self.contract.functions.setTimes(_min_open_time, _var_open_time, _min_closed_time, _var_closed_time)
        return self.send_transaction(tx, cred)

    def set_up_shop(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.setUpShop()
        return self.send_transaction(tx, cred)

    def unpause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unpause()
        return self.send_transaction(tx, cred)

    def var_closed_time(self) -> uint256:
        return self.contract.functions.varClosedTime().call()

    def var_open_time(self) -> uint256:
        return self.contract.functions.varOpenTime().call()

    def working_until(self) -> uint256:
        return self.contract.functions.workingUntil().call()