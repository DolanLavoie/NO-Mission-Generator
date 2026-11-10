import json
import random
from decimal import Decimal, InvalidOperation
from pathlib import Path


# Change this to choose where the RandomMission folder is created.
# By default, it is created beside this Python script.
OUTPUT_PATH = Path(__file__).resolve().parent

MISSION_FOLDER_NAME = "RandomMission"
MISSION_FILE_NAME = "RandomMission.json"
META_FILE_NAME = "meta.json"

# Aircraft prices are in millions.
AIRCRAFT = [
    {"name": "MiG-15", "price": Decimal("2.5"), "size": "Small", "key": "Aryx_MiG-15"},
    {"name": "Cricket", "price": Decimal("11.5"), "size": "Small", "key": "COIN"},
    {
        "name": "Cavalier",
        "price": Decimal("12.0"),
        "size": "Small",
        "key": "Aryx_PropAttacker1",
    },
    {
        "name": "Knockout",
        "price": Decimal("16.0"),
        "size": "Small",
        "key": "Aryx_LightHelicopter1",
    },
    {"name": "Compass", "price": Decimal("21.8"), "size": "Small", "key": "trainer"},
    {"name": "Kukri", "price": Decimal("24.0"), "size": "Small", "key": "AH31_Kukri"},
    {
        "name": "Vagrant",
        "price": Decimal("28.9"),
        "size": "Small",
        "key": "VTOLTrainer1",
    },
    {"name": "Ibis", "price": Decimal("29.5"), "size": "Small", "key": "UtilityHelo1"},
    {
        "name": "Chicane",
        "price": Decimal("31.0"),
        "size": "Small",
        "key": "AttackHelo1",
    },
    {
        "name": "Shrike",
        "price": Decimal("35.0"),
        "size": "Small",
        "key": "Aryx_LightFighter1",
    },
    {"name": "Brawler", "price": Decimal("36.0"), "size": "Small", "key": "CAS1"},
    {"name": "Kestrel", "price": Decimal("47.0"), "size": "Small", "key": "kestrel"},
    {
        "name": "Tarantula",
        "price": Decimal("118.0"),
        "size": "Small",
        "key": "QuadVTOL1",
    },
    {
        "name": "King Viper",
        "price": Decimal("58.0"),
        "size": "Small",
        "key": "Aryx_F16M_KingViper",
    },
    {
        "name": "Agni",
        "price": Decimal("62.5"),
        "size": "Medium",
        "key": "1509_palafighter1",
    },
    {"name": "Revoker", "price": Decimal("65.0"), "size": "Medium", "key": "Fighter1"},
    {
        "name": "Vortex",
        "price": Decimal("90.0"),
        "size": "Medium",
        "key": "SmallFighter1",
    },
    {"name": "Ifrit", "price": Decimal("126.0"), "size": "Medium", "key": "Multirole1"},
    {
        "name": "Ternion",
        "price": Decimal("136.0"),
        "size": "Large",
        "key": "P_Trisurface1",
    },
    {"name": "Medusa", "price": Decimal("145.0"), "size": "Large", "key": "EW1"},
    {
        "name": "Chimera",
        "price": Decimal("160.0"),
        "size": "Large",
        "key": "Aryx_CargoPlane1",
    },
    {
        "name": "Strike Raptor",
        "price": Decimal("200.0"),
        "size": "Large",
        "key": "Aryx_F22E_StrikeRaptor",
    },
    {
        "name": "Darkreach",
        "price": Decimal("225.0"),
        "size": "Large",
        "key": "Darkreach",
    },
    {
        "name": "Eclipse",
        "price": Decimal("270.0"),
        "size": "Medium",
        "key": "Aryx_Interceptor1",
    },
    {
        "name": "Alkyon",
        "price": Decimal("390.0"),
        "size": "Large",
        "key": "FastBomber1",
    },
]

