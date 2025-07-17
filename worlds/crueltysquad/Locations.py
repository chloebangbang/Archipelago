from typing import Dict, List
from BaseClasses import Location

base_id = 6253413671257683

class CrueltySquadLocation(Location):
    game: str = "Cruelty Squad"

menu_locations = [
    "Start Weapon 1",
    "Start Weapon 2",
    "Starting Stage"
    "Shop Item 1",
    "Shop Item 2",
    "Shop Item 3",
    "Shop Item 4",
    "Shop Item 5",
    "Shop Item 6",
    "Shop Item 7",
    "Shop Item 8",
    "Shop Item 9",
    "Shop Item 10",
    "Shop Item 11",
    "Shop Item 12",
    "Shop Item 13",
    "Shop Item 14",
    "Shop Item 15",
    "Shop Item 16",
    "Shop Item 17",
    "Shop Item 18",
    "Shop Item 19",
    "Shop Item 20",
    "Shop Item 21",
    "Shop Item 22",
    "Shop Item 23",
    "Shop Item 24",
    "Shop Item 25",
    "Shop Item 26",
    "Shop Item 27",
    "Shop Item 28",
    "Shop Item 29",
    "Shop Item 30",
    "Shop Item 31",
    "Shop Item 32",
]

hq_locations = [
    "HQ Locker Money",
    "HQ Sewers Money",
    "Abominator Pickup",
    "ZKZ Transactional Rifle Pickup",
    "Ending 2"
]

pharmakokinetiks_locations = [
    "Death Surgery",
    "Pharmakokinetiks Rocket Pickup",
    "Sigismund's Gun",
    "Pharmakokinetiks DNA Scrambler Pickup",
    "Pharmakokinetiks Divine Money",
    "Pharmakokinetiks Lobby Money",
    "Pharmakokinetiks Storage Money",
    "Pharmakokinetiks Office Money",
    "Pharmakokinetiks Complete",
]

paradise_locations = [
    "Cursed Torch Pickup",
    "Icaros Machine Pickup",
    "Paradise Compound AWS",
    "Paradise Rocket Pickup",
    "Paradise Secret Exit",
    "Paradise Complete",
]

sinspace_locations = [
    "Fishing Rod Pickup",
    "Sin Space Armory Hypernova",
    "Sin Space Armory Silenced Pistol",
    "Sin Space Armory R5",
    "Sin Space Shipping Container Minato",
    "Sin Space Engineering Complete"
]

androgen_locations = [
    "Androgen Assault Riot Pacifier",
    "Androgen Assault Augment Pickup",
    "Androgen Assault Complete"
]

mall_locations = [
    "Mall Pizza Shotgun",
    "Mall Gun Shop 1",
    "Mall Gun Shop 2",
    "Mall Gun Shop 3",
    "Mall Gun Shop 4",
    "Mall Gun Shop 5",
    "Mall Gun Shop 6",
    "Plant Heaven Implant",
    "Mall Madness Complete"
]

apartment_locations = [
    "Apartment AWS",
    "Apartment Atrocity Complete"
]

seaside_locations = [
    "Seaside Shock Portside Weapon",
    "Seaside Shock Secret Exit",
    "Seaside Shock Complete",
]

bog_locations = [
    "Bog Business Implant",
    "Bog Business Secret Exit",
    "Bog Business Complete"
]

casino_locations = [
    "Gun Slot Machine",
    "Casino Catastrophy Complete"
]

idiot_party_locations = [
    "Idiot Party Cerebral Bore",
    "Idiot Party Tattered Rain Hat",
    "Idiot Party Bouncy Suit",
    "Idiot Party Secret Exit",
    "Idiot Party Complete"
]

office_locations = [
    "Office Bolt ACR",
    "Office Augment",
    "Office Complete"
]

archon_grid_locations = [
    "Archon Grid Augment",
    "Ending 1",
]

darkworld_locations = [
    "Darkworld Kitchen Implant",
    "Darkworld Complete"
]

alpine_locations = [
    "Alpine Hospitality Rightside Weapon",
    "Apine Hospitality Roof Implant",
    "Alpine Hospitality Complete"
]

miner_locations = [
    "Miner's Miracle Implant",
    "Miner's Miracle Complete"
]

neuron_locations = [
    "Neuron Activator Bank Money 1",
    "Neuron Activator Bank Money 2",
    "Neuron Activator Bank Money 3",
    "Neuron Activator Bank Money 4",
    "Neuron Activator Bank Money 5",
    "Neuron Activator Bank Money 6",
    "Neuron Activator Bank Money 7",
    "Neuron Activator Bank Money 8",
    "Neuron Activator Complete"
]

house_locations = [
    "Triagon 1", 
    "Triagon 2", 
    "Triagon 3",
    "House Fountain Implant",
    "House Complete",
]

trauma_locations = [
    "Trauma Loop Biojet Pickup",
    "Limit Chancellor Dead",
    "Ending 3",
]

#this line sucks
all_locations = menu_locations + hq_locations + pharmakokinetiks_locations + paradise_locations + sinspace_locations + androgen_locations + mall_locations + apartment_locations + seaside_locations + bog_locations + casino_locations + idiot_party_locations + office_locations + archon_grid_locations + darkworld_locations + alpine_locations + miner_locations + neuron_locations + house_locations + trauma_locations

#117 total locations