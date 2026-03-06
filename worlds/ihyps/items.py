from typing import TYPE_CHECKING

from BaseClasses import ItemClassification as IC
from BaseClasses import Item

from typing import List

class ItemDef: 
    def __init__(self, id: int, name: str, classification: IC, count: int = 1):
        self.id = id
        self.name = name
        self.classification = classification
        self.count = count

BASE_ID = 433996108

universal_items: List[ItemDef] = [
    ItemDef(BASE_ID + 0, "Devon", IC.progression),
    ItemDef(BASE_ID + 1, "Kyrie", IC.progression),
    ItemDef(BASE_ID + 2, "Jasper", IC.progression),
    ItemDef(BASE_ID + 3, "Bar", IC.progression),
    ItemDef(BASE_ID + 4, "Forest", IC.progression),
    ItemDef(BASE_ID + 5, "Tower", IC.progression),
    ItemDef(BASE_ID + 6, "Downtown", IC.progression),
    ItemDef(BASE_ID + 7, "Harbor", IC.progression),
    ItemDef(BASE_ID + 8, "Progressive AL Rank", IC.progression, 4),
    ItemDef(BASE_ID + 9, "Lockpicking Guide", IC.progression),
    # ItemDef(BASE_ID + 10, "Casino Keycard", IC.progression),
    ItemDef(BASE_ID + 11, "Progressive Dungeon Stone", IC.progression, 3),
    ItemDef(BASE_ID + 12, "Half a Photo", IC.progression, 2),
    ItemDef(BASE_ID + 13, "Lion's Den Password", IC.progression),
    ItemDef(BASE_ID + 14, "Kitchen Knife", IC.progression),
    ItemDef(BASE_ID + 15, "Victim's Bag", IC.progression),
    ItemDef(BASE_ID + 16, "Rare Game", IC.progression),
    ItemDef(BASE_ID + 17, "Homemade Chocolates", IC.progression),
    ItemDef(BASE_ID + 18, "Bleeding Heart Vodka", IC.useful),
    ItemDef(BASE_ID + 19, "Envelope", IC.progression),
    ItemDef(BASE_ID + 20, "Blessed Shades", IC.useful),
    ItemDef(BASE_ID + 21, "Sewer Key", IC.progression),
    ItemDef(BASE_ID + 22, "Strange Driftwood", IC.progression),
    ItemDef(BASE_ID + 23, "Arcade Token", IC.progression),
    ItemDef(BASE_ID + 24, "Decayer", IC.useful),
    ItemDef(BASE_ID + 25, "Lighthouse Deeds", IC.progression),
    # trauma certificate
    ItemDef(BASE_ID + 26, "Final Boss Key", IC.progression, 4),
    # ItemDef(BASE_ID + 27, "Rental Agreement", IC.progression),
    ItemDef(BASE_ID + 28, "Sealed Envelope", IC.progression),
    ItemDef(BASE_ID + 29, "Invite", IC.useful),
    ItemDef(BASE_ID + 30, "Baseball Cards", IC.progression),
    ItemDef(BASE_ID + 31, "Fuzzy Trip in Remix Land", IC.progression),
    ItemDef(BASE_ID + 32, "It's Time for Adventure v2", IC.filler),
    ItemDef(BASE_ID + 33, "ULTRA PERSON V1", IC.filler),
    ItemDef(BASE_ID + 34, "Shine Burst", IC.filler),
    ItemDef(BASE_ID + 35, "Nostalgia", IC.filler),
    ItemDef(BASE_ID + 36, "CORNER DOT COM", IC.filler),
    ItemDef(BASE_ID + 37, "Fuzzy Trip Volume 2", IC.filler),
    ItemDef(BASE_ID + 38, "Pump up the BRRRKRRRRR", IC.filler),
    ItemDef(BASE_ID + 39, "Exploding Head Syndrome", IC.filler),
    ItemDef(BASE_ID + 40, "You know where to find me", IC.filler),
    ItemDef(BASE_ID + 41, "Lightkill's Gun", IC.progression),
    ItemDef(BASE_ID + 42, "Lost Cell Phone", IC.progression),
    # bounties
    ItemDef(BASE_ID + 43, "Mack's Glove", IC.useful),
    ItemDef(BASE_ID + 44, "Bubos' Tooth", IC.useful),
    ItemDef(BASE_ID + 45, "Casino Logo Pin", IC.useful),
    ItemDef(BASE_ID + 46, "Chef's ID Card", IC.useful),
    ItemDef(BASE_ID + 47, "Flamberge Piece", IC.useful),
    ItemDef(BASE_ID + 48, "Rat Corpse", IC.useful),
    ItemDef(BASE_ID + 49, "Fleshy Rat", IC.useful),
    ItemDef(BASE_ID + 50, "Emily's Gasmask", IC.progression),
    # my girlfriend is an evil genius. these are the landlord's glasses
    ItemDef(BASE_ID + 51, "Pugilist's Hand Wraps", IC.useful),
    ItemDef(BASE_ID + 52, "Mother's Hairband", IC.useful),
    ItemDef(BASE_ID + 53, "Seagull Tongue", IC.useful),
    ItemDef(BASE_ID + 54, "Clarence's ID", IC.useful),
    ItemDef(BASE_ID + 55, "Abyssal Eye", IC.useful),
    ItemDef(BASE_ID + 56, "Crude ID", IC.useful),
    ItemDef(BASE_ID + 57, "License Plate", IC.useful),
    ItemDef(BASE_ID + 58, "Broken Antler", IC.useful),
    ItemDef(BASE_ID + 59, "Eyewitness Report", IC.useful),
    # equipment
    ItemDef(BASE_ID + 60, "Progressive Ramona Gear", IC.useful, 3),
    ItemDef(BASE_ID + 61, "Progressive Devon Gear", IC.useful, 3),
    ItemDef(BASE_ID + 62, "Progressive Kyrie Gear", IC.useful, 2),
    ItemDef(BASE_ID + 63, "Jasper Gear", IC.useful),

    ItemDef(BASE_ID + 64, "Meat Cleaver", IC.progression),
    # ItemDef(BASE_ID + 65, "Magic Knife", IC.progression),
    ItemDef(BASE_ID + 66, "Trish's Knife", IC.progression),

    ItemDef(BASE_ID + 67, "Wrench", IC.progression),
    ItemDef(BASE_ID + 68, "Cheater's Bat", IC.useful),
    
    ItemDef(BASE_ID + 69, "Blessed Construction Hammer", IC.useful),
    ItemDef(BASE_ID + 70, "Meat Tenderizer", IC.useful),

    # unused and broken. strictly worse than the machine gun
    # ItemDef(BASE_ID + 71, "Sleek Pistol", IC.useful),
    ItemDef(BASE_ID + 72, "Police-Issue Gun", IC.useful),
    ItemDef(BASE_ID + 73, "Doohickey", IC.useful),
    ItemDef(BASE_ID + 74, "Machine Gun", IC.useful),

    ItemDef(BASE_ID + 75, "Working for the Knife", IC.progression),
    ItemDef(BASE_ID + 76, "The Silence is Mine", IC.useful),
    ItemDef(BASE_ID + 77, "The Show", IC.useful),
    ItemDef(BASE_ID + 78, "Feel Good Inc.", IC.useful),

    ItemDef(BASE_ID + 79, "Jogger's Shorts", IC.useful),
    ItemDef(BASE_ID + 80, "Patrick's Locket", IC.useful),
    ItemDef(BASE_ID + 81, "Basalmo's Bracelet", IC.useful),
    ItemDef(BASE_ID + 82, "Black Cat Charm", IC.useful),
    ItemDef(BASE_ID + 83, "Cat Shawl", IC.useful),
    ItemDef(BASE_ID + 84, "Mack's Eyepatch", IC.useful),
    ItemDef(BASE_ID + 85, "Focus Charm", IC.useful),
    ItemDef(BASE_ID + 86, "Trish's Overcoat", IC.useful),
    ItemDef(BASE_ID + 87, "Burner Phone", IC.useful),
    ItemDef(BASE_ID + 88, "Air Freshener", IC.useful),
    ItemDef(BASE_ID + 89, "Raccoon King's Crown", IC.useful),
    ItemDef(BASE_ID + 90, "Quinnith's Necklace", IC.useful),
    ItemDef(BASE_ID + 91, "Spare Nametag", IC.useful),
    ItemDef(BASE_ID + 92, "Backup Shades", IC.useful),
    ItemDef(BASE_ID + 93, "Abernathy's Glasses", IC.useful),
    ItemDef(BASE_ID + 94, "Jessie's Pocket Watch", IC.useful),

    # quest rewards
    # stanley quest (normal)
    ItemDef(BASE_ID + 107, "$150", IC.filler),
    ItemDef(BASE_ID + 108, "$250", IC.filler),
    ItemDef(BASE_ID + 109, "$500", IC.filler),
    ItemDef(BASE_ID + 110, "$600", IC.filler),
    ItemDef(BASE_ID + 111, "$1000", IC.filler),
    ItemDef(BASE_ID + 112, "$333", IC.filler),
    ItemDef(BASE_ID + 113, "$1200", IC.filler, 2),
    ItemDef(BASE_ID + 114, "$1500", IC.filler),

    # spiritual healing rewards
    ItemDef(BASE_ID + 117, "Perfect Lunge", IC.useful),
    ItemDef(BASE_ID + 118, "Talk Shit, Get Hit", IC.useful),
    ItemDef(BASE_ID + 119, "Second Wind", IC.useful),
    ItemDef(BASE_ID + 120, "Pretend It's Not There", IC.useful),
    ItemDef(BASE_ID + 121, "Clear Mind", IC.useful),
    ItemDef(BASE_ID + 122, "Quiet Meditation", IC.useful),
    ItemDef(BASE_ID + 123, "Friendly Advice", IC.useful),
    ItemDef(BASE_ID + 124, "Killing Harmony", IC.useful),
    ItemDef(BASE_ID + 125, "Cool Down", IC.useful),
    ItemDef(BASE_ID + 126, "Long Range", IC.useful),
    ItemDef(BASE_ID + 127, "Dodge Roll", IC.useful),
    ItemDef(BASE_ID + 128, "Cry", IC.useful),
]