# Airbase data copied from the supplied mission.
AIRBASES = [
    {
        "IsOverride": True,
        "faction": "Boscali",
        "UniqueName": "North Boscali Airbase",
        "DisplayName": "North Boscali Airbase",
        "Disabled": False,
        "Capturable": True,
        "CaptureDefense": 10.0,
        "CaptureRange": 1561.0,
        "Center": {"x": -18632.0, "y": 138.76001, "z": 32049.0},
        "SelectionPosition": {"x": -18550.0, "y": 137.057, "z": 32192.7},
        "Tower": "<MAP_UNIT>++controlTower1",
        "VerticalLandingPoints": [],
        "ServicePoints": [],
        "roads": {"roads": []},
        "runways": [],
        "_size": "Large",
    },
    {
        "IsOverride": True,
        "faction": "Primeva",
        "UniqueName": "South Boscali General Aviation",
        "DisplayName": "South Boscali General Aviation",
        "Disabled": False,
        "Capturable": True,
        "CaptureDefense": 10.0,
        "CaptureRange": 900.0,
        "Center": {"x": -9895.2, "y": 136.6, "z": -6309.6},
        "SelectionPosition": {"x": -10265.02, "y": 136.43, "z": -6532.09},
        "Tower": "",
        "VerticalLandingPoints": [],
        "ServicePoints": [],
        "roads": {"roads": []},
        "runways": [],
        "_size": "Small",
    },
    {
        "IsOverride": True,
        "faction": "Boscali",
        "UniqueName": "Vigil Cay Naval Airbase",
        "DisplayName": "Vigil Cay Naval Airbase",
        "Disabled": False,
        "Capturable": True,
        "CaptureDefense": 10.0,
        "CaptureRange": 1332.0,
        "Center": {"x": -33994.5, "y": 18.3999939, "z": -12111.0},
        "SelectionPosition": {"x": -34213.5664, "y": 19.985, "z": -12459.1035},
        "Tower": "<MAP_UNIT>++controlTower1_4",
        "VerticalLandingPoints": [],
        "ServicePoints": [],
        "roads": {"roads": []},
        "runways": [],
        "_size": "Large",
    },
    {
        "IsOverride": True,
        "faction": "Primeva",
        "UniqueName": "Agrapol Airbase",
        "DisplayName": "Agrapol Airbase",
        "Disabled": False,
        "Capturable": True,
        "CaptureDefense": 10.0,
        "CaptureRange": 1463.0,
        "Center": {"x": -1131.0, "y": 137.6, "z": -26845.0},
        "SelectionPosition": {"x": -1024.9, "y": 139.414, "z": -27258.9},
        "Tower": "<MAP_UNIT>++controlTower1_2",
        "VerticalLandingPoints": [],
        "ServicePoints": [],
        "roads": {"roads": []},
        "runways": [],
        "_size": "Large",
    },
    {
        "IsOverride": True,
        "faction": "Boscali",
        "UniqueName": "Sandrift Airbase",
        "DisplayName": "Sandrift Airbase",
        "Disabled": False,
        "Capturable": True,
        "CaptureDefense": 10.0,
        "CaptureRange": 975.0,
        "Center": {"x": 27807.69, "y": 135.47345, "z": -18910.1543},
        "SelectionPosition": {"x": 27574.4785, "y": 135.432465, "z": -19351.6035},
        "Tower": "<MAP_UNIT>++controlTower1_3",
        "VerticalLandingPoints": [],
        "ServicePoints": [],
        "roads": {"roads": []},
        "runways": [],
        "_size": "Medium",
    },
    {
        "IsOverride": True,
        "faction": "Primeva",
        "UniqueName": "Maris Airport",
        "DisplayName": "Maris Airport",
        "Disabled": False,
        "Capturable": True,
        "CaptureDefense": 10.0,
        "CaptureRange": 1473.0,
        "Center": {"x": 13045.3, "y": 136.400757, "z": 19568.5},
        "SelectionPosition": {"x": 12654.53, "y": 137.221832, "z": 19062.91},
        "Tower": "<MAP_UNIT>++controlTower1_1",
        "VerticalLandingPoints": [],
        "ServicePoints": [],
        "roads": {"roads": []},
        "runways": [],
        "_size": "Large",
    },
    {
        "IsOverride": True,
        "faction": "Boscali",
        "UniqueName": "K92 Highway Strip",
        "DisplayName": "K92 Highway Strip",
        "Disabled": False,
        "Capturable": True,
        "CaptureDefense": 10.0,
        "CaptureRange": 746.0,
        "Center": {"x": 18756.0, "y": 136.159943, "z": 12406.0},
        "SelectionPosition": {"x": 18943.8867, "y": 132.814972, "z": 12574.958},
        "Tower": "",
        "VerticalLandingPoints": [],
        "ServicePoints": [],
        "roads": {"roads": []},
        "runways": [],
        "_size": "Small",
    },
    {
        "IsOverride": True,
        "faction": "Primeva",
        "UniqueName": "Dustbowl Highway Strip",
        "DisplayName": "Dustbowl Highway Strip",
        "Disabled": False,
        "Capturable": True,
        "CaptureDefense": 10.0,
        "CaptureRange": 746.0,
        "Center": {"x": 13326.0, "y": 146.120026, "z": -7450.0},
        "SelectionPosition": {"x": 13351.44, "y": 145.872009, "z": -7709.05},
        "Tower": "",
        "VerticalLandingPoints": [],
        "ServicePoints": [],
        "roads": {"roads": []},
        "runways": [],
        "_size": "Small",
    },
]

