from typing import TYPE_CHECKING

from BaseClasses import Location

apartment_locations = {
    "Devon: Devon Comes Over": 1,
    "Kyrie: Kyrie Comes Over": 2,
    "Jasper: Jasper Comes Over": 3,
    "Craft Burner Phone": 4,
    "Mack 1": 5,
    "Mack 2": 6,
    "The Butcher": 7,
    "Apartment Sewers": 8,
    "Sewer Encounter 1": 9,
    "Sewer Encounter 2": 10,
    "Exterminator": 11,
    "Apartment Musician": 12,
    "Snacks: Devon Edition": 13,
    "Snacks: Kyrie Edition": 14,
    "Snacks: Jasper Edition": 15,
    "Hartford Devil": 16,
    "Trading Cards 1": 17,
    "Trading Cards 2": 18,
    "Trading Cards 3": 19,
    "Legendary Raccoon": 20,
    "Photograph": 21,
    "Death Pugilist": 22,
    "Ramona's Kitchen": 23,
    "Stinger Trade": 24,
}

levelup_locations = {
    "Level 2": 50,
    "Level 3": 51,
    "Level 4": 52,
    "Level 5": 53,
    "Level 6": 54,
    "Level 7": 55,
    "Level 8": 56,
    "Level 9": 57,
    "Level 10": 58,
    "Level 11": 59,
}

bar_locations = {
    "Bar Vinyl": 100,
    # kyrie chat
    "Kyrie: Pills": 101,
    # jasper chat
    "Jasper: Guns and Bullets": 102,
    "Purchase Lockpicking Guide": 103,
    "Sandy Gift": 104,
    "Seki Gift": 105,
    "Wallace Gift": 106,
    "Scaled Bass Buyer": 107,
    "Lee Gift": 108,
    "Cyril Gift": 109,
    "Back of the Clinic": 110,
    # kyrie chat
    "Kyrie: The Clinic": 111,
    # devon chat
    "Devon: The Siren": 112,
    "Graveyard Chest": 113,
    # jasper chat
    "Jasper: In Memoriam": 114,
    "Marshall Gift": 115,
    "Mourner Gift": 116,
    "Emily": 117,
    "Construction Equipment": 118,

    # QUEST TURN INS
    "Group Infighting": 119,
    "Hornet Queen": 120,
    "Monster Trafficker": 121,
    "Storm the Manor": 122,
    "Necromancy Investigation": 123,
    "Haunted Arcade Cabinet": 124,
    "Casino Investigation": 125,
    "Lighthouse Reclamation": 126,
    "Lonely Hearts Quest": 127,

    "Stanley Gift": 128,
    "Devon: Learning About Artifacts": 129,
    "Jenny Gift": 130,
}

forest_locations = {
    "Deeds Trade": 200,
    "Jasper: Leadership": 201,
    "East Forest Chest": 202,
    "Forest Tourist": 203,
    # shrine
    "Trish License": 204,
    "Trish 1": 205,
    "Trish 2": 206,
    "Trish 3": 207,
    "Trish 4": 208,
    "Trish 5": 209,
    "Trish 6": 210,
    "Illusory Knife": 211,
    "Illusory Driftwood": 212,
    "Abernathy": 213,
    "Kyrie: Questioning": 224,
    "Kyrie: A Brief Media Chat": 225,
    "Mansion Basement Chest": 226,
    "Devon: The Ethics of Robbery": 227,
    "Mansion Dining Room Chest": 228,
    "Mansion Rec Room Chest": 229,

    "Forest Musician": 230,
    "Trash Trade": 231,
    "Gramophone": 232,
}

wasp_locations = {
    "Tent 1": 214,
    "Tent 2": 215,
    "West Forest Fishing Chest 1": 216,
    "West Forest Fishing Chest 2": 217,
    "West Forest Fishing Chest 3": 218,
    "Hell Deer": 219,
    "West Forest Crime Chest": 220,
    "Hornet Chest": 221,
    "Devon: Detour With Devon": 222,
    "Devon: Grave": 223,
    "Bonus Boss": 250,
}

