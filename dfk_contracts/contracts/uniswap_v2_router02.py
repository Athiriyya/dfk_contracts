
from ..abi_wrapper_contract import ABIWrapperContract
from ..solidity_types import *
from ..credentials import Credentials

CONTRACT_ADDRESS =     {
    "cv": "0x3C351E1afdd1b1BC44e931E12D4E05D6125eaeCa",
    "sd": "0x9e987E5E9aB872598f601BE4aCC5ac23F484845E"
}

ABI = """[
    {"type": "constructor", "inputs": [{"name": "_factory", "type": "address", "internalType": "address"}, {"name": "_WETH", "type": "address", "internalType": "address"}], "stateMutability": "nonpayable"},
    {"name": "WETH", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "addLiquidity", "type": "function", "inputs": [{"name": "tokenA", "type": "address", "internalType": "address"}, {"name": "tokenB", "type": "address", "internalType": "address"}, {"name": "amountADesired", "type": "uint256", "internalType": "uint256"}, {"name": "amountBDesired", "type": "uint256", "internalType": "uint256"}, {"name": "amountAMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountBMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountA", "type": "uint256", "internalType": "uint256"}, {"name": "amountB", "type": "uint256", "internalType": "uint256"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "addLiquidityETH", "type": "function", "inputs": [{"name": "token", "type": "address", "internalType": "address"}, {"name": "amountTokenDesired", "type": "uint256", "internalType": "uint256"}, {"name": "amountTokenMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountETHMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountToken", "type": "uint256", "internalType": "uint256"}, {"name": "amountETH", "type": "uint256", "internalType": "uint256"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}], "stateMutability": "payable"},
    {"name": "factory", "type": "function", "inputs": [], "outputs": [{"name": "", "type": "address", "internalType": "address"}], "stateMutability": "view"},
    {"name": "getAmountIn", "type": "function", "inputs": [{"name": "amountOut", "type": "uint256", "internalType": "uint256"}, {"name": "reserveIn", "type": "uint256", "internalType": "uint256"}, {"name": "reserveOut", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}], "stateMutability": "pure"},
    {"name": "getAmountOut", "type": "function", "inputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}, {"name": "reserveIn", "type": "uint256", "internalType": "uint256"}, {"name": "reserveOut", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountOut", "type": "uint256", "internalType": "uint256"}], "stateMutability": "pure"},
    {"name": "getAmountsIn", "type": "function", "inputs": [{"name": "amountOut", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "getAmountsOut", "type": "function", "inputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "view"},
    {"name": "quote", "type": "function", "inputs": [{"name": "amountA", "type": "uint256", "internalType": "uint256"}, {"name": "reserveA", "type": "uint256", "internalType": "uint256"}, {"name": "reserveB", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountB", "type": "uint256", "internalType": "uint256"}], "stateMutability": "pure"},
    {"name": "removeLiquidity", "type": "function", "inputs": [{"name": "tokenA", "type": "address", "internalType": "address"}, {"name": "tokenB", "type": "address", "internalType": "address"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}, {"name": "amountAMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountBMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountA", "type": "uint256", "internalType": "uint256"}, {"name": "amountB", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "removeLiquidityETH", "type": "function", "inputs": [{"name": "token", "type": "address", "internalType": "address"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}, {"name": "amountTokenMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountETHMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountToken", "type": "uint256", "internalType": "uint256"}, {"name": "amountETH", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "removeLiquidityETHSupportingFeeOnTransferTokens", "type": "function", "inputs": [{"name": "token", "type": "address", "internalType": "address"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}, {"name": "amountTokenMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountETHMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amountETH", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "removeLiquidityETHWithPermit", "type": "function", "inputs": [{"name": "token", "type": "address", "internalType": "address"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}, {"name": "amountTokenMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountETHMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}, {"name": "approveMax", "type": "bool", "internalType": "bool"}, {"name": "v", "type": "uint8", "internalType": "uint8"}, {"name": "r", "type": "bytes32", "internalType": "bytes32"}, {"name": "s", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "amountToken", "type": "uint256", "internalType": "uint256"}, {"name": "amountETH", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "removeLiquidityETHWithPermitSupportingFeeOnTransferTokens", "type": "function", "inputs": [{"name": "token", "type": "address", "internalType": "address"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}, {"name": "amountTokenMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountETHMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}, {"name": "approveMax", "type": "bool", "internalType": "bool"}, {"name": "v", "type": "uint8", "internalType": "uint8"}, {"name": "r", "type": "bytes32", "internalType": "bytes32"}, {"name": "s", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "amountETH", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "removeLiquidityWithPermit", "type": "function", "inputs": [{"name": "tokenA", "type": "address", "internalType": "address"}, {"name": "tokenB", "type": "address", "internalType": "address"}, {"name": "liquidity", "type": "uint256", "internalType": "uint256"}, {"name": "amountAMin", "type": "uint256", "internalType": "uint256"}, {"name": "amountBMin", "type": "uint256", "internalType": "uint256"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}, {"name": "approveMax", "type": "bool", "internalType": "bool"}, {"name": "v", "type": "uint8", "internalType": "uint8"}, {"name": "r", "type": "bytes32", "internalType": "bytes32"}, {"name": "s", "type": "bytes32", "internalType": "bytes32"}], "outputs": [{"name": "amountA", "type": "uint256", "internalType": "uint256"}, {"name": "amountB", "type": "uint256", "internalType": "uint256"}], "stateMutability": "nonpayable"},
    {"name": "swapETHForExactTokens", "type": "function", "inputs": [{"name": "amountOut", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "payable"},
    {"name": "swapExactETHForTokens", "type": "function", "inputs": [{"name": "amountOutMin", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "payable"},
    {"name": "swapExactETHForTokensSupportingFeeOnTransferTokens", "type": "function", "inputs": [{"name": "amountOutMin", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "payable"},
    {"name": "swapExactTokensForETH", "type": "function", "inputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}, {"name": "amountOutMin", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "nonpayable"},
    {"name": "swapExactTokensForETHSupportingFeeOnTransferTokens", "type": "function", "inputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}, {"name": "amountOutMin", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "swapExactTokensForTokens", "type": "function", "inputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}, {"name": "amountOutMin", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "nonpayable"},
    {"name": "swapExactTokensForTokensSupportingFeeOnTransferTokens", "type": "function", "inputs": [{"name": "amountIn", "type": "uint256", "internalType": "uint256"}, {"name": "amountOutMin", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [], "stateMutability": "nonpayable"},
    {"name": "swapTokensForExactETH", "type": "function", "inputs": [{"name": "amountOut", "type": "uint256", "internalType": "uint256"}, {"name": "amountInMax", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "nonpayable"},
    {"name": "swapTokensForExactTokens", "type": "function", "inputs": [{"name": "amountOut", "type": "uint256", "internalType": "uint256"}, {"name": "amountInMax", "type": "uint256", "internalType": "uint256"}, {"name": "path", "type": "address[]", "internalType": "address[]"}, {"name": "to", "type": "address", "internalType": "address"}, {"name": "deadline", "type": "uint256", "internalType": "uint256"}], "outputs": [{"name": "amounts", "type": "uint256[]", "internalType": "uint256[]"}], "stateMutability": "nonpayable"},
    {"type": "receive", "stateMutability": "payable"}
]
"""     

