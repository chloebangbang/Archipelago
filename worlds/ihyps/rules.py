from typing import Dict, Callable, TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.AutoWorld import World
from worlds.generic.Rules import add_rule, set_rule

def set_all_rules(world) -> None:
    if not world.options.no_logic:
        rules = IHYPSRules(world)
        rules.set_all_entrance_rules()
        rules.set_all_location_rules()

# based on inscryption's implementation
# which itself says its based on the messenger's implementation
class IHYPSRules:
    player: int
    world: World
    def __init__(self, world) -> None:
        self.player = world.player
        self.world = world

    # I hadn't figured out the design pattern of having a dict with callables yet
    # but I'm not going to rewrite it now.
    def set_all_entrance_rules(self) -> None:
        to_bar = self.world.get_entrance("To Bar")
        to_forest = self.world.get_entrance("To Forest")
        to_wasp = self.world.get_entrance("To West Forest")
        to_tower = self.world.get_entrance("To Tower")
        to_stratum_one = self.world.get_entrance("To Stratum 1")
        to_stratum_two = self.world.get_entrance("To Stratum 2")
        to_stratum_three = self.world.get_entrance("To Stratum 3")
        to_top_floor = self.world.get_entrance("To Tower Top Floor")
        stratum_three_warp = self.world.get_entrance("Stratum 3 Warp")
        top_floor_warp = self.world.get_entrance("Tower Top Floor Warp")
        begin_hearts_quest = self.world.get_entrance("Begin Hearts Quest")
        to_downtown = self.world.get_entrance("To Downtown")
        to_warehouse = self.world.get_entrance("To Warehouse")
        to_harbor = self.world.get_entrance("To Harbor")
        to_beach = self.world.get_entrance("To Beach")

        set_rule(to_bar, lambda state: state.has("Bar", self.player))
        if self.world.options.skillsanity:
            set_rule(to_forest, lambda state: state.has("Forest", self.player) and (self.can_do_combat(state) or (state.has("Bribery", self.player) and self.can_get_money(state))))
            set_rule(to_top_floor, lambda state: state.has_all_counts({"Final Boss Key": 4, "Progressive Dungeon Stone": 2}, self.player) and (self.has_full_party(state) or state.has_all(("Devon", "Business Talk", "All Business", "True Silence"), self.player)))
            set_rule(top_floor_warp, lambda state: state.has_all_counts({"Progressive Dungeon Stone": 3, "Final Boss Key": 4}, self.player) and ((state.has_all(("Devon", "Business Talk", "All Business", "True Silence"), self.player) and self.count_party_members(state) >= 3) or self.has_full_party(state)))
        else:
            set_rule(to_forest, lambda state: state.has("Forest", self.player) and (self.can_do_combat(state) or self.can_get_money(state)))
            set_rule(to_top_floor, lambda state: self.has_devon(state) and state.has_all_counts({"Final Boss Key": 4, "Progressive Dungeon Stone": 2}, self.player))
            # this is maybe a little lenient, but you can cheese the everloving shit out of melchom with silence + all business business talk
            set_rule(top_floor_warp, lambda state: self.has_devon(state) and state.has_all_counts({"Progressive Dungeon Stone": 3, "Final Boss Key": 4}, self.player) and self.count_party_members(state) >= 3)
        set_rule(to_tower, lambda state: state.has("Tower", self.player))
        set_rule(to_downtown, lambda state: state.has("Downtown", self.player))
        set_rule(to_harbor, lambda state: state.has("Harbor", self.player))

        set_rule(to_wasp, lambda state: state.has("Devon", self.player))
        set_rule(to_stratum_one, lambda state: state.has("Progressive AL Rank", self.player) and self.can_lockpick(state))   
        set_rule(to_stratum_two, lambda state: state.has("Kyrie", self.player))
        set_rule(to_stratum_three, lambda state: state.has_all(("Jasper", "Progressive Dungeon Stone"), self.player))
        set_rule(stratum_three_warp, lambda state: self.has_jasper(state) and state.count("Progressive Dungeon Stone", self.player) >= 2)
        set_rule(begin_hearts_quest, lambda state: state.has_all(("Bar", "Devon", "Kyrie", "Jasper"), self.player) and self.get_rank(state) >= 3) 
        set_rule(to_warehouse, lambda state: self.can_lockpick(state) and (state.can_reach_location("Hornet Queen", self.player) or state.can_reach_location("Casino Investigation", self.player)))
        set_rule(to_beach, lambda state: state.has_any(("Devon", "Kyrie", "Jasper"), self.player))

    def set_all_location_rules(self) -> None:
        # abusing can_reach_entrance and can_reach_location so much probably sucks performance wise
        # but we can worry about that when a second person uses this apworld
        # until then its just my own cpu time I'm wasting
        # later these can become event locations but I truly cannot be bothered rn
        location_rules: Dict[str, Callable[[CollectionState], bool]] = {
            # apt
            "Devon: Devon Comes Over": self.has_devon,
            "Kyrie: Kyrie Comes Over": self.has_kyrie,
            "Jasper: Jasper Comes Over": self.has_jasper,
            "Craft Burner Phone": lambda state: state.can_reach_entrance("To Beach", self.player) and state.has_all(("Lion's Den Password", "Devon"), self.player),
            "Mack 1": lambda state: (state.has("Forest", self.player) or state.can_reach_region("Warehouse", self.player)) and self.count_party_members(state) > 2,
            "Mack 2": lambda state: (state.has("Forest", self.player) or state.can_reach_region("Warehouse", self.player)) and self.count_party_members(state) > 2,
            "The Butcher": lambda state: state.has_all(("Tower", "Meat Cleaver"), self.player) and self.count_party_members(state) >= 2,
            "Apartment Sewers": self.can_lockpick,
            # after much deliberation making these sphere 1
            # you can run from most of the encounters 100% of the time
            # and the only ones you have to worry about are the double slimes.
            # which with the full heal and save of sleeping should be literally fine.
            # I've never once lost an appreciable amount of health to getting this without combat
            # "Sewer Encounter 1": lambda state: self.can_do_combat(state) or self.can_get_money(state),
            # "Sewer Encounter 2": lambda state: self.can_do_combat(state) or self.can_get_money(state),
            "Exterminator": self.can_do_combat,
            "Apartment Musician": lambda state: self.can_get_money(state) and state.has("Downtown", self.player),
            "Snacks: Devon Edition": self.has_devon,
            "Snacks: Kyrie Edition": self.has_kyrie,
            "Snacks: Jasper Edition": self.has_jasper,
            "Hartford Devil": lambda state: state.can_reach_location("Storm the Manor", self.player) and state.can_reach_location("Necromancy Investigation", self.player) and state.can_reach_location("Lonely Hearts Quest", self.player) and state.can_reach_region("Beach", self.player) and self.has_full_party(state),
            "Trading Cards 1": lambda state: state.has("Baseball Cards", self.player),
            "Trading Cards 2": lambda state: state.has("Baseball Cards", self.player),
            "Trading Cards 3": lambda state: state.has("Baseball Cards", self.player),
            "Legendary Raccoon": lambda state: state.has_any(("Downtown", "Harbor"), self.player) and self.count_party_members(state) > 2,
            "Photograph": lambda state: state.has_all(("Envelope", "Jasper"), self.player),
            "Death Pugilist": lambda state: state.can_reach_location("Melchom 1", self.player),
            "Stinger Trade": lambda state: (state.has("Forest", self.player) or state.can_reach_region("Warehouse", self.player)) and self.can_do_combat(state),

            "Level 2": self.can_do_combat,
            "Level 3": self.can_do_combat,
            "Level 4": self.can_do_combat,
            "Level 5": self.can_do_combat,
            "Level 6": self.can_do_combat,
            "Level 7": self.can_do_combat,
            "Level 8": self.can_do_combat,
            "Level 9": self.can_do_combat,
            "Level 10": self.can_do_combat,
            "Level 11": self.can_do_combat,

            # bar locations
            "Bar Vinyl": lambda state: self.can_get_money(state) and state.has("Progressive AL Rank", self.player),
            "Kyrie: Pills": self.has_kyrie,
            "Jasper: Guns and Bullets": self.has_jasper,
            "Sandy Gift": lambda state: state.can_reach_location("Casino Investigation", self.player) and self.can_get_money(state),
            "Seki Gift": lambda state: state.has("Progressive AL Rank", self.player),
            "Wallace Gift": lambda state: self.has_devon(state) and state.has("Progressive AL Rank", self.player),
            "Scaled Bass Buyer": lambda state: state.has_all(("Harbor", "Kyrie"), self.player),
            "Lee Gift": lambda state: state.can_reach_location("Sandy Gift", self.player),
            "Cyril Gift": lambda state: state.can_reach_location("Sandy Gift", self.player),
            "Kyrie: The Clinic": self.has_kyrie,
            "Back of the Clinic": self.has_devon,
            "Devon: The Siren": lambda state: self.has_devon(state) and state.can_reach_location("Necromancy Investigation", self.player),
            "Graveyard Chest": lambda state: state.has("Lockpicking Guide", self.player) and self.can_do_combat(state),
            "Jasper: In Memoriam": self.has_jasper,
            "Marshall Gift": lambda state: state.can_reach_location("Lonely Hearts Quest", self.player),
            "Mourner Gift": lambda state: state.can_reach_region("Beach", self.player),
            "Emily": lambda state: state.can_reach_location("Mack 1", self.player) and state.can_reach_location("Bubos 1", self.player) and state.can_reach_location("Myre 1", self.player) and state.can_reach_location("Stewart 1", self.player),
            "Construction Equipment": lambda state: state.can_reach_location("Necromancy Investigation", self.player),
            # quests
            "Group Infighting": lambda state: state.has_all(("Progressive AL Rank", "Forest"), self.player) and self.can_do_combat(state),
            "Hornet Queen": lambda state: state.has_all(("Forest", "Devon", "Progressive AL Rank"), self.player),
            "Monster Trafficker": lambda state: state.has_all(("Lockpicking Guide", "Progressive AL Rank"), self.player) and self.can_do_combat(state),
            "Storm the Manor": lambda state: self.get_rank(state) >= 2 and self.count_party_members(state) >= 3 and state.has("Forest", self.player),
            "Necromancy Investigation": lambda state: self.get_rank(state) >= 2 and self.count_party_members(state) >= 3 and self.has_kyrie(state),
            "Haunted Arcade Cabinet": lambda state: self.get_rank(state) >= 2 and self.count_party_members(state) >= 3 and state.has_all(("Arcade Token", "Harbor"), self.player),
            "Casino Investigation": lambda state: self.get_rank(state) >= 3 and self.count_party_members(state) == 4 and state.has_all(("Downtown", "Harbor"), self.player),
            "Lighthouse Reclamation": lambda state: self.get_rank(state) >= 3 and state.can_reach_region("Beach", self.player) and (state.has_all(("Forest", "Lion's Den Password"), self.player) or state.has("Tower", self.player)) and (self.has_full_party(state) or (state.has_all(("Forest", "Devon", "Lockpicking Guide"), self.player))),
            "Lonely Hearts Quest": lambda state: state.can_reach_region("Hearts Tower", self.player),
            "Stanley Gift": lambda state: state.can_reach_location("Lighthouse Reclamation", self.player),
            "Devon: Learning About Artifacts": lambda state: state.has("Devon", self.player) and state.can_reach_location("Group Infighting", self.player),
            "Jenny Gift": lambda state: state.can_reach_location("Sandy Gift", self.player),
            
            # forest
            "Deeds Trade": lambda state: state.has("Lighthouse Deeds", self.player),
            "Trash Trade": lambda state: state.has("Progressive AL Rank", self.player),
            "Jasper: Leadership": lambda state: state.has("Jasper", self.player),
            "East Forest Chest": self.can_lockpick,
            "Forest Tourist": lambda state: state.has_all(("Downtown", "Devon", "Jasper"), self.player),
            # todo: add conditions for when it would be in logic without buying souls
            # maybe for percentage of checks/items collected? would be hacky but
            "Trish 1": lambda state: state.can_reach_region("Beach", self.player) and self.can_get_money(state),
            "Trish 2": lambda state: state.has_all(("Devon", "Harbor"), self.player) and self.can_get_money(state),
            "Trish 3": lambda state: state.has_all(("Harbor", "Kyrie"), self.player) and self.can_get_money(state),
            "Trish 4": lambda state: state.can_reach_region("Beach", self.player) and self.can_get_money(state),
            "Trish 5": lambda state: state.has_all(("Jasper", "Harbor"), self.player) and self.can_get_money(state),
            "Trish 6": lambda state: state.has_all(("Harbor", "Devon", "Kyrie", "Jasper"), self.player) and self.can_get_money(state),
            "Illusory Knife": lambda state: state.has_all_counts({"Half a Photo": 2}, self.player) and state.can_reach_region("Beach", self.player) and self.can_get_money(state),
            "Illusory Driftwood": lambda state: state.has_all(("Devon", "Harbor", "Sewer Key"), self.player) and self.can_get_money(state),
            "Abernathy": lambda state: state.has_all(("Devon", "Kyrie", "Jasper", "Harbor"), self.player) and self.can_get_money(state),
            "Kyrie: Questioning": self.has_kyrie,
            "Kyrie: A Brief Media Chat": self.has_kyrie,
            "Mansion Basement Chest": lambda state: self.can_lockpick(state) and state.can_reach_location("Storm the Manor", self.player),
            "Devon: The Ethics of Robbery": self.has_devon,
            "Mansion Dining Room Chest": self.can_lockpick,
            "Mansion Rec Room Chest": self.can_lockpick,
            "Forest Musician": lambda state: state.has("Downtown", self.player) and self.can_get_money(state),
            "West Forest Fishing Chest 1": self.can_lockpick,
            "West Forest Fishing Chest 2": self.can_lockpick,
            "West Forest Fishing Chest 3": self.can_lockpick,
            "Hell Deer": lambda state: state.has("Bar", self.player),
            "West Forest Crime Chest": self.can_lockpick,
            "Hornet Chest": self.can_lockpick,
            "Devon: Grave": self.can_lockpick,
            "Bonus Boss": lambda state: state.has("Sealed Envelope", self.player) and state.can_reach_location("Melchom 1", self.player),
            "Gramophone": lambda state: state.has("Fuzzy Trip in Remix Land", self.player),

            # tower
            "Return Phone": lambda state: state.has("Lost Cell Phone", self.player),
            "Getting to Know Devon": self.has_devon,
            "Kyrie: Not My Fault": self.has_kyrie,
            "Minor Scale Trade": lambda state: self.can_do_combat(state) and (state.has_any(("Forest", "Bar"), self.player) or state.can_reach_region("Beach", self.player)),
            "Dungeon Food Stall": self.can_lockpick,
            "Dungeon Sewers Chest": lambda state: self.can_lockpick(state) and self.can_do_combat(state),
            "Devon: Sewer Slimes": lambda state: self.can_do_combat(state) and self.has_devon(state),
            "Chef Gift": lambda state: state.can_reach_location("The Butcher", self.player),
            "Sewer Fishing": lambda state: state.has("Bar", self.player) and self.can_do_combat(state),
            "Jasper: True Crime Speculation": self.has_jasper,

            # strata one
            "Devon: Grand Dungeons": self.has_devon,
            "Trish Tower Room 1": self.can_do_combat,
            "Trish Tower Room 2": self.can_do_combat,
            "Stratum 2 Reception Chest": self.can_do_combat,
            "Devon: Rest Stop": self.has_devon,
            "Reach Stratum 2": self.can_do_combat,

            # strata 2
            "Caligostro Floor Chest": lambda state: self.count_party_members(state) == 4,
            "Wire Trade": lambda state: state.can_reach_location("Storm the Manor", self.player),
            "Tower Four Graves 1": lambda state: state.can_reach_location("The Butcher", self.player) and state.has("Downtown", self.player),
            "Tower Four Graves 2": lambda state: state.can_reach_location("The Butcher", self.player) and state.has("Downtown", self.player),
            "Tower House 1": lambda state: state.can_reach_location("Clarence 1", self.player) and state.has_all(("Downtown", "Bar"), self.player),
            "Tower House 2": lambda state: state.can_reach_location("Tower House 1", self.player),
            "Stratum 3 Reception": lambda state: state.can_reach_location("Lonely Hearts Quest", self.player) and state.has_all(("Downtown", "Homemade Chocolates"), self.player),
            "Supervisor Fight": lambda state: state.can_reach_location("Necromancy Investigation", self.player) and state.has_all(("Forest", "Harbor"), self.player),
            "Clarence 1": lambda state: state.has_all(("Jasper", "Forest", "Bar"), self.player),
            "Clarence 2": lambda state: state.has_all(("Jasper", "Forest", "Bar"), self.player),

            # strata 3
            "Tower Musician 1": lambda state: state.has_all(("Bar", "Downtown", "Forest"), self.player),
            "Tower Musician 2": lambda state: state.can_reach_location("Tower Musician 1", self.player),
            "Ramona's Certificate": self.has_full_party,
            "Devon's Certificate": self.has_full_party,
            "Kyrie's Certificate": self.has_full_party,
            "Jasper's Certificate": lambda state: state.can_reach_location("Lonely Hearts Quest", self.player), 

            # hearts
            "Rare Game Trade": lambda state: state.has("Rare Game", self.player),
            "Hearts Record": lambda state: state.has("Fuzzy Trip in Remix Land", self.player),
            "Hearts Apology": lambda state: state.has("Fuzzy Trip in Remix Land", self.player),

            # downtown
            "Jasper: Suit Loving": self.has_jasper,
            "Kyrie: Staying Combat Ready": self.has_kyrie,
            "Grotesque Flower Trade": lambda state: state.can_reach_region("Tower Stratum 2", self.player) or (state.has("Forest", self.player) and self.can_do_combat(state)),
            "Downtown Musician": self.can_get_money,
            "Lightkill": lambda state: state.has_all(("Devon", "Kyrie", "Jasper", "Lightkill's Gun"), self.player),
            "Devon: A Frank Talk": self.has_devon,
            "Restroom Killer": lambda state: self.has_devon(state) and state.can_reach_region("Warehouse", self.player) and self.count_party_members(state) >= 3,
            # definitely being conservative with the logic for the arena compared to my other logic
            # but! I also hate the arena. so its fine.
            "Arena Tier 1": lambda state: self.count_party_members(state) >= 3,
            "Arena Tier 2": lambda state: self.has_full_party(state) and self.get_rank(state) >= 2,
            "Arena Tier 3": lambda state: self.has_full_party(state) and self.get_rank(state) >= 3,
            "Hannah's Office": lambda state: state.can_reach_location("Casino Investigation", self.player),
            "Casino Punishment": lambda state: self.can_lockpick(state) and self.can_get_money(state),
            "Patrick": lambda state: self.has_kyrie(state) and state.has_any(("Devon", "Jasper"), self.player),
            "Kyrie: Faunshalt Family": self.has_kyrie,                       
            "Downtown Sewers Chest": lambda state: self.can_lockpick(state) and self.can_do_combat(state),
            "Bubos 1": lambda state: state.has("Victim's Bag", self.player) and self.count_party_members(state) >= 3,
            "Bubos 2": lambda state: state.can_reach_location("Bubos 1", self.player),
            "Mimic": lambda state: state.has("Kyrie", self.player) and self.count_party_members(state) >= 3 and ((state.has("Bar", self.player) and state.has_any(("Progressive AL Rank", "Devon"), self.player)) or state.has("Tower", self.player) or (state.has("Harbor", self.player) and (self.has_jasper(state) or state.can_reach_location("Haunted Arcade Cabinet", self.player)))),
            "Kyrie: Loans": self.has_kyrie,
            "Devon: Albing Vending": self.has_devon,
            "Kyrie: Esteemed Town Hall": self.has_kyrie,
            "Kyrie: Visitation": self.has_kyrie,
            "Kyrie: Visitation": self.has_kyrie,
            "Mimic Visit": lambda state: state.can_reach_location("Mimic", self.player),
            "Wallace Visit": lambda state: state.can_reach_location("Lonely Hearts Quest", self.player),
            "Patrick's Drink": lambda state: state.has_all(("Kyrie", "Emily's Gasmask"), self.player),
            "Hannah": lambda state: self.count_party_members(state) >= 3,
            "Restroom Killer's Stash": lambda state: state.can_reach_location("Restroom Killer", self.player),
            
            # warehouse
            "Devon: Past Jobs": self.has_devon,
            "Kyrie: Stances": self.has_kyrie,
            "Kyrie Warehouse 1": lambda state: state.can_reach_location("Hornet Queen", self.player),
            "Kyrie Warehouse 2": lambda state: state.can_reach_location("Hornet Queen", self.player),
            "Kyrie Warehouse 3": lambda state: state.can_reach_location("Hornet Queen", self.player),
            "Kyrie Warehouse 4": lambda state: state.can_reach_location("Hornet Queen", self.player),
            "Back of Warehouse Single Chest 1": lambda state: state.can_reach_location("Casino Investigation", self.player),
            "Back of Warehouse Single Chest 2": lambda state: state.can_reach_location("Casino Investigation", self.player),
            "Back of Warehouse Double Chest 1": lambda state: state.can_reach_location("Casino Investigation", self.player),
            "Back of Warehouse Double Chest 2": lambda state: state.can_reach_location("Casino Investigation", self.player),

            # harbor
            "Kyrie: Fashion": self.has_kyrie,
            "Devon: Fishing": self.has_devon,
            "Docks Lupine": self.has_jasper,
            "Arcade Boss": lambda state: state.can_reach_location("Haunted Arcade Cabinet", self.player), 
            "Rainy Day Fund": lambda state: state.has("Downtown", self.player) and self.can_lockpick(state),
            
            # beach
            "Buried Cards": lambda state: state.has("Downtown", self.player) and state.can_reach_location("Hartford Devil", self.player),
            "Jasper: Beach Thoughts": self.has_jasper,
            "Rogue Seagull": lambda state: state.has("Bar", self.player) and self.count_party_members(state) >= 3,
            "Stewart 1": lambda state: state.has_all(("Devon", "Kyrie", "Jasper", "Wrench", "Tower", "Bar"), self.player),
            "Stewart 2": lambda state: state.has_all(("Devon", "Kyrie", "Jasper", "Wrench", "Tower", "Bar"), self.player),
            "Restaurant Owner": lambda state: state.can_reach_location("Rogue Seagull", self.player),
            "Devon: Empty": self.has_devon,
            "Myre 1": lambda state: state.has_all(("Devon", "Kyrie", "Jasper", "Tower", "Downtown"), self.player),
            "Myre 2": lambda state: state.has_all(("Devon", "Kyrie", "Jasper", "Tower", "Downtown"), self.player),
            "Lighthouse Chest 1": self.can_lockpick,
            "Lighthouse Chest 2": self.can_lockpick,
            "Abyssal": lambda state: state.can_reach_location("Lighthouse Reclamation", self.player),
            "Raccoon King": lambda state: state.can_reach_location("Lighthouse Reclamation", self.player),
            "Raccoon King Return": lambda state: state.can_reach_location("Lighthouse Reclamation", self.player),
            "Raccoon King Assassin": lambda state: state.can_reach_location("Lighthouse Reclamation", self.player) and state.can_reach_location("Legendary Raccoon", self.player),
            "Jasper: Beautiful Day": self.has_jasper,
            "Devon: Cursed": self.has_devon,
            "Black Market Crafter": lambda state: state.has_all(("Lion's Den Password", "Strange Driftwood"), self.player), 
            "Fired Company Man": lambda state: (state.can_reach_region("Tower Stratum 1", self.player) and self.has_devon(state)) or self.has_full_party(state),
            "Black Market Lost and Found": lambda state: state.has("Lion's Den Password", self.player),
        }

        multiworld = self.world.multiworld
        # TODO: implement other endings
        multiworld.completion_condition[self.player] = lambda state: state.can_reach_location("Bonus Boss", self.player) and state.can_reach_location("Melchom 1", self.player)
        for region in multiworld.get_regions(self.player):
            for loc in region.locations:
                if loc.name in location_rules:
                    loc.access_rule = location_rules[loc.name]

    def can_lockpick(self, state: CollectionState) -> bool:
        return state.has_all(("Lockpicking Guide", "Bar"), self.player) and self.can_get_money(state)
    
    def can_do_combat(self, state: CollectionState) -> bool:
        return state.has_any(("Devon", "Kyrie", "Jasper", "Working for the Knife", "Kitchen Knife", "Meat Cleaver", "Magic Knife"), self.player)

    def can_get_money(self, state: CollectionState) -> bool:
        return (state.has("Bar", self.player) and (self.can_do_combat(state) or state.has_any(("Harbor, Tower"), self.player))) or (state.has("Progressive AL Rank", self.player) and self.can_do_combat(state))

    def count_party_members(self, state: CollectionState) -> int:
        return state.count_from_list(("Devon", "Kyrie", "Jasper"), self.player) + 1

    def get_rank(self, state: CollectionState) -> int:
        return state.count("Progressive AL Rank", self.player)
    
    def has_devon(self, state: CollectionState) -> bool:
        return state.has("Devon", self.player)

    def has_kyrie(self, state: CollectionState) -> bool:
        return state.has("Kyrie", self.player)

    def has_jasper(self, state: CollectionState) -> bool:
        return state.has("Jasper", self.player)
    
    def has_full_party(self, state: CollectionState) -> bool:
        return state.has_all(("Devon", "Kyrie", "Jasper"), self.player)