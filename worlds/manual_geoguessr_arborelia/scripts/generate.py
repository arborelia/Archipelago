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
    },
    {
        "name": "An Arbitrary Asia",
        "author": "slashP",
        "difficulty": 4,
    },
    {
        "name": "An Arbitrary Africa",
        "author": "slashP",
    },
    {
        "name": "An Arbitrary Oceania",
        "author": "slashP",
        "difficulty": 4,
    },
    {
        "name": "An Arbitrary South America",
        "author": "slashP",
    },
    {
        "name": "An Arbitrary Europe",
        "author": "slashP",
    },
    {
        "name": "A Balanced Canada",
        "author": "slashP",
    },
    {
        "name": "A Balanced Urban World",
        "author": "TunaJoe74",
        "difficulty": 2,
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
    },
    {
        "name": "All about the North",
        "author": "Frímann Stefánsson",
        "difficulty": 4,
    },
    {
        "name": "A Mural World",
        "author": "Hugo",
    },
    {
        "name": "An Extraordinary Cow",
        "author": "KingMoo92",
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
    },
    {
        "name": "A Metaful World",
        "author": "Zem",
        "difficulty": 2,
    },
    {
        "name": "A Thrilling World",
        "author": "Zem",
        "difficulty": 2,
    },
    {
        "name": "Animals of the World",
        "author": "Rhiannonfuller",
    },
    {
        "name": "An Unexplored World",
        "difficulty": 5,
        "pinpointable": True,
    },
    {
        "name": "A Pinpointable World",
        "difficulty": 1,
        "pinpointable": True,
    },
    {
        "name": "A Rural World",
        "author": "Topotic",
        "difficulty": 4,
    },
    {
        "name": "A Speedrun World",
        "author": "Scribbles",
        "difficulty": 1,
        "pinpointable": True,
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
    },
    {
        "name": "CityGuessr",
        "author": "BOKSA",
        "difficulty": 2,
    },
    {
        "name": "Tokyo Metropolis",
        "author": "Phrost",
    },
    {
        "name": "City Skylines",
        "author": "Radu C",
    },
    {
        "name": "Coastal Cities 100K+",
        "author": "Scribbles",
    },
    {
        "name": "Dads of the World",
        "author": "Arsemann",
        "unofficial": True,
    },
    {
        "name": "DistanceGuessr",
        "author": "Scribbles",
        "difficulty": 2,
    },
    {
        "name": "European Diversity",
        "author": "Biquette",
    },
    {
        "name": "Fun with Flags",
        "author": "Cinnamonique",
        "unofficial": True,
    },
    {
        "name": "GeoDetective Africa",
        "author": "Hamfrags",
        "difficulty": 2,
        "unofficial": True,
        "pinpointable": True,
    },
    {
        "name": "GeoDetective",
        "author": "Geography Challenges (YouTube)",
        "difficulty": 1,
        "unofficial": True,
        "pinpointable": True,
    },
    {
        "name": "GeoDetective World",
        "author": "A little Eileen",
        "difficulty": 1,
        "unofficial": True,
        "pinpointable": True,
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
    },
    {
        "name": "I Like Trains",
        "author": "baszmania",
        "difficulty": 2,
    },
    {
        "name": "Intersectionguessr North America",
        "author": "PastequeHachee",
        "difficulty": 2,
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
    },
    {
        "name": "Living the Island Life",
        "author": "MagePower",
        "unofficial": True,
    },
    {
        "name": "Look at dem mountains tho",
        "author": "傻乎乎",
    },
    {
        "name": "McDonald's Worldwide",
        "author": "aurahack",
        "difficulty": 2,
    },
    {
        "name": "New York City",
        "author": "GeoGuessr",
    },
    {
        "name": "A Better Nordics Map",
        "author": "ChristofferDH",
    },
    {
        "name": "Regionguessing",
        "author": "Steve",
        "difficulty": 4,
    },
    {
        "name": "An Arbitrary Southeast Asia",
        "author": "John Harvey Kellogg",
        "difficulty": 4,
    },
    {
        "name": "Southwest and Central Asia",
        "author": "Tanderson",
        "difficulty": 5,
    },
    {
        "name": "UNESCO World Heritage Sites",
        "author": "Simi",
        "difficulty": 2,
    },
    {
        "name": "Default world map",
        "author": "GeoGuessr",
    },
    {
        "name": "World Cities (Bing Satellite)",
        "author": "[SIMBA] Jupaoqq",
        "unofficial": True,
    },
]