class UniswapV2Router02(ABIWrapperContract):

    def __init__(self, chain_key:str, rpc:str=None):
        contract_address = CONTRACT_ADDRESS.get(chain_key)
        super().__init__(contract_address=contract_address, abi=ABI, rpc=rpc)

    def weth(self) -> address:
        return self.contract.functions.WETH().call()

    def add_liquidity(self, cred:Credentials, token_a:address, token_b:address, amount_a_desired:uint256, amount_b_desired:uint256, amount_a_min:uint256, amount_b_min:uint256, to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.addLiquidity(token_a, token_b, amount_a_desired, amount_b_desired, amount_a_min, amount_b_min, to, deadline)
        return self.send_transaction(tx, cred)

    def add_liquidity_eth(self, cred:Credentials, token:address, amount_token_desired:uint256, amount_token_min:uint256, amount_eth_min:uint256, to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.addLiquidityETH(token, amount_token_desired, amount_token_min, amount_eth_min, to, deadline)
        return self.send_transaction(tx, cred)

    def factory(self) -> address:
        return self.contract.functions.factory().call()

    def get_amount_in(self, amount_out:uint256, reserve_in:uint256, reserve_out:uint256) -> uint256:
        return self.contract.functions.getAmountIn(amount_out, reserve_in, reserve_out).call()

    def get_amount_out(self, amount_in:uint256, reserve_in:uint256, reserve_out:uint256) -> uint256:
        return self.contract.functions.getAmountOut(amount_in, reserve_in, reserve_out).call()

    def get_amounts_in(self, amount_out:uint256, path:Sequence[address]) -> Sequence[uint256]:
        return self.contract.functions.getAmountsIn(amount_out, path).call()

    def get_amounts_out(self, amount_in:uint256, path:Sequence[address]) -> Sequence[uint256]:
        return self.contract.functions.getAmountsOut(amount_in, path).call()

    def quote(self, amount_a:uint256, reserve_a:uint256, reserve_b:uint256) -> uint256:
        return self.contract.functions.quote(amount_a, reserve_a, reserve_b).call()

    def remove_liquidity(self, cred:Credentials, token_a:address, token_b:address, liquidity:uint256, amount_a_min:uint256, amount_b_min:uint256, to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.removeLiquidity(token_a, token_b, liquidity, amount_a_min, amount_b_min, to, deadline)
        return self.send_transaction(tx, cred)

    def remove_liquidity_eth(self, cred:Credentials, token:address, liquidity:uint256, amount_token_min:uint256, amount_eth_min:uint256, to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.removeLiquidityETH(token, liquidity, amount_token_min, amount_eth_min, to, deadline)
        return self.send_transaction(tx, cred)

    def remove_liquidity_eth_supporting_fee_on_transfer_tokens(self, cred:Credentials, token:address, liquidity:uint256, amount_token_min:uint256, amount_eth_min:uint256, to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.removeLiquidityETHSupportingFeeOnTransferTokens(token, liquidity, amount_token_min, amount_eth_min, to, deadline)
        return self.send_transaction(tx, cred)

    def remove_liquidity_eth_with_permit(self, cred:Credentials, token:address, liquidity:uint256, amount_token_min:uint256, amount_eth_min:uint256, to:address, deadline:uint256, approve_max:bool, v:uint8, r:bytes32, s:bytes32) -> TxReceipt:
        tx = self.contract.functions.removeLiquidityETHWithPermit(token, liquidity, amount_token_min, amount_eth_min, to, deadline, approve_max, v, r, s)
        return self.send_transaction(tx, cred)

    def remove_liquidity_eth_with_permit_supporting_fee_on_transfer_tokens(self, cred:Credentials, token:address, liquidity:uint256, amount_token_min:uint256, amount_eth_min:uint256, to:address, deadline:uint256, approve_max:bool, v:uint8, r:bytes32, s:bytes32) -> TxReceipt:
        tx = self.contract.functions.removeLiquidityETHWithPermitSupportingFeeOnTransferTokens(token, liquidity, amount_token_min, amount_eth_min, to, deadline, approve_max, v, r, s)
        return self.send_transaction(tx, cred)

    def remove_liquidity_with_permit(self, cred:Credentials, token_a:address, token_b:address, liquidity:uint256, amount_a_min:uint256, amount_b_min:uint256, to:address, deadline:uint256, approve_max:bool, v:uint8, r:bytes32, s:bytes32) -> TxReceipt:
        tx = self.contract.functions.removeLiquidityWithPermit(token_a, token_b, liquidity, amount_a_min, amount_b_min, to, deadline, approve_max, v, r, s)
        return self.send_transaction(tx, cred)

    def swap_eth_for_exact_tokens(self, cred:Credentials, amount_out:uint256, path:Sequence[address], to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.swapETHForExactTokens(amount_out, path, to, deadline)
        return self.send_transaction(tx, cred)

    def swap_exact_eth_for_tokens(self, cred:Credentials, amount_out_min:uint256, path:Sequence[address], to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.swapExactETHForTokens(amount_out_min, path, to, deadline)
        return self.send_transaction(tx, cred)

    def swap_exact_eth_for_tokens_supporting_fee_on_transfer_tokens(self, cred:Credentials, amount_out_min:uint256, path:Sequence[address], to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(amount_out_min, path, to, deadline)
        return self.send_transaction(tx, cred)

    def swap_exact_tokens_for_eth(self, cred:Credentials, amount_in:uint256, amount_out_min:uint256, path:Sequence[address], to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.swapExactTokensForETH(amount_in, amount_out_min, path, to, deadline)
        return self.send_transaction(tx, cred)

    def swap_exact_tokens_for_eth_supporting_fee_on_transfer_tokens(self, cred:Credentials, amount_in:uint256, amount_out_min:uint256, path:Sequence[address], to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.swapExactTokensForETHSupportingFeeOnTransferTokens(amount_in, amount_out_min, path, to, deadline)
        return self.send_transaction(tx, cred)

    def swap_exact_tokens_for_tokens(self, cred:Credentials, amount_in:uint256, amount_out_min:uint256, path:Sequence[address], to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.swapExactTokensForTokens(amount_in, amount_out_min, path, to, deadline)
        return self.send_transaction(tx, cred)

    def swap_exact_tokens_for_tokens_supporting_fee_on_transfer_tokens(self, cred:Credentials, amount_in:uint256, amount_out_min:uint256, path:Sequence[address], to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.swapExactTokensForTokensSupportingFeeOnTransferTokens(amount_in, amount_out_min, path, to, deadline)
        return self.send_transaction(tx, cred)

    def swap_tokens_for_exact_eth(self, cred:Credentials, amount_out:uint256, amount_in_max:uint256, path:Sequence[address], to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.swapTokensForExactETH(amount_out, amount_in_max, path, to, deadline)
        return self.send_transaction(tx, cred)

    def swap_tokens_for_exact_tokens(self, cred:Credentials, amount_out:uint256, amount_in_max:uint256, path:Sequence[address], to:address, deadline:uint256) -> TxReceipt:
        tx = self.contract.functions.swapTokensForExactTokens(amount_out, amount_in_max, path, to, deadline)
        return self.send_transaction(tx, cred)