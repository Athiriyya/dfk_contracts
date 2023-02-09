
from typing import Sequence, Dict, Tuple
from web3.datastructures import AttributeDict

# We lose some detail here; Python doesnt have signed/unsigned int differentions
# or bytes sizes. For now, these type aliase let us use Soliditys native types 
# as type hints while being a little less particular to Pythons Mypy type analyzer
address = str
bool = bool
# tuple = Sequence
string = str
uint8 = int
uint16 = int
uint32 = int
uint64 = int
uint128 = int
uint256 = int
int64 = int
int256 = int
# bytes = bytes
bytes4 = bytes
bytes32 = bytes

TxReceipt = AttributeDict 