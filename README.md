# DFK Contracts
DFK Contracts is a set of all current contracts for [Defi Kingdoms](https://defikingdoms.com/), autogenerated from the contracts' ABI json files (findable on the [DFK Devs pages](https://devs.defikingdoms.com/)). See the [ABI Maker](https://github.com/Athiriyya/abi_maker) for more info on how this process works.

The intention

## Installation
Use pip:

```shell 
pip install dfk_contracts
```

## Usage
To get access to ALL of a DFK's contracts, there's a special object:
```python
from dfk_contracts.all_dfk_contracts import AllDfkContracts

# Use default Crystalvale RPC
all_cv_contracts = AllDfkContracts('cv')

# Or use a custom Serendale RPC
all_sd_contracts('sd', 'https://alternate.klaytn.rpc.com')

crystals = all_cv_contracts.crystal_core.get_user_crystals('0xYOUR_ADDRESS')

```

Each contract here can also be instantiated on its own, for example:
```python
from dfk_contracts.contracts import crystal_core

# Use default Crystalvale RPC
cc = crystal_core.CrystalCore('cv')
crystals = cc.get_user_crystals('0xYOUR_ADDRESS')
```


## Contact
File an [issue](https://github.com/Athiriyya/dfk_contracts/issues), write me at athiriyya@gmail.com, or find @Athiriyya on the [GameFi Devs Discord](https://discord.gg/psjY362pss).