MISSION_TEMPLATE = {
    "JsonVersion": 6,
    "MapKey": {"Type": "GameWorldPrefab", "Path": "Terrain1"},
    "missionSettings": {
        "description": "",
        "allowEventContent": False,
        "Tags": [],
        "playerMode": "SingleAndMultiplayer",
        "allowRespawn": True,
        "playerStartingRank": 6,
        "rankMultiplier": 1.0,
        "successfulSortieBonus": 0.25,
        "nuclearEscalationThreshold": 0.0,
        "strategicEscalationThreshold": 0.0,
        "minRankTacticalWarhead": 0,
        "minRankStrategicWarhead": 0,
        "cameraStartPosition": {
            "IsOverride": False,
            "Value": {
                "Position": {"x": 0.0, "y": 0.0, "z": 0.0},
                "Rotation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 0.0},
            },
        },
        "missionRoads": {"roads": []},
        "missionSeaLanes": {"roads": []},
        "wrecksMaxNumber": 10,
        "wrecksDecayTime": 1.0,
    },
    "environment": {
        "timeOfDay": 10.0,
        "timeFactor": 0.0,
        "weatherIntensity": 0.0,
        "cloudAltitude": 1800.0,
        "windSpeed": 0.0,
        "windTurbulence": 0.0,
        "windHeading": 0.0,
        "windRandomHeading": 0.0,
        "moonPhase": 14.0,
    },
    "aircraft": [],
    "vehicles": [],
    "ships": [],
    "buildings": [],
    "scenery": [],
    "containers": [],
    "missiles": [],
    "pilots": [],
    "factions": [
        {
            "factionName": "Boscali",
            "preventJoin": False,
            "preventDonation": False,
            "supplies": [],
            "startingBalance": 0.0,
            "playerJoinAllowance": 1225.0,
            "playerTaxRate": 0.2,
            "regularIncome": 5.0,
            "excessFundsDistributePercent": 0.25,
            "killReward": 1.0,
            "airSkillMultiplier": 2.0,
            "surfaceSkillMultiplier": 2.0,
            "startingWarheads": 0,
            "reserveWarheads": 0,
            "reserveAirframes": 0,
            "extraReservesPerPlayer": 1,
            "AIAircraftLimit": 16,
            "reduceAIPerFriendlyPlayer": 1.0,
            "addAIPerEnemyPlayer": 1.0,
            "cameraStartPosition": {
                "IsOverride": False,
                "Value": {
                    "Position": {"x": 0.0, "y": 0.0, "z": 0.0},
                    "Rotation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 0.0},
                },
            },
        },
        {
            "factionName": "Primeva",
            "preventJoin": True,
            "preventDonation": False,
            "supplies": [
                {"UnitType": "COIN", "Count": 2},
                {"UnitType": "trainer", "Count": 1},
            ],
            "startingBalance": 0.0,
            "playerJoinAllowance": 1225.0,
            "playerTaxRate": 0.2,
            "regularIncome": 5.0,
            "excessFundsDistributePercent": 0.25,
            "killReward": 1.0,
            "airSkillMultiplier": 2.0,
            "surfaceSkillMultiplier": 2.0,
            "startingWarheads": 0,
            "reserveWarheads": 0,
            "reserveAirframes": 0,
            "extraReservesPerPlayer": 1,
            "AIAircraftLimit": 16,
            "reduceAIPerFriendlyPlayer": 1.0,
            "addAIPerEnemyPlayer": 1.0,
            "cameraStartPosition": {
                "IsOverride": False,
                "Value": {
                    "Position": {"x": 0.0, "y": 0.0, "z": 0.0},
                    "Rotation": {"x": 0.0, "y": 0.0, "z": 0.0, "w": 0.0},
                },
            },
        },
    ],
    "airbases": [],
    "objectives": [
        {
            "Type": "None",
            "UniqueName": "Mission Start",
            "Faction": "",
            "DisplayName": "Mission Start",
            "Hidden": True,
            "Outcomes": ["StartObjective"],
        },
        {
            "Type": "CaptureAirbase",
            "UniqueName": "CaptureAirbase",
            "Faction": "Boscali",
            "DisplayName": "CaptureAirbase",
            "Hidden": False,
            "Outcomes": ["EndGame_1"],
            "completeOrder": "CompleteAny",
            "completeSomePercent": 0.0,
            "targetAirbases": ["South Boscali General Aviation"],
        },
        {
            "Type": "CaptureAirbase",
            "UniqueName": "CaptureAirbase_1",
            "Faction": "Primeva",
            "DisplayName": "CaptureAirbase",
            "Hidden": False,
            "Outcomes": ["EndGame"],
            "completeOrder": "CompleteAny",
            "completeSomePercent": 0.0,
            "targetAirbases": ["North Boscali Airbase"],
        },
    ],
    "outcomes": [
        {
            "Type": "EndGame",
            "UniqueName": "EndGame",
            "endType": "Victory",
            "endDelay": 0.0,
        },
        {
            "Type": "EndGame",
            "UniqueName": "EndGame_1",
            "endType": "Victory",
            "endDelay": 0.0,
        },
        {
            "Type": "StartObjective",
            "UniqueName": "StartObjective",
            "objectivesToStart": ["CaptureAirbase", "CaptureAirbase_1"],
        },
    ],
}


