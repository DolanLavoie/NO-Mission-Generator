import argparse
import json
import random
import re
from pathlib import Path
from math import floor

import random_mission_generator


# ============================================================
# CONFIGURATION
# ============================================================

BASE_PATH = Path(__file__).resolve().parent
SAVE_FOLDER = BASE_PATH / "Saves"

STARTING_BUDGET = 10
BUDGET_INCREASE = 10
BUDGET_MULTIPLIER = 1.5


# ============================================================
# AIRCRAFT DATABASE
# ============================================================

# Aircraft are stored using their Nuclear Option JSON keys.
# Rank is used as the aircraft tier.

AIRCRAFT = [
    {"name": "MiG-15", "key": "Aryx_MiG-15", "tier": 0},
    {"name": "Cricket", "key": "COIN", "tier": 0},
    {"name": "Cavalier", "key": "Aryx_PropAttacker1", "tier": 0},
    {"name": "Knockout", "key": "Aryx_LightHelicopter1", "tier": 0},
    {"name": "Compass", "key": "trainer", "tier": 1},
    {"name": "Kukri", "key": "AH31_Kukri", "tier": 1},
    {"name": "Vagrant", "key": "VTOLTrainer1", "tier": 1},
    {"name": "Ibis", "key": "UtilityHelo1", "tier": 1},
    {"name": "Chicane", "key": "AttackHelo1", "tier": 1},
    {"name": "Shrike", "key": "Aryx_LightFighter1", "tier": 2},
    {"name": "Brawler", "key": "CAS1", "tier": 2},
    {"name": "Kestrel", "key": "kestrel", "tier": 2},
    {"name": "Tarantula", "key": "QuadVTOL1", "tier": 2},
    {"name": "King Viper", "key": "Aryx_F16M_KingViper", "tier": 3},
    {"name": "Agni", "key": "1509_palafighter1", "tier": 3},
    {"name": "Revoker", "key": "Fighter1", "tier": 3},
    {"name": "Vortex", "key": "SmallFighter1", "tier": 3},
    {"name": "Ifrit", "key": "Multirole1", "tier": 4},
    {"name": "Ternion", "key": "P_Trisurface1", "tier": 4},
    {"name": "Medusa", "key": "EW1", "tier": 4},
    {"name": "Chimera", "key": "Aryx_CargoPlane1", "tier": 4},
    {"name": "Strike Raptor", "key": "Aryx_F22E_StrikeRaptor", "tier": 5},
    {"name": "Darkreach", "key": "Darkreach", "tier": 5},
    {"name": "Eclipse", "key": "Aryx_Interceptor1", "tier": 5},
    {"name": "Alkyon", "key": "FastBomber1", "tier": 6},
]


# ============================================================
# MUNITION DATABASE
# ============================================================

STARTING_MUNITIONS = [
    "PAB-125",
    "PAB-250",
    "Kingpin",
    "Lynchpin",
    "IRM-S1",
    "IRM-S2",
]

UNLOCKABLE_MUNITIONS = [
    "GPO-500",
    "PAB-80LR",
    "AT-145",
    "AGM-48",
    "Eyeball Mk.II",
    "ATP-1",
    "PAB-250LR",
    "AGM-68",
    "AGM-27 Pyre",
    "Demolition Bomb",
    "GPO-2P Auger",
    "AGR-37 Jester",
    "IRM-S5 Gladius",
    "MMR-S3",
    "CBO-400",
    "ARAD-45",
    "AGM-76 Atlatl",
    "MRM-S4 Broadsword",
    "PGM-400LR",
    "ARAD-116",
    "PAB-3000LR",
    "AAM-29 Scythe",
    "AGM-99",
    "ALM-C450",
    "Tusko-B",
    "AShM-300",
    "AAM-36 Scimitar",
    "GBM-500LR",
    "AAM-45 Sabre",
    "AGM-111 Nemesis",
    "Piledriver",
    "HSM-750 Starfall",
]


# ============================================================
# GENERAL FUNCTIONS
# ============================================================


def get_aircraft(key):
    return next((plane for plane in AIRCRAFT if plane["key"] == key), None)


def get_player_names():
    while True:
        raw = input("Enter player names separated by commas: ")

        names = [name.strip() for name in raw.split(",") if name.strip()]

        if not names:
            print("At least one player is required.")
            continue

        if len(set(name.lower() for name in names)) != len(names):
            print("Player names must be unique.")
            continue

        return names


