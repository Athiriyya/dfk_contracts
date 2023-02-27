
from ..abi_contract_wrapper import ABIContractWrapper
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x576C260513204392F0eC0bc865450872025CB1cA",
    "sd": "0x22e656419Be8A0abf0B53D0941FfDC3B70Fea36e"
}

ABI = """[
    {"name": "EggCracked", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "eggId", "type": "uint256", "indexed": true, "internalType": "uint256"}, {"name": "petId", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "EggIncubated", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "eggId", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "eggType", "type": "uint8", "indexed": true, "internalType": "uint8"}, {"name": "tier", "type": "uint8", "indexed": true, "internalType": "uint8"}], "anonymous": false},
    {"name": "FeeAddressAdded", "type": "event", "inputs": [{"name": "feeAddress", "type": "address", "indexed": true, "internalType": "address"}, {"name": "feePercent", "type": "uint256", "indexed": true, "internalType": "uint256"}], "anonymous": false},
    {"name": "FeeDeferred", "type": "event", "inputs": [{"name": "source", "type": "address", "indexed": true, "internalType": "address"}, {"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "token", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "timestamp", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
    {"name": "FeeDisbursed", "type": "event", "inputs": [{"name": "source", "type": "address", "indexed": true, "internalType": "address"}, {"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "token", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "timestamp", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
    {"name": "FeeLockedBurned", "type": "event", "inputs": [{"name": "source", "type": "address", "indexed": true, "internalType": "address"}, {"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "token", "type": "address", "indexed": false, "internalType": "address"}, {"name": "amount", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "timestamp", "type": "uint64", "indexed": false, "internalType": "uint64"}], "anonymous": false},
    {"name": "Initialized", "type": "event", "inputs": [{"name": "version", "type": "uint8", "indexed": false, "internalType": "uint8"}], "anonymous": false},
    {"name": "Paused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "RoleAdminChanged", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "previousAdminRole", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "newAdminRole", "type": "bytes32", "indexed": true, "internalType": "bytes32"}], "anonymous": false},
    {"name": "RoleGranted", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "account", "type": "address", "indexed": true, "internalType": "address"}, {"name": "sender", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "RoleRevoked", "type": "event", "inputs": [{"name": "role", "type": "bytes32", "indexed": true, "internalType": "bytes32"}, {"name": "account", "type": "address", "indexed": true, "internalType": "address"}, {"name": "sender", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "Unpaused", "type": "event", "inputs": [{"name": "account", "type": "address", "indexed": false, "internalType": "address"}], "anonymous": false},
    {"name": "DEFAULT_ADMIN_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "HATCHING_MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "MODERATOR_ROLE", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "crack", "type": "function", "inputs": [{"name": "_eggId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "eggTypeCosts", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "eggAddress", "type": "address", "internalType": "address"}, {"name": "itemAddress1", "type": "address", "internalType": "address"}, {"name": "itemAmount1", "type": "uint16", "internalType": "uint16"}, {"name": "itemAddress2", "type": "address", "internalType": "address"}, {"name": "itemAmount2", "type": "uint16", "internalType": "uint16"}], "stateMutability": "view"},
    {"name": "feeAddresses", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "feePercents", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "getEgg", "type": "function", "inputs": [{"name": "_eggId", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "tuple", "components": [{"name": "id", "type": "uint256", "internalType": "uint256"}, {"name": "petId", "type": "uint256", "internalType": "uint256"}, {"name": "owner", "type": "address", "internalType": "address"}, {"name": "eggType", "type": "uint8", "internalType": "uint8"}, {"name": "seedblock", "type": "uint256", "internalType": "uint256"}, {"name": "finishTime", "type": "uint256", "internalType": "uint256"}, {"name": "tier", "type": "uint8", "internalType": "uint8"}], "internalType": "struct UnhatchedEgg"}], "stateMutability": "view"},
    {"name": "getRoleAdmin", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "", "type": "bytes32", "internalType": "bytes32"}], "stateMutability": "view"},
    {"name": "getUserEggs", "type": "function", "inputs": [{"name": "_address", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "grantRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "hasRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "incubateEgg", "type": "function", "inputs": [{"name": "_eggType", "type": "uint8", "internalType": "uint8"}, {"name": "_tier", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "incubateEggWithLocked", "type": "function", "inputs": [{"name": "_eggType", "type": "uint8", "internalType": "uint8"}, {"name": "_tier", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "initialize", "type": "function", "inputs": [{"name": "_petCoreAddress", "type": "address", "internalType": "address"}, {"name": "_powerTokenAddress", "type": "address", "internalType": "address"}, {"name": "_goldAddress", "type": "address", "internalType": "address"}, {"name": "_gaiaTearsAddress", "type": "address", "internalType": "address"}, {"name": "_randomGeneratorAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "originId", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "pause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "paused", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "powerToken", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "contract IPowerToken"}], "stateMutability": "view"},
    {"name": "priceTiers", "type": "function", "inputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "powerTokenCost", "type": "uint8", "internalType": "uint8"}, {"name": "goldCost", "type": "uint16", "internalType": "uint16"}, {"name": "tearCost", "type": "uint8", "internalType": "uint8"}, {"name": "incubationTime", "type": "uint32", "internalType": "uint32"}, {"name": "shinyChance", "type": "uint16", "internalType": "uint16"}], "stateMutability": "view"},
    {"name": "renounceRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "revokeRole", "type": "function", "inputs": [{"name": "role", "type": "bytes32", "internalType": "bytes32"}, {"name": "account", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "season", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "setAppearanceChoices", "type": "function", "inputs": [{"name": "_eggType", "type": "uint8", "internalType": "uint8"}, {"name": "_rarity", "type": "uint8", "internalType": "uint8"}, {"name": "_isSpecial", "type": "uint8", "internalType": "uint8"}, {"name": "_startIndex", "type": "uint256", "internalType": "uint256"}, {"name": "_endIndex", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setEggTypeCosts", "type": "function", "inputs": [{"name": "_eggType", "type": "uint8", "internalType": "uint8"}, {"name": "_eggTypeCost", "type": "tuple", "components": [{"name": "eggAddress", "type": "address", "internalType": "address"}, {"name": "itemAddress1", "type": "address", "internalType": "address"}, {"name": "itemAmount1", "type": "uint16", "internalType": "uint16"}, {"name": "itemAddress2", "type": "address", "internalType": "address"}, {"name": "itemAmount2", "type": "uint16", "internalType": "uint16"}], "internalType": "struct EggTypeCost"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setFees", "type": "function", "inputs": [{"name": "_feeAddresses", "type": "address[]", "internalType": "address[]"}, {"name": "_feePercents", "type": "uint256[]", "internalType": "uint256[]"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setOriginId", "type": "function", "inputs": [{"name": "_originId", "type": "uint8", "internalType": "uint8"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setPetCore", "type": "function", "inputs": [{"name": "_petCoreAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setPriceTiers", "type": "function", "inputs": [{"name": "_priceTierIndex", "type": "uint8", "internalType": "uint8"}, {"name": "_priceTier", "type": "tuple", "components": [{"name": "powerTokenCost", "type": "uint8", "internalType": "uint8"}, {"name": "goldCost", "type": "uint16", "internalType": "uint16"}, {"name": "tearCost", "type": "uint8", "internalType": "uint8"}, {"name": "incubationTime", "type": "uint32", "internalType": "uint32"}, {"name": "shinyChance", "type": "uint16", "internalType": "uint16"}], "internalType": "struct PriceTier"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setTokenUnlocker", "type": "function", "inputs": [{"name": "_tokenUnlockerAddress", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "supportsInterface", "type": "function", "inputs": [{"name": "interfaceId", "type": "bytes4", "internalType": "bytes4"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "totalEggs", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "unpause", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class PetHatching(ABIContractWrapper):
    def __init__(self, chain_key:str, rpc:str):
        contract_address = CONTRACT_ADDRESS[chain_key]
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def crack(self, cred:Credentials, _egg_id:uint256) -> TxReceipt:
        tx = self.contract.functions.crack(_egg_id)
        return self.send_transaction(tx, cred)

    def egg_type_costs(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> Tuple[address, address, uint16, address, uint16]:
        return self.contract.functions.eggTypeCosts(a).call(block_identifier=block_identifier)

    def fee_addresses(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.feeAddresses(a).call(block_identifier=block_identifier)

    def fee_percents(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.feePercents(a).call(block_identifier=block_identifier)

    def get_egg(self, _egg_id:uint256, block_identifier:BlockIdentifier = 'latest') -> tuple:
        return self.contract.functions.getEgg(_egg_id).call(block_identifier=block_identifier)

    def get_user_eggs(self, _address:address, block_identifier:BlockIdentifier = 'latest') -> List[uint256]:
        return self.contract.functions.getUserEggs(_address).call(block_identifier=block_identifier)

    def incubate_egg(self, cred:Credentials, _egg_type:uint8, _tier:uint8) -> TxReceipt:
        tx = self.contract.functions.incubateEgg(_egg_type, _tier)
        return self.send_transaction(tx, cred)

    def incubate_egg_with_locked(self, cred:Credentials, _egg_type:uint8, _tier:uint8) -> TxReceipt:
        tx = self.contract.functions.incubateEggWithLocked(_egg_type, _tier)
        return self.send_transaction(tx, cred)

    def initialize(self, cred:Credentials, _pet_core_address:address, _power_token_address:address, _gold_address:address, _gaia_tears_address:address, _random_generator_address:address) -> TxReceipt:
        tx = self.contract.functions.initialize(_pet_core_address, _power_token_address, _gold_address, _gaia_tears_address, _random_generator_address)
        return self.send_transaction(tx, cred)

    def origin_id(self, block_identifier:BlockIdentifier = 'latest') -> uint8:
        return self.contract.functions.originId().call(block_identifier=block_identifier)

    def pause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.pause()
        return self.send_transaction(tx, cred)

    def paused(self, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.paused().call(block_identifier=block_identifier)

    def power_token(self, block_identifier:BlockIdentifier = 'latest') -> address:
        return self.contract.functions.powerToken().call(block_identifier=block_identifier)

    def price_tiers(self, a:uint256, block_identifier:BlockIdentifier = 'latest') -> Tuple[uint8, uint16, uint8, uint32, uint16]:
        return self.contract.functions.priceTiers(a).call(block_identifier=block_identifier)

    def season(self, block_identifier:BlockIdentifier = 'latest') -> uint8:
        return self.contract.functions.season().call(block_identifier=block_identifier)

    def set_appearance_choices(self, cred:Credentials, _egg_type:uint8, _rarity:uint8, _is_special:uint8, _start_index:uint256, _end_index:uint256) -> TxReceipt:
        tx = self.contract.functions.setAppearanceChoices(_egg_type, _rarity, _is_special, _start_index, _end_index)
        return self.send_transaction(tx, cred)

    def set_egg_type_costs(self, cred:Credentials, _egg_type:uint8, _egg_type_cost:tuple) -> TxReceipt:
        tx = self.contract.functions.setEggTypeCosts(_egg_type, _egg_type_cost)
        return self.send_transaction(tx, cred)

    def set_fees(self, cred:Credentials, _fee_addresses:Sequence[address], _fee_percents:Sequence[uint256]) -> TxReceipt:
        tx = self.contract.functions.setFees(_fee_addresses, _fee_percents)
        return self.send_transaction(tx, cred)

    def set_origin_id(self, cred:Credentials, _origin_id:uint8) -> TxReceipt:
        tx = self.contract.functions.setOriginId(_origin_id)
        return self.send_transaction(tx, cred)

    def set_pet_core(self, cred:Credentials, _pet_core_address:address) -> TxReceipt:
        tx = self.contract.functions.setPetCore(_pet_core_address)
        return self.send_transaction(tx, cred)

    def set_price_tiers(self, cred:Credentials, _price_tier_index:uint8, _price_tier:tuple) -> TxReceipt:
        tx = self.contract.functions.setPriceTiers(_price_tier_index, _price_tier)
        return self.send_transaction(tx, cred)

    def set_token_unlocker(self, cred:Credentials, _token_unlocker_address:address) -> TxReceipt:
        tx = self.contract.functions.setTokenUnlocker(_token_unlocker_address)
        return self.send_transaction(tx, cred)

    def supports_interface(self, interface_id:bytes4, block_identifier:BlockIdentifier = 'latest') -> bool:
        return self.contract.functions.supportsInterface(interface_id).call(block_identifier=block_identifier)

    def total_eggs(self, block_identifier:BlockIdentifier = 'latest') -> uint256:
        return self.contract.functions.totalEggs().call(block_identifier=block_identifier)

    def unpause(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unpause()
        return self.send_transaction(tx, cred)