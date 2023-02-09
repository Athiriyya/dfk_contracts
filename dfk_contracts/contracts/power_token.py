
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x04b9dA42306B023f3572e106B11D82aAd9D32EBb",
    "sd": "0xB3F5867E277798b50ba7A71C0b24FDcA03045eDF"
}

ABI = """[
    {"type": "constructor", "inputs": [{"name": "_name", "type": "string", "internalType": "string"}, {"name": "_symbol", "type": "string", "internalType": "string"}, {"name": "_cap", "type": "uint256", "internalType": "uint256"}, {"name": "_manualMintLimit", "type": "uint256", "internalType": "uint256"}, {"name": "_lockFromTime", "type": "uint256", "internalType": "uint256"}, {"name": "_lockToTime", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "Approval", "type": "event", "inputs": [{"name": "owner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "spender", "type": "address", "indexed": true, "internalType": "address"}, {"name": "value", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Lock", "type": "event", "inputs": [{"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "value", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "MaxTransferAmountRateUpdated", "type": "event", "inputs": [{"name": "previousRate", "type": "uint256", "indexed": false, "internalType": "uint256"}, {"name": "newRate", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "OwnershipTransferred", "type": "event", "inputs": [{"name": "previousOwner", "type": "address", "indexed": true, "internalType": "address"}, {"name": "newOwner", "type": "address", "indexed": true, "internalType": "address"}], "anonymous": false},
    {"name": "Transfer", "type": "event", "inputs": [{"name": "from", "type": "address", "indexed": true, "internalType": "address"}, {"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "value", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "Unlock", "type": "event", "inputs": [{"name": "to", "type": "address", "indexed": true, "internalType": "address"}, {"name": "value", "type": "uint256", "indexed": false, "internalType": "uint256"}], "anonymous": false},
    {"name": "addAuthorized", "type": "function", "inputs": [{"name": "_toAdd", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "allowance", "type": "function", "inputs": [{"name": "owner", "type": "address", "internalType": "address"}, {"name": "spender", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "approve", "type": "function", "inputs": [{"name": "spender", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "authorized", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "view"},
    {"name": "balanceOf", "type": "function", "inputs": [{"name": "account", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "canUnlockAmount", "type": "function", "inputs": [{"name": "_holder", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "cap", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "circulatingSupply", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "decimals", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint8", "internalType": "uint8"}], "stateMutability": "view"},
    {"name": "decreaseAllowance", "type": "function", "inputs": [{"name": "spender", "type": "address", "internalType": "address"}, {"name": "subtractedValue", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "increaseAllowance", "type": "function", "inputs": [{"name": "spender", "type": "address", "internalType": "address"}, {"name": "addedValue", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "lastUnlockTime", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "lock", "type": "function", "inputs": [{"name": "_holder", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "lockFromTime", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "lockFromUpdate", "type": "function", "inputs": [{"name": "_lockFromTime", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "lockOf", "type": "function", "inputs": [{"name": "_holder", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "lockToTime", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "lockToUpdate", "type": "function", "inputs": [{"name": "_lockToTime", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "manualMint", "type": "function", "inputs": [{"name": "_to", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "manualMintLimit", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "manualMinted", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "maxTransferAmount", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "maxTransferAmountRate", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint16", "internalType": "uint16"}], "stateMutability": "view"},
    {"name": "mint", "type": "function", "inputs": [{"name": "_to", "type": "address", "internalType": "address"}, {"name": "_amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "name", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "owner", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "removeAuthorized", "type": "function", "inputs": [{"name": "_toRemove", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "renounceOwnership", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "setExcludedFromAntiWhale", "type": "function", "inputs": [{"name": "_account", "type": "address", "internalType": "address"}, {"name": "_excluded", "type": "bool", "internalType": "bool"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "symbol", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "string", "internalType": "string"}], "stateMutability": "view"},
    {"name": "totalBalanceOf", "type": "function", "inputs": [{"name": "_holder", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "totalLock", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "totalSupply", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "transfer", "type": "function", "inputs": [{"name": "to", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "transferAll", "type": "function", "inputs": [{"name": "_to", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "transferAllInterval", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "transferAllIntervalUpdate", "type": "function", "inputs": [{"name": "_transferAllInterval", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "transferAllTracker", "type": "function", "inputs": [{"name": "", "type": "address", "internalType": "address"}], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "transferFrom", "type": "function", "inputs": [{"name": "from", "type": "address", "internalType": "address"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "", "type": "bool", "internalType": "bool"}], "stateMutability": "nonpayable"},
    {"name": "transferOwnership", "type": "function", "inputs": [{"name": "newOwner", "type": "address", "internalType": "address"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "unlock", "type": "function", "inputs": [], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "unlockForUser", "type": "function", "inputs": [{"name": "account", "type": "address", "internalType": "address"}, {"name": "amount", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "unlockedSupply", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "uint256", "internalType": "uint256"}], "stateMutability": "view"},
    {"name": "updateMaxTransferAmountRate", "type": "function", "inputs": [{"name": "_maxTransferAmountRate", "type": "uint16", "internalType": "uint16"}], "outputs": [], "stateMutability": "nonpayable"}
]
"""     

