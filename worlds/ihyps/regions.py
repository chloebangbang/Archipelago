from BaseClasses import Entrance, Region

def create_and_connect_regions(world) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world) -> None:
    apartment = Region("Apartment", world.player, world.multiworld)
    bar = Region("Bar", world.player, world.multiworld)
    forest = Region("Forest", world.player, world.multiworld)
    wasp_country = Region("West Forest", world.player, world.multiworld)
    tower = Region("Tower", world.player, world.multiworld)
    strata_one = Region("Tower Stratum 1", world.player, world.multiworld)
    strata_two = Region("Tower Stratum 2", world.player, world.multiworld)
    strata_three = Region("Tower Stratum 3", world.player, world.multiworld)
    top_floor = Region("Tower Top Floor", world.player, world.multiworld)
    hearts_tower = Region("Hearts Tower", world.player, world.multiworld)
    downtown = Region("Downtown", world.player, world.multiworld)
    warehouse = Region("Warehouse", world.player, world.multiworld)
    harbor = Region("Harbor", world.player, world.multiworld)
    beach = Region("Beach", world.player, world.multiworld)


    regions = [apartment, bar, forest, wasp_country, tower, strata_one, strata_two, strata_three, downtown, warehouse, harbor, beach, hearts_tower, top_floor]

    world.multiworld.regions += regions

def connect_regions(world) -> None:
    apartment = world.get_region("Apartment")
    bar = world.get_region("Bar")
    forest = world.get_region("Forest")
    wasp_country = world.get_region("West Forest")
    tower = world.get_region("Tower")
    strata_one = world.get_region("Tower Stratum 1")
    strata_two = world.get_region("Tower Stratum 2")
    strata_three = world.get_region("Tower Stratum 3")
    top_floor = world.get_region("Tower Top Floor")
    hearts_tower = world.get_region("Hearts Tower")
    downtown = world.get_region("Downtown")
    warehouse = world.get_region("Warehouse")
    harbor = world.get_region("Harbor")
    beach = world.get_region("Beach")

    apartment.connect(bar, "To Bar")
    apartment.connect(forest, "To Forest")
    apartment.connect(tower, "To Tower")
    apartment.connect(downtown, "To Downtown")
    apartment.connect(harbor, "To Harbor")
    forest.connect(wasp_country, "To West Forest")
    tower.connect(strata_one, "To Stratum 1")
    strata_one.connect(hearts_tower, "Begin Hearts Quest")
    strata_one.connect(strata_two, "To Stratum 2")
    strata_two.connect(strata_three, "To Stratum 3")
    strata_three.connect(top_floor, "To Tower Top Floor")
    strata_one.connect(strata_three, "Stratum 3 Warp")
    strata_one.connect(top_floor, "Tower Top Floor Warp")
    downtown.connect(warehouse, "To Warehouse")
    harbor.connect(beach, "To Beach")