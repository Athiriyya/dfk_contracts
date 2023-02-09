
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xBd1f65e7f350C614d364AEFeB2d87F829b0E465d",
    "sd": ""
}

ABI = """[
    {"type": "constructor", "inputs": [{"name": "_heroCoreAddress", "type": "address", "internalType": "address"}, {"name": "_geneScienceAddress", "type": "address", "internalType": "address"}], "stateMutability": "nonpayable"},
    {"name": "CrystalAirdrop", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "crystalId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "createdBlock", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "CrystalOpen", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "crystalId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "airdropCrystal", "type": "function", "inputs": [{"name": "_recipient", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "crystals", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "summonerTears", "type": "uint8", "internalType": "uint8"}, {"name": "assistantTears", "type": "uint8", "internalType": "uint8"}, {"name": "bonusItem", "type": "address", "internalType": "address"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "enabled", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "extractNumber", "type": "function", "inputs": [{"name": "randomNumber", "type": "uint256", "internalType": "uint256"}, {"name": "digits", "type": "uint256", "internalType": "uint256"}, {"name": "offset", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "result", "type": "uint256", "internalType": "uint256"}], "stateMutability": "pure"},
    {"name": "getCrystal", "type": "function", "inputs": [{"name": "_crystalId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "summonerId", "type": "uint256", "internalType": "uint256"}, {"name": "assistantId", "type": "uint256", "internalType": "uint256"}, {"name": "generation", "type": "uint16", "internalType": "uint16"}, {"name": "createdBlock", "type": "uint256", "internalType": "uint256"}, {"name": "heroId", "type": "uint256", "internalType": "uint256"}, {"name": "summonerTears", "type": "uint8", "internalType": "uint8"}, {"name": "assistantTears", "type": "uint8", "internalType": "uint8"}, {"name": "bonusItem", "type": "address", "internalType": "address"}, {"name": "maxSummons", "type": "uint32", "internalType": "uint32"}, {"name": "firstName", "type": "uint32", "internalType": "uint32"}, {"name": "lastName", "type": "uint32", "internalType": "uint32"}, {"name": "shinyStyle", "type": "uint8", "internalType": "uint8"}], "internalType": "struct ICrystalTypes.HeroCrystal"}], "stateMutability": "view"},
    {"name": "getUserCrystals", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "open", "type": "function", "inputs": [{"name": "_crystalId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "toggleEnabled", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "userCrystals", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "vrf", "type": "function", "inputs": [{"name": "blockNumber", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "result", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"}
]
"""     

class Gen0Airdrop(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def airdrop_crystal(self, cred:Credentials, _recipient:address) -> TxReceipt:
        tx = self.contract.functions.airdropCrystal(_recipient)
        return self.send_transaction(tx, cred)

    def crystals(self, a:uint256) -> Tuple[address, uint256, uint256, uint16, uint256, uint256, uint8, uint8, address, uint32, uint32, uint32, uint8]:
        return self.contract.functions.crystals(a).call()

    def enabled(self) -> bool:
        return self.contract.functions.enabled().call()

    def extract_number(self, random_number:uint256, digits:uint256, offset:uint256) -> uint256:
        return self.contract.functions.extractNumber(random_number, digits, offset).call()

    def get_crystal(self, _crystal_id:uint256) -> tuple:
        return self.contract.functions.getCrystal(_crystal_id).call()

    def get_user_crystals(self, _address:address) -> Sequence[uint256]:
        return self.contract.functions.getUserCrystals(_address).call()

    def open(self, cred:Credentials, _crystal_id:uint256) -> TxReceipt:
        tx = self.contract.functions.open(_crystal_id)
        return self.send_transaction(tx, cred)

    def toggle_enabled(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.toggleEnabled()
        return self.send_transaction(tx, cred)

    def user_crystals(self, a:address, b:uint256) -> uint256:
        return self.contract.functions.userCrystals(a, b).call()

    def vrf(self, block_number:uint256) -> bytes32:
        return self.contract.functions.vrf(block_number).call()