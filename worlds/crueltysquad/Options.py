from dataclasses import dataclass

from Options import Toggle, Choice, DeathLinkMixin, StartInventoryPool, PerGameCommonOptions

class Goal(Choice):
    display_name = "Goal"
    option_ending_1: 0
    option_ending_2: 1
    option_ending_3: 2
    option_all_endings: 3
    option_all_levels: 4
    default = 3

class TraumaLoopUnlockCondition(Choice):
    display_name = "Trauma Loop Unlock Condition"
    option_shuffled: 0
    option_clear_all_levels: 1
    option_clear_all_endings: 2
    default = 0

class DeathLinkBehavior(Choice):
    display_name = "Death Link Behavior"
    option_set_health_to_zero: 0
    option_instant_death: 1
    default = 0

@dataclass
class CrueltySquadOptions(DeathLinkMixin, PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    goal: Goal
    trauma_loop_unlock_condition: TraumaLoopUnlockCondition
    death_link_behavior: DeathLinkBehavior