def get_save_path(filename):
    # Prevent directory traversal and restrict saves to Saves/.
    filename = Path(filename).name

    if filename.lower().endswith(".json"):
        filename = filename[:-5]

    if not filename:
        raise ValueError("Invalid save filename.")

    if not re.fullmatch(r"[A-Za-z0-9_-]+", filename):
        raise ValueError(
            "Save names can only contain letters, numbers, underscores, and hyphens."
        )

    return SAVE_FOLDER / f"{filename}.json"


def save_game(save, path):
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(save, file, indent=4)


def load_game(path):
    with path.open("r", encoding="utf-8") as file:
        save = json.load(file)

    return save


# ============================================================
# BUDGET MANAGEMENT
# ============================================================


def calculate_next_budget(current_budget, player_count):
    per_player_budget = current_budget // player_count

    next_per_player = floor(per_player_budget * BUDGET_MULTIPLIER + BUDGET_INCREASE)

    return next_per_player * player_count


def get_current_enemy_budget(save_name):
    """
    Importable function for the mission generator.

    Example:
        budget = get_current_enemy_budget("Campaign1")
    """
    path = get_save_path(save_name)
    save = load_game(path)

    return save["current_enemy_budget"]


# ============================================================
# SAVE CREATION
# ============================================================


def create_new_save(save_name):
    path = get_save_path(save_name)

    if path.exists():
        print("A save with that name already exists.")
        return

    names = get_player_names()

    save = {
        "mission_number": 1,
        "current_enemy_budget": (STARTING_BUDGET * len(names)),
        "player_count": len(names),
        "players": {},
    }

    for name in names:
        save["players"][name] = {
            "aircraft": [plane["key"] for plane in AIRCRAFT if plane["tier"] == 0],
            "munitions": STARTING_MUNITIONS.copy(),
        }

    save_game(save, path)

    print("\nSave created successfully.")
    print(f"Save: {path}")
    print(f"Players: {len(names)}")
    print(f"Starting enemy budget: ${save['current_enemy_budget']}m")


# ============================================================
# AIRCRAFT LOSS MANAGEMENT
# ============================================================


def display_aircraft(aircraft):
    if not aircraft:
        print("  No aircraft owned.")
        return

    for index, key in enumerate(aircraft, start=1):
        plane = get_aircraft(key)

        name = plane["name"] if plane else key
        tier = plane["tier"] if plane else "?"

        print(f"  {index}. {name} (Tier {tier})")


def select_aircraft_losses(player):
    aircraft = player["aircraft"]

    print("\nAircraft inventory:")
    display_aircraft(aircraft)

    if not aircraft:
        return

    while True:
        raw = input(
            "\nEnter the numbers of aircraft lost, "
            "separated by commas (or press Enter for none): "
        ).strip()

        if not raw:
            return

        try:
            selections = [int(value.strip()) for value in raw.split(",")]

            if len(set(selections)) != len(selections):
                raise ValueError

            if any(number < 1 or number > len(aircraft) for number in selections):
                raise ValueError

            break

        except ValueError:
            print("Invalid selection. Try again.")

    # Remove in reverse order so indexes remain valid.
    for number in sorted(selections, reverse=True):
        lost = aircraft.pop(number - 1)

        plane = get_aircraft(lost)
        name = plane["name"] if plane else lost

        print(f"Lost: {name}")


# ============================================================
# REWARD GENERATION
# ============================================================


def generate_aircraft_reward(player):
    aircraft = player["aircraft"]

    owned_planes = [
        get_aircraft(key) for key in aircraft if get_aircraft(key) is not None
    ]

    if owned_planes:
        highest_tier = max(plane["tier"] for plane in owned_planes)
    else:
        highest_tier = 0

    eligible = [plane for plane in AIRCRAFT if plane["tier"] <= highest_tier + 1]

    return random.choice(eligible)


def generate_munition_rewards(player):
    unowned = [
        munition
        for munition in UNLOCKABLE_MUNITIONS
        if munition not in player["munitions"]
    ]

    return random.sample(unowned, min(3, len(unowned)))