def get_budget():
    """Read the enemy budget in millions."""
    while True:
        raw_budget = input("Enter the enemy budget (in millions): ").strip()

        try:
            budget = Decimal(raw_budget)
            if not budget.is_finite() or budget < 0:
                raise InvalidOperation
            return budget
        except InvalidOperation:
            print("Enter a valid non-negative number, such as 500 or 1250.5.")


def get_eligible_aircraft(airbase_size):
    """Return aircraft that can operate from the selected airbase size."""
    allowed_sizes = {
        "Small": {"Small"},
        "Medium": {"Small", "Medium"},
        "Large": {"Small", "Medium", "Large"},
    }
    return [
        aircraft
        for aircraft in AIRCRAFT
        if aircraft["size"] in allowed_sizes[airbase_size]
    ]


def purchase_aircraft(budget, airbase_size):
    """
    Randomly purchase aircraft until less than 10 million remains,
    or no eligible aircraft can be bought within the remaining budget.
    """
    remaining_budget = budget
    purchases = {}

    eligible_aircraft = get_eligible_aircraft(airbase_size)

    while remaining_budget >= Decimal("10.0"):
        affordable = [
            aircraft
            for aircraft in eligible_aircraft
            if aircraft["price"] <= remaining_budget
        ]

        if not affordable:
            break

        aircraft = random.choice(affordable)
        key = aircraft["key"]

        purchases[key] = purchases.get(key, 0) + 1
        remaining_budget -= aircraft["price"]

    supplies = [{"UnitType": key, "Count": count} for key, count in purchases.items()]

    return supplies, remaining_budget, purchases


def randomize_environment(environment):
    """Randomize the requested environment values to one decimal place."""
    environment["timeOfDay"] = round(random.uniform(0.0, 24.0), 1)
    environment["weatherIntensity"] = round(random.uniform(0.0, 1.0), 1)
    environment["cloudAltitude"] = round(random.uniform(500.0, 4000.0), 1)
    environment["windSpeed"] = round(random.uniform(0.0, 10.0), 1)
    environment["windTurbulence"] = round(random.uniform(0.0, 1.0), 1)
    environment["windHeading"] = round(random.uniform(0.0, 359.0), 1)
    environment["windRandomHeading"] = round(random.uniform(0.0, 180.0), 1)
    environment["moonPhase"] = round(random.uniform(0.0, 28.0), 1)


