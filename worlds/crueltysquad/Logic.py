from . import CrueltySquadWorld
from BaseClasses import MultiWorld, CollectionState

def can_fly(state: CollectionState, player: int) -> bool:
    return state.has("Abominator", player) or state.has("Grappendix") or state.has("Biojet")

# items required to get from hq attic to the shrines
def has_holy_vision(state: CollectionState, player: int) -> bool:
    return state.has("Resolution Options", player) or state.has("Holy Scope", player)

def can_rocket_jump(state: CollectionState, player: int) -> bool:
    return state.has("Security Systems Anti-Armor Device", player) and state.has("Tactical Blast Shield", player)

def can_access_hq_attic(state: CollectionState, player: int) -> bool:
    if state.has("Cruelty Squad HQ", player):
        if can_pierce_armor(state, player) or state.has("HE Grenade", player):
            return has_holy_vision(state, player)
        elif state.has("Icaros Machine", player) or (state.has("Death", player) and (state.has("Funkboosters", player) or state.has("Funkgrunters", player))) or \
        can_fly(state, player) or state.has("Biojet", player) :
            return has_holy_vision(state, player)
        # head slot is incompatible with holy scope
        elif state.has("Skullgun", player) or state.has("Goo Overdrive") or \
        (state.has("Flowerchute", player) and (state.has("Death", player) or state.has("Funkgrunters", player) or state.has("Funkboosters", player) or state.has("Speed Booster Total Organ Package", player))):
            return state.has("Resolution Options", player)
    return False

# can break cracked walls and doors
# can use arm slot
def can_break_walls(state:CollectionState, player: int) -> bool:
    can_pierce_armor(state, player) or state.has("HE Grenade", player)

# doesn't include skull gun
def can_pierce_armor(state: CollectionState, player: int) -> bool:
    return state.has("Security Systems Anti-Armor Device", player) or state.has("Stern AWS 3000", player) or \
        state.has("AMG4", player) or state.has("Stern M17", player) or state.has("MCR Carbine", player) or \
        state.has("MP-1 Nailer")

# any logical weapon for clearing out early game unarmored areas eg pharmakokinetiks
# including extremely low ammo weapons eg rocket launcher and aws
def has_any_weapon(state: CollectionState, player: int) -> bool:
    return state.has("Silenced Pistol", player) or state.has("K&H R5", player) or state.has("Batelli Hypernova", player) or \
      state.has("Riot Pacifier", player) or state.has("New Safety M62", player) or state.has("Minato M9", player) or \
      state.has("Security Systems Anti-Armor Device", player) or state.has("AMG4", player) or state.has("Precise Industry AS15", player) or \
      state.has("Mowser SP99", player) or state.has("Cerebral Bore", player) or state.has("MCR Carbine", player) or \
      

def can_divine_light(state: CollectionState, player: int) -> bool:
    return can_access_hq_attic(state, player) or state.has("Archon Grid Unlock")