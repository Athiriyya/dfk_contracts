
from ..abi_contract_wrapper import ABIContractWrapper
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x501CdC4ef10b63219704Bf6aDb785dfccb06deE2",
    "sd": "0x6d5B86EaC9097EA4a94B2b69Cd4854678B89f839"
}

ABI = """[
    {"name": "ERC1155Received", "type": "event", "inputs": [{"name": "_srcChainId", "type": "uint16", "internalType": "uint16", "indexed": false}, {"name": "_srcAddress", "type": "bytes", "internalType": "bytes", "indexed": false}, {"name": "receiver", "type": "address", "internalType": "address", "indexed": false}, {"name": "item", "type": "address", "internalType": "address", "indexed": false}, {"name": "amount", "type": "uint256", "internalType": "uint256", "indexed": false}, {"name": "id", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "internalType": "uint8", "indexed": false}], "anonymous": false},
    {"name": "ItemMapped", "type": "event", "inputs": [{"name": "identifier", "type": "bytes32", "internalType": "bytes32", "indexed": false}, {"name": "contractAddress", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "ItemReceived", "type": "event", "inputs": [{"name": "_srcChainId", "type": "uint16", "internalType": "uint16", "indexed": false}, {"name": "_srcAddress", "type": "bytes", "internalType": "bytes", "indexed": false}, {"name": "receiver", "type": "address", "internalType": "address", "indexed": false}, {"name": "item", "type": "address", "internalType": "address", "indexed": false}, {"name": "amount", "type": "uint256", "internalType": "uint256", "indexed": false}], "anonymous": false},
    {"name": "MessageFailed", "type": "event", "inputs": [{"name": "_srcChainId", "type": "uint16", "internalType": "uint16", "indexed": false}, {"name": "_srcAddress", "type": "bytes", "internalType": "bytes", "indexed": false}, {"name": "_nonce", "type": "uint64", "internalType": "uint64", "indexed": false}, {"name": "_payload", "type": "bytes", "internalType": "bytes", "indexed": false}], "anonymous": false},
    {"name": "OwnershipTransferred", "type": "event", "inputs": [{"name": "previousOwner", "type": "address", "internalType": "address", "indexed": true}, {"name": "newOwner", "type": "address", "internalType": "address", "indexed": true}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "SetTrustedRemote", "type": "event", "inputs": [{"name": "_srcChainId", "type": "uint16", "internalType": "uint16", "indexed": false}, {"name": "_srcAddress", "type": "bytes", "internalType": "bytes", "indexed": false}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "internalType": "address", "indexed": false}], "anonymous": false},
    {"name": "FUNCTION_TYPE_SEND", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "NO_EXTRA_GAS", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "__NonblockingLzAppUpgradeable_init", "type": "function", "inputs": [{"name": "_lzEndpoint", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "__NonblockingLzAppUpgradeable_init_unchained", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "estimateFeeSendERC1155", "type": "function", "inputs": [{"name": "_dstChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_receiver", "type": "address", "internalType": "address"}, {"name": "_item", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}, {"name": "_id", "type": "uint256", "internalType": "uint256"}, {"name": "_useZro", "type": "bool", "internalType": "bool"}, {"name": "_adapterParams", "type": "bytes", "internalType": "bytes"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "estimateFeeSendERC1155", "type": "function", "inputs": [{"name": "_dstChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_receiver", "type": "address", "internalType": "address"}, {"name": "_item", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}, {"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "estimateFeeSendERC20", "type": "function", "inputs": [{"name": "_dstChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_receiver", "type": "address", "internalType": "address"}, {"name": "_item", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "estimateFeeSendERC20", "type": "function", "inputs": [{"name": "_dstChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_receiver", "type": "address", "internalType": "address"}, {"name": "_item", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}, {"name": "_useZro", "type": "bool", "internalType": "bool"}, {"name": "_adapterParams", "type": "bytes", "internalType": "bytes"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "failedMessages", "type": "function", "inputs": [{"name": "", "type": "uint16", "internalType": "uint16"}, {"name": "", "type": "bytes", "internalType": "bytes"}, {"name": "", "type": "uint64", "internalType": "uint64"}], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "forceResumeReceive", "type": "function", "inputs": [{"name": "_srcChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_srcAddress", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getConfig", "type": "function", "inputs": [{"name": "_version", "type": "uint16", "internalType": "uint16"}, {"name": "_chainId", "type": "uint16", "internalType": "uint16"}, {"name": "", "type": "address", "internalType": "address"}, {"name": "_configType", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bytes", "internalType": "bytes"}], "stateMutability": "view"},
    {"name": "getGasLimit", "type": "function", "inputs": [{"name": "_adapterParams", "type": "bytes", "internalType": "bytes"}], "outputs": [{"name": "gasLimit", "type": "uint256", "internalType": "uint256"}], "stateMutability": "pure"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_lzEndpoint", "type": "address", "internalType": "address"}, {"name": "_itemMinter", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "isTrustedRemote", "type": "function", "inputs": [{"name": "_srcChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_srcAddress", "type": "bytes", "internalType": "bytes"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "itemAddresses", "type": "function", "inputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "itemIdentifiers", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "lzEndpoint", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract ILayerZeroEndpointUpgradeable"}], "stateMutability": "view"},
    {"name": "lzReceive", "type": "function", "inputs": [{"name": "_srcChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_srcAddress", "type": "bytes", "internalType": "bytes"}, {"name": "_nonce", "type": "uint64", "internalType": "uint64"}, {"name": "_payload", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "mapItem", "type": "function", "inputs": [{"name": "_identifier", "type": "string", "internalType": "string"}, {"name": "_contractAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "minDstGasLookup", "type": "function", "inputs": [{"name": "", "type": "uint16", "internalType": "uint16"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "nonblockingLzReceive", "type": "function", "inputs": [{"name": "_srcChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_srcAddress", "type": "bytes", "internalType": "bytes"}, {"name": "_nonce", "type": "uint64", "internalType": "uint64"}, {"name": "_payload", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "owner", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "renounceOwnership", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "retryMessage", "type": "function", "inputs": [{"name": "_srcChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_srcAddress", "type": "bytes", "internalType": "bytes"}, {"name": "_nonce", "type": "uint64", "internalType": "uint64"}, {"name": "_payload", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "payable"},
    {"name": "sendERC1155", "type": "function", "inputs": [{"name": "_dstChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_receiver", "type": "address", "internalType": "address"}, {"name": "_item", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}, {"name": "_id", "type": "uint256", "internalType": "uint256"}, {"name": "_zroPaymentAddress", "type": "address", "internalType": "address"}, {"name": "_adapterParams", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "payable"},
    {"name": "sendERC1155", "type": "function", "inputs": [{"name": "_dstChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_receiver", "type": "address", "internalType": "address"}, {"name": "_item", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}, {"name": "_id", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "payable"},
    {"name": "sendERC20", "type": "function", "inputs": [{"name": "_dstChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_receiver", "type": "address", "internalType": "address"}, {"name": "_item", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}, {"name": "_zroPaymentAddress", "type": "address", "internalType": "address"}, {"name": "_adapterParams", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "payable"},
    {"name": "sendERC20", "type": "function", "inputs": [{"name": "_dstChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_receiver", "type": "address", "internalType": "address"}, {"name": "_item", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "payable"},
    {"name": "setConfig", "type": "function", "inputs": [{"name": "_version", "type": "uint16", "internalType": "uint16"}, {"name": "_chainId", "type": "uint16", "internalType": "uint16"}, {"name": "_configType", "type": "uint256", "internalType": "uint256"}, {"name": "_config", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setMinDstGasLookup", "type": "function", "inputs": [{"name": "_dstChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_type", "type": "uint256", "internalType": "uint256"}, {"name": "_dstGasAmount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setReceiveVersion", "type": "function", "inputs": [{"name": "_version", "type": "uint16", "internalType": "uint16"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setSendVersion", "type": "function", "inputs": [{"name": "_version", "type": "uint16", "internalType": "uint16"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTrustedRemote", "type": "function", "inputs": [{"name": "_srcChainId", "type": "uint16", "internalType": "uint16"}, {"name": "_srcAddress", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setUseCustomAdapterParams", "type": "function", "inputs": [{"name": "_useCustomAdapterParams", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "transferOwnership", "type": "function", "inputs": [{"name": "newOwner", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "trustedRemoteLookup", "type": "function", "inputs": [{"name": "", "type": "uint16", "internalType": "uint16"}], "outputs": [{"name": "", "type": "bytes", "internalType": "bytes"}], "stateMutability": "view"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "useCustomAdapterParams", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"}
]
"""     