tower_base_locations = {
    "Return Phone": 300,
    "Getting to Know Devon": 301, 
    "Kyrie: Not My Fault": 302,
    "Minor Scale Trade": 303,
    "Dungeon Food Stall": 304,
    "Dungeon Sewers Chest": 305,
    "Devon: Sewer Slimes": 306,
    "Chef Gift": 307,
    "Sewer Fishing": 308,
    "Jasper: True Crime Speculation": 309,
}

strata_one_locations = {
    "Devon: Grand Dungeons": 400,
    "Sheya Gift": 401,

    "Trish Tower Room 1": 405,
    "Trish Tower Room 2": 406,
    "Stratum 2 Reception Chest": 407,
    "Devon: Rest Stop": 408,
    "Reach Stratum 2": 450, 
}

hearts_tower_locations = {
    "Solace Gift 1": 402,
    "Solace Gift 2": 403,
    "Solace Gift 3": 404,
    "Hearts Dorm 1": 410,
    "Hearts Dorm 2": 411,
    "Hearts Dorm Puzzle": 412,
    "Hearts Quiz": 413,
    "Hearts Record": 414,
    "Hearts Apology": 415,
    "Left Hearts Lieutenant": 416,
    "Left Hearts Lt. Chest": 417,
    "Hearts Slime": 418,
    "Health Stash 1": 419,
    "Health Stash 2": 420,
    "Hearts Garden": 421,
    "Rare Game Trade": 422,
}

strata_two_locations = {
    # moved for performance reasons more than organizational ones
    "Kyrie: Dating Life": 409,
    "Caligostro Floor Tools": 500,
    "Caligostro Floor Chest": 501,
    "Wire Trade": 502,
    "Tower Four Graves 1": 503,
    "Tower Four Graves 2": 504,
    "Tower House 1": 505,
    "Tower House 2": 506,
    "Stratum 3 Reception": 507,
    "Supervisor Fight": 508,
    "Clarence 1": 509,
    "Clarence 2": 510,
    "Reach Stratum 3": 511,
}

strata_three_locations = {
    "Jasper: Return": 600,
    "Tower Musician 1": 601,
    "Tower Musician 2": 602,
    "Survey Reward": 603,
    "Ramona's Certificate": 604,
    "Devon's Certificate": 605,
    "Kyrie's Certificate": 606,
    "Jasper's Certificate": 607,
    "Gaming Memorabilia": 608,
    "Reach Top Floor": 613,
}

top_floor_locations = {
    "Melchom 1": 609,
    "Melchom 2": 610,
    "Melchom 3": 611,
    "Melchom 4": 612,
}

downtown_locations = {
    "Jasper: Suit Loving": 700,
    "Kyrie: Staying Combat Ready": 701,
    "Grotesque Flower Trade": 702,
    "Downtown Musician": 703,
    "Lightkill": 704,
    "Devon: A Frank Talk": 705,
    "Restroom Killer": 706,
    "Arena Tier 1": 707,
    "Arena Tier 2": 708,
    "Arena Tier 3": 709,
    "Hannah's Office": 710,
    # "Quinnith's Office": 711,
    "Casino Punishment": 712,
    "Patrick": 731,
    "Kyrie: Faunshalt Family": 732,
    "Downtown Sewers Chest": 733,
    "Bubos 1": 734,
    "Bubos 2": 735,
    "Mimic": 736,
    "Kyrie: Loans": 737,
    "Devon: Albing Vending": 738,
    "Kyrie: Esteemed Town Hall": 739,
    "Kyrie: Visitation": 740,
    "Mimic Visit": 741,
    "Wallace Visit": 742,
    "Patrick's Drink": 743,
    "Hannah": 744,
    "Restroom Killer's Stash": 745,
}