filler_items: List[ItemDef] = [
    # filler items
    ItemDef(BASE_ID + 95, "Artifact Gatcha", IC.filler),
    ItemDef(BASE_ID + 96, "Artifact Tarot", IC.useful),
    ItemDef(BASE_ID + 97, "Mafia Noteriety", IC.trap),
    ItemDef(BASE_ID + 98, "Cursed!", IC.trap),
    ItemDef(BASE_ID + 99, "Miracle Drink", IC.filler),
    ItemDef(BASE_ID + 100, "Unwanted Guest", IC.trap),
    ItemDef(BASE_ID + 101, "Estrogen", IC.filler),
    ItemDef(BASE_ID + 102, "Testosterone", IC.filler),
    ItemDef(BASE_ID + 103, "Albing Knife", IC.filler),
    ItemDef(BASE_ID + 104, "Albing Staff", IC.filler),
    ItemDef(BASE_ID + 105, "Albing Hammer", IC.filler),
    ItemDef(BASE_ID + 106, "Albing Revolver", IC.filler),
    ItemDef(BASE_ID + 129, "Albing Weapon", IC.filler),
    ItemDef(BASE_ID + 130, "Nothing...", IC.filler),
]

skill_items: List[ItemDef] = [
    # ramona skills
    ItemDef(BASE_ID + 150, "Bribe", IC.progression),
    ItemDef(BASE_ID + 151, "Spray", IC.useful),
    ItemDef(BASE_ID + 152, "Progressive Lunge", IC.useful),
    ItemDef(BASE_ID + 153, "Business Talk", IC.progression),
    ItemDef(BASE_ID + 154, "Self-Care", IC.useful),
    ItemDef(BASE_ID + 155, "Loud Speech", IC.useful),
    ItemDef(BASE_ID + 156, "Money Toss", IC.useful),
    ItemDef(BASE_ID + 157, "Rummage", IC.useful),
    ItemDef(BASE_ID + 158, "Shank", IC.useful),
    ItemDef(BASE_ID + 159, "All Business", IC.useful),
    # devon skills
    ItemDef(BASE_ID + 160, "Shut You Up", IC.useful),
    ItemDef(BASE_ID + 161, "True Silence", IC.progression),
    ItemDef(BASE_ID + 162, "Erase Presence", IC.useful),
    ItemDef(BASE_ID + 163, "Silence is Bliss", IC.useful),
    ItemDef(BASE_ID + 164, "Swing for the Fences", IC.useful),
    ItemDef(BASE_ID + 165, "Redirected Noise", IC.useful),
    # kyrie skills
    ItemDef(BASE_ID + 166, "Death Threats", IC.useful),
    ItemDef(BASE_ID + 167, "Focused Blow", IC.useful),
    ItemDef(BASE_ID + 168, "Mask Up", IC.useful),
    ItemDef(BASE_ID + 169, "Blood Rush", IC.useful),
    ItemDef(BASE_ID + 170, "Hunt Down", IC.useful),
    ItemDef(BASE_ID + 171, "Vengeance", IC.useful),
    ItemDef(BASE_ID + 172, "Crocodile Tears", IC.useful),
    # jasper skills
    # not randomizing reload. that would suck bad
    # magic bullet is the reason I'm bothering randomizing starting skills at all. its so good
    # actually busted skill
    ItemDef(BASE_ID + 173, "Magic Bullet", IC.useful),
    ItemDef(BASE_ID + 174, "Perfect Shot", IC.useful),
    ItemDef(BASE_ID + 175, "Bullet Time", IC.useful),
    ItemDef(BASE_ID + 176, "Close Range", IC.useful),
    ItemDef(BASE_ID + 177, "Gun Whip", IC.useful),
]

