
from typing import Sequence, Dict, Tuple, List
from web3.datastructures import AttributeDict
from web3.types import TxReceipt, BlockIdentifier
from eth_typing.evm import ChecksumAddress

HexAddress = ChecksumAddress
# We lose some detail here; Python doesnt have signed/unsigned int differentions
# or bytes sizes. For now, these type aliases let us use Solidity's native types 
# as type hints while being a little less particular to Pythons Mypy type analyzer
address = ChecksumAddress
bool = bool
string = str
uint8 = int
uint16 = int
uint32 = int
uint64 = int
uint128 = int
uint256 = int
int64 = int
int256 = int
bytes4 = bytes
bytes32 = bytes
# These show up in some ABIs, but there's some extra work we'd need to do
# to use them in Python since they're already reserved words
# bytes = bytes
# tuple = Sequence