warehouse_locations = {
    "Devon: Past Jobs": 713,
    "Warehouse Sorting Chest": 714,
    "Warehouse Vending Machine 1": 715,
    "Warehouse Vending Machine 2": 716,
    "Kyrie: Stances": 717,
    "Warehouse Manager Chest": 718,
    "Kyrie Warehouse 1": 719,
    "Kyrie Warehouse 2": 720,
    "Kyrie Warehouse 3": 721,
    "Kyrie Warehouse 4": 722,
    "Back of Warehouse Single Chest 1": 723,
    "Back of Warehouse Double Chest 1": 724,
    "Back of Warehouse Double Chest 2": 725,
    "Back of Warehouse Single Chest 2": 726,
    "Warehouse Receiving 1": 727,
    "Warehouse Receiving 2": 728,
    "Warehouse Receiving 3": 729,
    "Warehouse Receiving 4": 730,
}

harbor_locations = {
    "Kyrie: Fashion": 800,
    "Devon: Fishing": 801,
    "Docks Lupine": 802,
    "Arcade Boss": 803,
    "Harbor Suitcase 1": 850,
    "Harbor Suitcase 2": 851,
    "Rainy Day Fund": 852,
}

beach_locations = {
    "Buried Cards": 804,
    "Jasper: Beach Thoughts": 805,
    "Rogue Seagull": 806,
    "Stewart 1": 807,
    "Stewart 2": 808,
    "Restaurant Owner": 809,
    "Devon: Empty": 810,
    "Myre 1": 811,
    "Myre 2": 812,
    "Lighthouse Chest 1": 813,
    "Lighthouse Chest 2": 814,
    "Abyssal": 815,
    "Raccoon King": 816, 
    "Raccoon King Return": 817,
    "Raccoon King Assassin": 818,
    "Jasper: Beautiful Day": 819,
    "Devon: Cursed": 820,
    "Black Market Crafter": 821,
    "Fired Company Man": 822,
    "Black Market Lost and Found": 823,
}

LOCATION_NAME_TO_ID = apartment_locations | bar_locations | forest_locations | \
    tower_base_locations | strata_one_locations | strata_two_locations | \
    strata_three_locations | downtown_locations | harbor_locations | \
    warehouse_locations | beach_locations | hearts_tower_locations | \
    wasp_locations | top_floor_locations | levelup_locations

class IHYPSLocation(Location):
    game = "I Hate You, Please Suffer"

def create_all_locations(world):
    create_regular_locations(world)

def create_regular_locations(world):
    apartment = world.get_region("Apartment")
    bar = world.get_region("Bar")
    forest = world.get_region("Forest")
    wasp_country = world.get_region("West Forest")
    tower_base = world.get_region("Tower")
    strata_one = world.get_region("Tower Stratum 1")
    strata_two = world.get_region("Tower Stratum 2")
    strata_three = world.get_region("Tower Stratum 3")
    top_floor = world.get_region("Tower Top Floor")
    hearts_tower = world.get_region("Hearts Tower")
    downtown = world.get_region("Downtown")
    warehouse = world.get_region("Warehouse")
    harbor = world.get_region("Harbor")
    beach = world.get_region("Beach")

    if world.options.skillsanity:
        apartment.add_locations(apartment_locations | levelup_locations, IHYPSLocation)
    else:
        apartment.add_locations(apartment_locations, IHYPSLocation)
    bar.add_locations(bar_locations, IHYPSLocation)
    forest.add_locations(forest_locations, IHYPSLocation)
    wasp_country.add_locations(wasp_locations, IHYPSLocation)
    tower_base.add_locations(tower_base_locations, IHYPSLocation)
    strata_one.add_locations(strata_one_locations, IHYPSLocation)
    strata_two.add_locations(strata_two_locations, IHYPSLocation)
    strata_three.add_locations(strata_three_locations, IHYPSLocation)
    top_floor.add_locations(top_floor_locations, IHYPSLocation)
    hearts_tower.add_locations(hearts_tower_locations, IHYPSLocation)
    downtown.add_locations(downtown_locations, IHYPSLocation)
    warehouse.add_locations(warehouse_locations, IHYPSLocation)
    harbor.add_locations(harbor_locations, IHYPSLocation)
    beach.add_locations(beach_locations, IHYPSLocation)
