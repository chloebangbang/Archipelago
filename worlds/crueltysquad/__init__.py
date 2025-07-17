# generally templated off the inscryption world
from .Options import CrueltySquadOptions
from .Locations import all_locations
from .Items import all_items, base_id
from BaseClasses import Region, Item, Tutorial, ItemClassification
from worlds.AutoWorld import World, WebWorld


class CrueltySquadWeb(WebWorld):
    theme = "dirt"

    guide_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Cruelty Squad Archipelago",
        "English",
        "setup_en.md",
        "setup/en",
        ["chloe!!"]
    )

    tutorials = [guide_en]

class CrueltySquadWorld(World):
    # TODO: Write a docstring
    
    game = "Cruelty Squad"
    web = CrueltySquadWeb()
    options_dataclass = CrueltySquadOptions
    options: CrueltySquadOptions
    all_items = all_items
    item_name_to_id = { item["name"]: i + base_id for i, item in enumerate(all_items) }
    all_locations = all_locations
    location_name_to_id = { item["name"]: i + base_id for i, item in enumerate(all_locations) }
