
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x739B1666c2956f601f095298132773074c3E184b",
    "sd": "0xEE258eF5F4338B37E9BA9dE6a56382AdB32056E2"
}

ABI = """[
    {"name": "AdminChanged", "type": "event", "inputs": [{"name": "previousAdmin", "type": "address", "indexed": false, "internalType": "address"}, {"name": "newAdmin", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "Upgraded", "type": "event", "inputs": [{"name": "implementation", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"type": "fallback", "stateMutability": "payable"},
    {"name": "admin", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "nonpayable"},
    {"name": "changeAdmin", "type": "function", "inputs": [{"name": "newAdmin", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "implementation", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "nonpayable"},
    {"name": "upgradeTo", "type": "function", "inputs": [{"name": "newImplementation", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "upgradeToAndCall", "type": "function", "inputs": [{"name": "newImplementation", "type": "address", "internalType": "address"}, {"name": "data", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "payable"},
    {"type": "receive", "stateMutability": "payable"},
    {"name": "HeroArrived", "type": "event", "inputs": [{"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "arrivalChainId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "HeroSent", "type": "event", "inputs": [{"name": "heroId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "arrivalChainId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "OwnershipTransferred", "type": "event", "inputs": [{"name": "previousOwner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "newOwner", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "SetTrustedRemote", "type": "event", "inputs": [{"name": "_srcChainId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "_srcAddress", "type": "bytes32", "indexed": false, "internalType": "bytes32"}], "anonymous": false},
    {"name": "assistingAuction", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "executeMessage", "type": "function", "inputs": [{"name": "_srcAddress", "type": "bytes32", "internalType": "bytes32"}, {"name": "_srcChainId", "type": "uint256", "internalType": "uint256"}, {"name": "_message", "type": "bytes", "internalType": "bytes"}, {"name": "_executor", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getTrustedRemote", "type": "function", "inputs": [{"name": "_chainId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "trustedRemote", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "heroes", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_messageBus", "type": "address", "internalType": "address"}, {"name": "_heroes", "type": "address", "internalType": "address"}, {"name": "_assistingAuction", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "messageBus", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "msgGasLimit", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "owner", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "renounceOwnership", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "sendHero", "type": "function", "inputs": [{"name": "_heroId", "type": "uint256", "internalType": "uint256"}, {"name": "_dstChainId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "payable"},
    {"name": "setAssistingAuctionAddress", "type": "function", "inputs": [{"name": "_assistingAuction", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setMessageBus", "type": "function", "inputs": [{"name": "_messageBus", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setMsgGasLimit", "type": "function", "inputs": [{"name": "_msgGasLimit", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTrustedRemote", "type": "function", "inputs": [{"name": "_srcChainId", "type": "uint256", "internalType": "uint256"}, {"name": "_srcAddress", "type": "bytes32", "internalType": "bytes32"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "transferOwnership", "type": "function", "inputs": [{"name": "newOwner", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"type": "constructor", "inputs": [{"name": "initialLogic", "type": "address", "internalType": "address"}, {"name": "initialAdmin", "type": "address", "internalType": "address"}, {"name": "_data", "type": "bytes", "internalType": "bytes"}], "stateMutability": "payable"}
]
"""     

class HeroBridge(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def admin(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.admin()
        return self.send_transaction(tx, cred)

    def change_admin(self, cred:Credentials, new_admin:address) -> TxReceipt:
        tx = self.contract.functions.changeAdmin(new_admin)
        return self.send_transaction(tx, cred)

    def implementation(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.implementation()
        return self.send_transaction(tx, cred)

    def upgrade_to(self, cred:Credentials, new_implementation:address) -> TxReceipt:
        tx = self.contract.functions.upgradeTo(new_implementation)
        return self.send_transaction(tx, cred)

    def upgrade_to_and_call(self, cred:Credentials, new_implementation:address, data:bytes) -> TxReceipt:
        tx = self.contract.functions.upgradeToAndCall(new_implementation, data)
        return self.send_transaction(tx, cred)

    def assisting_auction(self) -> address:
        return self.contract.functions.assistingAuction().call()

    def execute_message(self, cred:Credentials, _src_address:bytes32, _src_chain_id:uint256, _message:bytes, _executor:address) -> TxReceipt:
        tx = self.contract.functions.executeMessage(_src_address, _src_chain_id, _message, _executor)
        return self.send_transaction(tx, cred)

    def get_trusted_remote(self, _chain_id:uint256) -> bytes32:
        return self.contract.functions.getTrustedRemote(_chain_id).call()

    def heroes(self) -> address:
        return self.contract.functions.heroes().call()

    def initialize(self, cred:Credentials, _message_bus:address, _heroes:address, _assisting_auction:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_message_bus, _heroes, _assisting_auction)
        return self.send_transaction(tx, cred)

    def message_bus(self) -> address:
        return self.contract.functions.messageBus().call()

    def msg_gas_limit(self) -> uint256:
        return self.contract.functions.msgGasLimit().call()

    def owner(self) -> address:
        return self.contract.functions.owner().call()

    def renounce_ownership(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.renounceOwnership()
        return self.send_transaction(tx, cred)

    def send_hero(self, cred:Credentials, _hero_id:uint256, _dst_chain_id:uint256) -> TxReceipt:
        tx = self.contract.functions.sendHero(_hero_id, _dst_chain_id)
        return self.send_transaction(tx, cred)

    def set_assisting_auction_address(self, cred:Credentials, _assisting_auction:address) -> TxReceipt:
        tx = self.contract.functions.setAssistingAuctionAddress(_assisting_auction)
        return self.send_transaction(tx, cred)

    def set_message_bus(self, cred:Credentials, _message_bus:address) -> TxReceipt:
        tx = self.contract.functions.setMessageBus(_message_bus)
        return self.send_transaction(tx, cred)

    def set_msg_gas_limit(self, cred:Credentials, _msg_gas_limit:uint256) -> TxReceipt:
        tx = self.contract.functions.setMsgGasLimit(_msg_gas_limit)
        return self.send_transaction(tx, cred)

    def set_trusted_remote(self, cred:Credentials, _src_chain_id:uint256, _src_address:bytes32) -> TxReceipt:
        tx = self.contract.functions.setTrustedRemote(_src_chain_id, _src_address)
        return self.send_transaction(tx, cred)

    def transfer_ownership(self, cred:Credentials, new_owner:address) -> TxReceipt:
        tx = self.contract.functions.transferOwnership(new_owner)
        return self.send_transaction(tx, cred)