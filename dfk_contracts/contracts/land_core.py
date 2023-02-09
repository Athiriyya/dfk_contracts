
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0xD5f5bE1037e457727e011ADE9Ca54d21c21a3F8A",
    "sd": "0x07520d5b2a7bf2DD0d48Bf08311Ac598F9ab4D4A"
}

ABI = """[
    {"name": "Approval", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "approved", "type": "address", "indexed": true, "internalType": "address"}, {"name": "tokenId", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "ApprovalForAll", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "operator", "type": "address", "indexed": true, "internalType": "address"}, {"name": "approved", "type": "bool", "indexed": false, "internalType": "bool"}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "LandClaimed", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "landId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "region", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "LandMoved", "type": "event", "inputs": [{"name": "landId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "oldRegion", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "newRegion", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "Transfer", "type": "event", "inputs": [{"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "tokenId", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "approve", "type": "function", "inputs": [{"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "balanceOf", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "claimLand", "type": "function", "inputs": [{"name": "_to", "type": "address", "internalType": "address"}, {"name": "_tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "getAccountLands", "type": "function", "inputs": [{"name": "_account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "landId", "type": "uint256", "internalType": "uint256"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "owner", "type": "address", "internalType": "address"}, {"name": "region", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "steward", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint64", "internalType": "uint64"}], "internalType": "struct LandCore.LandMeta[]"}], "stateMutability": "view"},
    {"name": "getAllLands", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "landId", "type": "uint256", "internalType": "uint256"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "owner", "type": "address", "internalType": "address"}, {"name": "region", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "steward", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint64", "internalType": "uint64"}], "internalType": "struct LandCore.LandMeta[]"}], "stateMutability": "view"},
    {"name": "getApproved", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "getLand", "type": "function", "inputs": [{"name": "_landId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "landId", "type": "uint256", "internalType": "uint256"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "owner", "type": "address", "internalType": "address"}, {"name": "region", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "steward", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint64", "internalType": "uint64"}], "internalType": "struct LandCore.LandMeta"}], "stateMutability": "view"},
    {"name": "getLandsByRegion", "type": "function", "inputs": [{"name": "_region", "type": "uint32", "internalType": "uint32"}], "outputs": [{"name": "", "type": "tuple[]", "components": [{"name": "landId", "type": "uint256", "internalType": "uint256"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "owner", "type": "address", "internalType": "address"}, {"name": "region", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "steward", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint64", "internalType": "uint64"}], "internalType": "struct LandCore.LandMeta[]"}], "stateMutability": "view"},
    {"name": "initialize", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "isApprovedForAll", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "operator", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "landIdToMeta", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "landId", "type": "uint256", "internalType": "uint256"}, {"name": "name", "type": "string", "internalType": "string"}, {"name": "owner", "type": "address", "internalType": "address"}, {"name": "region", "type": "uint256", "internalType": "uint256"}, {"name": "level", "type": "uint8", "internalType": "uint8"}, {"name": "steward", "type": "uint256", "internalType": "uint256"}, {"name": "score", "type": "uint64", "internalType": "uint64"}], "stateMutability": "view"},
    {"name": "name", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "onERC721Received", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "address", "internalType": "address"}, {"name": "", "type": "uint256", "internalType": "uint256"}, {"name": "", "type": "bytes", "internalType": "bytes"}], "outputs": [{"name": "", "type": "bytes4", "internalType": "bytes4"}], "stateMutability": "pure"},
    {"name": "ownerOf", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "regionToLandCount", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "regionToLands", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}, {"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "safeMint", "type": "function", "inputs": [{"name": "_owner", "type": "address", "internalType": "address"}, {"name": "_landId", "type": "uint256", "internalType": "uint256"}, {"name": "_name", "type": "string", "internalType": "string"}, {"name": "_region", "type": "uint32", "internalType": "uint32"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "safeTransferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "safeTransferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}, {"name": "_data", "type": "bytes", "internalType": "bytes"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setApprovalForAll", "type": "function", "inputs": [{"name": "operator", "type": "address", "internalType": "address"}, {"name": "approved", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "symbol", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "tokenByIndex", "type": "function", "inputs": [{"name": "index", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "tokenOfOwnerByIndex", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "index", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "tokenURI", "type": "function", "inputs": [{"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "totalSupply", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "transferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "tokenId", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "updateLandRegion", "type": "function", "inputs": [{"name": "_landId", "type": "uint256", "internalType": "uint256"}, {"name": "_region", "type": "uint256", "internalType": "uint256"}, {"name": "_oldLandIndex", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class LandCore(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def approve(self, cred:Credentials, to:address, token_id:uint256) -> TxReceipt:
        tx = self.contract.functions.approve(to, token_id)
        return self.send_transaction(tx, cred)

    def balance_of(self, owner:address) -> uint256:
        return self.contract.functions.balanceOf(owner).call()

    def claim_land(self, cred:Credentials, _to:address, _token_id:uint256) -> TxReceipt:
        tx = self.contract.functions.claimLand(_to, _token_id)
        return self.send_transaction(tx, cred)

    def get_account_lands(self, _account:address) -> Sequence[tuple]:
        return self.contract.functions.getAccountLands(_account).call()

    def get_all_lands(self) -> Sequence[tuple]:
        return self.contract.functions.getAllLands().call()

    def get_approved(self, token_id:uint256) -> address:
        return self.contract.functions.getApproved(token_id).call()

    def get_land(self, _land_id:uint256) -> tuple:
        return self.contract.functions.getLand(_land_id).call()

    def get_lands_by_region(self, _region:uint32) -> Sequence[tuple]:
        return self.contract.functions.getLandsByRegion(_region).call()

    def initialize(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.initialize()
        return self.send_transaction(tx, cred)

    def is_approved_for_all(self, owner:address, operator:address) -> bool:
        return self.contract.functions.isApprovedForAll(owner, operator).call()

    def land_id_to_meta(self, a:uint256) -> Tuple[uint256, string, address, uint256, uint8, uint256, uint64]:
        return self.contract.functions.landIdToMeta(a).call()

    def name(self) -> string:
        return self.contract.functions.name().call()

    def on_erc721_received(self, a:address, b:address, c:uint256, d:bytes) -> bytes4:
        return self.contract.functions.onERC721Received(a, b, c, d).call()

    def owner_of(self, token_id:uint256) -> address:
        return self.contract.functions.ownerOf(token_id).call()

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
        return self.send_transaction(tx, cred)

    def paused(self) -> bool:
        return self.contract.functions.paused().call()

    def region_to_land_count(self, a:uint256) -> uint256:
        return self.contract.functions.regionToLandCount(a).call()

    def region_to_lands(self, a:uint256, b:uint256) -> uint256:
        return self.contract.functions.regionToLands(a, b).call()

    def safe_mint(self, cred:Credentials, _owner:address, _land_id:uint256, _name:string, _region:uint32) -> TxReceipt:
        tx = self.contract.functions.safeMint(_owner, _land_id, _name, _region)
        return self.send_transaction(tx, cred)

    def safe_transfer_from(self, cred:Credentials, _from:address, to:address, token_id:uint256) -> TxReceipt:
        tx = self.contract.functions.safeTransferFrom(_from, to, token_id)
        return self.send_transaction(tx, cred)

    def safe_transfer_from(self, cred:Credentials, _from:address, to:address, token_id:uint256, _data:bytes) -> TxReceipt:
        tx = self.contract.functions.safeTransferFrom(_from, to, token_id, _data)
        return self.send_transaction(tx, cred)

    def set_approval_for_all(self, cred:Credentials, operator:address, approved:bool) -> TxReceipt:
        tx = self.contract.functions.setApprovalForAll(operator, approved)
        return self.send_transaction(tx, cred)

    def symbol(self) -> string:
        return self.contract.functions.symbol().call()

    def token_by_index(self, index:uint256) -> uint256:
        return self.contract.functions.tokenByIndex(index).call()

    def token_of_owner_by_index(self, owner:address, index:uint256) -> uint256:
        return self.contract.functions.tokenOfOwnerByIndex(owner, index).call()

    def token_uri(self, token_id:uint256) -> string:
        return self.contract.functions.tokenURI(token_id).call()

    def total_supply(self) -> uint256:
        return self.contract.functions.totalSupply().call()

    def transfer_from(self, cred:Credentials, _from:address, to:address, token_id:uint256) -> TxReceipt:
        tx = self.contract.functions.transferFrom(_from, to, token_id)
        return self.send_transaction(tx, cred)

    def unpause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unpause()
        return self.send_transaction(tx, cred)

    def update_land_region(self, cred:Credentials, _land_id:uint256, _region:uint256, _old_land_index:uint256) -> TxReceipt:
        tx = self.contract.functions.updateLandRegion(_land_id, _region, _old_land_index)
        return self.send_transaction(tx, cred)