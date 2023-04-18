
from ..abi_contract_wrapper import ABIContractWrapper
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x36829ba54e6A0f11fB6e5A45aC5aD2742ec86a0B",
    "sd": "0x5EcB820B32b60cCEd4506bd3b06C80BaFb879446"
}

ABI = """[
    {"name": "AdminChanged", "type": "event", "inputs": [{"name": "previousAdmin", "type": "address", "internalType": "address", "indexed": false}, {"name": "newAdmin", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "Upgraded", "type": "event", "inputs": [{"name": "implementation", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
    {"type": "fallback", "stateMutability": "payable"},
    {"name": "admin", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "nonpayable"},
    {"name": "changeAdmin", "type": "function", "inputs": [{"name": "newAdmin", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "implementation", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "nonpayable"},
    {"name": "upgradeTo", "type": "function", "inputs": [{"name": "newImplementation", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "upgradeToAndCall", "type": "function", "inputs": [{"name": "newImplementation", "type": "address", "internalType": "address"}, {"name": "data", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "payable"},
    {"type": "receive", "stateMutability": "payable"},
    {"name": "OwnershipTransferred", "type": "event", "inputs": [{"name": "previousOwner", "type": "address", "internalType": "address", "indexed": true}, {"name": "newOwner", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
    {"name": "PetArrived", "type": "event", "inputs": [{"name": "petId", "type": "uint256", "internalType": "uint256", "indexed": true}, {"name": "arrivalChainId", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "PetSent", "type": "event", "inputs": [{"name": "petId", "type": "uint256", "internalType": "uint256", "indexed": true}, {"name": "arrivalChainId", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "SetTrustedRemote", "type": "event", "inputs": [{"name": "_srcChainId", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "_srcAddress", "type": "bytes32", "internalType": "bytes32", "indexed": false}], "anonymous": false},
    {"name": "executeMessage", "type": "function", "inputs": [{"name": "_srcAddress", "type": "bytes32", "internalType": "bytes32"}, {"name": "_srcChainId", "type": "uint256", "internalType": "uint256"}, {"name": "_message", "type": "bytes", "internalType": "bytes"}, {"name": "_executor", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getTrustedRemote", "type": "function", "inputs": [{"name": "_chainId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "trustedRemote", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_messageBus", "type": "address", "internalType": "address"}, {"name": "_pets", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "messageBus", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "msgGasLimit", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "owner", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "pets", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "renounceOwnership", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "sendPet", "type": "function", "inputs": [{"name": "_petId", "type": "uint256", "internalType": "uint256"}, {"name": "_dstChainId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "payable"},
    {"name": "setMessageBus", "type": "function", "inputs": [{"name": "_messageBus", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setMsgGasLimit", "type": "function", "inputs": [{"name": "_msgGasLimit", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTrustedRemote", "type": "function", "inputs": [{"name": "_srcChainId", "type": "uint256", "internalType": "uint256"}, {"name": "_srcAddress", "type": "bytes32", "internalType": "bytes32"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "transferOwnership", "type": "function", "inputs": [{"name": "newOwner", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"type": "constructor", "inputs": [{"name": "initialLogic", "type": "address", "internalType": "address"}, {"name": "initialAdmin", "type": "address", "internalType": "address"}, {"name": "_data", "type": "bytes", "internalType": "bytes"}], "stateMutability": "payable"}
]
"""     

class PetBridge(ABIContractWrapper):
    def __init__(self, chain_key:str, rpc:str):
        contract_address = CONTRACT_ADDRESS[chain_key]
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

    def execute_message(self, cred:Credentials, _src_address:bytes32, _src_chain_id:uint256, _message:bytes, _executor:address) -> TxReceipt:
        tx = self.contract.functions.executeMessage(_src_address, _src_chain_id, _message, _executor)
        return self.send_transaction(tx, cred)

    def get_trusted_remote(self, _chain_id:uint256, block_identifier:BlockIdentifier = 'latest') -> bytes32:
        return self.contract.functions.getTrustedRemote(_chain_id).call(block_identifier=block_identifier)

    def initialize(self, cred:Credentials, _message_bus:address, _pets:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_message_bus, _pets)
        return self.send_transaction(tx, cred)

    def message_bus(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.messageBus().call(block_identifier=block_identifier)

    def msg_gas_limit(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.msgGasLimit().call(block_identifier=block_identifier)

    def owner(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.owner().call(block_identifier=block_identifier)

    def pets(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.pets().call(block_identifier=block_identifier)

    def renounce_ownership(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.renounceOwnership()
        return self.send_transaction(tx, cred)

    def send_pet(self, cred:Credentials, _pet_id:uint256, _dst_chain_id:uint256) -> TxReceipt:
        tx = self.contract.functions.sendPet(_pet_id, _dst_chain_id)
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