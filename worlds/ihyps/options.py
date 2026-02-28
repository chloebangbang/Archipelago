from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class NoLogic(Toggle):
    """
    Whether to disable logic. If logic is disabled, items will be placed randomly.

    WARNING: if you select no logic, your seed will be, in all likelihood, uncompletable. 
    This is an option put here by and for sickos. Proceed with extreme caution
    """
    display_name = "No Logic"

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

    # default = option_happy_ending_plus_gacy

class Skillsanity(Toggle):
    """
    Locks all skills learned by level up behind a requisite item.
    Also adds locations on level up to make leveling up not wholly useless.
    """

class TrapChance(Range):
    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 5

@dataclass
class IHYPSOptions(PerGameCommonOptions):
    no_logic: NoLogic
    # goal: Goal
    skillsanity: Skillsanity
    trap_chance: TrapChance