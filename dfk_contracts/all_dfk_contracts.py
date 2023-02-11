
#! /usr/bin/env python

from .contracts.airdrop_claim import AirdropClaim
from .contracts.alchemist import Alchemist
from .contracts.assisting_auction import AssistingAuction
from .contracts.atonement_crystal import AtonementCrystal
from .contracts.banker import Banker
from .contracts.birthday_cake import BirthdayCake
from .contracts.charity_fund import CharityFund
from .contracts.crystal_core import CrystalCore
from .contracts.power_token import PowerToken
from .contracts.dark_summoning import DarkSummoning
from .contracts.dfk_duel_s2 import DFKDuelS2
from .contracts.duel_rank_claim import DuelRankClaim
from .contracts.erc20 import ERC20
from .contracts.gen0_airdrop import Gen0Airdrop
from .contracts.gen0_reroll import Gen0Reroll
from .contracts.hero_auction import HeroAuction
from .contracts.hero_bridge import HeroBridge
from .contracts.hero_core import HeroCore
from .contracts.hero_summoning import HeroSummoning
from .contracts.item_consumer import ItemConsumer
from .contracts.item_gold_trader_v2 import ItemGoldTraderV2
from .contracts.jewel_token import JewelToken
from .contracts.land_auction import LandAuction
from .contracts.land_core import LandCore
from .contracts.master_gardener import MasterGardener
from .contracts.meditation_circle import MeditationCircle
from .contracts.pasture import Pasture
from .contracts.pet_auction import PetAuction
from .contracts.pet_core import PetCore
from .contracts.pet_exchange import PetExchange
from .contracts.pet_hatching import PetHatching
from .contracts.profiles import Profiles
from .contracts.quest_core import QuestCore
from .contracts.raffle_master import RaffleMaster
from .contracts.raffle_ticket import RaffleTicket
from .contracts.stone_carver import StoneCarver
from .contracts.stylist import Stylist
from .contracts.token_disburse import TokenDisburse
from .contracts.uniswap_v2_factory import UniswapV2Factory
from .contracts.uniswap_v2_router02 import UniswapV2Router02
from .contracts.validator_fund import ValidatorFund

DEFAULT_RPC = {
    "cv": "https://subnets.avax.network/defi-kingdoms/dfk-chain/rpc",
    "sd": "https://klaytn.rpc.defikingdoms.com/"
}

class AllDfkContracts:
    # TODO: we might want to be able to specify other traits, like gas fees or timeout
    def __init__(self, chain_key:str, rpc:str=None):
        self.rpc = rpc or DEFAULT_RPC[chain_key]
        self.chain_key = chain_key

        self.airdrop_claim = AirdropClaim(self.chain_key, self.rpc)
        self.alchemist = Alchemist(self.chain_key, self.rpc)
        self.assisting_auction = AssistingAuction(self.chain_key, self.rpc)
        self.atonement_crystal = AtonementCrystal(self.chain_key, self.rpc)
        self.banker = Banker(self.chain_key, self.rpc)
        self.birthday_cake = BirthdayCake(self.chain_key, self.rpc)
        self.charity_fund = CharityFund(self.chain_key, self.rpc)
        self.crystal_core = CrystalCore(self.chain_key, self.rpc)
        self.power_token = PowerToken(self.chain_key, self.rpc)
        self.dark_summoning = DarkSummoning(self.chain_key, self.rpc)
        self.dfk_duel_s2 = DFKDuelS2(self.chain_key, self.rpc)
        self.duel_rank_claim = DuelRankClaim(self.chain_key, self.rpc)
        self.erc20 = ERC20(self.chain_key, self.rpc)
        self.gen0_airdrop = Gen0Airdrop(self.chain_key, self.rpc)
        self.gen0_reroll = Gen0Reroll(self.chain_key, self.rpc)
        self.hero_auction = HeroAuction(self.chain_key, self.rpc)
        self.hero_bridge = HeroBridge(self.chain_key, self.rpc)
        self.hero_core = HeroCore(self.chain_key, self.rpc)
        self.hero_summoning = HeroSummoning(self.chain_key, self.rpc)
        self.item_consumer = ItemConsumer(self.chain_key, self.rpc)
        self.item_gold_trader_v2 = ItemGoldTraderV2(self.chain_key, self.rpc)
        self.jewel_token = JewelToken(self.chain_key, self.rpc)
        self.land_auction = LandAuction(self.chain_key, self.rpc)
        self.land_core = LandCore(self.chain_key, self.rpc)
        self.master_gardener = MasterGardener(self.chain_key, self.rpc)
        self.meditation_circle = MeditationCircle(self.chain_key, self.rpc)
        self.pasture = Pasture(self.chain_key, self.rpc)
        self.pet_auction = PetAuction(self.chain_key, self.rpc)
        self.pet_core = PetCore(self.chain_key, self.rpc)
        self.pet_exchange = PetExchange(self.chain_key, self.rpc)
        self.pet_hatching = PetHatching(self.chain_key, self.rpc)
        self.profiles = Profiles(self.chain_key, self.rpc)
        self.quest_core = QuestCore(self.chain_key, self.rpc)
        self.raffle_master = RaffleMaster(self.chain_key, self.rpc)
        self.raffle_ticket = RaffleTicket(self.chain_key, self.rpc)
        self.stone_carver = StoneCarver(self.chain_key, self.rpc)
        self.stylist = Stylist(self.chain_key, self.rpc)
        self.token_disburse = TokenDisburse(self.chain_key, self.rpc)
        self.uniswap_v2_factory = UniswapV2Factory(self.chain_key, self.rpc)
        self.uniswap_v2_router02 = UniswapV2Router02(self.chain_key, self.rpc)
        self.validator_fund = ValidatorFund(self.chain_key, self.rpc)

