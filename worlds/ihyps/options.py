from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

# class Goal(Choice):
    # """
    # The victory condition of the world.
    
    # fresh_start: You will need to attain the Fresh Start ending by paying your rent, completing 
    # every Rank 3 quest, and buying out of your lease to move out. 

    # happy_ending: You will need to complete the final Lonely Hearts quest,
    # defeat Melchom, fight the Landlord, and purchase a floor of the Tower.

    # rental: Pay your rent
    # """
    # option_fresh_start: 0
    # option_happy_ending: 1
    # option_happy_ending_plus_gacy: 2
    # option_rental: 3

    # default = option_happy_ending_plus_gacy

class TrapChance(Range):
    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 5

@dataclass
class IHYPSOptions(PerGameCommonOptions):
    # goal: Goal
    trap_chance: TrapChance