class PowerToken(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def add_authorized(self, cred:Credentials, _to_add:address) -> TxReceipt:
        tx = self.contract.functions.addAuthorized(_to_add)
        return self.send_transaction(tx, cred)

    def allowance(self, owner:address, spender:address) -> uint256:
        return self.contract.functions.allowance(owner, spender).call()

    def approve(self, cred:Credentials, spender:address, amount:uint256) -> TxReceipt:
        tx = self.contract.functions.approve(spender, amount)
        return self.send_transaction(tx, cred)

    def authorized(self, a:address) -> bool:
        return self.contract.functions.authorized(a).call()

    def balance_of(self, account:address) -> uint256:
        return self.contract.functions.balanceOf(account).call()

    def can_unlock_amount(self, _holder:address) -> uint256:
        return self.contract.functions.canUnlockAmount(_holder).call()

    def cap(self) -> uint256:
        return self.contract.functions.cap().call()

    def circulating_supply(self) -> uint256:
        return self.contract.functions.circulatingSupply().call()

    def decimals(self) -> uint8:
        return self.contract.functions.decimals().call()

    def decrease_allowance(self, cred:Credentials, spender:address, subtracted_value:uint256) -> TxReceipt:
        tx = self.contract.functions.decreaseAllowance(spender, subtracted_value)
        return self.send_transaction(tx, cred)

    def increase_allowance(self, cred:Credentials, spender:address, added_value:uint256) -> TxReceipt:
        tx = self.contract.functions.increaseAllowance(spender, added_value)
        return self.send_transaction(tx, cred)

    def last_unlock_time(self, a:address) -> uint256:
        return self.contract.functions.lastUnlockTime(a).call()

    def lock(self, cred:Credentials, _holder:address, _amount:uint256) -> TxReceipt:
        tx = self.contract.functions.lock(_holder, _amount)
        return self.send_transaction(tx, cred)

    def lock_from_time(self) -> uint256:
        return self.contract.functions.lockFromTime().call()

    def lock_from_update(self, cred:Credentials, _lock_from_time:uint256) -> TxReceipt:
        tx = self.contract.functions.lockFromUpdate(_lock_from_time)
        return self.send_transaction(tx, cred)

    def lock_of(self, _holder:address) -> uint256:
        return self.contract.functions.lockOf(_holder).call()

    def lock_to_time(self) -> uint256:
        return self.contract.functions.lockToTime().call()

    def lock_to_update(self, cred:Credentials, _lock_to_time:uint256) -> TxReceipt:
        tx = self.contract.functions.lockToUpdate(_lock_to_time)
        return self.send_transaction(tx, cred)

    def manual_mint(self, cred:Credentials, _to:address, _amount:uint256) -> TxReceipt:
        tx = self.contract.functions.manualMint(_to, _amount)
        return self.send_transaction(tx, cred)

    def manual_mint_limit(self) -> uint256:
        return self.contract.functions.manualMintLimit().call()

    def manual_minted(self) -> uint256:
        return self.contract.functions.manualMinted().call()

    def max_transfer_amount(self) -> uint256:
        return self.contract.functions.maxTransferAmount().call()

    def max_transfer_amount_rate(self) -> uint16:
        return self.contract.functions.maxTransferAmountRate().call()

    def mint(self, cred:Credentials, _to:address, _amount:uint256) -> TxReceipt:
        tx = self.contract.functions.mint(_to, _amount)
        return self.send_transaction(tx, cred)

    def name(self) -> string:
        return self.contract.functions.name().call()

    def owner(self) -> address:
        return self.contract.functions.owner().call()

    def remove_authorized(self, cred:Credentials, _to_remove:address) -> TxReceipt:
        tx = self.contract.functions.removeAuthorized(_to_remove)
        return self.send_transaction(tx, cred)

    def renounce_ownership(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.renounceOwnership()
        return self.send_transaction(tx, cred)

    def set_excluded_from_anti_whale(self, cred:Credentials, _account:address, _excluded:bool) -> TxReceipt:
        tx = self.contract.functions.setExcludedFromAntiWhale(_account, _excluded)
        return self.send_transaction(tx, cred)

    def symbol(self) -> string:
        return self.contract.functions.symbol().call()

    def total_balance_of(self, _holder:address) -> uint256:
        return self.contract.functions.totalBalanceOf(_holder).call()

    def total_lock(self) -> uint256:
        return self.contract.functions.totalLock().call()

    def total_supply(self) -> uint256:
        return self.contract.functions.totalSupply().call()

    def transfer(self, cred:Credentials, to:address, amount:uint256) -> TxReceipt:
        tx = self.contract.functions.transfer(to, amount)
        return self.send_transaction(tx, cred)

    def transfer_all(self, cred:Credentials, _to:address) -> TxReceipt:
        tx = self.contract.functions.transferAll(_to)
        return self.send_transaction(tx, cred)

    def transfer_all_interval(self) -> uint256:
        return self.contract.functions.transferAllInterval().call()

    def transfer_all_interval_update(self, cred:Credentials, _transfer_all_interval:uint256) -> TxReceipt:
        tx = self.contract.functions.transferAllIntervalUpdate(_transfer_all_interval)
        return self.send_transaction(tx, cred)

    def transfer_all_tracker(self, a:address) -> uint256:
        return self.contract.functions.transferAllTracker(a).call()

    def transfer_from(self, cred:Credentials, _from:address, to:address, amount:uint256) -> TxReceipt:
        tx = self.contract.functions.transferFrom(_from, to, amount)
        return self.send_transaction(tx, cred)

    def transfer_ownership(self, cred:Credentials, new_owner:address) -> TxReceipt:
        tx = self.contract.functions.transferOwnership(new_owner)
        return self.send_transaction(tx, cred)

    def unlock(self, cred:Credentials) -> TxReceipt:
        tx = self.contract.functions.unlock()
        return self.send_transaction(tx, cred)

    def unlock_for_user(self, cred:Credentials, account:address, amount:uint256) -> TxReceipt:
        tx = self.contract.functions.unlockForUser(account, amount)
        return self.send_transaction(tx, cred)

    def unlocked_supply(self) -> uint256:
        return self.contract.functions.unlockedSupply().call()

    def update_max_transfer_amount_rate(self, cred:Credentials, _max_transfer_amount_rate:uint16) -> TxReceipt:
        tx = self.contract.functions.updateMaxTransferAmountRate(_max_transfer_amount_rate)
        return self.send_transaction(tx, cred)