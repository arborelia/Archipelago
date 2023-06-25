from operator import itemgetter
import random
import json

START_MAP = "A Community World"
START_MAP_AUTHOR = "MatePotato"

# official maps with 50k+ locations, in popularity order.
# 4 of these will be selected: 2 from the top 10 and 2 from the rest.
# Consider these to be difficulty 4.

regional_maps = [
    "United States",
    "Japan",
    "United Kingdom",
    "France",
    "Spain",
    "Russia",
    "Italy",
    "Netherlands",
    "Brazil",
    "Germany",
    "Poland",
    "Turkey",
    "Sweden",
    "Norway",
    "Argentina",
    "Ukraine",
    "Switzerland",
    "New Zealand",
    "Portugal",
    "Finland",
    "Denmark",
    "Indonesia",
    "Ireland",
    "Romania",
    "Belgium",
    "Serbia",
    "Mexico",
    "Greece",
    "Paris",
    "Bulgaria",
    "Chile",
    "Croatia",
    "Czech Republic",
    "Hungary",
    "Israel",
    "Austria",
    "Slovakia",
    "Colombia",
    "Taiwan",
    "Philippines",
    "Singapore",
    "Lithuania",
    "Estonia",
    "South Africa",
    "Slovenia",
    "South Korea",
    "Iceland",
    "Latvia",
    "Thailand",
    "Malaysia",
    "Peru",
    "Ecuador",
    "Uruguay",
    "Mongolia",
    "Botswana",
    "Sri Lanka",
]

# Choose 20 of these
user_maps = [
    {
        "name": "An Amaizing World of Corn",
        "author": "Cinnamonique",
        "streakable": True,
    },
    {
        "name": "An Arbitrary Asia",
        "author": "slashP",
        "difficulty": 4,
        "streakable": True,
    },
    {
        "name": "An Arbitrary Africa",
        "author": "slashP",
        "streakable": True,
    },
    {
        "name": "An Arbitrary Oceania",
        "author": "slashP",
        "difficulty": 4,
        "streakable": True,
    },
    {
        "name": "An Arbitrary South America",
        "author": "slashP",
        "streakable": True,
    },
    {
        "name": "An Arbitrary Europe",
        "author": "slashP",
        "streakable": True,
    },
    {
        "name": "A Balanced Canada",
        "author": "slashP",
    },
    {
        "name": "A Balanced Urban World",
        "author": "TunaJoe74",
        "difficulty": 2,
        "streakable": True,
    },
    {
        "name": "Aesthetic World",
        "author": "baszmania",
        "unofficial": True,
    },
    {
        "name": "A Linguistic World",
        "author": "nuujaku",
        "difficulty": 2,
        "streakable": True,
    },
    {
        "name": "All about the North",
        "author": "Frímann Stefánsson",
        "difficulty": 4,
        "streakable": True,
    },
    {
        "name": "A Mural World",
        "author": "Hugo",
        "streakable": True,
    },
    {
        "name": "An Extraordinary Cow",
        "author": "KingMoo92",
        "streakable": True,
    },
    {
        "name": "An Extraordinary World",
        "author": "Alok",
        "unofficial": True,
        "difficulty": 4,
    },
    {
        "name": "An Improved World",
        "author": "Wolftrekker",
        "streakable": True,
    },
    {
        "name": "A Metaful World",
        "author": "Zem",
        "difficulty": 2,
        "streakable": True,
    },
    {
        "name": "A Thrilling World",
        "author": "Zem",
        "difficulty": 2,
        "streakable": True,
    },
    {
        "name": "Animals of the World",
        "author": "Rhiannonfuller",
        "streakable": True,
    },
    {
        "name": "An Unexplored World",
        "difficulty": 5,
        "pinpointable": True,
        "unofficial": True,
    },
    {
        "name": "A Pinpointable World",
        "difficulty": 1,
        "pinpointable": True,
        "streakable": True,
    },
    {
        "name": "A Rural World",
        "author": "Topotic",
        "difficulty": 4,
        "streakable": True,
    },
    {
        "name": "A Speedrun World",
        "author": "Scribbles",
        "difficulty": 1,
        "pinpointable": True,
        "streakable": True,
    },
    {
        "name": "A Drone World",
        "author": "Armire",
        "unofficial": True,
        "satellite": True,
    },
    {
        "name": "Border Control",
        "author": "0321654",
        "difficulty": 2,
        "streakable": True,
    },
    {
        "name": "CityGuessr",
        "author": "BOKSA",
        "difficulty": 2,
        "streakable": True,
    },
    {
        "name": "Tokyo Metropolis",
        "author": "Phrost",
    },
    {
        "name": "City Skylines",
        "author": "Radu C",
        "streakable": True,
    },
    {
        "name": "Coastal Cities 100K+",
        "author": "Scribbles",
        "streakable": True,
    },
    {
        "name": "Dads of the World",
        "author": "Arsemann",
        "unofficial": True,
        "streakable": True,
    },
    {
        "name": "DistanceGuessr",
        "author": "Scribbles",
        "difficulty": 2,
        "streakable": True,
    },
    {
        "name": "European Diversity",
        "author": "Biquette",
        "streakable": True,
    },
    {
        "name": "Fun with Flags",
        "author": "Cinnamonique",
        "unofficial": True,
        "streakable": True,
    },
    {
        "name": "GeoDetective Africa",
        "author": "Hamfrags",
        "difficulty": 2,
        "unofficial": True,
        "pinpointable": True,
        "streakable": True,
    },
    {
        "name": "GeoDetective",
        "author": "Geography Challenges (YouTube)",
        "difficulty": 1,
        "unofficial": True,
        "pinpointable": True,
        "streakable": True,
    },
    {
        "name": "GeoDetective World",
        "author": "A little Eileen",
        "difficulty": 1,
        "unofficial": True,
        "pinpointable": True,
        "streakable": True,
    },
    {
        "name": "Detective Japan",
        "author": "工藤新一",
        "difficulty": 2,
    },
    {
        "name": "GeoGuessr in 2069",
        "author": "J I G E N",
        "difficulty": 4,
        "unofficial": True,
        "streakable": True,
    },
    {
        "name": "I Like Trains",
        "author": "baszmania",
        "difficulty": 2,
        "streakable": True,
    },
    {
        "name": "Intersectionguessr North America",
        "author": "PastequeHachee",
        "difficulty": 2,
        "streakable": True,
    },
    {
        "name": "Lakes of the World",
        "author": "Alok",
        "unofficial": True,
    },
    {
        "name": "La Diversite Francaise",
        "author": "La Commu GeoFrance",
        "difficulty": 4,
    },
    {
        "name": "Latin America (Balanced Distribution)",
        "author": "Radu C",
        "streakable": True,
    },
    {
        "name": "Living the Island Life",
        "author": "MagePower",
        "unofficial": True,
    },
    {
        "name": "Look at dem mountains tho",
        "author": "傻乎乎",
        "streakable": True,
    },
    {
        "name": "McDonald's Worldwide",
        "author": "aurahack",
        "difficulty": 2,
        "streakable": True,
    },
    {
        "name": "New York City",
        "author": "GeoGuessr",
    },
    {
        "name": "A Better Nordics Map",
        "author": "ChristofferDH",
        "streakable": True,
    },
    {
        "name": "Regionguessing",
        "author": "Steve",
        "difficulty": 4,
        "streakable": True,
    },
    {
        "name": "An Arbitrary Southeast Asia",
        "author": "John Harvey Kellogg",
        "difficulty": 4,
        "streakable": True,
    },
    {
        "name": "Southwest and Central Asia",
        "author": "Tanderson",
        "difficulty": 5,
        "streakable": True,
    },
    {
        "name": "UNESCO World Heritage Sites",
        "author": "Simi",
        "difficulty": 2,
        "streakable": True,
    },
    {
        "name": "Default world map",
        "author": "GeoGuessr",
        "streakable": True,
    },
    {
        "name": "World Cities (Bing Satellite)",
        "author": "[SIMBA] Jupaoqq",
        "unofficial": True,
    },
]