class ItemBridge(ABIContractWrapper):
    def __init__(self, chain_key:str, rpc:str):
        contract_address = CONTRACT_ADDRESS[chain_key]
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def function_type_send(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.FUNCTION_TYPE_SEND().call(block_identifier=block_identifier)

    def no_extra_gas(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.NO_EXTRA_GAS().call(block_identifier=block_identifier)

    def ___nonblocking_lz_app_upgradeable_init(self, cred:Credentials, _lz_endpoint:address) -> TxReceipt:
        tx = self.contract.functions.__NonblockingLzAppUpgradeable_init(_lz_endpoint)
        return self.send_transaction(tx, cred)

    def ___nonblocking_lz_app_upgradeable_init_unchained(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.__NonblockingLzAppUpgradeable_init_unchained()
        return self.send_transaction(tx, cred)

    def estimate_fee_send_erc1155(self, _dst_chain_id:uint16, _receiver:address, _item:address, _amount:uint256, _id:uint256, _use_zro:bool, _adapter_params:bytes, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.estimateFeeSendERC1155(_dst_chain_id, _receiver, _item, _amount, _id, _use_zro, _adapter_params).call(block_identifier=block_identifier)

    def estimate_fee_send_erc1155(self, _dst_chain_id:uint16, _receiver:address, _item:address, _amount:uint256, _id:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.estimateFeeSendERC1155(_dst_chain_id, _receiver, _item, _amount, _id).call(block_identifier=block_identifier)

    def estimate_fee_send_erc20(self, _dst_chain_id:uint16, _receiver:address, _item:address, _amount:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.estimateFeeSendERC20(_dst_chain_id, _receiver, _item, _amount).call(block_identifier=block_identifier)

    def estimate_fee_send_erc20(self, _dst_chain_id:uint16, _receiver:address, _item:address, _amount:uint256, _use_zro:bool, _adapter_params:bytes, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.estimateFeeSendERC20(_dst_chain_id, _receiver, _item, _amount, _use_zro, _adapter_params).call(block_identifier=block_identifier)

    def failed_messages(self, a:uint16, b:bytes, c:uint64, block_identifier:BlockIdentifier = 'latest') -> bytes32:
        return self.contract.functions.failedMessages(a, b, c).call(block_identifier=block_identifier)

    def force_resume_receive(self, cred:Credentials, _src_chain_id:uint16, _src_address:bytes) -> TxReceipt:
        tx = self.contract.functions.forceResumeReceive(_src_chain_id, _src_address)
        return self.send_transaction(tx, cred)

    def get_config(self, _version:uint16, _chain_id:uint16, a:address, _config_type:uint256, block_identifier:BlockIdentifier = 'latest') -> bytes:
        return self.contract.functions.getConfig(_version, _chain_id, a, _config_type).call(block_identifier=block_identifier)

    def get_gas_limit(self, _adapter_params:bytes, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.getGasLimit(_adapter_params).call(block_identifier=block_identifier)

    def initialize(self, cred:Credentials, _lz_endpoint:address, _item_minter:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_lz_endpoint, _item_minter)
        return self.send_transaction(tx, cred)

    def is_trusted_remote(self, _src_chain_id:uint16, _src_address:bytes, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.isTrustedRemote(_src_chain_id, _src_address).call(block_identifier=block_identifier)

    def item_addresses(self, a:bytes32, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.itemAddresses(a).call(block_identifier=block_identifier)

    def item_identifiers(self, a:address, block_identifier:BlockIdentifier = 'latest') -> bytes32:
        return self.contract.functions.itemIdentifiers(a).call(block_identifier=block_identifier)

    def lz_endpoint(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.lzEndpoint().call(block_identifier=block_identifier)

    def lz_receive(self, cred:Credentials, _src_chain_id:uint16, _src_address:bytes, _nonce:uint64, _payload:bytes) -> TxReceipt:
        tx = self.contract.functions.lzReceive(_src_chain_id, _src_address, _nonce, _payload)
        return self.send_transaction(tx, cred)

    def map_item(self, cred:Credentials, _identifier:string, _contract_address:address) -> TxReceipt:
        tx = self.contract.functions.mapItem(_identifier, _contract_address)
        return self.send_transaction(tx, cred)

    def min_dst_gas_lookup(self, a:uint16, b:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.minDstGasLookup(a, b).call(block_identifier=block_identifier)

    def nonblocking_lz_receive(self, cred:Credentials, _src_chain_id:uint16, _src_address:bytes, _nonce:uint64, _payload:bytes) -> TxReceipt:
        tx = self.contract.functions.nonblockingLzReceive(_src_chain_id, _src_address, _nonce, _payload)
        return self.send_transaction(tx, cred)

    def owner(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.owner().call(block_identifier=block_identifier)

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
        return self.send_transaction(tx, cred)

    def paused(self, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.paused().call(block_identifier=block_identifier)

    def renounce_ownership(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.renounceOwnership()
        return self.send_transaction(tx, cred)

    def retry_message(self, cred:Credentials, _src_chain_id:uint16, _src_address:bytes, _nonce:uint64, _payload:bytes) -> TxReceipt:
        tx = self.contract.functions.retryMessage(_src_chain_id, _src_address, _nonce, _payload)
        return self.send_transaction(tx, cred)

    def send_erc1155(self, cred:Credentials, _dst_chain_id:uint16, _receiver:address, _item:address, _amount:uint256, _id:uint256, _zro_payment_address:address, _adapter_params:bytes) -> TxReceipt:
        tx = self.contract.functions.sendERC1155(_dst_chain_id, _receiver, _item, _amount, _id, _zro_payment_address, _adapter_params)
        return self.send_transaction(tx, cred)

    def send_erc1155(self, cred:Credentials, _dst_chain_id:uint16, _receiver:address, _item:address, _amount:uint256, _id:uint256) -> TxReceipt:
        tx = self.contract.functions.sendERC1155(_dst_chain_id, _receiver, _item, _amount, _id)
        return self.send_transaction(tx, cred)

    def send_erc20(self, cred:Credentials, _dst_chain_id:uint16, _receiver:address, _item:address, _amount:uint256, _zro_payment_address:address, _adapter_params:bytes) -> TxReceipt:
        tx = self.contract.functions.sendERC20(_dst_chain_id, _receiver, _item, _amount, _zro_payment_address, _adapter_params)
        return self.send_transaction(tx, cred)

    def send_erc20(self, cred:Credentials, _dst_chain_id:uint16, _receiver:address, _item:address, _amount:uint256) -> TxReceipt:
        tx = self.contract.functions.sendERC20(_dst_chain_id, _receiver, _item, _amount)
        return self.send_transaction(tx, cred)

    def set_config(self, cred:Credentials, _version:uint16, _chain_id:uint16, _config_type:uint256, _config:bytes) -> TxReceipt:
        tx = self.contract.functions.setConfig(_version, _chain_id, _config_type, _config)
        return self.send_transaction(tx, cred)

    def set_min_dst_gas_lookup(self, cred:Credentials, _dst_chain_id:uint16, _type:uint256, _dst_gas_amount:uint256) -> TxReceipt:
        tx = self.contract.functions.setMinDstGasLookup(_dst_chain_id, _type, _dst_gas_amount)
        return self.send_transaction(tx, cred)

    def set_receive_version(self, cred:Credentials, _version:uint16) -> TxReceipt:
        tx = self.contract.functions.setReceiveVersion(_version)
        return self.send_transaction(tx, cred)

    def set_send_version(self, cred:Credentials, _version:uint16) -> TxReceipt:
        tx = self.contract.functions.setSendVersion(_version)
        return self.send_transaction(tx, cred)

    def set_trusted_remote(self, cred:Credentials, _src_chain_id:uint16, _src_address:bytes) -> TxReceipt:
        tx = self.contract.functions.setTrustedRemote(_src_chain_id, _src_address)
        return self.send_transaction(tx, cred)

    def set_use_custom_adapter_params(self, cred:Credentials, _use_custom_adapter_params:bool) -> TxReceipt:
        tx = self.contract.functions.setUseCustomAdapterParams(_use_custom_adapter_params)
        return self.send_transaction(tx, cred)

    def transfer_ownership(self, cred:Credentials, new_owner:address) -> TxReceipt:
        tx = self.contract.functions.transferOwnership(new_owner)
        return self.send_transaction(tx, cred)

    def trusted_remote_lookup(self, a:uint16, block_identifier:BlockIdentifier = 'latest') -> bytes:
        return self.contract.functions.trustedRemoteLookup(a).call(block_identifier=block_identifier)

    def unpause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unpause()
        return self.send_transaction(tx, cred)

    def use_custom_adapter_params(self, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.useCustomAdapterParams().call(block_identifier=block_identifier)