def select_reward(player):
    munitions = generate_munition_rewards(player)
    aircraft = generate_aircraft_reward(player)

    print("\nAvailable rewards:")

    rewards = []

    for munition in munitions:
        rewards.append({"type": "munition", "value": munition})

    rewards.append({"type": "aircraft", "value": aircraft["key"]})

    for index, reward in enumerate(rewards, start=1):
        if reward["type"] == "munition":
            description = f"Munition unlock: {reward['value']}"
        else:
            plane = get_aircraft(reward["value"])

            description = f"Aircraft: {plane['name']} (Tier {plane['tier']})"

        print(f"  {index}. {description}")

    while True:
        try:
            selection = int(input("\nSelect your reward: "))

            if 1 <= selection <= len(rewards):
                break

        except ValueError:
            pass

        print("Invalid selection.")

    reward = rewards[selection - 1]

    if reward["type"] == "munition":
        player["munitions"].append(reward["value"])
        print(f"\nUnlocked munition: {reward['value']}")

    else:
        player["aircraft"].append(reward["value"])

        plane = get_aircraft(reward["value"])

        print(f"\nUnlocked aircraft: {plane['name']}")


# ============================================================
# MISSION END
# ============================================================


def process_mission_end(save, path):
    print("\n================================")
    print("         MISSION END")
    print("================================")

    print(f"Mission {save['mission_number']} complete.")

    for name, player in save["players"].items():
        print(f"\n================================")
        print(f"PLAYER: {name}")
        print("================================")

        # Step 1: Select lost aircraft.
        select_aircraft_losses(player)

        # Step 2: Select a reward.
        select_reward(player)

        print(f"\nUpdated inventory for {name}:")
        print("\nAircraft:")
        display_aircraft(player["aircraft"])

        print("\nMunitions:")
        for munition in player["munitions"]:
            print(f"  - {munition}")

    # Advance mission and budget after all players are processed.
    save["mission_number"] += 1

    save["current_enemy_budget"] = calculate_next_budget(
        save["current_enemy_budget"], save["player_count"]
    )

    save_game(save, path)

    # Generate the next mission using the newly calculated enemy budget.
    print("\n================================")
    print("      GENERATING NEXT MISSION")
    print("================================")

    try:
        random_mission_generator.generate_mission(
            save["current_enemy_budget"], overwrite=True, verbose=True
        )
    except Exception as error:
        print(f"Failed to generate the next mission: {error}")

    continue_save(save_name=path.stem)


# ============================================================
# SAVE CONTINUATION
# ============================================================


def continue_save(save_name):
    path = get_save_path(save_name)

    if not path.exists():
        print(f"Save not found: {path}")
        return

    save = load_game(path)

    print("\n================================")
    print("          SAVE LOADED")
    print("================================")

    print(f"Mission: {save['mission_number']}")

    print(f"Current enemy budget: ${save['current_enemy_budget']}m")

    print(f"Players: {save['player_count']}")

    for name, player in save["players"].items():
        print(f"\n{name}")

        print(f"Aircraft owned: {len(player['aircraft'])}")
        print(f"Munitions unlocked: {len(player['munitions'])}")

    print("\n1. Process mission end")
    print("2. Exit")

    while True:
        selection = input("\nSelect an option: ").strip()

        if selection == "1":
            process_mission_end(save, path)
            break

        elif selection == "2":
            break

        else:
            print("Invalid selection.")


# ============================================================
# COMMAND LINE INTERFACE
# ============================================================


def main():
    parser = argparse.ArgumentParser(description="Nuclear Option Campaign Save Manager")

    subparsers = parser.add_subparsers(dest="command", required=True)

    new_parser = subparsers.add_parser("new", help="Create a new campaign save.")

    new_parser.add_argument("save_name", help="Name of the new save file.")

    continue_parser = subparsers.add_parser(
        "continue", help="Continue an existing campaign."
    )

    continue_parser.add_argument("save_name", help="Name of the save file to load.")

    budget_parser = subparsers.add_parser(
        "budget", help="Display the current enemy budget."
    )

    budget_parser.add_argument("save_name", help="Name of the save file.")

    args = parser.parse_args()

    SAVE_FOLDER.mkdir(parents=True, exist_ok=True)

    if args.command == "new":
        create_new_save(args.save_name)

    elif args.command == "continue":
        continue_save(args.save_name)

    elif args.command == "budget":
        try:
            budget = get_current_enemy_budget(args.save_name)
            print(budget)

        except FileNotFoundError:
            print("Save not found.")
            raise SystemExit(1)


if __name__ == "__main__":
    main()