# There are 100 points-based unlocks and 3 extras
non_map_items = [
    {
        "name": "Progressive Pan/Zoom/Move",
        "progression": True,
        "count": 3,
        "category": ["Features"],
    },
    {
        "name": "Progressive Compass/Car",
        "progression": True,
        "count": 2,
        "category": ["Features"],
    },
    {"name": "Terrain Map View", "progression": True, "category": ["Features"]},
    {"name": "Satellite Map View", "progression": True, "category": ["Features"]},
    {"name": "OpenStreetMap View", "useful": True, "category": ["Features"]},
    {"name": "Time machine", "useful": True, "category": ["Features"]},
    {"name": "Map Score +1000", "useful": True, "count": 10, "category": ["Boosts"]},
    {
        "name": "Map Score +5000",
        "useful": True,
        "count": 5,
        "progression": True,
        "category": ["Boosts"],
    },
    {"name": "More Time", "progression": True, "count": 31, "category": ["Features"]},
    {"name": "Fix 1 point", "useful": True, "count": 3, "category": ["Boosts"]},
    {"name": "20 Second Timer Trap", "count": 3, "trap": True, "category": ["Traps"]},
    {"name": "Mosaic Trap", "count": 2, "trap": True, "category": ["Traps"]},
    {"name": "Watercolor Map Trap", "count": 2, "trap": True, "category": ["Traps"]},
    {"name": "Death Metal Map Trap", "count": 2, "trap": True, "category": ["Traps"]},
    {"name": "Labelless Trap", "count": 2, "trap": True, "category": ["Traps"]},
    {
        "name": "Mega Plonk Trap",
        "count": 1,
        "trap": True,
        "category": ["Traps"],
        # all the remaining items will be this too
    },
    {"name": "Space Plonk Trap", "count": 2, "trap": True, "category": ["Traps"]},
]