def generate_mission(budget, *, overwrite=True, verbose=True):
    """
    Generate a random mission for the given enemy budget (in millions).

    budget: numeric or Decimal enemy budget in millions.
    overwrite: when True, overwrite existing mission files without prompting.
               When False, prompt the user before overwriting.
    verbose: when True, print a summary of the generated mission.

    Returns True when a mission was written, False if it was cancelled.
    """
    budget = Decimal(str(budget))

    # Select a large airbase for the player.
    large_airbases = [base for base in AIRBASES if base["_size"] == "Large"]
    player_airbase = random.choice(large_airbases)

    # Select any different airbase for the enemy.
    enemy_candidates = [base for base in AIRBASES if base is not player_airbase]
    enemy_airbase = random.choice(enemy_candidates)

    # Copy only the selected airbases and assign their factions.
    selected_airbases = []
    for source_base, faction in (
        (player_airbase, "Boscali"),
        (enemy_airbase, "Primeva"),
    ):
        base = {key: value for key, value in source_base.items() if key != "_size"}
        base["faction"] = faction
        selected_airbases.append(base)

    mission = json.loads(json.dumps(MISSION_TEMPLATE))

    mission["airbases"] = selected_airbases
    randomize_environment(mission["environment"])

    # Keep all faction settings unchanged except Primeva's supplies.
    primeva = next(
        faction
        for faction in mission["factions"]
        if faction["factionName"] == "Primeva"
    )

    supplies, remaining_budget, purchases = purchase_aircraft(
        budget,
        enemy_airbase["_size"],
    )
    primeva["supplies"] = supplies

    # Make the objectives match the randomly selected airbases.
    objectives_by_name = {
        objective["UniqueName"]: objective for objective in mission["objectives"]
    }

    objectives_by_name["CaptureAirbase"]["targetAirbases"] = [
        enemy_airbase["UniqueName"]
    ]
    objectives_by_name["CaptureAirbase_1"]["targetAirbases"] = [
        player_airbase["UniqueName"]
    ]

    # Set the objective factions to match the selected bases.
    objectives_by_name["CaptureAirbase"]["Faction"] = "Boscali"
    objectives_by_name["CaptureAirbase_1"]["Faction"] = "Primeva"

    output_folder = Path(OUTPUT_PATH) / MISSION_FOLDER_NAME
    mission_path = output_folder / MISSION_FILE_NAME
    meta_path = output_folder / META_FILE_NAME

    if (
        not overwrite
        and output_folder.exists()
        and (mission_path.exists() or meta_path.exists())
    ):
        answer = (
            input(
                f"{output_folder} already contains mission files. Overwrite them? (y/n): "
            )
            .strip()
            .lower()
        )
        if answer != "y":
            print("Mission generation cancelled.")
            return False

    output_folder.mkdir(parents=True, exist_ok=True)

    with mission_path.open("w", encoding="utf-8") as file:
        json.dump(mission, file, indent=2)

    with meta_path.open("w", encoding="utf-8") as file:
        json.dump({"FileName": MISSION_FOLDER_NAME}, file, indent=2)

    total_spent = budget - remaining_budget

    if verbose:
        print("\nMission generated successfully.")
        print(f"Output folder: {output_folder}")
        print(f"Boscali airbase: {player_airbase['UniqueName']} (Large)")
        print(
            f"Primeva airbase: {enemy_airbase['UniqueName']} ({enemy_airbase['_size']})"
        )
        print(f"Enemy budget: ${budget} million")
        print(f"Aircraft spending: ${total_spent} million")
        print(f"Remaining budget: ${remaining_budget} million")
        print("\nPrimeva aircraft:")
        if supplies:
            for item in supplies:
                print(f"  {item['UnitType']}: {item['Count']}")
        else:
            print("  No aircraft purchased.")

    return True


def create_mission():
    """Interactive entry point: prompt for the budget, then generate a mission."""
    budget = get_budget()
    generate_mission(budget, overwrite=False, verbose=True)


if __name__ == "__main__":
    create_mission()