items = universal_items + filler_items + skill_items

ITEM_NAME_TO_ID = {item.name: item.id for item in items}


class IHYPSItem(Item): 
    game = "I Hate You, Please Suffer"

def get_random_filler_item_name(world) -> str:
    if world.random.randint(0, 99) < world.options.trap_chance:
        trap_roll = world.random.randint(0, 2)
        match trap_roll:
            case 0: return "Cursed!"
            case 1: return "Unwanted Guest"
            case 2: return "Mafia Noteriety"
    else:
        filler_roll = world.random.randint(0, 99)
        if filler_roll < 50:
            return "Artifact Gatcha"
        elif filler_roll < 60:
            return "Miracle Drink"
        elif filler_roll < 65:
            return "Estrogen"
        elif filler_roll < 70:
            return "Testosterone"
        elif filler_roll < 72:
            return "Artifact Tarot"
        elif filler_roll < 76:
            return "Nothing..."
        else:
            return "Albing Weapon"

def create_item(world, name: str) -> IHYPSItem:
    # TODO: find out why the hell this would ever need to be a line of code
    # what is going on. this is a hacky fix. why do I need to create none item
    if name == None:
        name = get_random_filler_item_name(world)
    # I am deeply regretting the way I structured this
    itemdef = [item for item in items if item.name == name][0]

    return IHYPSItem(name, itemdef.classification, itemdef.id, world.player)

def create_all_items(world) -> IHYPSItem:
    itempool: list[IHYPSItem] = []
    randomized_items = universal_items
    if world.options.skillsanity:
        randomized_items += skill_items
    for item in randomized_items:
        if not (world.options.skillsanity and item.name == "Perfect Lunge"): 
            for _ in range(item.count):
                itempool.append(world.create_item(item.name))
    item_count = len(itempool)
    unfilled_locations_count = len(world.multiworld.get_unfilled_locations(world.player))
    needed_filler_count = unfilled_locations_count - item_count
    itempool += [world.create_filler() for _ in range(needed_filler_count)]
    world.multiworld.itempool += itempool