non_map_goals = [
    {
        "name": "Perfect score on 1 map",
        "requires": [
            "Progressive Compass/Car",
            "Progressive Pan/Zoom/Move:3",
            "More Time:15",
        ],
    },
    {
        "name": "Perfect score on 2 maps",
        "requires": [
            "Progressive Compass/Car",
            "Progressive Pan/Zoom/Move:3",
            "More Time:21",
            "Satellite Map View",
        ],
    },
    {
        "name": "Perfect score on 3 maps",
        "requires": [
            "Progressive Compass/Car:2",
            "Progressive Pan/Zoom/Move:3",
            "More Time:30",
            "Terrain Map View",
            "Satellite Map View",
        ],
        "victory": True,
    },
    {
        "name": "Confetti #1",
        "requires": [
            "Progressive Compass/Car",
            "Progressive Pan/Zoom/Move:2",
            "More Time:3",
        ],
    },
    {
        "name": "Confetti #2",
        "requires": [
            "Progressive Compass/Car",
            "Progressive Pan/Zoom/Move:2",
            "More Time:6",
        ],
    },
    {
        "name": "Confetti #3",
        "requires": [
            "Progressive Compass/Car",
            "Progressive Pan/Zoom/Move:2",
            "More Time:9",
        ],
    },
    {
        "name": "Confetti #4",
        "requires": [
            "Progressive Compass/Car",
            "Progressive Pan/Zoom/Move:2",
            "More Time:12",
        ],
    },
    {
        "name": "Confetti #5",
        "requires": [
            "Progressive Compass/Car",
            "Progressive Pan/Zoom/Move:2",
            "More Time:15",
        ],
    },
]


base_difficulty = {"5k": 1, "10k": 2, "15k": 3, "20k": 5, "5 streak": 5}


def make_json():
    selected_maps = [
        {"name": START_MAP, "author": START_MAP_AUTHOR, "streakable": True},
    ]
    for mapname in random.sample(regional_maps[:10], 2) + random.sample(
        regional_maps[10:], 2
    ):
        mapdata = {"name": mapname, "author": "GeoGuessr", "difficulty": 4}
        selected_maps.append(mapdata)

    for mapdata in random.sample(user_maps, 16):
        selected_maps.append(mapdata)

    selected_maps.sort(key=itemgetter("name"))

    locations = non_map_goals[:]
    items = non_map_items[:]
    regions = {}
    for mapdata in selected_maps:
        mapname = mapdata["name"]
        items.append({"name": mapname, "progression": True, "category": ["Maps"]})
        region_info = {"requires": [mapname]}
        if mapname == START_MAP:
            region_info["starting"] = True
        goals = ["5k", "10k", "15k", "20k"]
        if mapdata.get("streakable"):
            goals.append("5 streak")
        for goal in goals:
            requires = [mapname]
            difficulty = base_difficulty[goal] + mapdata.get("difficulty", 3)
            if difficulty >= 9:
                requires.append("Progressive Pan/Zoom/Move:3")
                requires.append("Progressive Compass/Car:2")
                requires.append("More Time:10")
                requires.append("Satellite Map View")
                requires.append("Map Score +5000:2")
            elif difficulty >= 8:
                requires.append("Progressive Pan/Zoom/Move:2")
                requires.append("Progressive Compass/Car")
                requires.append("More Time:8")
                requires.append("Terrain Map View")
                requires.append("Map Score +5000")
            elif difficulty >= 7:
                requires.append("Progressive Pan/Zoom/Move")
                requires.append("Progressive Compass/Car")
                requires.append("More Time:5")
                requires.append("Map Score +5000")
            elif difficulty >= 6:
                requires.append("Progressive Pan/Zoom/Move")
                requires.append("Progressive Compass/Car")
                requires.append("More Time:3")
            elif difficulty >= 5:
                requires.append("Progressive Compass/Car")
                requires.append("More Time:2")
            elif difficulty >= 4:
                requires.append("More Time:1")
            locations.append(
                {
                    "name": f"{mapname} {goal}",
                    "requires": requires,
                    "category": [mapname],
                }
            )

    with open("data/items.json", "w") as out:
        print(json.dumps(items, indent=4), file=out)

    with open("data/locations.json", "w") as out:
        print(json.dumps(locations, indent=4), file=out)

    with open("data/regions.json", "w") as out:
        print(json.dumps(regions, indent=4), file=out)

    possible_start_maps = [
        map["name"] for map in selected_maps if map["name"] != START_MAP
    ]
    start_inventory = [random.choice(possible_start_maps), START_MAP, "More Time"]
    start_inventory_lines = "\n".join(f"    {item!r}: 1" for item in start_inventory)

    yaml_out = f"""
Manual_GeoGuessr_arborelia:
  progression_balancing: 50
  accessibility: items

  start_inventory:
{start_inventory_lines}

description: 'Generated by https://archipelago.gg/'
game: Manual_GeoGuessr_arborelia
name: Where's Elia
"""
    with open("data/GeoGuessr.yaml", "w") as out:
        print(yaml_out, file=out)


if __name__ == "__main__":
    make_json()
