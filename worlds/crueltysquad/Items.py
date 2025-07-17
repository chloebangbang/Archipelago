# most of this shamelessly templated from the inscryption apworld
from BaseClasses import ItemClassification
from typing import TypedDict, List

from BaseClasses import Item

base_id = 6253413671257683

class CrueltySquadItem(Item):
    name: str = "Cruelty Squad"

class ItemDict(TypedDict):
    name: str
    count: int
    classification: ItemClassification

stage_items: List[ItemDict] = [
    {
        'name': "Cruelty Squad HQ Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Pharmakokinetiks Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Paradise Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Sin Space Engineering Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Androgen Assault Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Mall Madness Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Apartment Atrocity Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Seaside Shock Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Bog Business Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Casino Catastrophy Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Idiot Party Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Office Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Archon Grid Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Darkworld Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Alpine Hospitality Unlock",
        'count': 1,
        'classification': ItemClassification.progression,
    },
    {
        'name': "Miner's Miracle Unlock",
        'count': 1,
        'classification': ItemClassification.progression,
    },
    {
        'name': "Neuron Activator Unlock",
        'count': 1,
        'classification': ItemClassification.progression,
    },
    {
        'name': "House Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Trauma Loop Unlock",
        'count': 1,
        'classification': ItemClassification.progression
    }
]

weapon_items: List[ItemDict] = [
    {
        'name': "Silenced Pistol",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "K&H R5",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Animal Control Pistol",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Expandable Baton",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Balotelli Hypernova",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "Riot Pacifier",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "New Safety M62",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Minato M9",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "Security Systems Anti-Armor Device",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "AMG4",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Precise Industry AS15",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Mowzer SP99",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Cerebral Bore",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "MCR Carbine",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "Bolt ACR",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "DNA Scrambler",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Stern M17",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "Stern AWS 3000",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "BAG-82",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "BN-99",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "Zippy 3000",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Flashlight",
        'count': 1,
        'classification': ItemClassification.progression,
    },
    {
        'name': "Fiberglass Fishing Rod",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "RPO-80 Sanitization System",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "ZKZ Transactional Rifle",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "MP-1 Nailer",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Raymond Shocktroop Tactical",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Abscess Ironworks Lux",
        'count': 1,
        'classification': ItemClassification.progression
    }
]

augment_items: List[ItemDict] = [
    {
        'name': "Speed Enhancer Gland",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Speed Enhancer Node Cluster",
        'count': 1,
        'classification': ItemClassification.useful,
    },
    {
        'name': "Speed Enhancer Total Organ Package",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Level II Body Armor",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Level IIB Body Armor",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Level III Body Armor",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Level IV Body Armor",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Level V Biosuit",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Level VI Golem Exosuit",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Tactical Blast Shield",
        'count': 1,
        'classification': ItemClassification.progression,
    },
    {
        'name': "Load Bearing Vest",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Hazmat Suit",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Military Camouflage",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Stealth Suit",
        'count': 1,
        'classification': ItemClassification.useful,
    },
    {
        'name': "Bouncy Suit",
        'count': 1,
        'classification': ItemClassification.progression,
    },
    {
        'name': "Extravagant Suit",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Biothruster",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Biojet",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "HE Grenade",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Flechette Grenade",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Sedative Grenade",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "First Aid Kit",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Portable Cassette Player",
        'count': 1,
        'classification': ItemClassification.filler
    },
    {
        'name': "Augmented Arms",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Abominator",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Grappendix",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Angular Advantage Tactical Munitions",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Ammunition Gland",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Cursed Torch",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Alien Leg Wetware",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Pneumatic Legs",
        'count': 1,
        'classification': ItemClassification.useful,
    },
    {
        'name': "Vertical Entry Device",
        'count': 1,
        'classification': ItemClassification.useful,
    },
    {
        'name': "Icaros Machine",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Funkboosters",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Funkgrunters",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Microbial Oil Secretion Glands",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Composite Helmet",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Bionic Eyes",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Life Sensors",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Skullgun",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "Goo Overdrive",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Flowerchute",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "Cortical Scaledown+",
        'count': 1,
        'classification': ItemClassification.useful
    },
    {
        'name': "Tattered Rain Hat",
        'count': 1,
        'classification': ItemClassification.filler
    },
    {
        'name': "Eyes of Corporate Insight",
        'count': 1,
        'classification': ItemClassification.filler
    },
    {
        'name': "Nightmare Vision Goggles",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Night Vision Goggles",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Holy Scope",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
]

misc_items: List[ItemDict] = [
    {
        'name': "Death",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "Resolution Options",
        'count': 1,
        'classification': ItemClassification.progression
    }, 
    {
        'name': "Malign Influence Immunity",
        'count': 1,
        'classification': ItemClassification.progression
    },
    {
        'name': "One Million Dollars",
        'count': 3,
        'classification': ItemClassification.progression
    }
]

filler_items: List[ItemDict] = [
    {
        'name': "10x Random Stock",
        'count': 1,
        'classification': ItemClassification.filler
    },
    {
        'name': "5000 Dollars",
        'count': 1,
        'classification': ItemClassification.filler
    },
    {
        'name': "50% Health Refill",
        'count': 1,
        'classification': ItemClassification.filler
    },

]

trap_items: List[ItemDict] = [
    {
        'name': "Flesh Automaton Trap",
        'count': 0,
        'classification': ItemClassification.trap
    },
    {
        'name': "Toxic Crisis Trap",
        'count': 0,
        'classification': ItemClassification.trap
    }
]

all_items: List[ItemDict] = weapon_items + augment_items + stage_items + misc_items + filler_items + trap_items

#101 required items