# There are 100 points-based unlocks and 3 extras
non_map_items = [
    {"name": "Progressive Pan/Zoom/Move", "progression": True, "count": 3},
    {"name": "Progressive Compass/Car", "progression": True, "count": 2},
    {"name": "Terrain Map View", "progression": True},
    {"name": "Satellite Map View", "progression": True},
    {"name": "OpenStreetMap View", "useful": True},
    {"name": "Time machine", "useful": True},
    {"name": "Map Score +1000", "useful": True, "count": 10},
    {"name": "Map Score +5000", "useful": True, "count": 5, "progression": True},
    {"name": "More Time", "progression": True, "count": 31},
    {"name": "Count 24999 as perfect", "useful": True, "count": 3},
    {"name": "20 Second Timer Trap", "count": 3, "trap": True},
    {"name": "Mosaic Trap", "count": 2, "trap": True},
    {"name": "Watercolor Map Trap", "count": 2, "trap": True},
    {"name": "Death Metal Map Trap", "count": 2, "trap": True},
    {"name": "Labelless Trap", "count": 3, "trap": True},
    {
        "name": "Mega Plonk Trap",
        "count": 1,
        "trap": True
        # all the remaining items will be this too
    },
    {"name": "Space Plonk Trap", "count": 3, "trap": True},
]

non_map_goals = [
    {
        "name": "Perfect score on 1 map",
        "requires": [
            "Progressive Compass/Car",
            "Progressive Pan/Zoom/Move:3",
            "More Time:15",
        ],
        "category": ["Anywhere"],
    },
    {
        "name": "Perfect score on 2 maps",
        "requires": [
            "Progressive Compass/Car",
            "Progressive Pan/Zoom/Move:3",
            "More Time:21",
            "Satellite Map View",
        ],
        "category": ["Anywhere"],
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
        "category": ["Anywhere"],
    },
    {
        "name": "Confetti #1",
        "requires": ["Progressive Compass/Car", "Progressive Pan/Zoom/Move:2"],
        "category": ["Anywhere"],
    },
    {
        "name": "Confetti #2",
        "requires": ["Progressive Compass/Car", "Progressive Pan/Zoom/Move:2"],
        "category": ["Anywhere"],
    },
    {
        "name": "Confetti #3",
        "requires": ["Progressive Compass/Car", "Progressive Pan/Zoom/Move:2"],
        "category": ["Anywhere"],
    },
    {
        "name": "Confetti #4",
        "requires": ["Progressive Compass/Car", "Progressive Pan/Zoom/Move:2"],
        "category": ["Anywhere"],
    },
    {
        "name": "Confetti #5",
        "requires": ["Progressive Compass/Car", "Progressive Pan/Zoom/Move:2"],
        "category": ["Anywhere"],
    },
    {
        "name": "World 5 Country Streak",
        "requires": [
            "Progressive Compass/Car",
            "Progressive Pan/Zoom/Move",
            "More Time:5",
        ],
        "category": ["Anywhere"],
    },
    {
        "name": "World 10 Country Streak",
        "requires": [
            "Progressive Compass/Car",
            "Progressive Pan/Zoom/Move:2",
            "More Time:10",
        ],
        "category": ["Anywhere"],
    },
]


base_difficulty = {"5k": 1, "10k": 2, "15k": 3, "20k": 5}


def make_json():
    selected_maps = [
        {"name": START_MAP, "author": START_MAP_AUTHOR},
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
        items.append({"name": mapname, "progression": True})
        region_info = {"requires": [mapname]}
        if mapname == START_MAP:
            region_info["starting"] = True
        # don't write regions until we figure them out
        # regions[mapname] = region_info
        for goal in ["5k", "10k", "15k", "20k"]:
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