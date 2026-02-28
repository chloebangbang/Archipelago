from collections.abc import Mapping

from BaseClasses import Tutorial
from worlds.AutoWorld import World, WebWorld

from . import items, locations, regions, rules
from . import options as ihyps_options

class IHYPSWebWorld(WebWorld):
    game = "I Hate You, Please Suffer"
    theme = "stone"
    setup_en = Tutorial(
        "Setup Guide",
        "A guide for setting up I Hate You, Please Suffer for Archipelago",
        "English",
        "setup_en.md",
        "setup/en",
        ["chloe!!"],
    )
    tutorials = [setup_en]

class IHYPSWorld(World):
    """
    I Hate You, Please Suffer is a heart-filled RPG about paying your rent in a hostile world.
    """
    game = "I Hate You, Please Suffer"
    web = IHYPSWebWorld()
    options_dataclass = ihyps_options.IHYPSOptions
    options: ihyps_options.IHYPSOptions
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID
    origin_region_name = "Apartment"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)
    
    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)
    
    def create_item(self, name: str) -> items.IHYPSItem:
        return items.create_item(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, any]:
        return self.options.as_dict(
            "trap_chance", "skillsanity"
        )