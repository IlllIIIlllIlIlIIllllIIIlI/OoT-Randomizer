from __future__ import annotations
import sys
from collections import OrderedDict
from typing import Optional, TYPE_CHECKING

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    TypeAlias = str

LocationDefault: TypeAlias = "Optional[int | tuple[int, ...] | list[tuple[int, ...]]]"
LocationAddress: TypeAlias = "Optional[int | list[int]]"
LocationAddresses: TypeAlias = "Optional[tuple[LocationAddress, LocationAddress]]"
LocationFilterTags: TypeAlias = "Optional[tuple[str, ...] | str]"

if TYPE_CHECKING:
    from World import World


def shop_address(shop_id: int, shelf_id: int) -> int:
    return 0xC71ED0 + (0x40 * shop_id) + (0x08 * shelf_id)


#   Abbreviations
#       DMC     Death Mountain Crater
#       DMT     Death Mountain Trail
#       GC      Goron City
#       GF      Gerudo Fortress
#       GS      Gold Skulltula
#       GV      Gerudo Valley
#       HC      Hyrule Castle
#       HF      Hyrule Field
#       KF      Kokiri Forest
#       LH      Lake Hylia
#       LLR     Lon Lon Ranch
#       LW      Lost Woods
#       OGC     Outside Ganon's Castle
#       SFM     Sacred Forest Meadow
#       ToT     Temple of Time
#       ZD      Zora's Domain
#       ZF      Zora's Fountain
#       ZR      Zora's River

# The order of this table is reflected in the spoiler's list of locations (except Hints aren't included).
# Within a section, the order of types is: gifts/freestanding/chests, Deku Scrubs, Cows, Gold Skulltulas, Shops.

# Scrubs are on the overworld, while GrottoScrub is a special handler for Grottos
# Grottos scrubs are the same scene and actor, so we use a unique grotto ID for the scene

# Note that the scene for skulltulas is not the actual scene the token appears in
# Rather, it is the index of the grouping used when storing skulltula collection
# For example, zora river, zora's domain, and zora fountain are all a single 'scene' for skulltulas

# For pot/crate/freestanding locations, the Default variable contains a tuple of the format (Room ID, Scene Setup, Actor ID) where:
#   Room ID - The room index in the scene
#   Scene Setup - The scene setup that the location exists in. This is a number 0-3: 0=Child Day, 1=Child Night, 2=Adult Day, 3=Adult Night.
#   Actor ID - The position of the actor in the actor table.
# The default variable can also be a list of such tuples in the case that multiple scene setups contain the same locations to be shuffled together.

# Note: for ActorOverride locations, the "Addresses" variable is in the form ([addresses], [bytes]) where addresses is a list of memory locations in ROM to be updated, and bytes is the data that will be written to that location

#   Location:                                                        Type             Scene  Default Addresses                      Vanilla Item                             Categories
location_table: dict[
    str,
    tuple[
        str, Optional[int], LocationDefault, LocationAddresses, Optional[str], LocationFilterTags
    ],
] = OrderedDict(
    [
        ## Dungeon Rewards
        (
            "ToT Reward from Rauru",
            (
                "Cutscene",
                0xFF,
                0x04,
                None,
                "Light Medallion",
                (
                    "Temple of Time",
                    "NPCs",
                    "Dungeon Rewards",
                ),
            ),
        ),
        (
            "Queen Gohma",
            (
                "Boss",
                0x11,
                0x65,
                None,
                "Kokiri Emerald",
                (
                    "Deku Tree",
                    "Deku Tree MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Dungeon Rewards",
                ),
            ),
        ),
        (
            "King Dodongo",
            (
                "Boss",
                0x12,
                0x65,
                None,
                "Goron Ruby",
                (
                    "Dodongo's Cavern",
                    "Dodongo's Cavern MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Dungeon Rewards",
                ),
            ),
        ),
        (
            "Barinade",
            (
                "Boss",
                0x13,
                0x65,
                None,
                "Zora Sapphire",
                (
                    "Jabu Jabu's Belly",
                    "Jabu Jabu's Belly MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Dungeon Rewards",
                ),
            ),
        ),
        (
            "Phantom Ganon",
            (
                "Boss",
                0x14,
                0x65,
                None,
                "Forest Medallion",
                (
                    "Forest Temple",
                    "Forest Temple MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Dungeon Rewards",
                ),
            ),
        ),
        (
            "Volvagia",
            (
                "Boss",
                0x15,
                0x65,
                None,
                "Fire Medallion",
                (
                    "Fire Temple",
                    "Fire Temple MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Dungeon Rewards",
                ),
            ),
        ),
        (
            "Morpha",
            (
                "Boss",
                0x16,
                0x65,
                None,
                "Water Medallion",
                (
                    "Water Temple",
                    "Water Temple MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Dungeon Rewards",
                ),
            ),
        ),
        (
            "Bongo Bongo",
            (
                "Boss",
                0x18,
                0x65,
                None,
                "Shadow Medallion",
                (
                    "Shadow Temple",
                    "Shadow Temple MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Dungeon Rewards",
                ),
            ),
        ),
        (
            "Twinrova",
            (
                "Boss",
                0x17,
                0x65,
                None,
                "Spirit Medallion",
                (
                    "Spirit Temple",
                    "Spirit Temple MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Dungeon Rewards",
                ),
            ),
        ),
        ("Ganon", ("Event", None, None, None, "Triforce", None)),
        ("Gift from Sages", ("Cutscene", 0xFF, 0x03, None, None, None)),
        ## Songs
        (
            "Song from Impa",
            (
                "Song",
                0xFF,
                0x26,
                (0x2E8E925, 0x2E8E925),
                "Zeldas Lullaby",
                (
                    "Hyrule Castle",
                    "Songs",
                ),
            ),
        ),
        (
            "Song from Malon",
            (
                "Song",
                0xFF,
                0x27,
                (0x0D7EB53, 0x0D7EBCF),
                "Eponas Song",
                (
                    "Lon Lon Ranch",
                    "Songs",
                ),
            ),
        ),
        (
            "Song from Saria",
            (
                "Song",
                0xFF,
                0x28,
                (0x20B1DB1, 0x20B1DB1),
                "Sarias Song",
                (
                    "Sacred Forest Meadow",
                    "Forest Area",
                    "Songs",
                ),
            ),
        ),
        (
            "Song from Royal Familys Tomb",
            (
                "Song",
                0xFF,
                0x29,
                (0x332A871, 0x332A871),
                "Suns Song",
                (
                    "Graveyard",
                    "Grottos",
                    "Songs",
                ),
            ),
        ),
        (
            "Song from Ocarina of Time",
            (
                "Song",
                0xFF,
                0x2A,
                (0x252FC89, 0x252FC89),
                "Song of Time",
                (
                    "Hyrule Field",
                    "Songs",
                    "Need Spiritual Stones",
                ),
            ),
        ),
        (
            "Song from Windmill",
            (
                "Song",
                0xFF,
                0x2B,
                (0x0E42C07, 0x0E42B8B),
                "Song of Storms",
                (
                    "Kakariko Village",
                    "Songs",
                ),
            ),
        ),
        (
            "Sheik in Forest",
            (
                "Song",
                0xFF,
                0x20,
                (0x20B0809, 0x20B0809),
                "Minuet of Forest",
                (
                    "Sacred Forest Meadow",
                    "Forest Area",
                    "Songs",
                ),
            ),
        ),
        (
            "Sheik in Crater",
            (
                "Song",
                0xFF,
                0x21,
                (0x224D7F1, 0x224D7F1),
                "Bolero of Fire",
                (
                    "Death Mountain Crater",
                    "Songs",
                ),
            ),
        ),
        (
            "Sheik in Ice Cavern",
            (
                "Song",
                0xFF,
                0x22,
                (0x2BEC889, 0x2BEC889),
                "Serenade of Water",
                (
                    "Ice Cavern",
                    "Songs",
                ),
            ),
        ),
        (
            "Sheik at Colossus",
            (
                "Song",
                0xFF,
                0x23,
                (0x218C57D, 0x218C57D),
                "Requiem of Spirit",
                (
                    "Desert Colossus",
                    "Songs",
                ),
            ),
        ),
        (
            "Sheik in Kakariko",
            (
                "Song",
                0xFF,
                0x24,
                (0x2000FE1, 0x2000FE1),
                "Nocturne of Shadow",
                (
                    "Kakariko Village",
                    "Songs",
                ),
            ),
        ),
        (
            "Sheik at Temple",
            (
                "Song",
                0xFF,
                0x25,
                (0x2531329, 0x2531329),
                "Prelude of Light",
                (
                    "Temple of Time",
                    "Songs",
                ),
            ),
        ),
        ## Overworld
        # Kokiri Forest
        (
            "KF Midos Top Left Chest",
            (
                "Chest",
                0x28,
                0x00,
                None,
                "Rupees (5)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Chests",
                ),
            ),
        ),
        (
            "KF Midos Top Right Chest",
            (
                "Chest",
                0x28,
                0x01,
                None,
                "Rupees (5)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Chests",
                ),
            ),
        ),
        (
            "KF Midos Bottom Left Chest",
            (
                "Chest",
                0x28,
                0x02,
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Chests",
                ),
            ),
        ),
        (
            "KF Midos Bottom Right Chest",
            (
                "Chest",
                0x28,
                0x03,
                None,
                "Recovery Heart",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Chests",
                ),
            ),
        ),
        (
            "KF Kokiri Sword Chest",
            (
                "Chest",
                0x55,
                0x00,
                None,
                "Kokiri Sword",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Chests",
                ),
            ),
        ),
        (
            "KF Storms Grotto Chest",
            (
                "Chest",
                0x3E,
                0x0C,
                None,
                "Rupees (20)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "KF Links House Cow",
            (
                "NPC",
                0x34,
                0x15,
                None,
                "Milk",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Cows",
                    "Minigames",
                ),
            ),
        ),
        (
            "KF GS Know It All House",
            (
                "GS Token",
                0x0C,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "KF GS Bean Patch",
            (
                "GS Token",
                0x0C,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "KF GS House of Twins",
            (
                "GS Token",
                0x0C,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "KF Shop Item 1",
            (
                "Shop",
                0x2D,
                0x30,
                (shop_address(0, 0), None),
                "Buy Deku Shield",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Shops",
                ),
            ),
        ),
        (
            "KF Shop Item 2",
            (
                "Shop",
                0x2D,
                0x31,
                (shop_address(0, 1), None),
                "Buy Deku Nut (5)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Shops",
                ),
            ),
        ),
        (
            "KF Shop Item 3",
            (
                "Shop",
                0x2D,
                0x32,
                (shop_address(0, 2), None),
                "Buy Deku Nut (10)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Shops",
                ),
            ),
        ),
        (
            "KF Shop Item 4",
            (
                "Shop",
                0x2D,
                0x33,
                (shop_address(0, 3), None),
                "Buy Deku Stick (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Shops",
                ),
            ),
        ),
        (
            "KF Shop Item 5",
            (
                "Shop",
                0x2D,
                0x34,
                (shop_address(0, 4), None),
                "Buy Deku Seeds (30)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Shops",
                ),
            ),
        ),
        (
            "KF Shop Item 6",
            (
                "Shop",
                0x2D,
                0x35,
                (shop_address(0, 5), None),
                "Buy Arrows (10)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Shops",
                ),
            ),
        ),
        (
            "KF Shop Item 7",
            (
                "Shop",
                0x2D,
                0x36,
                (shop_address(0, 6), None),
                "Buy Arrows (30)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Shops",
                ),
            ),
        ),
        (
            "KF Shop Item 8",
            (
                "Shop",
                0x2D,
                0x37,
                (shop_address(0, 7), None),
                "Buy Heart",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Shops",
                ),
            ),
        ),
        # Kokiri Forest Freestanding
        (
            "KF Behind Midos Blue Rupee",
            (
                "Freestanding",
                0x55,
                (0, 0, 6),
                None,
                "Rupees (5)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF Boulder Maze Blue Rupee 1",
            (
                "Freestanding",
                0x55,
                (2, 0, 1),
                None,
                "Rupees (5)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF Boulder Maze Blue Rupee 2",
            (
                "Freestanding",
                0x55,
                (2, 0, 2),
                None,
                "Rupees (5)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF End of Bridge Blue Rupee",
            (
                "Freestanding",
                0x55,
                (0, 0, 7),
                None,
                "Rupees (5)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF Top of Sarias Recovery Heart 1",
            (
                "Freestanding",
                0x55,
                (0, 0, 20),
                None,
                "Recovery Heart",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF Top of Sarias Recovery Heart 2",
            (
                "Freestanding",
                0x55,
                (0, 0, 21),
                None,
                "Recovery Heart",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF Top of Sarias Recovery Heart 3",
            (
                "Freestanding",
                0x55,
                (0, 0, 22),
                None,
                "Recovery Heart",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF Bean Platform Green Rupee 1",
            (
                "RupeeTower",
                0x55,
                [(0, 2, 12, 1), (0, 3, 10, 1)],
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "KF Bean Platform Green Rupee 2",
            (
                "RupeeTower",
                0x55,
                [(0, 2, 12, 2), (0, 3, 10, 2)],
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "KF Bean Platform Green Rupee 3",
            (
                "RupeeTower",
                0x55,
                [(0, 2, 12, 3), (0, 3, 10, 3)],
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "KF Bean Platform Green Rupee 4",
            (
                "RupeeTower",
                0x55,
                [(0, 2, 12, 4), (0, 3, 10, 4)],
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "KF Bean Platform Green Rupee 5",
            (
                "RupeeTower",
                0x55,
                [(0, 2, 12, 5), (0, 3, 10, 5)],
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "KF Bean Platform Green Rupee 6",
            (
                "RupeeTower",
                0x55,
                [(0, 2, 12, 6), (0, 3, 10, 6)],
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "KF Bean Platform Red Rupee",
            (
                "RupeeTower",
                0x55,
                [(0, 2, 12, 7), (0, 3, 10, 7)],
                None,
                "Rupees (20)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "KF Grass Near Ramp Green Rupee 1",
            (
                "Freestanding",
                0x55,
                (0, 0, 2),
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF Grass Near Ramp Green Rupee 2",
            (
                "Freestanding",
                0x55,
                (0, 0, 3),
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF Grass Near Midos Green Rupee 1",
            (
                "Freestanding",
                0x55,
                (0, 0, 4),
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF Grass Near Midos Green Rupee 2",
            (
                "Freestanding",
                0x55,
                (0, 0, 5),
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF Sarias House Recovery Heart 1",
            (
                "Freestanding",
                0x29,
                (0, 0, 3),
                None,
                "Recovery Heart",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF Sarias House Recovery Heart 2",
            (
                "Freestanding",
                0x29,
                (0, 0, 4),
                None,
                "Recovery Heart",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF Sarias House Recovery Heart 3",
            (
                "Freestanding",
                0x29,
                (0, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "KF Sarias House Recovery Heart 4",
            (
                "Freestanding",
                0x29,
                (0, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        # Kokiri Forest Pots
        (
            "KF Links House Pot",
            (
                "Pot",
                0x34,
                (0, 0, 3),
                None,
                "Recovery Heart",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Pots",
                ),
            ),
        ),
        (
            "KF Know it All House Pot 1",
            (
                "Pot",
                0x26,
                (0, 0, 7),
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Pots",
                ),
            ),
        ),
        (
            "KF Know it All House Pot 2",
            (
                "Pot",
                0x26,
                (0, 0, 8),
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Pots",
                ),
            ),
        ),
        (
            "KF House of Twins Pot 1",
            (
                "Pot",
                0x27,
                (0, 0, 3),
                None,
                "Rupee (1)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Pots",
                ),
            ),
        ),
        (
            "KF House of Twins Pot 2",
            (
                "Pot",
                0x27,
                (0, 0, 4),
                None,
                "Rupees (5)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Pots",
                ),
            ),
        ),
        # Kokiri Forest Beehives
        (
            "KF Storms Grotto Beehive 1",
            (
                "Beehive",
                0x3E,
                (0, 0x0C, 8),
                None,
                "Rupees (5)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "KF Storms Grotto Beehive 2",
            (
                "Beehive",
                0x3E,
                (0, 0x0C, 9),
                None,
                "Rupees (20)",
                (
                    "Kokiri Forest",
                    "Forest Area",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        # Kokiri Forest Wonderitems
        (
            "KF Child Stepping Stones Wonderitem",
            (
                "Wonderitem",
                0x55,
                (0, 0, 39),
                None,
                "Rupees (5)",
                ("Kokiri Forest", "Forest", "Wonderitem"),
            ),
        ),
        (
            "KF Child Water Wonderitem",
            (
                "Wonderitem",
                0x55,
                (0, 0, 34),
                None,
                "Rupees (5)",
                ("Kokiri Forest", "Forest", "Wonderitem"),
            ),
        ),
        (
            "KF Child Sign Wonderitem",
            (
                "Wonderitem",
                0x55,
                (0, 0, 33),
                None,
                "Rupees (5)",
                ("Kokiri Forest", "Forest", "Wonderitem"),
            ),
        ),
        (
            "KF Child Training Wonderitem 1",
            (
                "Wonderitem",
                0x55,
                (0, 0, 40),
                None,
                "Rupees (5)",
                ("Kokiri Forest", "Forest", "Wonderitem"),
            ),
        ),
        (
            "KF Child Training Wonderitem 2",
            (
                "Wonderitem",
                0x55,
                (0, 0, 41),
                None,
                "Rupees (5)",
                ("Kokiri Forest", "Forest", "Wonderitem"),
            ),
        ),
        (
            "KF Child Training Wonderitem 3",
            (
                "Wonderitem",
                0x55,
                (0, 0, 42),
                None,
                "Rupees (5)",
                ("Kokiri Forest", "Forest", "Wonderitem"),
            ),
        ),
        (
            "KF Child Maze Grass Wonderitem 1",
            (
                "Wonderitem",
                0x55,
                (2, 0, 6),
                None,
                "Rupees (5)",
                ("Kokiri Forest", "Forest", "Wonderitem"),
            ),
        ),
        (
            "KF Child Maze Grass Wonderitem 2",
            (
                "Wonderitem",
                0x55,
                (2, 0, 7),
                None,
                "Rupees (5)",
                ("Kokiri Forest", "Forest", "Wonderitem"),
            ),
        ),
        (
            "KF Shop Wonderitem",
            (
                "Wonderitem",
                0x2D,
                (0, 0, 5),
                None,
                "Rupees (5)",
                ("Kokiri Forest", "Forest", "Wonderitem"),
            ),
        ),
        # Lost Woods
        (
            "LW Gift from Saria",
            (
                "Cutscene",
                0xFF,
                0x02,
                None,
                "Ocarina",
                (
                    "Lost Woods",
                    "Forest Area",
                    "NPCs",
                ),
            ),
        ),
        (
            "LW Ocarina Memory Game",
            (
                "NPC",
                0x5B,
                0x76,
                None,
                "Piece of Heart",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Minigames",
                ),
            ),
        ),
        (
            "LW Target in Woods",
            (
                "NPC",
                0x5B,
                0x60,
                None,
                "Slingshot",
                (
                    "Lost Woods",
                    "Forest Area",
                    "NPCs",
                ),
            ),
        ),
        (
            "LW Near Shortcuts Grotto Chest",
            (
                "Chest",
                0x3E,
                0x14,
                None,
                "Rupees (5)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "LW Trade Cojiro",
            (
                "NPC",
                0x5B,
                0x1F,
                None,
                "Odd Mushroom",
                (
                    "Lost Woods",
                    "Forest",
                ),
            ),
        ),
        (
            "LW Trade Odd Potion",
            (
                "NPC",
                0x5B,
                0x21,
                None,
                "Poachers Saw",
                (
                    "Lost Woods",
                    "Forest",
                ),
            ),
        ),
        (
            "Deku Theater Skull Mask",
            (
                "NPC",
                0x3E,
                0x77,
                None,
                "Deku Stick Capacity",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Grottos",
                ),
            ),
        ),
        (
            "Deku Theater Mask of Truth",
            (
                "NPC",
                0x3E,
                0x7A,
                None,
                "Deku Nut Capacity",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Need Spiritual Stones",
                    "Grottos",
                ),
            ),
        ),
        (
            "LW Skull Kid",
            (
                "NPC",
                0x5B,
                0x3E,
                None,
                "Piece of Heart",
                (
                    "Lost Woods",
                    "Forest Area",
                    "NPCs",
                ),
            ),
        ),
        (
            "LW Deku Scrub Near Bridge",
            (
                "Scrub",
                0x5B,
                0x77,
                None,
                "Deku Stick Capacity",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Deku Scrubs",
                    "Deku Scrub Upgrades",
                ),
            ),
        ),
        (
            "LW Deku Scrub Near Deku Theater Left",
            (
                "Scrub",
                0x5B,
                0x31,
                None,
                "Buy Deku Stick (1)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "LW Deku Scrub Near Deku Theater Right",
            (
                "Scrub",
                0x5B,
                0x30,
                None,
                "Buy Deku Nut (5)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "LW Deku Scrub Grotto Front",
            (
                "GrottoScrub",
                0xF5,
                0x79,
                None,
                "Deku Nut Capacity",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Deku Scrubs",
                    "Deku Scrub Upgrades",
                    "Grottos",
                ),
            ),
        ),
        (
            "LW Deku Scrub Grotto Rear",
            (
                "GrottoScrub",
                0xF5,
                0x33,
                None,
                "Buy Deku Seeds (30)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "LW GS Bean Patch Near Bridge",
            (
                "GS Token",
                0x0D,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "LW GS Bean Patch Near Theater",
            (
                "GS Token",
                0x0D,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "LW GS Above Theater",
            (
                "GS Token",
                0x0D,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Lost Woods Freestanding
        (
            "LW Under Boulder Blue Rupee",
            (
                "Freestanding",
                0x5B,
                [(7, 0, 5), (7, 2, 2)],
                None,
                "Rupees (5)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LW Underwater Green Rupee 1",
            (
                "Freestanding",
                0x5B,
                (3, 0, 5),
                None,
                "Rupee (1)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LW Underwater Green Rupee 2",
            (
                "Freestanding",
                0x5B,
                (3, 0, 6),
                None,
                "Rupee (1)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LW Underwater Green Rupee 3",
            (
                "Freestanding",
                0x5B,
                (3, 0, 8),
                None,
                "Rupee (1)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LW Underwater Green Rupee 4",
            (
                "Freestanding",
                0x5B,
                (3, 0, 9),
                None,
                "Rupee (1)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LW Underwater Green Rupee 5",
            (
                "Freestanding",
                0x5B,
                (3, 0, 10),
                None,
                "Rupee (1)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LW Underwater Green Rupee 6",
            (
                "Freestanding",
                0x5B,
                (3, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LW Underwater Green Rupee 7",
            (
                "Freestanding",
                0x5B,
                (3, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LW Underwater Shortcut Green Rupee",
            (
                "Freestanding",
                0x5B,
                (3, 0, 7),
                None,
                "Rupee (1)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Freestandings",
                ),
            ),
        ),
        # Lost Woods Beehives
        (
            "LW Near Shortcuts Grotto Beehive 1",
            (
                "Beehive",
                0x3E,
                (0, 0x14, 8),
                None,
                "Rupees (5)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "LW Near Shortcuts Grotto Beehive 2",
            (
                "Beehive",
                0x3E,
                (0, 0x14, 9),
                None,
                "Rupees (20)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "LW Scrubs Grotto Beehive",
            (
                "Beehive",
                0x3E,
                (6, 0x15, 4),
                None,
                "Rupees (20)",
                (
                    "Lost Woods",
                    "Forest Area",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        # Lost Woods Wonderitems
        (
            "LW Near Ocarina Game Wonderitem 1",
            (
                "Wonderitem",
                0x5B,
                (1, 0, 6),
                None,
                "Rupees (5)",
                ("Lost Woods", "Forest Area", "Wonderitem"),
            ),
        ),
        (
            "LW Near Ocarina Game Wonderitem 2",
            (
                "Wonderitem",
                0x5B,
                (1, 0, 7),
                None,
                "Rupees (5)",
                ("Lost Woods", "Forest Area", "Wonderitem"),
            ),
        ),
        (
            "LW Near Ocarina Game Wonderitem 3",
            (
                "Wonderitem",
                0x5B,
                (1, 0, 8),
                None,
                "Rupees (5)",
                ("Lost Woods", "Forest Area", "Wonderitem"),
            ),
        ),
        # Sacred Forest Meadow
        (
            "SFM Wolfos Grotto Chest",
            (
                "Chest",
                0x3E,
                0x11,
                None,
                "Rupees (50)",
                (
                    "Sacred Forest Meadow",
                    "Forest Area",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "SFM Deku Scrub Grotto Front",
            (
                "GrottoScrub",
                0xEE,
                0x3A,
                None,
                "Buy Green Potion",
                (
                    "Sacred Forest Meadow",
                    "Forest Area",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "SFM Deku Scrub Grotto Rear",
            (
                "GrottoScrub",
                0xEE,
                0x39,
                None,
                "Buy Red Potion for 30 Rupees",
                (
                    "Sacred Forest Meadow",
                    "Forest Area",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "SFM GS",
            (
                "GS Token",
                0x0D,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Sacred Forest Meadow",
                    "Forest Area",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Sacred Forest Meadow Beehives
        (
            "SFM Storms Grotto Beehive",
            (
                "Beehive",
                0x3E,
                (9, 0x0E, 3),
                None,
                "Rupees (20)",
                (
                    "Sacred Forest Meadow",
                    "Forest Area",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        # Sacred Forest Meadow Wonderitems
        (
            "SFM Near Lost Woods Wonderitem",
            (
                "Wonderitem",
                0x56,
                [(0, 0, 16), (0, 2, 19)],
                None,
                "Rupees (5)",
                ("Sacred Forest Meadow", "Forest Area", "Wonderitem"),
            ),
        ),
        (
            "SFM Maze Wonderitem 1",
            (
                "Wonderitem",
                0x56,
                [(0, 0, 13), (0, 2, 16)],
                None,
                "Rupees (5)",
                ("Sacred Forest Meadow", "Forest Area", "Wonderitem"),
            ),
        ),
        (
            "SFM Maze Wonderitem 2",
            (
                "Wonderitem",
                0x56,
                [(0, 0, 14), (0, 2, 17)],
                None,
                "Rupees (5)",
                ("Sacred Forest Meadow", "Forest Area", "Wonderitem"),
            ),
        ),
        (
            "SFM Maze Wonderitem 3",
            (
                "Wonderitem",
                0x56,
                [(0, 0, 15), (0, 2, 18)],
                None,
                "Rupees (5)",
                ("Sacred Forest Meadow", "Forest Area", "Wonderitem"),
            ),
        ),
        (
            "SFM Maze Wonderitem 4",
            (
                "Wonderitem",
                0x56,
                [(0, 0, 17), (0, 2, 20)],
                None,
                "Rupees (5)",
                ("Sacred Forest Meadow", "Forest Area", "Wonderitem"),
            ),
        ),
        (
            "SFM Maze Wonderitem 5",
            (
                "Wonderitem",
                0x56,
                [(0, 0, 18), (0, 2, 21)],
                None,
                "Rupees (5)",
                ("Sacred Forest Meadow", "Forest Area", "Wonderitem"),
            ),
        ),
        # Hyrule Field
        (
            "HF Ocarina of Time Item",
            (
                "NPC",
                0x51,
                0x0C,
                None,
                "Ocarina",
                (
                    "Hyrule Field",
                    "Need Spiritual Stones",
                    "NPCs",
                ),
            ),
        ),
        (
            "HF Near Market Grotto Chest",
            (
                "Chest",
                0x3E,
                0x00,
                None,
                "Rupees (5)",
                (
                    "Hyrule Field",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "HF Tektite Grotto Freestanding PoH",
            (
                "Collectable",
                0x3E,
                0x01,
                None,
                "Piece of Heart",
                (
                    "Hyrule Field",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "HF Southeast Grotto Chest",
            (
                "Chest",
                0x3E,
                0x02,
                None,
                "Rupees (20)",
                (
                    "Hyrule Field",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "HF Open Grotto Chest",
            (
                "Chest",
                0x3E,
                0x03,
                None,
                "Rupees (5)",
                (
                    "Hyrule Field",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "HF Deku Scrub Grotto",
            (
                "GrottoScrub",
                0xE6,
                0x3E,
                None,
                "Piece of Heart",
                (
                    "Hyrule Field",
                    "Deku Scrubs",
                    "Deku Scrub Upgrades",
                    "Grottos",
                ),
            ),
        ),
        (
            "HF Cow Grotto Cow",
            (
                "NPC",
                0x3E,
                0x16,
                None,
                "Milk",
                (
                    "Hyrule Field",
                    "Cows",
                    "Grottos",
                ),
            ),
        ),
        (
            "HF GS Cow Grotto",
            (
                "GS Token",
                0x0A,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Hyrule Field",
                    "Gold Skulltulas",
                    "Grottos",
                ),
            ),
        ),
        (
            "HF GS Near Kak Grotto",
            (
                "GS Token",
                0x0A,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Hyrule Field",
                    "Gold Skulltulas",
                    "Grottos",
                ),
            ),
        ),
        # Hyrule Field Pots
        (
            "HF Cow Grotto Pot 1",
            (
                "Pot",
                0x3E,
                (4, 4, 6),
                None,
                "Deku Nuts (5)",
                (
                    "Hyrule Field",
                    "Grottos",
                    "Pots",
                ),
            ),
        ),
        (
            "HF Cow Grotto Pot 2",
            (
                "Pot",
                0x3E,
                (4, 4, 8),
                None,
                "Rupees (5)",
                (
                    "Hyrule Field",
                    "Grottos",
                    "Pots",
                ),
            ),
        ),
        # Hyrule Field Beehives
        (
            "HF Near Market Grotto Beehive 1",
            (
                "Beehive",
                0x3E,
                (0, 0, 8),
                None,
                "Rupees (5)",
                (
                    "Hyrule Field",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "HF Near Market Grotto Beehive 2",
            (
                "Beehive",
                0x3E,
                (0, 0, 9),
                None,
                "Rupees (20)",
                (
                    "Hyrule Field",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "HF Open Grotto Beehive 1",
            (
                "Beehive",
                0x3E,
                (0, 3, 8),
                None,
                "Rupees (5)",
                (
                    "Hyrule Field",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "HF Open Grotto Beehive 2",
            (
                "Beehive",
                0x3E,
                (0, 3, 9),
                None,
                "Rupees (20)",
                (
                    "Hyrule Field",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "HF Southeast Grotto Beehive 1",
            (
                "Beehive",
                0x3E,
                (0, 2, 8),
                None,
                "Rupees (5)",
                (
                    "Hyrule Field",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "HF Southeast Grotto Beehive 2",
            (
                "Beehive",
                0x3E,
                (0, 2, 9),
                None,
                "Rupees (20)",
                (
                    "Hyrule Field",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "HF Inside Fence Grotto Beehive",
            (
                "Beehive",
                0x3E,
                (1, 6, 2),
                None,
                "Rupees (20)",
                (
                    "Hyrule Field",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        # Hyrule Field Wonderitems
        (
            "HF Child Above Drawbridge Wonderitem 1",
            (
                "Wonderitem",
                0x51,
                [(0, 0, 53), (0, 1, 51)],
                None,
                "Rupees (20)",
                ("Hyrule Field", "Wonderitem"),
            ),
        ),
        (
            "HF Child Above Drawbridge Wonderitem 2",
            (
                "Wonderitem",
                0x51,
                [(0, 0, 54), (0, 1, 52)],
                None,
                "Rupees (20)",
                ("Hyrule Field", "Wonderitem"),
            ),
        ),
        (
            "HF Child Above Drawbridge Wonderitem 3",
            (
                "Wonderitem",
                0x51,
                [(0, 0, 55), (0, 1, 53)],
                None,
                "Rupees (20)",
                ("Hyrule Field", "Wonderitem"),
            ),
        ),
        (
            "Market Shooting Gallery Reward",
            (
                "NPC",
                0x42,
                0x60,
                None,
                "Slingshot",
                (
                    "Market",
                    "Minigames",
                ),
            ),
        ),
        (
            "Market Bombchu Bowling First Prize",
            (
                "NPC",
                0x4B,
                0x34,
                None,
                "Bomb Bag",
                (
                    "Market",
                    "Minigames",
                ),
            ),
        ),
        (
            "Market Bombchu Bowling Second Prize",
            (
                "NPC",
                0x4B,
                0x3E,
                None,
                "Piece of Heart",
                (
                    "Market",
                    "Minigames",
                ),
            ),
        ),
        ("Market Bombchu Bowling Bombchus", ("NPC", 0x4B, 0x03, None, "Bombchus (10)", None)),
        ("Market Bombchu Bowling Bomb", ("NPC", 0x4B, 0x65, None, "Bomb (1)", None)),
        (
            "Market Lost Dog",
            (
                "NPC",
                0x35,
                0x3E,
                None,
                "Piece of Heart",
                (
                    "Market",
                    "NPCs",
                ),
            ),
        ),
        (
            "Market Treasure Chest Game Salesman",
            (
                "NPC",
                0x10,
                0x71,
                None,
                "Small Key (Treasure Chest Game)",
                (
                    "Market",
                    "Minigames",
                    "NPCs",
                ),
            ),
        ),
        (
            "Market Treasure Chest Game Room 1 Bottom",
            (
                "Chest",
                0x10,
                0x00,
                None,
                "Rupee (Treasure Chest Game) (1)",
                (
                    "Market",
                    "Minigames",
                    "Chests",
                ),
            ),
        ),
        (
            "Market Treasure Chest Game Room 1 Top",
            (
                "Chest",
                0x10,
                0x01,
                None,
                "Small Key (Treasure Chest Game)",
                (
                    "Market",
                    "Minigames",
                    "Chests",
                ),
            ),
        ),
        (
            "Market Treasure Chest Game Room 2 Bottom",
            (
                "Chest",
                0x10,
                0x02,
                None,
                "Rupee (Treasure Chest Game) (1)",
                (
                    "Market",
                    "Minigames",
                    "Chests",
                ),
            ),
        ),
        (
            "Market Treasure Chest Game Room 2 Top",
            (
                "Chest",
                0x10,
                0x03,
                None,
                "Small Key (Treasure Chest Game)",
                (
                    "Market",
                    "Minigames",
                    "Chests",
                ),
            ),
        ),
        (
            "Market Treasure Chest Game Room 3 Bottom",
            (
                "Chest",
                0x10,
                0x04,
                None,
                "Rupees (Treasure Chest Game) (5)",
                (
                    "Market",
                    "Minigames",
                    "Chests",
                ),
            ),
        ),
        (
            "Market Treasure Chest Game Room 3 Top",
            (
                "Chest",
                0x10,
                0x05,
                None,
                "Small Key (Treasure Chest Game)",
                (
                    "Market",
                    "Minigames",
                    "Chests",
                ),
            ),
        ),
        (
            "Market Treasure Chest Game Room 4 Bottom",
            (
                "Chest",
                0x10,
                0x06,
                None,
                "Rupees (Treasure Chest Game) (5)",
                (
                    "Market",
                    "Minigames",
                    "Chests",
                ),
            ),
        ),
        (
            "Market Treasure Chest Game Room 4 Top",
            (
                "Chest",
                0x10,
                0x07,
                None,
                "Small Key (Treasure Chest Game)",
                (
                    "Market",
                    "Minigames",
                    "Chests",
                ),
            ),
        ),
        (
            "Market Treasure Chest Game Room 5 Bottom",
            (
                "Chest",
                0x10,
                0x08,
                None,
                "Rupees (Treasure Chest Game) (20)",
                (
                    "Market",
                    "Minigames",
                    "Chests",
                ),
            ),
        ),
        (
            "Market Treasure Chest Game Room 5 Top",
            (
                "Chest",
                0x10,
                0x09,
                None,
                "Small Key (Treasure Chest Game)",
                (
                    "Market",
                    "Minigames",
                    "Chests",
                ),
            ),
        ),
        (
            "Market Treasure Chest Game Reward",
            (
                "Chest",
                0x10,
                0x0A,
                None,
                "Piece of Heart (Treasure Chest Game)",
                (
                    "Market",
                    "Minigames",
                    "Chests",
                ),
            ),
        ),
        (
            "Market 10 Big Poes",
            (
                "NPC",
                0x4D,
                0x0F,
                None,
                "Bottle",
                (
                    "Market",
                    "NPCs",
                ),
            ),
        ),
        (
            "Market GS Guard House",
            (
                "GS Token",
                0x0E,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Market",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Market Mask Shop Item 1",
            (
                "MaskShop",
                0x33,
                0x53,
                (shop_address(10, 0), None),
                "Gerudo Mask",
                ("Market", "Shops"),
            ),
        ),
        (
            "Market Mask Shop Item 2",
            ("MaskShop", 0x33, 0x52, (shop_address(10, 1), None), "Zora Mask", ("Market", "Shops")),
        ),
        (
            "Market Mask Shop Item 3",
            (
                "MaskShop",
                0x33,
                0x1C,
                (shop_address(10, 2), None),
                "Mask of Truth",
                ("Market", "Shops"),
            ),
        ),
        (
            "Market Mask Shop Item 4",
            (
                "MaskShop",
                0x33,
                0x51,
                (shop_address(10, 3), None),
                "Goron Mask",
                ("Market", "Shops"),
            ),
        ),
        (
            "Market Mask Shop Item 5",
            (
                "MaskShop",
                0x33,
                0x17,
                (shop_address(10, 4), None),
                "Skull Mask",
                ("Market", "Shops"),
            ),
        ),
        (
            "Market Mask Shop Item 6",
            (
                "MaskShop",
                0x33,
                0x1A,
                (shop_address(10, 5), None),
                "Keaton Mask",
                ("Market", "Shops"),
            ),
        ),
        (
            "Market Mask Shop Item 7",
            (
                "MaskShop",
                0x33,
                0x1B,
                (shop_address(10, 6), None),
                "Bunny Hood",
                ("Market", "Shops"),
            ),
        ),
        (
            "Market Mask Shop Item 8",
            (
                "MaskShop",
                0x33,
                0x18,
                (shop_address(10, 7), None),
                "Spooky Mask",
                ("Market", "Shops"),
            ),
        ),
        (
            "Market Bazaar Item 1",
            (
                "Shop",
                0x2C,
                0x30,
                (shop_address(4, 0), None),
                "Buy Hylian Shield",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bazaar Item 2",
            (
                "Shop",
                0x2C,
                0x31,
                (shop_address(4, 1), None),
                "Buy Bombs (5) for 35 Rupees",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bazaar Item 3",
            (
                "Shop",
                0x2C,
                0x32,
                (shop_address(4, 2), None),
                "Buy Deku Nut (5)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bazaar Item 4",
            (
                "Shop",
                0x2C,
                0x33,
                (shop_address(4, 3), None),
                "Buy Heart",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bazaar Item 5",
            (
                "Shop",
                0x2C,
                0x34,
                (shop_address(4, 4), None),
                "Buy Arrows (10)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bazaar Item 6",
            (
                "Shop",
                0x2C,
                0x35,
                (shop_address(4, 5), None),
                "Buy Arrows (50)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bazaar Item 7",
            (
                "Shop",
                0x2C,
                0x36,
                (shop_address(4, 6), None),
                "Buy Deku Stick (1)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bazaar Item 8",
            (
                "Shop",
                0x2C,
                0x37,
                (shop_address(4, 7), None),
                "Buy Arrows (30)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Potion Shop Item 1",
            (
                "Shop",
                0x31,
                0x30,
                (shop_address(3, 0), None),
                "Buy Green Potion",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Potion Shop Item 2",
            (
                "Shop",
                0x31,
                0x31,
                (shop_address(3, 1), None),
                "Buy Blue Fire",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Potion Shop Item 3",
            (
                "Shop",
                0x31,
                0x32,
                (shop_address(3, 2), None),
                "Buy Red Potion for 30 Rupees",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Potion Shop Item 4",
            (
                "Shop",
                0x31,
                0x33,
                (shop_address(3, 3), None),
                "Buy Fairy's Spirit",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Potion Shop Item 5",
            (
                "Shop",
                0x31,
                0x34,
                (shop_address(3, 4), None),
                "Buy Deku Nut (5)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Potion Shop Item 6",
            (
                "Shop",
                0x31,
                0x35,
                (shop_address(3, 5), None),
                "Buy Bottle Bug",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Potion Shop Item 7",
            (
                "Shop",
                0x31,
                0x36,
                (shop_address(3, 6), None),
                "Buy Poe",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Potion Shop Item 8",
            (
                "Shop",
                0x31,
                0x37,
                (shop_address(3, 7), None),
                "Buy Fish",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bombchu Shop Item 1",
            (
                "Shop",
                0x32,
                0x30,
                (shop_address(2, 0), None),
                "Buy Bombchu (5)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bombchu Shop Item 2",
            (
                "Shop",
                0x32,
                0x31,
                (shop_address(2, 1), None),
                "Buy Bombchu (10)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bombchu Shop Item 3",
            (
                "Shop",
                0x32,
                0x32,
                (shop_address(2, 2), None),
                "Buy Bombchu (10)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bombchu Shop Item 4",
            (
                "Shop",
                0x32,
                0x33,
                (shop_address(2, 3), None),
                "Buy Bombchu (10)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bombchu Shop Item 5",
            (
                "Shop",
                0x32,
                0x34,
                (shop_address(2, 4), None),
                "Buy Bombchu (20)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bombchu Shop Item 6",
            (
                "Shop",
                0x32,
                0x35,
                (shop_address(2, 5), None),
                "Buy Bombchu (20)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bombchu Shop Item 7",
            (
                "Shop",
                0x32,
                0x36,
                (shop_address(2, 6), None),
                "Buy Bombchu (20)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "Market Bombchu Shop Item 8",
            (
                "Shop",
                0x32,
                0x37,
                (shop_address(2, 7), None),
                "Buy Bombchu (20)",
                (
                    "Market",
                    "Shops",
                ),
            ),
        ),
        (
            "ToT Light Arrows Cutscene",
            (
                "Cutscene",
                0xFF,
                0x01,
                None,
                "Light Arrows",
                (
                    "Temple of Time",
                    "NPCs",
                ),
            ),
        ),
        # Market Pots/Crates
        (
            "Market Night Red Rupee Crate",
            (
                "Crate",
                0x21,
                (0, 0, 23),
                None,
                "Rupees (20)",
                (
                    "Market",
                    "Crates",
                ),
            ),
        ),
        (
            "Market Night Green Rupee Crate 1",
            (
                "Crate",
                0x21,
                (0, 0, 24),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Crates",
                ),
            ),
        ),
        (
            "Market Night Green Rupee Crate 2",
            (
                "Crate",
                0x21,
                (0, 0, 25),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Crates",
                ),
            ),
        ),
        (
            "Market Night Green Rupee Crate 3",
            (
                "Crate",
                0x21,
                (0, 0, 26),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Crates",
                ),
            ),
        ),
        (
            "Market Day Crate 1",
            (
                "Crate",
                0x20,
                (0, 0, 34),
                None,
                "Nothing",
                (
                    "Market",
                    "Crates",
                ),
            ),
        ),
        (
            "Market Day Crate 2",
            (
                "Crate",
                0x20,
                (0, 0, 35),
                None,
                "Nothing",
                (
                    "Market",
                    "Crates",
                ),
            ),
        ),
        (
            "Market Day Crate 3",
            (
                "Crate",
                0x20,
                (0, 0, 36),
                None,
                "Nothing",
                (
                    "Market",
                    "Crates",
                ),
            ),
        ),
        (
            "Market Day Crate 4",
            (
                "Crate",
                0x20,
                (0, 0, 37),
                None,
                "Nothing",
                (
                    "Market",
                    "Crates",
                ),
            ),
        ),
        (
            "Market Dog Lady House Crate",
            (
                "Crate",
                0x35,
                (0, 0, 3),
                None,
                "Rupees (5)",
                (
                    "Market",
                    "Crates",
                ),
            ),
        ),
        (
            "Market Guard House Child Crate 1",
            (
                "Crate",
                0x4D,
                (0, 0, 4),
                None,
                "Nothing",
                (
                    "Market",
                    "Crates",
                ),
            ),
        ),
        (
            "Market Guard House Child Crate 2",
            (
                "Crate",
                0x4D,
                (0, 0, 5),
                None,
                "Nothing",
                (
                    "Market",
                    "Crates",
                ),
            ),
        ),
        (
            "Market Guard House Child Crate 3",
            (
                "Crate",
                0x4D,
                (0, 0, 7),
                None,
                "Nothing",
                (
                    "Market",
                    "Crates",
                ),
            ),
        ),
        (
            "Market Guard House Child Crate 4",
            (
                "Crate",
                0x4D,
                (0, 0, 6),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Crates",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 1",
            (
                "Pot",
                0x4D,
                (0, 0, 9),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 2",
            (
                "Pot",
                0x4D,
                (0, 0, 10),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 3",
            (
                "Pot",
                0x4D,
                (0, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 4",
            (
                "Pot",
                0x4D,
                (0, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 5",
            (
                "Pot",
                0x4D,
                (0, 0, 13),
                None,
                "Rupees (5)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 6",
            (
                "Pot",
                0x4D,
                (0, 0, 14),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 7",
            (
                "Pot",
                0x4D,
                (0, 0, 15),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 8",
            (
                "Pot",
                0x4D,
                (0, 0, 16),
                None,
                "Rupees (5)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 9",
            (
                "Pot",
                0x4D,
                (0, 0, 17),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 10",
            (
                "Pot",
                0x4D,
                (0, 0, 18),
                None,
                "Rupees (5)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 11",
            (
                "Pot",
                0x4D,
                (0, 0, 19),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 12",
            (
                "Pot",
                0x4D,
                (0, 0, 20),
                None,
                "Rupees (5)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 13",
            (
                "Pot",
                0x4D,
                (0, 0, 21),
                None,
                "Recovery Heart",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 14",
            (
                "Pot",
                0x4D,
                (0, 0, 22),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 15",
            (
                "Pot",
                0x4D,
                (0, 0, 23),
                None,
                "Recovery Heart",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 16",
            (
                "Pot",
                0x4D,
                (0, 0, 24),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 17",
            (
                "Pot",
                0x4D,
                (0, 0, 25),
                None,
                "Rupees (5)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 18",
            (
                "Pot",
                0x4D,
                (0, 0, 26),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 19",
            (
                "Pot",
                0x4D,
                (0, 0, 27),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 20",
            (
                "Pot",
                0x4D,
                (0, 0, 28),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 21",
            (
                "Pot",
                0x4D,
                (0, 0, 29),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 22",
            (
                "Pot",
                0x4D,
                (0, 0, 30),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 23",
            (
                "Pot",
                0x4D,
                (0, 0, 31),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 24",
            (
                "Pot",
                0x4D,
                (0, 0, 32),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 25",
            (
                "Pot",
                0x4D,
                (0, 0, 33),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 26",
            (
                "Pot",
                0x4D,
                (0, 0, 34),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 27",
            (
                "Pot",
                0x4D,
                (0, 0, 35),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 28",
            (
                "Pot",
                0x4D,
                (0, 0, 36),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 29",
            (
                "Pot",
                0x4D,
                (0, 0, 37),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 30",
            (
                "Pot",
                0x4D,
                (0, 0, 38),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 31",
            (
                "Pot",
                0x4D,
                (0, 0, 39),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 32",
            (
                "Pot",
                0x4D,
                (0, 0, 40),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 33",
            (
                "Pot",
                0x4D,
                (0, 0, 41),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 34",
            (
                "Pot",
                0x4D,
                (0, 0, 42),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 35",
            (
                "Pot",
                0x4D,
                (0, 0, 43),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 36",
            (
                "Pot",
                0x4D,
                (0, 0, 44),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 37",
            (
                "Pot",
                0x4D,
                (0, 0, 45),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 38",
            (
                "Pot",
                0x4D,
                (0, 0, 46),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 39",
            (
                "Pot",
                0x4D,
                (0, 0, 47),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 40",
            (
                "Pot",
                0x4D,
                (0, 0, 48),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 41",
            (
                "Pot",
                0x4D,
                (0, 0, 49),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 42",
            (
                "Pot",
                0x4D,
                (0, 0, 50),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 43",
            (
                "Pot",
                0x4D,
                (0, 0, 51),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Child Pot 44",
            (
                "Pot",
                0x4D,
                (0, 0, 52),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Adult Pot 1",
            (
                "Pot",
                0x4D,
                (0, 2, 2),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Adult Pot 2",
            (
                "Pot",
                0x4D,
                (0, 2, 3),
                None,
                "Nothing",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Adult Pot 3",
            (
                "Pot",
                0x4D,
                (0, 2, 4),
                None,
                "Recovery Heart",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Adult Pot 4",
            (
                "Pot",
                0x4D,
                (0, 2, 5),
                None,
                "Rupees (20)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Adult Pot 5",
            (
                "Pot",
                0x4D,
                (0, 2, 6),
                None,
                "Nothing",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Adult Pot 6",
            (
                "Pot",
                0x4D,
                (0, 2, 7),
                None,
                "Recovery Heart",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Adult Pot 7",
            (
                "Pot",
                0x4D,
                (0, 2, 8),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Adult Pot 8",
            (
                "Pot",
                0x4D,
                (0, 2, 9),
                None,
                "Nothing",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Adult Pot 9",
            (
                "Pot",
                0x4D,
                (0, 2, 10),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Adult Pot 10",
            (
                "Pot",
                0x4D,
                (0, 2, 11),
                None,
                "Nothing",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Guard House Adult Pot 11",
            (
                "Pot",
                0x4D,
                (0, 2, 12),
                None,
                "Rupee (1)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Man in Green House Pot 1",
            (
                "Pot",
                0x2B,
                (0, 0, 3),
                None,
                "Recovery Heart",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Man in Green House Pot 2",
            (
                "Pot",
                0x2B,
                (0, 0, 4),
                None,
                "Recovery Heart",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        (
            "Market Man in Green House Pot 3",
            (
                "Pot",
                0x2B,
                (0, 0, 5),
                None,
                "Rupees (5)",
                (
                    "Market",
                    "Pots",
                ),
            ),
        ),
        # Market Wonderitems
        (
            "Market Daytime Balcony Wonderitem 1",
            ("Wonderitem", 0x20, (0, 0, 16), None, "Rupees (5)", ("Market", "Wonderitem")),
        ),
        (
            "Market Daytime Balcony Wonderitem 2",
            ("Wonderitem", 0x20, (0, 0, 17), None, "Rupees (5)", ("Market", "Wonderitem")),
        ),
        (
            "Market Daytime Balcony Wonderitem 3",
            ("Wonderitem", 0x20, (0, 0, 18), None, "Rupees (5)", ("Market", "Wonderitem")),
        ),
        (
            "Market Daytime Balcony Wonderitem 4",
            ("Wonderitem", 0x20, (0, 0, 19), None, "Rupees (5)", ("Market", "Wonderitem")),
        ),
        (
            "Market Daytime Balcony Wonderitem 5",
            ("Wonderitem", 0x20, (0, 0, 20), None, "Rupees (5)", ("Market", "Wonderitem")),
        ),
        (
            "Market Night Balcony Wonderitem 1",
            ("Wonderitem", 0x21, (0, 0, 6), None, "Rupees (5)", ("Market", "Wonderitem")),
        ),
        (
            "Market Night Balcony Wonderitem 2",
            ("Wonderitem", 0x21, (0, 0, 7), None, "Rupees (5)", ("Market", "Wonderitem")),
        ),
        # Hyrule Castle
        (
            "HC Malon Egg",
            (
                "NPC",
                0x5F,
                0x47,
                None,
                "Weird Egg",
                (
                    "Hyrule Castle",
                    "NPCs",
                ),
            ),
        ),
        (
            "HC Zeldas Letter",
            (
                "NPC",
                0x4A,
                0x0B,
                None,
                "Zeldas Letter",
                (
                    "Hyrule Castle",
                    "NPCs",
                ),
            ),
        ),
        (
            "HC Great Fairy Reward",
            (
                "Cutscene",
                0xFF,
                0x11,
                None,
                "Dins Fire",
                (
                    "Hyrule Castle",
                    "Great Fairies",
                ),
            ),
        ),
        (
            "HC GS Tree",
            (
                "GS Token",
                0x0E,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Hyrule Castle",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "HC GS Storms Grotto",
            (
                "GS Token",
                0x0E,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Hyrule Castle",
                    "Gold Skulltulas",
                    "Grottos",
                ),
            ),
        ),
        (
            "HC Storms Grotto Pot 1",
            (
                "Pot",
                0x3E,
                (8, 0x16, 7),
                None,
                "Rupees (20)",
                (
                    "Hyrule Castle",
                    "Grottos",
                    "Pots",
                ),
            ),
        ),
        (
            "HC Storms Grotto Pot 2",
            (
                "Pot",
                0x3E,
                (8, 0x16, 8),
                None,
                "Bombs (5)",
                (
                    "Hyrule Castle",
                    "Grottos",
                    "Pots",
                ),
            ),
        ),
        (
            "HC Storms Grotto Pot 3",
            (
                "Pot",
                0x3E,
                (8, 0x16, 10),
                None,
                "Arrows (5)",
                (
                    "Hyrule Castle",
                    "Grottos",
                    "Pots",
                ),
            ),
        ),
        (
            "HC Storms Grotto Pot 4",
            (
                "Pot",
                0x3E,
                (8, 0x16, 12),
                None,
                "Deku Nuts (5)",
                (
                    "Hyrule Castle",
                    "Grottos",
                    "Pots",
                ),
            ),
        ),
        # Hyrule Castle Wonderitems
        (
            "HC Castle Torch Wonderitem 1",
            ("Wonderitem", 0x5F, (0, 0, 13), None, "Rupees (20)", ("Hyrule Castle", "Wonderitem")),
        ),
        (
            "HC Castle Torch Wonderitem 2",
            ("Wonderitem", 0x5F, (0, 0, 14), None, "Rupees (20)", ("Hyrule Castle", "Wonderitem")),
        ),
        (
            "HC Castle Moat Wonderitem 1",
            ("Wonderitem", 0x5F, (0, 0, 33), None, "Rupee (1)", ("Hyrule Castle", "Wonderitem")),
        ),
        (
            "HC Castle Moat Wonderitem 2",
            ("Wonderitem", 0x5F, (0, 0, 34), None, "Rupee (1)", ("Hyrule Castle", "Wonderitem")),
        ),
        (
            "HC Castle Moat Wonderitem 3",
            ("Wonderitem", 0x5F, (0, 0, 35), None, "Rupee (1)", ("Hyrule Castle", "Wonderitem")),
        ),
        (
            "HC Castle Moat Wonderitem 4",
            ("Wonderitem", 0x5F, (0, 0, 36), None, "Rupee (1)", ("Hyrule Castle", "Wonderitem")),
        ),
        (
            "HC Castle Moat Wonderitem 5",
            ("Wonderitem", 0x5F, (0, 0, 37), None, "Rupee (1)", ("Hyrule Castle", "Wonderitem")),
        ),
        (
            "HC Castle Moat Wonderitem 6",
            ("Wonderitem", 0x5F, (0, 0, 38), None, "Rupee (1)", ("Hyrule Castle", "Wonderitem")),
        ),
        (
            "HC Castle Moat Wonderitem 7",
            ("Wonderitem", 0x5F, (0, 0, 39), None, "Rupee (1)", ("Hyrule Castle", "Wonderitem")),
        ),
        (
            "HC Castle Moat Wonderitem 8",
            ("Wonderitem", 0x5F, (0, 0, 40), None, "Rupee (1)", ("Hyrule Castle", "Wonderitem")),
        ),
        (
            "HC Castle Moat Wonderitem 9",
            ("Wonderitem", 0x5F, (0, 0, 41), None, "Rupee (1)", ("Hyrule Castle", "Wonderitem")),
        ),
        (
            "HC Castle Moat Wonderitem 10",
            ("Wonderitem", 0x5F, (0, 0, 42), None, "Rupee (1)", ("Hyrule Castle", "Wonderitem")),
        ),
        (
            "HC Zeldas Courtyard Mario Wonderitem",
            ("Wonderitem", 0x4A, (0, 0, 6), None, "Rupees (20)", ("Hyrule Castle", "Wonderitem")),
        ),
        (
            "LLR Talons Chickens",
            (
                "NPC",
                0x4C,
                0x14,
                None,
                "Bottle with Milk",
                (
                    "Lon Lon Ranch",
                    "Minigames",
                ),
            ),
        ),
        (
            "LLR Freestanding PoH",
            (
                "Collectable",
                0x4C,
                0x01,
                None,
                "Piece of Heart",
                (
                    "Lon Lon Ranch",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LLR Deku Scrub Grotto Left",
            (
                "GrottoScrub",
                0xFC,
                0x30,
                None,
                "Buy Deku Nut (5)",
                (
                    "Lon Lon Ranch",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "LLR Deku Scrub Grotto Center",
            (
                "GrottoScrub",
                0xFC,
                0x33,
                None,
                "Buy Deku Seeds (30)",
                (
                    "Lon Lon Ranch",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "LLR Deku Scrub Grotto Right",
            (
                "GrottoScrub",
                0xFC,
                0x37,
                None,
                "Buy Bombs (5) for 35 Rupees",
                (
                    "Lon Lon Ranch",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "LLR Stables Left Cow",
            (
                "NPC",
                0x36,
                0x15,
                None,
                "Milk",
                (
                    "Lon Lon Ranch",
                    "Cows",
                ),
            ),
        ),
        (
            "LLR Stables Right Cow",
            (
                "NPC",
                0x36,
                0x16,
                None,
                "Milk",
                (
                    "Lon Lon Ranch",
                    "Cows",
                ),
            ),
        ),
        (
            "LLR Tower Left Cow",
            (
                "NPC",
                0x4C,
                0x16,
                None,
                "Milk",
                (
                    "Lon Lon Ranch",
                    "Cows",
                ),
            ),
        ),
        (
            "LLR Tower Right Cow",
            (
                "NPC",
                0x4C,
                0x15,
                None,
                "Milk",
                (
                    "Lon Lon Ranch",
                    "Cows",
                ),
            ),
        ),
        (
            "LLR GS House Window",
            (
                "GS Token",
                0x0B,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Lon Lon Ranch",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "LLR GS Tree",
            (
                "GS Token",
                0x0B,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Lon Lon Ranch",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "LLR GS Rain Shed",
            (
                "GS Token",
                0x0B,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Lon Lon Ranch",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "LLR GS Back Wall",
            (
                "GS Token",
                0x0B,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Lon Lon Ranch",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Lon Lon Ranch Pots/Crates
        (
            "LLR Front Pot 1",
            (
                "Pot",
                0x63,
                [(0, 0, 6), (0, 1, 5)],
                None,
                "Recovery Heart",
                (
                    "Lon Lon Ranch",
                    "Pots",
                ),
            ),
        ),
        (
            "LLR Front Pot 2",
            (
                "Pot",
                0x63,
                [(0, 0, 4), (0, 1, 3)],
                None,
                "Recovery Heart",
                (
                    "Lon Lon Ranch",
                    "Pots",
                ),
            ),
        ),
        (
            "LLR Front Pot 3",
            (
                "Pot",
                0x63,
                [(0, 0, 7), (0, 1, 6)],
                None,
                "Rupee (1)",
                (
                    "Lon Lon Ranch",
                    "Pots",
                ),
            ),
        ),
        (
            "LLR Front Pot 4",
            (
                "Pot",
                0x63,
                [(0, 0, 5), (0, 1, 4)],
                None,
                "Rupee (1)",
                (
                    "Lon Lon Ranch",
                    "Pots",
                ),
            ),
        ),
        (
            "LLR Rain Shed Pot 1",
            (
                "Pot",
                0x63,
                [(0, 0, 8), (0, 1, 7)],
                None,
                "Recovery Heart",
                (
                    "Lon Lon Ranch",
                    "Pots",
                ),
            ),
        ),
        (
            "LLR Rain Shed Pot 2",
            (
                "Pot",
                0x63,
                [(0, 0, 9), (0, 1, 8)],
                None,
                "Recovery Heart",
                (
                    "Lon Lon Ranch",
                    "Pots",
                ),
            ),
        ),
        (
            "LLR Rain Shed Pot 3",
            (
                "Pot",
                0x63,
                [(0, 0, 10), (0, 1, 9)],
                None,
                "Recovery Heart",
                (
                    "Lon Lon Ranch",
                    "Pots",
                ),
            ),
        ),
        (
            "LLR Talons House Pot 1",
            (
                "Pot",
                0x4C,
                (2, 0, 1),
                None,
                "Rupees (5)",
                (
                    "Lon Lon Ranch",
                    "Pots",
                ),
            ),
        ),
        (
            "LLR Talons House Pot 2",
            (
                "Pot",
                0x4C,
                (2, 0, 2),
                None,
                "Rupees (5)",
                (
                    "Lon Lon Ranch",
                    "Pots",
                ),
            ),
        ),
        (
            "LLR Talons House Pot 3",
            (
                "Pot",
                0x4C,
                (2, 0, 3),
                None,
                "Rupees (5)",
                (
                    "Lon Lon Ranch",
                    "Pots",
                ),
            ),
        ),
        (
            "LLR Child Crate",
            (
                "Crate",
                0x63,
                [(0, 0, 25), (0, 1, 30)],
                None,
                "Rupee (1)",
                (
                    "Lon Lon Ranch",
                    "Crates",
                ),
            ),
        ),
        # Lon Lon Ranch Beehives
        (
            "LLR Grotto Beehive",
            (
                "Beehive",
                0x3E,
                (12, 0x1C, 4),
                None,
                "Rupees (20)",
                (
                    "Lon Lon Ranch",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        # Lon Lon Ranch Wonderitems
        (
            "LLR Epona Hurdle Wonderitem 1",
            (
                "Wonderitem",
                0x63,
                [(0, 2, 25), (0, 3, 9)],
                None,
                "Rupees (5)",
                ("Lon Lon Ranch", "Wonderitem"),
            ),
        ),
        (
            "LLR Epona Hurdle Wonderitem 2",
            (
                "Wonderitem",
                0x63,
                [(0, 2, 26), (0, 3, 10)],
                None,
                "Rupees (5)",
                ("Lon Lon Ranch", "Wonderitem"),
            ),
        ),
        # Kakariko Village
        (
            "Kak Anju as Child",
            (
                "NPC",
                0x52,
                0x0F,
                None,
                "Bottle",
                (
                    "Kakariko Village",
                    "Minigames",
                ),
            ),
        ),
        (
            "Kak Anju as Adult",
            (
                "NPC",
                0x52,
                0x1D,
                None,
                "Pocket Egg",
                (
                    "Kakariko Village",
                    "NPCs",
                ),
            ),
        ),
        (
            "Kak Anju Trade Pocket Cucco",
            (
                "NPC",
                0x52,
                0x0E,
                None,
                "Cojiro",
                (
                    "Kakariko Village",
                    "Kakariko",
                ),
            ),
        ),
        (
            "Kak Granny Trade Odd Mushroom",
            (
                "NPC",
                0x4E,
                0x20,
                None,
                "Odd Potion",
                (
                    "Kakariko Village",
                    "Kakariko",
                ),
            ),
        ),
        (
            "Kak Granny Buy Blue Potion",
            (
                "NPC",
                0x4E,
                0x12,
                None,
                "Blue Potion",
                (
                    "Kakariko Village",
                    "Kakariko",
                ),
            ),
        ),
        (
            "Kak Impas House Freestanding PoH",
            (
                "Collectable",
                0x37,
                0x01,
                None,
                "Piece of Heart",
                (
                    "Kakariko Village",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Kak Windmill Freestanding PoH",
            (
                "Collectable",
                0x48,
                0x01,
                None,
                "Piece of Heart",
                (
                    "Kakariko Village",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Kak Man on Roof",
            (
                "NPC",
                0x52,
                0x3E,
                None,
                "Piece of Heart",
                (
                    "Kakariko Village",
                    "NPCs",
                ),
            ),
        ),
        (
            "Kak Open Grotto Chest",
            (
                "Chest",
                0x3E,
                0x08,
                None,
                "Rupees (20)",
                (
                    "Kakariko Village",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "Kak Redead Grotto Chest",
            (
                "Chest",
                0x3E,
                0x0A,
                None,
                "Rupees (200)",
                (
                    "Kakariko Village",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "Kak Shooting Gallery Reward",
            (
                "NPC",
                0x42,
                0x30,
                None,
                "Bow",
                (
                    "Kakariko Village",
                    "Minigames",
                ),
            ),
        ),
        (
            "Kak 10 Gold Skulltula Reward",
            (
                "NPC",
                0x50,
                0x45,
                None,
                "Progressive Wallet",
                (
                    "Kakariko Village",
                    "Skulltula House",
                    "NPCs",
                ),
            ),
        ),
        (
            "Kak 20 Gold Skulltula Reward",
            (
                "NPC",
                0x50,
                0x39,
                None,
                "Stone of Agony",
                (
                    "Kakariko Village",
                    "Skulltula House",
                    "NPCs",
                ),
            ),
        ),
        (
            "Kak 30 Gold Skulltula Reward",
            (
                "NPC",
                0x50,
                0x46,
                None,
                "Progressive Wallet",
                (
                    "Kakariko Village",
                    "Skulltula House",
                    "NPCs",
                ),
            ),
        ),
        (
            "Kak 40 Gold Skulltula Reward",
            (
                "NPC",
                0x50,
                0x03,
                None,
                "Bombchus (10)",
                (
                    "Kakariko Village",
                    "Skulltula House",
                    "NPCs",
                ),
            ),
        ),
        (
            "Kak 50 Gold Skulltula Reward",
            (
                "NPC",
                0x50,
                0x3E,
                None,
                "Piece of Heart",
                (
                    "Kakariko Village",
                    "Skulltula House",
                    "NPCs",
                ),
            ),
        ),
        (
            "Kak Impas House Cow",
            (
                "NPC",
                0x37,
                0x15,
                None,
                "Milk",
                (
                    "Kakariko Village",
                    "Cows",
                ),
            ),
        ),
        (
            "Kak GS Tree",
            (
                "GS Token",
                0x10,
                0x20,
                None,
                "Gold Skulltula Token",
                (
                    "Kakariko Village",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Kak GS Near Gate Guard",
            (
                "GS Token",
                0x10,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Kakariko Village",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Kak GS Watchtower",
            (
                "GS Token",
                0x10,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Kakariko Village",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Kak GS Skulltula House",
            (
                "GS Token",
                0x10,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Kakariko Village",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Kak GS House Under Construction",
            (
                "GS Token",
                0x10,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Kakariko Village",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Kak GS Above Impas House",
            (
                "GS Token",
                0x10,
                0x40,
                None,
                "Gold Skulltula Token",
                (
                    "Kakariko Village",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Kak Bazaar Item 1",
            (
                "Shop",
                0x2C,
                0x38,
                (shop_address(5, 0), None),
                "Buy Hylian Shield",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Bazaar Item 2",
            (
                "Shop",
                0x2C,
                0x39,
                (shop_address(5, 1), None),
                "Buy Bombs (5) for 35 Rupees",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Bazaar Item 3",
            (
                "Shop",
                0x2C,
                0x3A,
                (shop_address(5, 2), None),
                "Buy Deku Nut (5)",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Bazaar Item 4",
            (
                "Shop",
                0x2C,
                0x3B,
                (shop_address(5, 3), None),
                "Buy Heart",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Bazaar Item 5",
            (
                "Shop",
                0x2C,
                0x3D,
                (shop_address(5, 4), None),
                "Buy Arrows (10)",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Bazaar Item 6",
            (
                "Shop",
                0x2C,
                0x3E,
                (shop_address(5, 5), None),
                "Buy Arrows (50)",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Bazaar Item 7",
            (
                "Shop",
                0x2C,
                0x3F,
                (shop_address(5, 6), None),
                "Buy Deku Stick (1)",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Bazaar Item 8",
            (
                "Shop",
                0x2C,
                0x40,
                (shop_address(5, 7), None),
                "Buy Arrows (30)",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Potion Shop Item 1",
            (
                "Shop",
                0x30,
                0x30,
                (shop_address(1, 0), None),
                "Buy Deku Nut (5)",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Potion Shop Item 2",
            (
                "Shop",
                0x30,
                0x31,
                (shop_address(1, 1), None),
                "Buy Fish",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Potion Shop Item 3",
            (
                "Shop",
                0x30,
                0x32,
                (shop_address(1, 2), None),
                "Buy Red Potion for 30 Rupees",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Potion Shop Item 4",
            (
                "Shop",
                0x30,
                0x33,
                (shop_address(1, 3), None),
                "Buy Green Potion",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Potion Shop Item 5",
            (
                "Shop",
                0x30,
                0x34,
                (shop_address(1, 4), None),
                "Buy Blue Fire",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Potion Shop Item 6",
            (
                "Shop",
                0x30,
                0x35,
                (shop_address(1, 5), None),
                "Buy Bottle Bug",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Potion Shop Item 7",
            (
                "Shop",
                0x30,
                0x36,
                (shop_address(1, 6), None),
                "Buy Poe",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        (
            "Kak Potion Shop Item 8",
            (
                "Shop",
                0x30,
                0x37,
                (shop_address(1, 7), None),
                "Buy Fairy's Spirit",
                (
                    "Kakariko Village",
                    "Shops",
                ),
            ),
        ),
        # Kakariko Village Pots
        (
            "Kak Near Potion Shop Pot 1",
            (
                "Pot",
                0x52,
                [(0, 0, 9), (0, 1, 8)],
                None,
                "Recovery Heart",
                (
                    "Kakariko Village",
                    "Pots",
                ),
            ),
        ),
        (
            "Kak Near Potion Shop Pot 2",
            (
                "Pot",
                0x52,
                [(0, 0, 10), (0, 1, 9)],
                None,
                "Recovery Heart",
                (
                    "Kakariko Village",
                    "Pots",
                ),
            ),
        ),
        (
            "Kak Near Potion Shop Pot 3",
            (
                "Pot",
                0x52,
                [(0, 0, 11), (0, 1, 10)],
                None,
                "Recovery Heart",
                (
                    "Kakariko Village",
                    "Pots",
                ),
            ),
        ),
        (
            "Kak Near Impas House Pot 1",
            (
                "Pot",
                0x52,
                [(0, 0, 12), (0, 1, 11)],
                None,
                "Recovery Heart",
                (
                    "Kakariko Village",
                    "Pots",
                ),
            ),
        ),
        (
            "Kak Near Impas House Pot 2",
            (
                "Pot",
                0x52,
                [(0, 0, 13), (0, 1, 12)],
                None,
                "Recovery Heart",
                (
                    "Kakariko Village",
                    "Pots",
                ),
            ),
        ),
        (
            "Kak Near Impas House Pot 3",
            (
                "Pot",
                0x52,
                [(0, 0, 14), (0, 1, 13)],
                None,
                "Recovery Heart",
                (
                    "Kakariko Village",
                    "Pots",
                ),
            ),
        ),
        (
            "Kak Near Guards House Pot 1",
            (
                "Pot",
                0x52,
                [(0, 0, 15), (0, 1, 14)],
                None,
                "Recovery Heart",
                (
                    "Kakariko Village",
                    "Pots",
                ),
            ),
        ),
        (
            "Kak Near Guards House Pot 2",
            (
                "Pot",
                0x52,
                [(0, 0, 16), (0, 1, 15)],
                None,
                "Recovery Heart",
                (
                    "Kakariko Village",
                    "Pots",
                ),
            ),
        ),
        (
            "Kak Near Guards House Pot 3",
            (
                "Pot",
                0x52,
                [(0, 0, 17), (0, 1, 16)],
                None,
                "Recovery Heart",
                (
                    "Kakariko Village",
                    "Pots",
                ),
            ),
        ),
        (
            "Kak Near Odd Medicine Building Pot 1",
            (
                "Pot",
                0x52,
                [(0, 0, 18), (0, 1, 17)],
                None,
                "Recovery Heart",
                (
                    "Kakariko Village",
                    "Pots",
                ),
            ),
        ),
        (
            "Kak Near Odd Medicine Building Pot 2",
            (
                "Pot",
                0x52,
                [(0, 0, 19), (0, 1, 18)],
                None,
                "Recovery Heart",
                (
                    "Kakariko Village",
                    "Pots",
                ),
            ),
        ),
        (
            "Kak Adult Crate 1",
            (
                "Crate",
                0x52,
                [(0, 2, 35), (0, 3, 33)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),  # Behind Skull House
        (
            "Kak Adult Crate 2",
            (
                "Crate",
                0x52,
                [(0, 2, 36), (0, 3, 34)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),  # Near Poor Kid
        (
            "Kak Adult Arrows Crate",
            (
                "Crate",
                0x52,
                [(0, 2, 37), (0, 3, 40)],
                None,
                "Arrows (10)",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),  # Near poor kid (arrows)
        (
            "Kak Adult Crate 3",
            (
                "Crate",
                0x52,
                [(0, 2, 38), (0, 3, 36)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),  # Near impas
        (
            "Kak Adult Crate 4",
            (
                "Crate",
                0x52,
                [(0, 2, 39), (0, 3, 37)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),  # near impas
        (
            "Kak Adult Crate 5",
            (
                "Crate",
                0x52,
                [(0, 2, 40), (0, 3, 38)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),  # Near house w/ talon
        (
            "Kak Adult Crate 6",
            (
                "Crate",
                0x52,
                [(0, 2, 41), (0, 3, 39)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),  # Near house w/ talon
        (
            "Kak Adult Crate 7",
            (
                "Crate",
                0x52,
                [(0, 2, 42), (0, 3, 35)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),  # Shooting gallery (normally night time 40)
        (
            "Kak Adult Crate 8",
            (
                "Crate",
                0x52,
                [(0, 2, 43), (0, 3, 41)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),  # Near potion shop
        (
            "Kak Adult Backyard Crate 1",
            (
                "Crate",
                0x52,
                [(0, 2, 44), (0, 3, 42)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),  # Backyard
        (
            "Kak Adult Backyard Crate 2",
            (
                "Crate",
                0x52,
                [(0, 2, 45), (0, 3, 44)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),
        (
            "Kak Adult Red Rupee Crate",
            (
                "Crate",
                0x52,
                [(0, 2, 46), (0, 3, 43)],
                None,
                "Rupees (20)",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),
        (
            "Kak Adult Backyard Crate 3",
            (
                "Crate",
                0x52,
                [(0, 2, 47), (0, 3, 45)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),
        (
            "Kak Child Crate 1",
            (
                "Crate",
                0x52,
                [(0, 0, 50), (0, 1, 43)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),
        (
            "Kak Child Crate 2",
            (
                "Crate",
                0x52,
                [(0, 0, 51), (0, 1, 44)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),
        (
            "Kak Child Crate 3",
            (
                "Crate",
                0x52,
                [(0, 0, 52), (0, 1, 45)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),
        (
            "Kak Child Crate 4",
            (
                "Crate",
                0x52,
                [(0, 0, 53), (0, 1, 46)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),
        (
            "Kak Child Crate 5",
            (
                "Crate",
                0x52,
                [(0, 0, 54), (0, 1, 47)],
                None,
                "Nothing",
                (
                    "Kakariko Village",
                    "Crates",
                ),
            ),
        ),
        # Kakariko Village Beehives
        (
            "Kak Open Grotto Beehive 1",
            (
                "Beehive",
                0x3E,
                (0, 0x08, 8),
                None,
                "Rupees (5)",
                (
                    "Kakariko Village",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "Kak Open Grotto Beehive 2",
            (
                "Beehive",
                0x3E,
                (0, 0x08, 9),
                None,
                "Rupees (20)",
                (
                    "Kakariko Village",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        # Kakariko Village Wonderitems
        (
            "Kak Child Construction Wonderitem",
            (
                "Wonderitem",
                0x52,
                [(0, 0, 56), (0, 1, 49)],
                None,
                "Rupees (20)",
                ("Kakariko Village", "Wonderitem"),
            ),
        ),
        (
            "Kak Impas House Wonderitem",
            (
                "Wonderitem",
                0x37,
                (0, 0, 7),
                None,
                "Rupees (20)",
                ("Kakariko Village", "Wonderitem"),
            ),
        ),
        # Graveyard
        (
            "Graveyard Shield Grave Chest",
            (
                "Chest",
                0x40,
                0x00,
                None,
                "Hylian Shield",
                (
                    "Graveyard",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "Graveyard Heart Piece Grave Chest",
            (
                "Chest",
                0x3F,
                0x00,
                None,
                "Piece of Heart",
                (
                    "Graveyard",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "Graveyard Royal Familys Tomb Chest",
            (
                "Chest",
                0x41,
                0x00,
                None,
                "Bombs (5)",
                (
                    "Graveyard",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "Graveyard Freestanding PoH",
            (
                "Collectable",
                0x53,
                0x04,
                None,
                "Piece of Heart",
                (
                    "Graveyard",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Graveyard Dampe Gravedigging Tour",
            (
                "Collectable",
                0x53,
                0x08,
                None,
                "Piece of Heart",
                (
                    "Graveyard",
                    "Minigames",
                ),
            ),
        ),
        (
            "Graveyard Dampe Race Hookshot Chest",
            (
                "Chest",
                0x48,
                0x00,
                None,
                "Progressive Hookshot",
                (
                    "Graveyard",
                    "Grottos",
                    "Minigames",
                    "Chests",
                ),
            ),
        ),
        (
            "Graveyard Dampe Race Freestanding PoH",
            (
                "Collectable",
                0x48,
                0x07,
                None,
                "Piece of Heart",
                (
                    "Graveyard",
                    "Grottos",
                    "Minigames",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Graveyard GS Bean Patch",
            (
                "GS Token",
                0x10,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Graveyard",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Graveyard GS Wall",
            (
                "GS Token",
                0x10,
                0x80,
                None,
                "Gold Skulltula Token",
                (
                    "Graveyard",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Graveyard Freestanding
        (
            "Graveyard Dampe Race Rupee 1",
            (
                "Freestanding",
                0x48,
                (1, 0, 1),
                None,
                "Rupee (1)",
                (
                    "Graveyard",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Graveyard Dampe Race Rupee 2",
            (
                "Freestanding",
                0x48,
                (1, 0, 2),
                None,
                "Rupee (1)",
                (
                    "Graveyard",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Graveyard Dampe Race Rupee 3",
            (
                "Freestanding",
                0x48,
                (1, 0, 3),
                None,
                "Rupee (1)",
                (
                    "Graveyard",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Graveyard Dampe Race Rupee 4",
            (
                "Freestanding",
                0x48,
                (2, 0, 1),
                None,
                "Rupee (1)",
                (
                    "Graveyard",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Graveyard Dampe Race Rupee 5",
            (
                "Freestanding",
                0x48,
                (2, 0, 2),
                None,
                "Rupee (1)",
                (
                    "Graveyard",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Graveyard Dampe Race Rupee 6",
            (
                "Freestanding",
                0x48,
                (2, 0, 3),
                None,
                "Rupee (1)",
                (
                    "Graveyard",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Graveyard Dampe Race Rupee 7",
            (
                "Freestanding",
                0x48,
                (3, 0, 1),
                None,
                "Rupee (1)",
                (
                    "Graveyard",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Graveyard Dampe Race Rupee 8",
            (
                "Freestanding",
                0x48,
                (3, 0, 2),
                None,
                "Rupee (1)",
                (
                    "Graveyard",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        # Graveyard Pots/Crates
        (
            "Graveyard Freestanding PoH Crate",
            (
                "Crate",
                0x53,
                [(1, 0, 22), (1, 1, 24), (1, 2, 34), (1, 3, 34)],
                None,
                "Nothing",
                ("Graveyard", "Crates"),
            ),
        ),
        (
            "Graveyard Dampe Pot 1",
            (
                "Pot",
                0x48,
                (0, 0, 1),
                None,
                "Recovery Heart",
                (
                    "Graveyard",
                    "Grottos",
                    "Pots",
                ),
            ),
        ),
        (
            "Graveyard Dampe Pot 2",
            (
                "Pot",
                0x48,
                (0, 0, 2),
                None,
                "Deku Nuts (5)",
                (
                    "Graveyard",
                    "Grottos",
                    "Pots",
                ),
            ),
        ),
        (
            "Graveyard Dampe Pot 3",
            (
                "Pot",
                0x48,
                (0, 0, 3),
                None,
                "Bombs (5)",
                (
                    "Graveyard",
                    "Grottos",
                    "Pots",
                ),
            ),
        ),
        (
            "Graveyard Dampe Pot 4",
            (
                "Pot",
                0x48,
                (0, 0, 4),
                None,
                "Arrows (10)",
                (
                    "Graveyard",
                    "Grottos",
                    "Pots",
                ),
            ),
        ),
        (
            "Graveyard Dampe Pot 5",
            (
                "Pot",
                0x48,
                (0, 0, 5),
                None,
                "Rupees (20)",
                (
                    "Graveyard",
                    "Grottos",
                    "Pots",
                ),
            ),
        ),
        (
            "Graveyard Dampe Pot 6",
            (
                "Pot",
                0x48,
                (0, 0, 6),
                None,
                "Rupees (20)",
                (
                    "Graveyard",
                    "Grottos",
                    "Pots",
                ),
            ),
        ),
        # Graveyard Wonderitems
        (
            "Graveyard Dampe Race Wonderitem 1",
            (
                "Wonderitem",
                0x48,
                (1, 0, 6),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 2",
            (
                "Wonderitem",
                0x48,
                (1, 0, 7),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 3",
            (
                "Wonderitem",
                0x48,
                (1, 0, 8),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 4",
            (
                "Wonderitem",
                0x48,
                (1, 0, 9),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 5",
            (
                "Wonderitem",
                0x48,
                (1, 0, 10),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 6",
            (
                "Wonderitem",
                0x48,
                (2, 0, 8),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 7",
            (
                "Wonderitem",
                0x48,
                (2, 0, 9),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 8",
            (
                "Wonderitem",
                0x48,
                (2, 0, 10),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 9",
            (
                "Wonderitem",
                0x48,
                (2, 0, 11),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 10",
            (
                "Wonderitem",
                0x48,
                (2, 0, 12),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 11",
            (
                "Wonderitem",
                0x48,
                (3, 0, 9),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 12",
            (
                "Wonderitem",
                0x48,
                (3, 0, 10),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 13",
            (
                "Wonderitem",
                0x48,
                (3, 0, 11),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 14",
            (
                "Wonderitem",
                0x48,
                (3, 0, 12),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        (
            "Graveyard Dampe Race Wonderitem 15",
            (
                "Wonderitem",
                0x48,
                (3, 0, 13),
                None,
                "Rupees (5)",
                ("Graveyard", "Grottos", "Wonderitem"),
            ),
        ),
        # Death Mountain Trail
        (
            "DMT Freestanding PoH",
            (
                "Collectable",
                0x60,
                0x1E,
                None,
                "Piece of Heart",
                (
                    "Death Mountain Trail",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMT Chest",
            (
                "Chest",
                0x60,
                0x01,
                None,
                "Rupees (50)",
                (
                    "Death Mountain Trail",
                    "Chests",
                ),
            ),
        ),
        (
            "DMT Storms Grotto Chest",
            (
                "Chest",
                0x3E,
                0x17,
                None,
                "Rupees (200)",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "DMT Great Fairy Reward",
            (
                "Cutscene",
                0xFF,
                0x13,
                None,
                "Magic Meter",
                (
                    "Death Mountain Trail",
                    "Great Fairies",
                ),
            ),
        ),
        (
            "DMT Biggoron",
            (
                "NPC",
                0x60,
                0x57,
                None,
                "Biggoron Sword",
                (
                    "Death Mountain Trail",
                    "NPCs",
                ),
            ),
        ),
        (
            "DMT Trade Broken Sword",
            (
                "NPC",
                0x60,
                0x23,
                None,
                "Prescription",
                (
                    "Death Mountain Trail",
                    "Death Mountain",
                ),
            ),
        ),
        (
            "DMT Trade Eyedrops",
            (
                "NPC",
                0x60,
                0x26,
                None,
                "Claim Check",
                (
                    "Death Mountain Trail",
                    "Death Mountain",
                ),
            ),
        ),
        (
            "DMT Cow Grotto Cow",
            (
                "NPC",
                0x3E,
                0x15,
                None,
                "Milk",
                (
                    "Death Mountain Trail",
                    "Cows",
                    "Grottos",
                ),
            ),
        ),
        (
            "DMT GS Near Kak",
            (
                "GS Token",
                0x0F,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Death Mountain Trail",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "DMT GS Bean Patch",
            (
                "GS Token",
                0x0F,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Death Mountain Trail",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "DMT GS Above Dodongos Cavern",
            (
                "GS Token",
                0x0F,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Death Mountain Trail",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "DMT GS Falling Rocks Path",
            (
                "GS Token",
                0x0F,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Death Mountain Trail",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Death Mountain Trail Freestanding
        (
            "DMT Rock Red Rupee",
            (
                "Freestanding",
                0x60,
                (0, 0, 2),
                None,
                "Rupees (20)",
                (
                    "Death Mountain Trail",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMT Rock Blue Rupee",
            (
                "Freestanding",
                0x60,
                (0, 0, 3),
                None,
                "Rupees (5)",
                (
                    "Death Mountain Trail",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMT Cow Grotto Green Rupee 1",
            (
                "RupeeTower",
                0x3E,
                (3, 0x18, 6, 1),
                None,
                "Rupee (1)",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMT Cow Grotto Green Rupee 2",
            (
                "RupeeTower",
                0x3E,
                (3, 0x18, 6, 2),
                None,
                "Rupee (1)",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMT Cow Grotto Green Rupee 3",
            (
                "RupeeTower",
                0x3E,
                (3, 0x18, 6, 3),
                None,
                "Rupee (1)",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMT Cow Grotto Green Rupee 4",
            (
                "RupeeTower",
                0x3E,
                (3, 0x18, 6, 4),
                None,
                "Rupee (1)",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMT Cow Grotto Green Rupee 5",
            (
                "RupeeTower",
                0x3E,
                (3, 0x18, 6, 5),
                None,
                "Rupee (1)",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMT Cow Grotto Green Rupee 6",
            (
                "RupeeTower",
                0x3E,
                (3, 0x18, 6, 6),
                None,
                "Rupee (1)",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMT Cow Grotto Red Rupee",
            (
                "RupeeTower",
                0x3E,
                (3, 0x18, 6, 7),
                None,
                "Rupees (20)",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMT Cow Grotto Recovery Heart 1",
            (
                "Freestanding",
                0x3E,
                (3, 0x18, 7),
                None,
                "Recovery Heart",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMT Cow Grotto Recovery Heart 2",
            (
                "Freestanding",
                0x3E,
                (3, 0x18, 8),
                None,
                "Recovery Heart",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMT Cow Grotto Recovery Heart 3",
            (
                "Freestanding",
                0x3E,
                (3, 0x18, 9),
                None,
                "Recovery Heart",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMT Cow Grotto Recovery Heart 4",
            (
                "Freestanding",
                0x3E,
                (3, 0x18, 10),
                None,
                "Recovery Heart",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        # Death Mountain Trial Beehives
        (
            "DMT Cow Grotto Beehive",
            (
                "Beehive",
                0x3E,
                (3, 0x18, 4),
                None,
                "Rupees (20)",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "DMT Storms Grotto Beehive 1",
            (
                "Beehive",
                0x3E,
                (0, 0x17, 8),
                None,
                "Rupees (5)",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "DMT Storms Grotto Beehive 2",
            (
                "Beehive",
                0x3E,
                (0, 0x17, 9),
                None,
                "Rupees (20)",
                (
                    "Death Mountain Trail",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        # Goron City
        (
            "GC Darunias Joy",
            (
                "NPC",
                0x62,
                0x54,
                None,
                "Progressive Strength Upgrade",
                (
                    "Goron City",
                    "NPCs",
                ),
            ),
        ),
        (
            "GC Pot Freestanding PoH",
            (
                "Collectable",
                0x62,
                0x1F,
                None,
                "Piece of Heart",
                (
                    "Goron City",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GC Rolling Goron as Child",
            (
                "NPC",
                0x62,
                0x34,
                None,
                "Bomb Bag",
                (
                    "Goron City",
                    "NPCs",
                ),
            ),
        ),
        (
            "GC Rolling Goron as Adult",
            (
                "NPC",
                0x62,
                0x2C,
                None,
                "Goron Tunic",
                (
                    "Goron City",
                    "NPCs",
                ),
            ),
        ),
        (
            "GC Medigoron",
            (
                "NPC",
                0x62,
                0x28,
                None,
                "Giants Knife",
                (
                    "Goron City",
                    "NPCs",
                ),
            ),
        ),
        (
            "GC Maze Left Chest",
            (
                "Chest",
                0x62,
                0x00,
                None,
                "Rupees (200)",
                (
                    "Goron City",
                    "Chests",
                ),
            ),
        ),
        (
            "GC Maze Center Chest",
            (
                "Chest",
                0x62,
                0x02,
                None,
                "Rupees (50)",
                (
                    "Goron City",
                    "Chests",
                ),
            ),
        ),
        (
            "GC Maze Right Chest",
            (
                "Chest",
                0x62,
                0x01,
                None,
                "Rupees (50)",
                (
                    "Goron City",
                    "Chests",
                ),
            ),
        ),
        (
            "GC Deku Scrub Grotto Left",
            (
                "GrottoScrub",
                0xFB,
                0x30,
                None,
                "Buy Deku Nut (5)",
                (
                    "Goron City",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "GC Deku Scrub Grotto Center",
            (
                "GrottoScrub",
                0xFB,
                0x33,
                None,
                "Buy Arrows (30)",
                (
                    "Goron City",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "GC Deku Scrub Grotto Right",
            (
                "GrottoScrub",
                0xFB,
                0x37,
                None,
                "Buy Bombs (5) for 35 Rupees",
                (
                    "Goron City",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "GC GS Center Platform",
            (
                "GS Token",
                0x0F,
                0x20,
                None,
                "Gold Skulltula Token",
                (
                    "Goron City",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "GC GS Boulder Maze",
            (
                "GS Token",
                0x0F,
                0x40,
                None,
                "Gold Skulltula Token",
                (
                    "Goron City",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "GC Shop Item 1",
            (
                "Shop",
                0x2E,
                0x30,
                (shop_address(8, 0), None),
                "Buy Bombs (5) for 25 Rupees",
                (
                    "Goron City",
                    "Shops",
                ),
            ),
        ),
        (
            "GC Shop Item 2",
            (
                "Shop",
                0x2E,
                0x31,
                (shop_address(8, 1), None),
                "Buy Bombs (10)",
                (
                    "Goron City",
                    "Shops",
                ),
            ),
        ),
        (
            "GC Shop Item 3",
            (
                "Shop",
                0x2E,
                0x32,
                (shop_address(8, 2), None),
                "Buy Bombs (20)",
                (
                    "Goron City",
                    "Shops",
                ),
            ),
        ),
        (
            "GC Shop Item 4",
            (
                "Shop",
                0x2E,
                0x33,
                (shop_address(8, 3), None),
                "Buy Bombs (30)",
                (
                    "Goron City",
                    "Shops",
                ),
            ),
        ),
        (
            "GC Shop Item 5",
            (
                "Shop",
                0x2E,
                0x34,
                (shop_address(8, 4), None),
                "Buy Goron Tunic",
                (
                    "Goron City",
                    "Shops",
                ),
            ),
        ),
        (
            "GC Shop Item 6",
            (
                "Shop",
                0x2E,
                0x35,
                (shop_address(8, 5), None),
                "Buy Heart",
                (
                    "Goron City",
                    "Shops",
                ),
            ),
        ),
        (
            "GC Shop Item 7",
            (
                "Shop",
                0x2E,
                0x36,
                (shop_address(8, 6), None),
                "Buy Red Potion for 40 Rupees",
                (
                    "Goron City",
                    "Shops",
                ),
            ),
        ),
        (
            "GC Shop Item 8",
            (
                "Shop",
                0x2E,
                0x37,
                (shop_address(8, 7), None),
                "Buy Heart",
                (
                    "Goron City",
                    "Shops",
                ),
            ),
        ),
        (
            "GC Spinning Pot Bomb Drop 1",
            (
                "Freestanding",
                0x62,
                (3, 0, 41, 1),
                None,
                "Bombs (5)",
                (
                    "Goron City",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GC Spinning Pot Bomb Drop 2",
            (
                "Freestanding",
                0x62,
                (3, 0, 41, 2),
                None,
                "Bombs (5)",
                (
                    "Goron City",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GC Spinning Pot Bomb Drop 3",
            (
                "Freestanding",
                0x62,
                (3, 0, 41, 3),
                None,
                "Bombs (5)",
                (
                    "Goron City",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GC Spinning Pot Rupee Drop 1",
            (
                "Freestanding",
                0x62,
                (3, 0, 41, 4),
                None,
                "Rupee (1)",
                (
                    "Goron City",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GC Spinning Pot Rupee Drop 2",
            (
                "Freestanding",
                0x62,
                (3, 0, 41, 5),
                None,
                "Rupee (1)",
                (
                    "Goron City",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GC Spinning Pot Rupee Drop 3",
            (
                "Freestanding",
                0x62,
                (3, 0, 41, 6),
                None,
                "Rupee (1)",
                (
                    "Goron City",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GC Spinning Pot PoH Drop Rupee 1",
            (
                "Freestanding",
                0x62,
                (3, 0, 41, 7),
                None,
                "Rupees (20)",
                (
                    "Goron City",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GC Spinning Pot PoH Drop Rupee 2",
            (
                "Freestanding",
                0x62,
                (3, 0, 41, 8),
                None,
                "Rupees (5)",
                (
                    "Goron City",
                    "Freestandings",
                ),
            ),
        ),
        # Goron City Pots.
        (
            "GC Darunia Pot 1",
            (
                "Pot",
                0x62,
                [(1, 0, 6), (1, 2, 2)],
                None,
                "Deku Stick (1)",
                (
                    "Goron City",
                    "Pots",
                ),
            ),
        ),
        (
            "GC Darunia Pot 2",
            (
                "Pot",
                0x62,
                [(1, 0, 7), (1, 2, 3)],
                None,
                "Rupee (1)",
                (
                    "Goron City",
                    "Pots",
                ),
            ),
        ),
        (
            "GC Darunia Pot 3",
            (
                "Pot",
                0x62,
                [(1, 0, 8), (1, 2, 4)],
                None,
                "Deku Stick (1)",
                (
                    "Goron City",
                    "Pots",
                ),
            ),
        ),
        (
            "GC Medigoron Pot",
            (
                "Pot",
                0x62,
                [(2, 0, 4), (2, 2, 4)],
                None,
                "Rupees (5)",
                (
                    "Goron City",
                    "Pots",
                ),
            ),
        ),
        (
            "GC Lower Staircase Pot 1",
            (
                "Pot",
                0x62,
                [(3, 0, 42), (3, 2, 9)],
                None,
                "Deku Stick (1)",
                (
                    "Goron City",
                    "Pots",
                ),
            ),
        ),
        (
            "GC Lower Staircase Pot 2",
            (
                "Pot",
                0x62,
                [(3, 0, 46), (3, 2, 13)],
                None,
                "Recovery Heart",
                (
                    "Goron City",
                    "Pots",
                ),
            ),
        ),
        (
            "GC Upper Staircase Pot 1",
            (
                "Pot",
                0x62,
                [(3, 0, 43), (3, 2, 10)],
                None,
                "Rupees (5)",
                (
                    "Goron City",
                    "Pots",
                ),
            ),
        ),
        (
            "GC Upper Staircase Pot 2",
            (
                "Pot",
                0x62,
                [(3, 0, 44), (3, 2, 11)],
                None,
                "Rupee (1)",
                (
                    "Goron City",
                    "Pots",
                ),
            ),
        ),
        (
            "GC Upper Staircase Pot 3",
            (
                "Pot",
                0x62,
                [(3, 0, 45), (3, 2, 12)],
                None,
                "Rupees (5)",
                (
                    "Goron City",
                    "Pots",
                ),
            ),
        ),
        (
            "GC Boulder Maze Crate",
            (
                "Crate",
                0x62,
                [(0, 0, 50), (0, 2, 47)],
                None,
                "Rupee (1)",
                (
                    "Goron City",
                    "Crates",
                ),
            ),
        ),
        # Goron City Beehives
        (
            "GC Grotto Beehive",
            (
                "Beehive",
                0x3E,
                (12, 0x1B, 4),
                None,
                "Rupees (20)",
                (
                    "Goron City",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        # Death Mountain Crater
        (
            "DMC Volcano Freestanding PoH",
            (
                "Collectable",
                0x61,
                0x08,
                None,
                "Piece of Heart",
                (
                    "Death Mountain Crater",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMC Wall Freestanding PoH",
            (
                "Collectable",
                0x61,
                0x02,
                None,
                "Piece of Heart",
                (
                    "Death Mountain Crater",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMC Upper Grotto Chest",
            (
                "Chest",
                0x3E,
                0x1A,
                None,
                "Bombs (20)",
                (
                    "Death Mountain Crater",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "DMC Great Fairy Reward",
            (
                "Cutscene",
                0xFF,
                0x14,
                None,
                "Magic Meter",
                (
                    "Death Mountain Crater",
                    "Great Fairies",
                ),
            ),
        ),
        (
            "DMC Deku Scrub",
            (
                "Scrub",
                0x61,
                0x37,
                None,
                "Buy Bombs (5) for 35 Rupees",
                (
                    "Death Mountain Crater",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "DMC Deku Scrub Grotto Left",
            (
                "GrottoScrub",
                0xF9,
                0x30,
                None,
                "Buy Deku Nut (5)",
                (
                    "Death Mountain Crater",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "DMC Deku Scrub Grotto Center",
            (
                "GrottoScrub",
                0xF9,
                0x33,
                None,
                "Buy Arrows (30)",
                (
                    "Death Mountain Crater",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "DMC Deku Scrub Grotto Right",
            (
                "GrottoScrub",
                0xF9,
                0x37,
                None,
                "Buy Bombs (5) for 35 Rupees",
                (
                    "Death Mountain Crater",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "DMC GS Crate",
            (
                "GS Token",
                0x0F,
                0x80,
                None,
                "Gold Skulltula Token",
                (
                    "Death Mountain Crater",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "DMC GS Bean Patch",
            (
                "GS Token",
                0x0F,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Death Mountain Crater",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Death Mountain Crater Freestanding
        (
            "DMC Adult Green Rupee 1",
            (
                "RupeeTower",
                0x61,
                (1, 2, 19, 1),
                None,
                "Rupee (1)",
                (
                    "Death Mountain Crater",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMC Adult Green Rupee 2",
            (
                "RupeeTower",
                0x61,
                (1, 2, 19, 2),
                None,
                "Rupee (1)",
                (
                    "Death Mountain Crater",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMC Adult Green Rupee 3",
            (
                "RupeeTower",
                0x61,
                (1, 2, 19, 3),
                None,
                "Rupee (1)",
                (
                    "Death Mountain Crater",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMC Adult Green Rupee 4",
            (
                "RupeeTower",
                0x61,
                (1, 2, 19, 4),
                None,
                "Rupee (1)",
                (
                    "Death Mountain Crater",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMC Adult Green Rupee 5",
            (
                "RupeeTower",
                0x61,
                (1, 2, 19, 5),
                None,
                "Rupee (1)",
                (
                    "Death Mountain Crater",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMC Adult Green Rupee 6",
            (
                "RupeeTower",
                0x61,
                (1, 2, 19, 6),
                None,
                "Rupee (1)",
                (
                    "Death Mountain Crater",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMC Adult Red Rupee",
            (
                "RupeeTower",
                0x61,
                (1, 2, 19, 7),
                None,
                "Rupees (20)",
                (
                    "Death Mountain Crater",
                    "Rupee Towers",
                ),
            ),
        ),
        (
            "DMC Child Red Rupee 1",
            (
                "Freestanding",
                0x61,
                (1, 0, 2),
                None,
                "Rupees (20)",
                (
                    "Death Mountain Crater",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMC Child Red Rupee 2",
            (
                "Freestanding",
                0x61,
                (1, 0, 3),
                None,
                "Rupees (20)",
                (
                    "Death Mountain Crater",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMC Child Blue Rupee 1",
            (
                "Freestanding",
                0x61,
                (1, 0, 4),
                None,
                "Rupees (5)",
                (
                    "Death Mountain Crater",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMC Child Blue Rupee 2",
            (
                "Freestanding",
                0x61,
                (1, 0, 5),
                None,
                "Rupees (5)",
                (
                    "Death Mountain Crater",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMC Child Blue Rupee 3",
            (
                "Freestanding",
                0x61,
                (1, 0, 6),
                None,
                "Rupees (5)",
                (
                    "Death Mountain Crater",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMC Child Blue Rupee 4",
            (
                "Freestanding",
                0x61,
                (1, 0, 7),
                None,
                "Rupees (5)",
                (
                    "Death Mountain Crater",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMC Child Blue Rupee 5",
            (
                "Freestanding",
                0x61,
                (1, 0, 8),
                None,
                "Rupees (5)",
                (
                    "Death Mountain Crater",
                    "Freestandings",
                ),
            ),
        ),
        (
            "DMC Child Blue Rupee 6",
            (
                "Freestanding",
                0x61,
                (1, 0, 9),
                None,
                "Rupees (5)",
                (
                    "Death Mountain Crater",
                    "Freestandings",
                ),
            ),
        ),
        # Death Mountain Crater Pots
        (
            "DMC Near GC Pot 1",
            (
                "Pot",
                0x61,
                [(1, 2, 14), (1, 0, 16)],
                None,
                "Recovery Heart",
                (
                    "Death Mountain Crater",
                    "Pots",
                ),
            ),
        ),
        (
            "DMC Near GC Pot 2",
            (
                "Pot",
                0x61,
                [(1, 2, 15), (1, 0, 17)],
                None,
                "Arrows (10)",
                (
                    "Death Mountain Crater",
                    "Pots",
                ),
            ),
        ),
        (
            "DMC Near GC Pot 3",
            (
                "Pot",
                0x61,
                [(1, 2, 16), (1, 0, 18)],
                None,
                "Rupees (5)",
                (
                    "Death Mountain Crater",
                    "Pots",
                ),
            ),
        ),
        (
            "DMC Near GC Pot 4",
            (
                "Pot",
                0x61,
                [(1, 2, 17), (1, 0, 19)],
                None,
                "Rupees (5)",
                (
                    "Death Mountain Crater",
                    "Pots",
                ),
            ),
        ),
        # Death mountain Crater Beehives
        (
            "DMC Upper Grotto Beehive 1",
            (
                "Beehive",
                0x3E,
                (0, 0x1A, 8),
                None,
                "Rupees (5)",
                (
                    "Death Mountain Crater",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "DMC Upper Grotto Beehive 2",
            (
                "Beehive",
                0x3E,
                (0, 0x1A, 9),
                None,
                "Rupees (20)",
                (
                    "Death Mountain Crater",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "DMC Hammer Grotto Beehive",
            (
                "Beehive",
                0x3E,
                (12, 0x19, 4),
                None,
                "Rupees (20)",
                (
                    "Death Mountain Crater",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        # Zora's River
        (
            "ZR Magic Bean Salesman",
            (
                "NPC",
                0x54,
                0x16,
                None,
                "Buy Magic Bean",
                (
                    "Zora's River",
                    "NPCs",
                ),
            ),
        ),
        (
            "ZR Open Grotto Chest",
            (
                "Chest",
                0x3E,
                0x09,
                None,
                "Rupees (20)",
                (
                    "Zora's River",
                    "Grottos",
                    "Chests",
                ),
            ),
        ),
        (
            "ZR Frogs Zeldas Lullaby",
            (
                "NPC",
                0x54,
                0x65,
                None,
                "Rupees (50)",
                (
                    "Zora's River",
                    "Minigames",
                ),
            ),
        ),
        (
            "ZR Frogs Eponas Song",
            (
                "NPC",
                0x54,
                0x66,
                None,
                "Rupees (50)",
                (
                    "Zora's River",
                    "Minigames",
                ),
            ),
        ),
        (
            "ZR Frogs Sarias Song",
            (
                "NPC",
                0x54,
                0x67,
                None,
                "Rupees (50)",
                (
                    "Zora's River",
                    "Minigames",
                ),
            ),
        ),
        (
            "ZR Frogs Suns Song",
            (
                "NPC",
                0x54,
                0x68,
                None,
                "Rupees (50)",
                (
                    "Zora's River",
                    "Minigames",
                ),
            ),
        ),
        (
            "ZR Frogs Song of Time",
            (
                "NPC",
                0x54,
                0x69,
                None,
                "Rupees (50)",
                (
                    "Zora's River",
                    "Minigames",
                ),
            ),
        ),
        (
            "ZR Frogs in the Rain",
            (
                "NPC",
                0x54,
                0x3E,
                None,
                "Piece of Heart",
                (
                    "Zora's River",
                    "Minigames",
                ),
            ),
        ),
        (
            "ZR Frogs Ocarina Game",
            (
                "NPC",
                0x54,
                0x76,
                None,
                "Piece of Heart",
                (
                    "Zora's River",
                    "Minigames",
                ),
            ),
        ),
        (
            "ZR Near Open Grotto Freestanding PoH",
            (
                "Collectable",
                0x54,
                0x04,
                None,
                "Piece of Heart",
                (
                    "Zora's River",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZR Near Domain Freestanding PoH",
            (
                "Collectable",
                0x54,
                0x0B,
                None,
                "Piece of Heart",
                (
                    "Zora's River",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZR Deku Scrub Grotto Front",
            (
                "GrottoScrub",
                0xEB,
                0x3A,
                None,
                "Buy Green Potion",
                (
                    "Zora's River",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "ZR Deku Scrub Grotto Rear",
            (
                "GrottoScrub",
                0xEB,
                0x39,
                None,
                "Buy Red Potion for 30 Rupees",
                (
                    "Zora's River",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "ZR GS Tree",
            (
                "GS Token",
                0x11,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Zora's River",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "ZR GS Ladder",
            (
                "GS Token",
                0x11,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Zora's River",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "ZR GS Near Raised Grottos",
            (
                "GS Token",
                0x11,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Zora's River",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "ZR GS Above Bridge",
            (
                "GS Token",
                0x11,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Zora's River",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Zora's River Freestanding
        (
            "ZR Waterfall Red Rupee 1",
            (
                "Freestanding",
                0x54,
                (1, 2, 2),
                None,
                "Rupees (20)",
                (
                    "Zora's River",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZR Waterfall Red Rupee 2",
            (
                "Freestanding",
                0x54,
                (1, 2, 3),
                None,
                "Rupees (20)",
                (
                    "Zora's River",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZR Waterfall Red Rupee 3",
            (
                "Freestanding",
                0x54,
                (1, 2, 4),
                None,
                "Rupees (20)",
                (
                    "Zora's River",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZR Waterfall Red Rupee 4",
            (
                "Freestanding",
                0x54,
                (1, 2, 5),
                None,
                "Rupees (20)",
                (
                    "Zora's River",
                    "Freestandings",
                ),
            ),
        ),
        # Zora's River Beehives
        (
            "ZR Open Grotto Beehive 1",
            (
                "Beehive",
                0x3E,
                (0, 0x09, 8),
                None,
                "Rupees (5)",
                (
                    "Zora's River",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "ZR Open Grotto Beehive 2",
            (
                "Beehive",
                0x3E,
                (0, 0x09, 9),
                None,
                "Rupees (20)",
                (
                    "Zora's River",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        (
            "ZR Storms Grotto Beehive",
            (
                "Beehive",
                0x3E,
                (9, 0x0B, 3),
                None,
                "Rupees (20)",
                (
                    "Zora's River",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        # Zora's River Wonderitems
        (
            "ZR Child Front River Wonderitem 1",
            ("Wonderitem", 0x54, (0, 0, 17), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child Front River Wonderitem 2",
            ("Wonderitem", 0x54, (0, 0, 18), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child Front River Wonderitem 3",
            ("Wonderitem", 0x54, (0, 0, 19), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child Front River Wonderitem 4",
            ("Wonderitem", 0x54, (0, 0, 20), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 1",
            ("Wonderitem", 0x54, (1, 0, 6), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 2",
            ("Wonderitem", 0x54, (1, 0, 7), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 3",
            ("Wonderitem", 0x54, (1, 0, 8), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 4",
            ("Wonderitem", 0x54, (1, 0, 9), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 5",
            ("Wonderitem", 0x54, (0, 0, 16), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 6",
            ("Wonderitem", 0x54, (0, 0, 21), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 7",
            ("Wonderitem", 0x54, (0, 0, 22), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 8",
            ("Wonderitem", 0x54, (0, 0, 23), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 9",
            ("Wonderitem", 0x54, (0, 0, 24), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 10",
            ("Wonderitem", 0x54, (0, 0, 25), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 11",
            ("Wonderitem", 0x54, (0, 0, 26), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 12",
            ("Wonderitem", 0x54, (0, 0, 27), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 13",
            ("Wonderitem", 0x54, (0, 0, 28), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 14",
            ("Wonderitem", 0x54, (0, 0, 29), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 15",
            ("Wonderitem", 0x54, (0, 0, 30), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 16",
            ("Wonderitem", 0x54, (0, 0, 31), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 17",
            ("Wonderitem", 0x54, (0, 0, 32), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 18",
            ("Wonderitem", 0x54, (0, 0, 33), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 19",
            ("Wonderitem", 0x54, (0, 0, 34), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 20",
            ("Wonderitem", 0x54, (0, 0, 35), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 21",
            ("Wonderitem", 0x54, (0, 0, 36), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 22",
            ("Wonderitem", 0x54, (0, 0, 37), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 23",
            ("Wonderitem", 0x54, (0, 0, 38), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 24",
            ("Wonderitem", 0x54, (0, 0, 39), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 25",
            ("Wonderitem", 0x54, (0, 0, 40), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 26",
            ("Wonderitem", 0x54, (0, 0, 41), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        (
            "ZR Child River Wonderitem 27",
            ("Wonderitem", 0x54, (0, 0, 42), None, "Rupees (5)", ("Zora's River", "Wonderitem")),
        ),
        # Zora's Domain
        (
            "ZD Diving Minigame",
            (
                "NPC",
                0x58,
                0x37,
                None,
                "Progressive Scale",
                (
                    "Zora's Domain",
                    "Minigames",
                ),
            ),
        ),
        (
            "ZD Chest",
            (
                "Chest",
                0x58,
                0x00,
                None,
                "Piece of Heart",
                (
                    "Zora's Domain",
                    "Chests",
                ),
            ),
        ),
        (
            "ZD King Zora Thawed",
            (
                "NPC",
                0x58,
                0x2D,
                None,
                "Zora Tunic",
                (
                    "Zora's Domain",
                    "NPCs",
                ),
            ),
        ),
        ("ZD Trade Prescription", ("NPC", 0x58, 0x24, None, "Eyeball Frog", ("Zora's Domain",))),
        (
            "ZD GS Frozen Waterfall",
            (
                "GS Token",
                0x11,
                0x40,
                None,
                "Gold Skulltula Token",
                (
                    "Zora's Domain",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "ZD Shop Item 1",
            (
                "Shop",
                0x2F,
                0x30,
                (shop_address(7, 0), None),
                "Buy Zora Tunic",
                (
                    "Zora's Domain",
                    "Shops",
                ),
            ),
        ),
        (
            "ZD Shop Item 2",
            (
                "Shop",
                0x2F,
                0x31,
                (shop_address(7, 1), None),
                "Buy Arrows (10)",
                (
                    "Zora's Domain",
                    "Shops",
                ),
            ),
        ),
        (
            "ZD Shop Item 3",
            (
                "Shop",
                0x2F,
                0x32,
                (shop_address(7, 2), None),
                "Buy Heart",
                (
                    "Zora's Domain",
                    "Shops",
                ),
            ),
        ),
        (
            "ZD Shop Item 4",
            (
                "Shop",
                0x2F,
                0x33,
                (shop_address(7, 3), None),
                "Buy Arrows (30)",
                (
                    "Zora's Domain",
                    "Shops",
                ),
            ),
        ),
        (
            "ZD Shop Item 5",
            (
                "Shop",
                0x2F,
                0x34,
                (shop_address(7, 4), None),
                "Buy Deku Nut (5)",
                (
                    "Zora's Domain",
                    "Shops",
                ),
            ),
        ),
        (
            "ZD Shop Item 6",
            (
                "Shop",
                0x2F,
                0x35,
                (shop_address(7, 5), None),
                "Buy Arrows (50)",
                (
                    "Zora's Domain",
                    "Shops",
                ),
            ),
        ),
        (
            "ZD Shop Item 7",
            (
                "Shop",
                0x2F,
                0x36,
                (shop_address(7, 6), None),
                "Buy Fish",
                (
                    "Zora's Domain",
                    "Shops",
                ),
            ),
        ),
        (
            "ZD Shop Item 8",
            (
                "Shop",
                0x2F,
                0x37,
                (shop_address(7, 7), None),
                "Buy Red Potion for 50 Rupees",
                (
                    "Zora's Domain",
                    "Shops",
                ),
            ),
        ),
        # Zora's Domain Pots
        (
            "ZD Pot 1",
            (
                "Pot",
                0x58,
                [(1, 2, 6), (1, 0, 22)],
                None,
                "Deku Stick (1)",
                (
                    "Zora's Domain",
                    "Pots",
                ),
            ),
        ),
        (
            "ZD Pot 2",
            (
                "Pot",
                0x58,
                [(1, 2, 5), (1, 0, 23)],
                None,
                "Deku Nuts (5)",
                (
                    "Zora's Domain",
                    "Pots",
                ),
            ),
        ),
        (
            "ZD Pot 3",
            (
                "Pot",
                0x58,
                [(1, 2, 4), (1, 0, 24)],
                None,
                "Recovery Heart",
                (
                    "Zora's Domain",
                    "Pots",
                ),
            ),
        ),
        (
            "ZD Pot 4",
            (
                "Pot",
                0x58,
                [(1, 2, 3), (1, 0, 25)],
                None,
                "Recovery Heart",
                (
                    "Zora's Domain",
                    "Pots",
                ),
            ),
        ),
        (
            "ZD Pot 5",
            (
                "Pot",
                0x58,
                [(1, 2, 2), (1, 0, 26)],
                None,
                "Rupees (5)",
                (
                    "Zora's Domain",
                    "Pots",
                ),
            ),
        ),
        # Zora's Domain Beehives
        (
            "ZD In Front of King Zora Beehive 1",
            (
                "Beehive",
                0x58,
                (0, 0, 10),
                None,
                "Rupees (20)",
                (
                    "Zora's Domain",
                    "Beehives",
                ),
            ),
        ),
        (
            "ZD In Front of King Zora Beehive 2",
            (
                "Beehive",
                0x58,
                (0, 0, 11),
                None,
                "Rupees (20)",
                (
                    "Zora's Domain",
                    "Beehives",
                ),
            ),
        ),
        (
            "ZD Behind King Zora Beehive",
            (
                "Beehive",
                0x58,
                (0, 0, 12),
                None,
                "Rupees (20)",
                (
                    "Zora's Domain",
                    "Beehives",
                ),
            ),
        ),
        # Zora's Fountain
        (
            "ZF Great Fairy Reward",
            (
                "Cutscene",
                0xFF,
                0x10,
                None,
                "Farores Wind",
                (
                    "Zora's Fountain",
                    "Great Fairies",
                ),
            ),
        ),
        (
            "ZF Iceberg Freestanding PoH",
            (
                "Collectable",
                0x59,
                0x01,
                None,
                "Piece of Heart",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Freestanding PoH",
            (
                "Collectable",
                0x59,
                0x14,
                None,
                "Piece of Heart",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF GS Above the Log",
            (
                "GS Token",
                0x11,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Zora's Fountain",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "ZF GS Tree",
            (
                "GS Token",
                0x11,
                0x80,
                None,
                "Gold Skulltula Token",
                (
                    "Zora's Fountain",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "ZF GS Hidden Cave",
            (
                "GS Token",
                0x11,
                0x20,
                None,
                "Gold Skulltula Token",
                (
                    "Zora's Fountain",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Zora's Fountain Freestanding
        (
            "ZF Bottom Green Rupee 1",
            (
                "Freestanding",
                0x59,
                (0, 2, 1),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 2",
            (
                "Freestanding",
                0x59,
                (0, 2, 2),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 3",
            (
                "Freestanding",
                0x59,
                (0, 2, 3),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 4",
            (
                "Freestanding",
                0x59,
                (0, 2, 4),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 5",
            (
                "Freestanding",
                0x59,
                (0, 2, 5),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 6",
            (
                "Freestanding",
                0x59,
                (0, 2, 6),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 7",
            (
                "Freestanding",
                0x59,
                (0, 2, 7),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 8",
            (
                "Freestanding",
                0x59,
                (0, 2, 8),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 9",
            (
                "Freestanding",
                0x59,
                (0, 2, 9),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 10",
            (
                "Freestanding",
                0x59,
                (0, 2, 10),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 11",
            (
                "Freestanding",
                0x59,
                (0, 2, 11),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 12",
            (
                "Freestanding",
                0x59,
                (0, 2, 12),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 13",
            (
                "Freestanding",
                0x59,
                (0, 2, 13),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 14",
            (
                "Freestanding",
                0x59,
                (0, 2, 14),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 15",
            (
                "Freestanding",
                0x59,
                (0, 2, 15),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 16",
            (
                "Freestanding",
                0x59,
                (0, 2, 16),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 17",
            (
                "Freestanding",
                0x59,
                (0, 2, 17),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        (
            "ZF Bottom Green Rupee 18",
            (
                "Freestanding",
                0x59,
                (0, 2, 18),
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Freestandings",
                ),
            ),
        ),
        # Zora's Fountain Pots
        (
            "ZF Hidden Cave Pot 1",
            (
                "Pot",
                0x59,
                (0, 2, 43),
                None,
                "Rupees (5)",
                (
                    "Zora's Fountain",
                    "Pots",
                ),
            ),
        ),
        (
            "ZF Hidden Cave Pot 2",
            (
                "Pot",
                0x59,
                (0, 2, 44),
                None,
                "Rupees (5)",
                (
                    "Zora's Fountain",
                    "Pots",
                ),
            ),
        ),
        (
            "ZF Hidden Cave Pot 3",
            (
                "Pot",
                0x59,
                (0, 2, 45),
                None,
                "Arrows (10)",
                (
                    "Zora's Fountain",
                    "Pots",
                ),
            ),
        ),
        (
            "ZF Near Jabu Pot 1",
            (
                "Pot",
                0x59,
                [(0, 0, 20), (0, 1, 20)],
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Pots",
                ),
            ),
        ),
        (
            "ZF Near Jabu Pot 2",
            (
                "Pot",
                0x59,
                [(0, 0, 22), (0, 1, 22)],
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Pots",
                ),
            ),
        ),
        (
            "ZF Near Jabu Pot 3",
            (
                "Pot",
                0x59,
                [(0, 0, 23), (0, 1, 23)],
                None,
                "Rupee (1)",
                (
                    "Zora's Fountain",
                    "Pots",
                ),
            ),
        ),
        (
            "ZF Near Jabu Pot 4",
            (
                "Pot",
                0x59,
                [(0, 0, 24), (0, 1, 24)],
                None,
                "Recovery Heart",
                (
                    "Zora's Fountain",
                    "Pots",
                ),
            ),
        ),
        # Lake Hylia
        (
            "LH Underwater Item",
            (
                "NPC",
                0x57,
                0x15,
                None,
                "Rutos Letter",
                (
                    "Lake Hylia",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LH Child Fishing",
            (
                "NPC",
                0x49,
                0x3E,
                None,
                "Piece of Heart",
                (
                    "Lake Hylia",
                    "Minigames",
                ),
            ),
        ),
        (
            "LH Adult Fishing",
            (
                "NPC",
                0x49,
                0x38,
                None,
                "Progressive Scale",
                (
                    "Lake Hylia",
                    "Minigames",
                ),
            ),
        ),
        ("LH Loach Fishing", ("NPC", 0x49, 0x56, None, "Rupees (50)", ("Lake Hylia", "Minigames"))),
        (
            "LH Lab Dive",
            (
                "NPC",
                0x38,
                0x3E,
                None,
                "Piece of Heart",
                (
                    "Lake Hylia",
                    "NPCs",
                ),
            ),
        ),
        ("LH Trade Eyeball Frog", ("NPC", 0x38, 0x25, None, "Eyedrops", ("Lake Hylia",))),
        (
            "LH Freestanding PoH",
            (
                "Collectable",
                0x57,
                0x1E,
                None,
                "Piece of Heart",
                (
                    "Lake Hylia",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LH Sun",
            (
                "NPC",
                0x57,
                0x58,
                None,
                "Fire Arrows",
                (
                    "Lake Hylia",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LH Deku Scrub Grotto Left",
            (
                "GrottoScrub",
                0xEF,
                0x30,
                None,
                "Buy Deku Nut (5)",
                (
                    "Lake Hylia",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "LH Deku Scrub Grotto Center",
            (
                "GrottoScrub",
                0xEF,
                0x33,
                None,
                "Buy Deku Seeds (30)",
                (
                    "Lake Hylia",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "LH Deku Scrub Grotto Right",
            (
                "GrottoScrub",
                0xEF,
                0x37,
                None,
                "Buy Bombs (5) for 35 Rupees",
                (
                    "Lake Hylia",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "LH GS Bean Patch",
            (
                "GS Token",
                0x12,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Lake Hylia",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "LH GS Lab Wall",
            (
                "GS Token",
                0x12,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Lake Hylia",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "LH GS Small Island",
            (
                "GS Token",
                0x12,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Lake Hylia",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "LH GS Lab Crate",
            (
                "GS Token",
                0x12,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Lake Hylia",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "LH GS Tree",
            (
                "GS Token",
                0x12,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Lake Hylia",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Lake Hylia Freestanding
        (
            "LH Underwater Near Shore Green Rupee",
            (
                "Freestanding",
                0x57,
                (0, 0, 50),
                None,
                "Rupee (1)",
                (
                    "Lake Hylia",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LH Underwater Green Rupee 1",
            (
                "Freestanding",
                0x57,
                (0, 0, 51),
                None,
                "Rupee (1)",
                (
                    "Lake Hylia",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LH Underwater Green Rupee 2",
            (
                "Freestanding",
                0x57,
                (0, 0, 52),
                None,
                "Rupee (1)",
                (
                    "Lake Hylia",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LH Lab Dive Red Rupee 1",
            (
                "Freestanding",
                0x38,
                (0, 0, 2),
                None,
                "Rupees (20)",
                (
                    "Lake Hylia",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LH Lab Dive Red Rupee 2",
            (
                "Freestanding",
                0x38,
                (0, 0, 3),
                None,
                "Rupees (20)",
                (
                    "Lake Hylia",
                    "Freestandings",
                ),
            ),
        ),
        (
            "LH Lab Dive Red Rupee 3",
            (
                "Freestanding",
                0x38,
                (0, 0, 4),
                None,
                "Rupees (20)",
                (
                    "Lake Hylia",
                    "Freestandings",
                ),
            ),
        ),
        # Lake Hylia Beehives
        (
            "LH Grotto Beehive",
            (
                "Beehive",
                0x3E,
                (12, 0x0F, 4),
                None,
                "Rupees (20)",
                (
                    "Lake Hylia",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        # Gerudo Valley
        (
            "GV Crate Freestanding PoH",
            (
                "Collectable",
                0x5A,
                0x02,
                None,
                "Piece of Heart",
                (
                    "Gerudo Valley",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GV Waterfall Freestanding PoH",
            (
                "Collectable",
                0x5A,
                0x01,
                None,
                "Piece of Heart",
                (
                    "Gerudo Valley",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GV Chest",
            (
                "Chest",
                0x5A,
                0x00,
                None,
                "Rupees (50)",
                (
                    "Gerudo Valley",
                    "Chests",
                ),
            ),
        ),
        (
            "GV Deku Scrub Grotto Front",
            (
                "GrottoScrub",
                0xF0,
                0x3A,
                None,
                "Buy Green Potion",
                (
                    "Gerudo Valley",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "GV Deku Scrub Grotto Rear",
            (
                "GrottoScrub",
                0xF0,
                0x39,
                None,
                "Buy Red Potion for 30 Rupees",
                (
                    "Gerudo Valley",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "GV Trade Poachers Saw",
            (
                "NPC",
                0x5A,
                0x22,
                None,
                "Broken Sword",
                (
                    "Gerudo Valley",
                    "Gerudo",
                ),
            ),
        ),
        (
            "GV Cow",
            (
                "NPC",
                0x5A,
                0x15,
                None,
                "Milk",
                (
                    "Gerudo Valley",
                    "Cows",
                ),
            ),
        ),
        (
            "GV GS Small Bridge",
            (
                "GS Token",
                0x13,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Gerudo Valley",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "GV GS Bean Patch",
            (
                "GS Token",
                0x13,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Gerudo Valley",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "GV GS Behind Tent",
            (
                "GS Token",
                0x13,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Gerudo Valley",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "GV GS Pillar",
            (
                "GS Token",
                0x13,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Gerudo Valley",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Gerudo Valley Freestanding
        (
            "GV Octorok Grotto Red Rupee",
            (
                "Freestanding",
                0x3E,
                (5, 0x12, 9),
                None,
                "Rupees (20)",
                (
                    "Gerudo Valley",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GV Octorok Grotto Blue Rupee 1",
            (
                "Freestanding",
                0x3E,
                (5, 0x12, 2),
                None,
                "Rupees (5)",
                (
                    "Gerudo Valley",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GV Octorok Grotto Blue Rupee 2",
            (
                "Freestanding",
                0x3E,
                (5, 0x12, 3),
                None,
                "Rupees (5)",
                (
                    "Gerudo Valley",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GV Octorok Grotto Blue Rupee 3",
            (
                "Freestanding",
                0x3E,
                (5, 0x12, 4),
                None,
                "Rupees (5)",
                (
                    "Gerudo Valley",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GV Octorok Grotto Green Rupee 1",
            (
                "Freestanding",
                0x3E,
                (5, 0x12, 5),
                None,
                "Rupee (1)",
                (
                    "Gerudo Valley",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GV Octorok Grotto Green Rupee 2",
            (
                "Freestanding",
                0x3E,
                (5, 0x12, 6),
                None,
                "Rupee (1)",
                (
                    "Gerudo Valley",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GV Octorok Grotto Green Rupee 3",
            (
                "Freestanding",
                0x3E,
                (5, 0x12, 7),
                None,
                "Rupee (1)",
                (
                    "Gerudo Valley",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        (
            "GV Octorok Grotto Green Rupee 4",
            (
                "Freestanding",
                0x3E,
                (5, 0x12, 8),
                None,
                "Rupee (1)",
                (
                    "Gerudo Valley",
                    "Grottos",
                    "Freestandings",
                ),
            ),
        ),
        # Gerudo Valley Pots/Crates
        (
            "GV Crate Near Cow",
            (
                "Crate",
                0x5A,
                (0, 0, 38),
                None,
                "Rupee (1)",
                (
                    "Gerudo Valley",
                    "Crates",
                ),
            ),
        ),
        (
            "GV Freestanding PoH Crate",
            (
                "Crate",
                0x5A,
                [(0, 2, 31), (0, 0, 39)],
                None,
                "Rupee (1)",
                (
                    "Gerudo Valley",
                    "Crates",
                ),
            ),
        ),
        # Gerudo Valley Beehives
        (
            "GV Storms Grotto Beehive",
            (
                "Beehive",
                0x3E,
                (9, 0x10, 3),
                None,
                "Rupees (20)",
                (
                    "Gerudo Valley",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        # Gerudo Valley Wonderitems
        (
            "GV Adult Upper Waterfall Wonderitem",
            ("Wonderitem", 0x5A, (0, 2, 41), None, "Rupees (20)", ("Gerudo Valley", "Wonderitem")),
        ),
        (
            "GV Adult Lower Waterfall Wonderitem",
            ("Wonderitem", 0x5A, (0, 2, 42), None, "Rupees (20)", ("Gerudo Valley", "Wonderitem")),
        ),
        # Gerudo's Fortress
        (
            "GF Chest",
            (
                "Chest",
                0x5D,
                0x00,
                None,
                "Piece of Heart",
                (
                    "Gerudo's Fortress",
                    "Chests",
                ),
            ),
        ),
        (
            "GF HBA 1000 Points",
            (
                "NPC",
                0x5D,
                0x3E,
                None,
                "Piece of Heart",
                (
                    "Gerudo's Fortress",
                    "Minigames",
                ),
            ),
        ),
        (
            "GF HBA 1500 Points",
            (
                "NPC",
                0x5D,
                0x30,
                None,
                "Bow",
                (
                    "Gerudo's Fortress",
                    "Minigames",
                ),
            ),
        ),
        (
            "GF GS Top Floor",
            (
                "GS Token",
                0x14,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Gerudo's Fortress",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "GF GS Archery Range",
            (
                "GS Token",
                0x14,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Gerudo's Fortress",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Gerudo's Fortress Crates/Pots
        (
            "GF Crate 1",
            (
                "Crate",
                0x5D,
                [(0, 2, 13), (0, 3, 13), (0, 0, 15)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF Crate 2",
            (
                "Crate",
                0x5D,
                [(0, 2, 14), (0, 3, 14), (0, 0, 16)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF Crate 3",
            (
                "Crate",
                0x5D,
                [(0, 2, 15), (0, 3, 15), (0, 0, 17)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF Crate 4",
            (
                "Crate",
                0x5D,
                [(0, 2, 16), (0, 3, 16), (0, 0, 18)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF Crate 5",
            (
                "Crate",
                0x5D,
                [(0, 2, 17), (0, 3, 17), (0, 0, 21)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF Crate 6",
            (
                "Crate",
                0x5D,
                [(0, 2, 18), (0, 3, 18), (0, 0, 20)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF Above Jail Crate",
            (
                "Crate",
                0x5D,
                [(0, 2, 19), (0, 3, 19)],
                None,
                "Rupees (50)",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF HBA Crate 1",
            (
                "Crate",
                0x5D,
                [(1, 3, 2), (1, 2, 9), (1, 0, 1)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF HBA Crate 2",
            (
                "Crate",
                0x5D,
                [(1, 3, 3), (1, 2, 10), (1, 0, 2)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF HBA Crate 3",
            (
                "Crate",
                0x5D,
                [(1, 3, 4), (1, 2, 11), (1, 0, 3)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF HBA Crate 4",
            (
                "Crate",
                0x5D,
                [(1, 3, 5), (1, 2, 12), (1, 0, 14)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF HBA Crate 5",
            (
                "Crate",
                0x5D,
                [(1, 3, 6), (1, 2, 13), (1, 0, 5)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF HBA Crate 6",
            (
                "Crate",
                0x5D,
                [(1, 3, 7), (1, 2, 14), (1, 0, 6)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF HBA Crate 7",
            (
                "Crate",
                0x5D,
                [(1, 3, 8), (1, 2, 15), (1, 0, 7)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF HBA Crate 8",
            (
                "Crate",
                0x5D,
                [(1, 3, 9), (1, 2, 16), (1, 0, 8)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF HBA Crate 9",
            (
                "Crate",
                0x5D,
                [(1, 3, 10), (1, 2, 17), (1, 0, 9)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF HBA Crate 10",
            (
                "Crate",
                0x5D,
                [(1, 3, 11), (1, 2, 18), (1, 0, 10)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF HBA Crate 11",
            (
                "Crate",
                0x5D,
                [(1, 3, 12), (1, 2, 19), (1, 0, 11)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF HBA Crate 12",
            (
                "Crate",
                0x5D,
                [(1, 3, 13), (1, 2, 20), (1, 0, 12)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        (
            "GF HBA Crate 13",
            (
                "Crate",
                0x5D,
                [(1, 3, 14), (1, 2, 21), (1, 0, 13)],
                None,
                "Nothing",
                (
                    "Gerudo's Fortress",
                    "Crates",
                ),
            ),
        ),
        # Gerudo's Fortress Wonderitems
        (
            "GF Sign Wonderitem Near Entrance",
            (
                "Wonderitem",
                0x5D,
                [(0, 2, 6), (0, 3, 6)],
                None,
                "Rupees (20)",
                ("Gerudo's Fortress", "Wonderitem"),
            ),
        ),
        (
            "GF Sign Wonderitem Near HBA",
            (
                "Wonderitem",
                0x5D,
                [(0, 2, 7), (0, 3, 7)],
                None,
                "Rupees (20)",
                ("Gerudo's Fortress", "Wonderitem"),
            ),
        ),
        # Thieves' Hideout
        (
            "Hideout 1 Torch Jail Gerudo Key",
            ("Collectable", 0x0C, 0x0C, None, "Small Key (Thieves Hideout)", ("Thieves' Hideout",)),
        ),
        (
            "Hideout 2 Torches Jail Gerudo Key",
            ("Collectable", 0x0C, 0x0F, None, "Small Key (Thieves Hideout)", ("Thieves' Hideout",)),
        ),
        (
            "Hideout 3 Torches Jail Gerudo Key",
            ("Collectable", 0x0C, 0x0A, None, "Small Key (Thieves Hideout)", ("Thieves' Hideout",)),
        ),
        (
            "Hideout 4 Torches Jail Gerudo Key",
            ("Collectable", 0x0C, 0x0E, None, "Small Key (Thieves Hideout)", ("Thieves' Hideout",)),
        ),
        (
            "Hideout Gerudo Membership Card",
            (
                "NPC",
                0x0C,
                0x3A,
                None,
                "Gerudo Membership Card",
                (
                    "Thieves' Hideout",
                    "NPCs",
                ),
            ),
        ),
        # Thieves' Hideout Pots/Crates
        (
            "Hideout Break Room Pot 1",
            (
                "Pot",
                0x0C,
                (0, 0, 5),
                None,
                "Arrows (10)",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout Break Room Pot 2",
            (
                "Pot",
                0x0C,
                (0, 0, 6),
                None,
                "Rupees (5)",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout 1 Torch Jail Pot 1",
            (
                "Pot",
                0x0C,
                (2, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout 1 Torch Jail Pot 2",
            (
                "Pot",
                0x0C,
                (2, 0, 8),
                None,
                "Arrows (10)",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout 1 Torch Jail Pot 3",
            (
                "Pot",
                0x0C,
                (2, 0, 9),
                None,
                "Rupees (20)",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout Kitchen Pot 1",
            (
                "Pot",
                0x0C,
                (3, 0, 6),
                None,
                "Arrows (10)",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout Kitchen Pot 2",
            (
                "Pot",
                0x0C,
                (3, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout 4 Torch Jail Pot 1",
            (
                "Pot",
                0x0C,
                (4, 0, 10),
                None,
                "Rupees (5)",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout 4 Torch Jail Pot 2",
            (
                "Pot",
                0x0C,
                (4, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout 2 Torch Jail Pot 1",
            (
                "Pot",
                0x0C,
                (5, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout 2 Torch Jail Pot 2",
            (
                "Pot",
                0x0C,
                (5, 0, 9),
                None,
                "Rupees (5)",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout 2 Torch Jail Pot 3",
            (
                "Pot",
                0x0C,
                (5, 0, 10),
                None,
                "Rupees (20)",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout 2 Torch Jail In Cell Pot 1",
            (
                "Pot",
                0x0C,
                (5, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout 2 Torch Jail In Cell Pot 2",
            (
                "Pot",
                0x0C,
                (5, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout 2 Torch Jail In Cell Pot 3",
            (
                "Pot",
                0x0C,
                (5, 0, 13),
                None,
                "Recovery Heart",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout 2 Torch Jail In Cell Pot 4",
            (
                "Pot",
                0x0C,
                (5, 0, 14),
                None,
                "Recovery Heart",
                (
                    "Thieves' Hideout",
                    "Pots",
                ),
            ),
        ),
        (
            "Hideout Break Room Crate 1",
            (
                "Crate",
                0x0C,
                (0, 0, 7),
                None,
                "Rupee (1)",
                (
                    "Thieves' Hideout",
                    "Crates",
                ),
            ),
        ),
        (
            "Hideout Break Room Crate 2",
            (
                "Crate",
                0x0C,
                (0, 0, 8),
                None,
                "Rupee (1)",
                (
                    "Thieves' Hideout",
                    "Crates",
                ),
            ),
        ),
        (
            "Hideout Break Room Hallway Crate 1",
            (
                "Crate",
                0x0C,
                (0, 0, 9),
                None,
                "Rupee (1)",
                (
                    "Thieves' Hideout",
                    "Crates",
                ),
            ),
        ),
        (
            "Hideout Break Room Hallway Crate 2",
            (
                "Crate",
                0x0C,
                (0, 0, 10),
                None,
                "Rupee (1)",
                (
                    "Thieves' Hideout",
                    "Crates",
                ),
            ),
        ),
        (
            "Hideout 1 Torch Jail Crate",
            (
                "Crate",
                0x0C,
                (2, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Thieves' Hideout",
                    "Crates",
                ),
            ),
        ),
        (
            "Hideout 3 Torch Jail Crate",
            (
                "Crate",
                0x0C,
                (1, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Thieves' Hideout",
                    "Crates",
                ),
            ),
        ),
        (
            "Hideout Near Kitchen Crate 1",
            (
                "Crate",
                0x0C,
                (3, 0, 8),
                None,
                "Rupee (1)",
                (
                    "Thieves' Hideout",
                    "Crates",
                ),
            ),
        ),
        (
            "Hideout Near Kitchen Crate 2",
            (
                "Crate",
                0x0C,
                (3, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Thieves' Hideout",
                    "Crates",
                ),
            ),
        ),
        (
            "Hideout Near Kitchen Crate 3",
            (
                "Crate",
                0x0C,
                (3, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Thieves' Hideout",
                    "Crates",
                ),
            ),
        ),
        (
            "Hideout Near Kitchen Crate 4",
            (
                "Crate",
                0x0C,
                (3, 0, 13),
                None,
                "Rupee (1)",
                (
                    "Thieves' Hideout",
                    "Crates",
                ),
            ),
        ),
        (
            "Hideout Near Kitchen Crate 5",
            (
                "Crate",
                0x0C,
                (3, 0, 14),
                None,
                "Rupee (1)",
                (
                    "Thieves' Hideout",
                    "Crates",
                ),
            ),
        ),
        (
            "Hideout 2 Torch Jail Crate 1",
            (
                "Crate",
                0x0C,
                (5, 0, 16),
                None,
                "Rupee (1)",
                (
                    "Thieves' Hideout",
                    "Crates",
                ),
            ),
        ),
        (
            "Hideout 2 Torch Jail Crate 2",
            (
                "Crate",
                0x0C,
                (5, 0, 17),
                None,
                "Rupee (1)",
                (
                    "Thieves' Hideout",
                    "Crates",
                ),
            ),
        ),
        # Thieves Hideout Wonderitems
        (
            "Hideout Break Room Wonderitem",
            ("Wonderitem", 0x0C, (0, 0, 3), None, "Rupees (5)", ("Thieves' Hideout", "Wonderitem")),
        ),
        (
            "Hideout Break Room Hall to Balcony Wonderitem",
            ("Wonderitem", 0x0C, (0, 0, 4), None, "Rupees (5)", ("Thieves' Hideout", "Wonderitem")),
        ),
        (
            "Hideout 3 Torch Jail Wonderitem 1",
            ("Wonderitem", 0x0C, (1, 0, 4), None, "Rupees (5)", ("Thieves' Hideout", "Wonderitem")),
        ),
        (
            "Hideout 3 Torch Jail Wonderitem 2",
            ("Wonderitem", 0x0C, (1, 0, 5), None, "Rupees (5)", ("Thieves' Hideout", "Wonderitem")),
        ),
        (
            "Hideout 1 Torch Jail Wonderitem 1",
            ("Wonderitem", 0x0C, (2, 0, 3), None, "Rupees (5)", ("Thieves' Hideout", "Wonderitem")),
        ),
        (
            "Hideout 1 Torch Jail Wonderitem 2",
            ("Wonderitem", 0x0C, (2, 0, 4), None, "Rupees (5)", ("Thieves' Hideout", "Wonderitem")),
        ),
        (
            "Hideout Kitchen Stove Wonderitem",
            ("Wonderitem", 0x0C, (3, 0, 5), None, "Rupees (5)", ("Thieves' Hideout", "Wonderitem")),
        ),
        (
            "Hideout Kitchen Wonderitem",
            ("Wonderitem", 0x0C, (3, 0, 4), None, "Rupees (5)", ("Thieves' Hideout", "Wonderitem")),
        ),
        (
            "Hideout 4 Torch Jail Wonderitem 1",
            ("Wonderitem", 0x0C, (4, 0, 3), None, "Rupees (5)", ("Thieves' Hideout", "Wonderitem")),
        ),
        (
            "Hideout 4 Torch Jail Wonderitem 2",
            ("Wonderitem", 0x0C, (4, 0, 4), None, "Rupees (5)", ("Thieves' Hideout", "Wonderitem")),
        ),
        (
            "Hideout 2 Torch Jail Wonderitem 1",
            ("Wonderitem", 0x0C, (5, 0, 3), None, "Rupees (5)", ("Thieves' Hideout", "Wonderitem")),
        ),
        (
            "Hideout 2 Torch Jail Wonderitem 2",
            ("Wonderitem", 0x0C, (5, 0, 4), None, "Rupees (5)", ("Thieves' Hideout", "Wonderitem")),
        ),
        # Haunted Wasteland
        (
            "Wasteland Bombchu Salesman",
            (
                "NPC",
                0x5E,
                0x03,
                None,
                "Bombchus (10)",
                (
                    "Haunted Wasteland",
                    "NPCs",
                ),
            ),
        ),
        (
            "Wasteland Chest",
            (
                "Chest",
                0x5E,
                0x00,
                None,
                "Rupees (50)",
                (
                    "Haunted Wasteland",
                    "Chests",
                ),
            ),
        ),
        (
            "Wasteland GS",
            (
                "GS Token",
                0x15,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Haunted Wasteland",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Haunted Wasteland Pots/Crates
        (
            "Wasteland Near GS Pot 1",
            (
                "Pot",
                0x5E,
                (0, 0, 1),
                None,
                "Recovery Heart",
                (
                    "Haunted Wasteland",
                    "Pots",
                ),
            ),
        ),
        (
            "Wasteland Near GS Pot 2",
            (
                "Pot",
                0x5E,
                (0, 0, 2),
                None,
                "Deku Nuts (5)",
                (
                    "Haunted Wasteland",
                    "Pots",
                ),
            ),
        ),
        (
            "Wasteland Near GS Pot 3",
            (
                "Pot",
                0x5E,
                (0, 0, 3),
                None,
                "Fairy Drop",
                (
                    "Haunted Wasteland",
                    "Pots",
                ),
            ),
        ),
        (
            "Wasteland Near GS Pot 4",
            (
                "Pot",
                0x5E,
                (0, 0, 4),
                None,
                "Rupees (5)",
                (
                    "Haunted Wasteland",
                    "Pots",
                ),
            ),
        ),
        (
            "Wasteland Crate Before Quicksand",
            (
                "Crate",
                0x5E,
                (1, 0, 38),
                None,
                "Rupee (1)",
                (
                    "Haunted Wasteland",
                    "Crates",
                ),
            ),
        ),
        (
            "Wasteland Crate After Quicksand 1",
            (
                "Crate",
                0x5E,
                (1, 0, 35),
                None,
                "Rupee (1)",
                (
                    "Haunted Wasteland",
                    "Crates",
                ),
            ),
        ),
        (
            "Wasteland Crate After Quicksand 2",
            (
                "Crate",
                0x5E,
                (1, 0, 36),
                None,
                "Rupee (1)",
                (
                    "Haunted Wasteland",
                    "Crates",
                ),
            ),
        ),
        (
            "Wasteland Crate After Quicksand 3",
            (
                "Crate",
                0x5E,
                (1, 0, 37),
                None,
                "Rupee (1)",
                (
                    "Haunted Wasteland",
                    "Crates",
                ),
            ),
        ),
        (
            "Wasteland Crate Near Colossus",
            (
                "Crate",
                0x5E,
                (1, 0, 34),
                None,
                "Rupee (1)",
                (
                    "Haunted Wasteland",
                    "Crates",
                ),
            ),
        ),
        # Desert Colossus
        (
            "Colossus Great Fairy Reward",
            (
                "Cutscene",
                0xFF,
                0x12,
                None,
                "Nayrus Love",
                (
                    "Desert Colossus",
                    "Great Fairies",
                ),
            ),
        ),
        (
            "Colossus Freestanding PoH",
            (
                "Collectable",
                0x5C,
                0x0D,
                None,
                "Piece of Heart",
                (
                    "Desert Colossus",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Colossus Deku Scrub Grotto Front",
            (
                "GrottoScrub",
                0xFD,
                0x3A,
                None,
                "Buy Green Potion",
                (
                    "Desert Colossus",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "Colossus Deku Scrub Grotto Rear",
            (
                "GrottoScrub",
                0xFD,
                0x39,
                None,
                "Buy Red Potion for 30 Rupees",
                (
                    "Desert Colossus",
                    "Deku Scrubs",
                    "Grottos",
                ),
            ),
        ),
        (
            "Colossus GS Bean Patch",
            (
                "GS Token",
                0x15,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Desert Colossus",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Colossus GS Tree",
            (
                "GS Token",
                0x15,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Desert Colossus",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Colossus GS Hill",
            (
                "GS Token",
                0x15,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Desert Colossus",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Colossus Beehives
        (
            "Colossus Grotto Beehive",
            (
                "Beehive",
                0x3E,
                (9, 0x1D, 3),
                None,
                "Rupees (20)",
                (
                    "Desert Colossus",
                    "Grottos",
                    "Beehives",
                ),
            ),
        ),
        # Colossus Wonderitems
        (
            "Colossus Tree Wonderitem 1",
            (
                "Wonderitem",
                0x5C,
                [(0, 0, 20), (0, 2, 23)],
                None,
                "Rupees (5)",
                ("Desert Colossus", "Wonderitem"),
            ),
        ),
        (
            "Colossus Tree Wonderitem 2",
            (
                "Wonderitem",
                0x5C,
                [(0, 0, 22), (0, 2, 24)],
                None,
                "Rupees (5)",
                ("Desert Colossus", "Wonderitem"),
            ),
        ),
        (
            "Colossus Tree Wonderitem 3 Child",
            ("Wonderitem", 0x5C, (0, 0, 23), None, "Rupees (5)", ("Desert Colossus", "Wonderitem")),
        ),
        (
            "Colossus Tree Wonderitem 4",
            (
                "Wonderitem",
                0x5C,
                [(0, 0, 21), (0, 2, 25)],
                None,
                "Rupees (5)",
                ("Desert Colossus", "Wonderitem"),
            ),
        ),
        (
            "Colossus Tree Wonderitem 5",
            (
                "Wonderitem",
                0x5C,
                [(0, 0, 24), (0, 2, 26)],
                None,
                "Rupees (20)",
                ("Desert Colossus", "Wonderitem"),
            ),
        ),
        # Outside Ganon's Castle
        (
            "OGC Great Fairy Reward",
            (
                "Cutscene",
                0xFF,
                0x15,
                None,
                "Double Defense",
                (
                    "Outside Ganon's Castle",
                    "Great Fairies",
                ),
            ),
        ),
        (
            "OGC GS",
            (
                "GS Token",
                0x0E,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Outside Ganon's Castle",
                    "Gold Skulltulas",
                ),
            ),
        ),
        ## Dungeons
        # Deku Tree Vanilla
        (
            "Deku Tree Map Chest",
            (
                "Chest",
                0x00,
                0x03,
                None,
                "Map (Deku Tree)",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Deku Tree Slingshot Room Side Chest",
            (
                "Chest",
                0x00,
                0x05,
                None,
                "Recovery Heart",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Deku Tree Slingshot Chest",
            (
                "Chest",
                0x00,
                0x01,
                None,
                "Slingshot",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Deku Tree Compass Chest",
            (
                "Chest",
                0x00,
                0x02,
                None,
                "Compass (Deku Tree)",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Deku Tree Compass Room Side Chest",
            (
                "Chest",
                0x00,
                0x06,
                None,
                "Recovery Heart",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Deku Tree Basement Chest",
            (
                "Chest",
                0x00,
                0x04,
                None,
                "Recovery Heart",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Deku Tree GS Compass Room",
            (
                "GS Token",
                0x00,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Deku Tree GS Basement Vines",
            (
                "GS Token",
                0x00,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Deku Tree GS Basement Gate",
            (
                "GS Token",
                0x00,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Deku Tree GS Basement Back Room",
            (
                "GS Token",
                0x00,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Deku Tree Freestanding
        (
            "Deku Tree Lower Lobby Recovery Heart",
            (
                "Freestanding",
                0x00,
                (0, 0, 26),
                None,
                "Recovery Heart",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Deku Tree Upper Lobby Recovery Heart",
            (
                "Freestanding",
                0x00,
                (0, 0, 27),
                None,
                "Recovery Heart",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Deku Tree Basement Recovery Heart 1",
            (
                "Freestanding",
                0x00,
                (9, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Deku Tree Basement Recovery Heart 2",
            (
                "Freestanding",
                0x00,
                (9, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Deku Tree Basement Recovery Heart 3",
            (
                "Freestanding",
                0x00,
                (9, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Deku Tree",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        # Deku Tree MQ
        (
            "Deku Tree MQ Map Chest",
            (
                "Chest",
                0x00,
                0x03,
                None,
                "Map (Deku Tree)",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Deku Tree MQ Slingshot Chest",
            (
                "Chest",
                0x00,
                0x06,
                None,
                "Slingshot",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Deku Tree MQ Slingshot Room Back Chest",
            (
                "Chest",
                0x00,
                0x02,
                None,
                "Deku Shield",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Deku Tree MQ Compass Chest",
            (
                "Chest",
                0x00,
                0x01,
                None,
                "Compass (Deku Tree)",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Deku Tree MQ Basement Chest",
            (
                "Chest",
                0x00,
                0x04,
                None,
                "Deku Shield",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Deku Tree MQ Before Spinning Log Chest",
            (
                "Chest",
                0x00,
                0x05,
                None,
                "Recovery Heart",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Deku Tree MQ After Spinning Log Chest",
            (
                "Chest",
                0x00,
                0x00,
                None,
                "Rupees (50)",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Deku Tree MQ Deku Scrub",
            (
                "Scrub",
                0x00,
                0x34,
                None,
                "Buy Deku Shield",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Deku Tree MQ GS Lobby",
            (
                "GS Token",
                0x00,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Deku Tree MQ GS Compass Room",
            (
                "GS Token",
                0x00,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Deku Tree MQ GS Basement Graves Room",
            (
                "GS Token",
                0x00,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Deku Tree MQ GS Basement Back Room",
            (
                "GS Token",
                0x00,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Deku Tree MQ Freestanding
        (
            "Deku Tree MQ Lower Lobby Recovery Heart",
            (
                "Freestanding",
                0x00,
                (0, 0, 19),
                None,
                "Recovery Heart",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Deku Tree MQ Near Compass Room Recovery Heart",
            (
                "Freestanding",
                0x00,
                (1, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Deku Tree MQ Compass Room Recovery Heart",
            (
                "Freestanding",
                0x00,
                (2, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Deku Tree MQ Basement Recovery Heart 1",
            (
                "Freestanding",
                0x00,
                (9, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Deku Tree MQ Basement Recovery Heart 2",
            (
                "Freestanding",
                0x00,
                (9, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Deku Tree MQ Basement Recovery Heart 3",
            (
                "Freestanding",
                0x00,
                (9, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Deku Tree MQ Slingshot Room Recovery Heart",
            (
                "Freestanding",
                0x00,
                (10, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        # Deku Tree MQ Pots/Crates
        (
            "Deku Tree MQ Lobby Crate",
            (
                "Crate",
                0x0,
                (0, 0, 29),
                None,
                "Rupee (1)",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Deku Tree MQ Slingshot Room Crate 1",
            (
                "Crate",
                0x0,
                (10, 0, 17),
                None,
                "Rupee (1)",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Deku Tree MQ Slingshot Room Crate 2",
            (
                "Crate",
                0x0,
                (10, 0, 18),
                None,
                "Rupee (1)",
                (
                    "Deku Tree MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        # Deku Tree MQ Wonderitems
        (
            "Deku Tree MQ Basement Graves Wonderitem 1",
            (
                "Wonderitem",
                0x00,
                (7, 0, 10),
                None,
                "Recovery Heart",
                ("Deku Tree", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Deku Tree MQ Basement Graves Wonderitem 2",
            (
                "Wonderitem",
                0x00,
                (7, 0, 11),
                None,
                "Recovery Heart",
                ("Deku Tree", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Deku Tree MQ Basement Graves Wonderitem 3",
            (
                "Wonderitem",
                0x00,
                (7, 0, 12),
                None,
                "Recovery Heart",
                ("Deku Tree", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Deku Tree MQ Basement Graves Wonderitem 4",
            (
                "Wonderitem",
                0x00,
                (7, 0, 13),
                None,
                "Recovery Heart",
                ("Deku Tree", "Master Quest", "Wonderitem"),
            ),
        ),
        # Deku Tree Shared
        (
            "Deku Tree Queen Gohma Heart",
            (
                "BossHeart",
                0x11,
                0x4F,
                None,
                "Heart Container",
                (
                    "Deku Tree",
                    "Deku Tree MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                ),
            ),
        ),
        # Dodongo's Cavern Vanilla
        (
            "Dodongos Cavern Map Chest",
            (
                "Chest",
                0x01,
                0x08,
                None,
                "Map (Dodongos Cavern)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Dodongos Cavern Compass Chest",
            (
                "Chest",
                0x01,
                0x05,
                None,
                "Compass (Dodongos Cavern)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Dodongos Cavern Bomb Flower Platform Chest",
            (
                "Chest",
                0x01,
                0x06,
                None,
                "Rupees (20)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Dodongos Cavern Bomb Bag Chest",
            (
                "Chest",
                0x01,
                0x04,
                None,
                "Bomb Bag",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Dodongos Cavern End of Bridge Chest",
            (
                "Chest",
                0x01,
                0x0A,
                None,
                "Deku Shield",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Dodongos Cavern Deku Scrub Side Room Near Dodongos",
            (
                "Scrub",
                0x01,
                0x31,
                None,
                "Buy Deku Stick (1)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Dodongos Cavern Deku Scrub Lobby",
            (
                "Scrub",
                0x01,
                0x34,
                None,
                "Buy Deku Shield",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Dodongos Cavern Deku Scrub Near Bomb Bag Left",
            (
                "Scrub",
                0x01,
                0x30,
                None,
                "Buy Deku Nut (5)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Dodongos Cavern Deku Scrub Near Bomb Bag Right",
            (
                "Scrub",
                0x01,
                0x33,
                None,
                "Buy Deku Seeds (30)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Dodongos Cavern GS Side Room Near Lower Lizalfos",
            (
                "GS Token",
                0x01,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Dodongos Cavern GS Scarecrow",
            (
                "GS Token",
                0x01,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Dodongos Cavern GS Alcove Above Stairs",
            (
                "GS Token",
                0x01,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Dodongos Cavern GS Vines Above Stairs",
            (
                "GS Token",
                0x01,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Dodongos Cavern GS Back Room",
            (
                "GS Token",
                0x01,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Dodongo's Cavern Vanilla Freestanding
        (
            "Dodongos Cavern Lizalfos Upper Recovery Heart 1",
            (
                "Freestanding",
                0x01,
                (3, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Dodongos Cavern Lizalfos Upper Recovery Heart 2",
            (
                "Freestanding",
                0x01,
                (3, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Dodongos Cavern Blade Room Behind Block Recovery Heart",
            (
                "Freestanding",
                0x01,
                (9, 0, 14),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        # Dodongo's Cavern Vanilla Pots
        (
            "Dodongos Cavern Right Side Pot 1",
            (
                "Pot",
                0x01,
                (1, 0, 13),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Right Side Pot 2",
            (
                "Pot",
                0x01,
                (1, 0, 14),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Right Side Pot 3",
            (
                "Pot",
                0x01,
                (1, 0, 16),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Right Side Pot 4",
            (
                "Pot",
                0x01,
                (1, 0, 17),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Right Side Pot 5",
            (
                "Pot",
                0x01,
                (1, 0, 18),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Right Side Pot 6",
            (
                "Pot",
                0x01,
                (1, 0, 19),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Lower Lizalfos Pot 1",
            (
                "Pot",
                0x01,
                (3, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Lower Lizalfos Pot 2",
            (
                "Pot",
                0x01,
                (3, 0, 10),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Lower Lizalfos Pot 3",
            (
                "Pot",
                0x01,
                (3, 0, 11),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Lower Lizalfos Pot 4",
            (
                "Pot",
                0x01,
                (3, 0, 12),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Torch Room Pot 1",
            (
                "Pot",
                0x01,
                (4, 0, 11),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Torch Room Pot 2",
            (
                "Pot",
                0x01,
                (4, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Torch Room Pot 3",
            (
                "Pot",
                0x01,
                (4, 0, 13),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Torch Room Pot 4",
            (
                "Pot",
                0x01,
                (4, 0, 14),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Staircase Pot 1",
            (
                "Pot",
                0x01,
                (2, 0, 24),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Staircase Pot 2",
            (
                "Pot",
                0x01,
                (2, 0, 25),
                None,
                "Rupees (20)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Staircase Pot 3",
            (
                "Pot",
                0x01,
                (2, 0, 26),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Staircase Pot 4",
            (
                "Pot",
                0x01,
                (2, 0, 27),
                None,
                "Rupees (20)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Last Block Pot 1",
            (
                "Pot",
                0x01,
                (7, 0, 7),
                None,
                "Bombs (5)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Last Block Pot 2",
            (
                "Pot",
                0x01,
                (7, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Last Block Pot 3",
            (
                "Pot",
                0x01,
                (8, 0, 7),
                None,
                "Deku Seeds (30)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Last Block Pot 4",
            (
                "Pot",
                0x01,
                (8, 0, 8),
                None,
                "Fairy Drop",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Blade Room Pot 1",
            (
                "Pot",
                0x01,
                (9, 0, 15),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Blade Room Pot 2",
            (
                "Pot",
                0x01,
                (9, 0, 16),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Single Eye Switch Room Pot 1",
            (
                "Pot",
                0x01,
                (10, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Single Eye Switch Room Pot 2",
            (
                "Pot",
                0x01,
                (10, 0, 8),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Double Eye Switch Room Pot 1",
            (
                "Pot",
                0x01,
                (12, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern Double Eye Switch Room Pot 2",
            (
                "Pot",
                0x01,
                (12, 0, 7),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        # Dodongo's Cavern MQ
        (
            "Dodongos Cavern MQ Map Chest",
            (
                "Chest",
                0x01,
                0x00,
                None,
                "Map (Dodongos Cavern)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Bomb Bag Chest",
            (
                "Chest",
                0x01,
                0x04,
                None,
                "Bomb Bag",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Torch Puzzle Room Chest",
            (
                "Chest",
                0x01,
                0x03,
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Larvae Room Chest",
            (
                "Chest",
                0x01,
                0x02,
                None,
                "Deku Shield",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Compass Chest",
            (
                "Chest",
                0x01,
                0x05,
                None,
                "Compass (Dodongos Cavern)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Under Grave Chest",
            (
                "Chest",
                0x01,
                0x01,
                None,
                "Hylian Shield",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Deku Scrub Lobby Front",
            (
                "Scrub",
                0x01,
                0x33,
                None,
                "Buy Deku Seeds (30)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Deku Scrub Lobby Rear",
            (
                "Scrub",
                0x01,
                0x31,
                None,
                "Buy Deku Stick (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Deku Scrub Side Room Near Lower Lizalfos",
            (
                "Scrub",
                0x01,
                0x39,
                None,
                "Buy Red Potion for 30 Rupees",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Deku Scrub Staircase",
            (
                "Scrub",
                0x01,
                0x34,
                None,
                "Buy Deku Shield",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ GS Scrub Room",
            (
                "GS Token",
                0x01,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ GS Larvae Room",
            (
                "GS Token",
                0x01,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ GS Lizalfos Room",
            (
                "GS Token",
                0x01,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ GS Song of Time Block Room",
            (
                "GS Token",
                0x01,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ GS Back Area",
            (
                "GS Token",
                0x01,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Dodongo's Cavern MQ Freestanding
        (
            "Dodongos Cavern MQ Torch Puzzle Room Recovery Heart",
            (
                "Freestanding",
                0x01,
                (9, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        # Dodongo's Cavern MQ Pots
        (
            "Dodongos Cavern MQ Right Side Pot 1",
            (
                "Pot",
                0x01,
                (1, 0, 8),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Right Side Pot 2",
            (
                "Pot",
                0x01,
                (1, 0, 9),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Right Side Pot 3",
            (
                "Pot",
                0x01,
                (1, 0, 10),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Right Side Pot 4",
            (
                "Pot",
                0x01,
                (1, 0, 11),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Staircase Pot 1",
            (
                "Pot",
                0x01,
                (2, 0, 17),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Staircase Pot 2",
            (
                "Pot",
                0x01,
                (2, 0, 18),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Staircase Pot 3",
            (
                "Pot",
                0x01,
                (2, 0, 19),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Staircase Pot 4",
            (
                "Pot",
                0x01,
                (2, 0, 20),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Upper Lizalfos Pot 1",
            (
                "Pot",
                0x01,
                (3, 0, 8),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Upper Lizalfos Pot 2",
            (
                "Pot",
                0x01,
                (3, 0, 9),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Upper Lizalfos Pot 3",
            (
                "Pot",
                0x01,
                (3, 0, 10),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Upper Lizalfos Pot 4",
            (
                "Pot",
                0x01,
                (3, 0, 11),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Poes Room Pot 1",
            (
                "Pot",
                0x01,
                (4, 0, 6),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Poes Room Pot 2",
            (
                "Pot",
                0x01,
                (4, 0, 7),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Poes Room Pot 3",
            (
                "Pot",
                0x01,
                (4, 0, 8),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Poes Room Pot 4",
            (
                "Pot",
                0x01,
                (4, 0, 9),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Room Before Boss Pot 1",
            (
                "Pot",
                0x01,
                (7, 0, 7),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Room Before Boss Pot 2",
            (
                "Pot",
                0x01,
                (7, 0, 8),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Armos Army Room Upper Pot 1",
            (
                "Pot",
                0x01,
                (8, 0, 20),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Armos Army Room Upper Pot 2",
            (
                "Pot",
                0x01,
                (8, 0, 21),
                None,
                "Fairy Drop",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Armos Army Room Pot 1",
            (
                "Pot",
                0x01,
                (8, 0, 22),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Armos Army Room Pot 2",
            (
                "Pot",
                0x01,
                (8, 0, 23),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Torch Puzzle Room Pot Pillar",
            (
                "Pot",
                0x01,
                (9, 0, 12),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Torch Puzzle Room Pot Corner",
            (
                "Pot",
                0x01,
                (9, 0, 13),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Before Upper Lizalfos Pot 1",
            (
                "Pot",
                0x01,
                (10, 0, 17),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Before Upper Lizalfos Pot 2",
            (
                "Pot",
                0x01,
                (10, 0, 18),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ After Upper Lizalfos Pot 1",
            (
                "Pot",
                0x01,
                (12, 0, 6),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ After Upper Lizalfos Pot 2",
            (
                "Pot",
                0x01,
                (12, 0, 7),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Back Poe Room Pot 1",
            (
                "Pot",
                0x01,
                (14, 0, 3),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Back Poe Room Pot 2",
            (
                "Pot",
                0x01,
                (14, 0, 4),
                None,
                "Rupees (5)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        # Dodongo's Cavern MQ Crates
        (
            "Dodongos Cavern MQ Staircase Crate Bottom Left",
            (
                "Crate",
                0x1,
                (2, 0, 41),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Staircase Crate Bottom Right",
            (
                "Crate",
                0x1,
                (2, 0, 42),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Staircase Crate Mid Left",
            (
                "Crate",
                0x1,
                (2, 0, 39),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Staircase Crate Top Left",
            (
                "Crate",
                0x1,
                (2, 0, 40),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Staircase Crate Mid Right",
            (
                "Crate",
                0x1,
                (2, 0, 43),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Staircase Crate Top Right",
            (
                "Crate",
                0x1,
                (2, 0, 44),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Poes Room Crate 1",
            (
                "Crate",
                0x1,
                (4, 0, 25),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Poes Room Crate 2",
            (
                "Crate",
                0x1,
                (4, 0, 26),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Poes Room Crate 3",
            (
                "Crate",
                0x1,
                (4, 0, 27),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Poes Room Crate 4",
            (
                "Crate",
                0x1,
                (4, 0, 28),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Poes Room Crate 5",
            (
                "Crate",
                0x1,
                (4, 0, 23),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Poes Room Crate 6",
            (
                "Crate",
                0x1,
                (4, 0, 24),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Poes Room Crate 7",
            (
                "Crate",
                0x1,
                (4, 0, 30),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Poes Room Crate Near Bomb Flower",
            (
                "Crate",
                0x1,
                (4, 0, 29),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Larvae Room Crate 1",
            (
                "Crate",
                0x1,
                (6, 0, 7),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Larvae Room Crate 2",
            (
                "Crate",
                0x1,
                (6, 0, 8),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Larvae Room Crate 3",
            (
                "Crate",
                0x1,
                (6, 0, 9),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Larvae Room Crate 4",
            (
                "Crate",
                0x1,
                (6, 0, 10),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Larvae Room Crate 5",
            (
                "Crate",
                0x1,
                (6, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Larvae Room Crate 6",
            (
                "Crate",
                0x1,
                (6, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ After Upper Lizalfos Crate 1",
            (
                "Crate",
                0x1,
                (12, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ After Upper Lizalfos Crate 2",
            (
                "Crate",
                0x1,
                (12, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        # Dodongo's Cavern MQ Silver Rupees
        (
            "Dodongos Cavern MQ Staircase Silver Rupee Beamos",
            (
                "SilverRupee",
                0x1,
                (2, 0, 11),
                None,
                "Silver Rupee (Dodongos Cavern Staircase)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Staircase Silver Rupee Lower Crate",
            (
                "SilverRupee",
                0x1,
                (2, 0, 12),
                None,
                "Silver Rupee (Dodongos Cavern Staircase)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Staircase Silver Rupee Mid Left Crate",
            (
                "SilverRupee",
                0x1,
                (2, 0, 13),
                None,
                "Silver Rupee (Dodongos Cavern Staircase)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Staircase Silver Rupee Vines",
            (
                "SilverRupee",
                0x1,
                (2, 0, 14),
                None,
                "Silver Rupee (Dodongos Cavern Staircase)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Dodongos Cavern MQ Staircase Silver Rupee Top Right Crate",
            (
                "SilverRupee",
                0x1,
                (2, 0, 15),
                None,
                "Silver Rupee (Dodongos Cavern Staircase)",
                (
                    "Dodongo's Cavern MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        # Dodongo's Cavern Shared
        (
            "Dodongos Cavern Lower Lizalfos Hidden Recovery Heart",
            (
                "Freestanding",
                0x01,
                (3, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Dodongo's Cavern",
                    "Dodongo's Cavern MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Dodongos Cavern Boss Room Chest",
            (
                "Chest",
                0x12,
                0x00,
                None,
                "Bombs (5)",
                (
                    "Dodongo's Cavern",
                    "Dodongo's Cavern MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Dodongos Cavern King Dodongo Heart",
            (
                "BossHeart",
                0x12,
                0x4F,
                None,
                "Heart Container",
                (
                    "Dodongo's Cavern",
                    "Dodongo's Cavern MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                ),
            ),
        ),
        # Jabu Jabu's Belly Vanilla
        (
            "Jabu Jabus Belly Boomerang Chest",
            (
                "Chest",
                0x02,
                0x01,
                None,
                "Boomerang",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Map Chest",
            (
                "Chest",
                0x02,
                0x02,
                None,
                "Map (Jabu Jabus Belly)",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Compass Chest",
            (
                "Chest",
                0x02,
                0x04,
                None,
                "Compass (Jabu Jabus Belly)",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Deku Scrub",
            (
                "Scrub",
                0x02,
                0x30,
                None,
                "Buy Deku Nut (5)",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly GS Water Switch Room",
            (
                "GS Token",
                0x02,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly GS Lobby Basement Lower",
            (
                "GS Token",
                0x02,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly GS Lobby Basement Upper",
            (
                "GS Token",
                0x02,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly GS Near Boss",
            (
                "GS Token",
                0x02,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Jabu Jabu's Belly Vanilla Pots
        (
            "Jabu Jabus Belly Above Big Octo Pot 1",
            (
                "Pot",
                0x02,
                (6, 0, 7),
                None,
                "Fairy Drop",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Above Big Octo Pot 2",
            (
                "Pot",
                0x02,
                (6, 0, 8),
                None,
                "Deku Nuts (5)",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Above Big Octo Pot 3",
            (
                "Pot",
                0x02,
                (6, 0, 9),
                None,
                "Deku Nuts (5)",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Basement 2 Octoroks Pot 5",
            (
                "Pot",
                0x02,
                (13, 0, 4),
                None,
                "Fairy Drop",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Basement 2 Octoroks Pot 1",
            (
                "Pot",
                0x02,
                (13, 0, 5),
                None,
                "Rupees (5)",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Basement 2 Octoroks Pot 2",
            (
                "Pot",
                0x02,
                (13, 0, 6),
                None,
                "Rupees (20)",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Basement 2 Octoroks Pot 3",
            (
                "Pot",
                0x02,
                (13, 0, 7),
                None,
                "Rupees (20)",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Basement 2 Octoroks Pot 4",
            (
                "Pot",
                0x02,
                (13, 0, 8),
                None,
                "Rupees (5)",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Basement Switch Room Pot 1",
            (
                "Pot",
                0x02,
                (14, 0, 8),
                None,
                "Deku Seeds (30)",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Basement Switch Room Pot 2",
            (
                "Pot",
                0x02,
                (14, 0, 9),
                None,
                "Fairy Drop",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Basement Switch Room Pot 3",
            (
                "Pot",
                0x02,
                (14, 0, 10),
                None,
                "Deku Seeds (30)",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Small Wooden Crate 1",
            (
                "SmallCrate",
                0x02,
                (1, 0, 7),
                None,
                "Nothing",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Small Wooden Crate 2",
            (
                "SmallCrate",
                0x02,
                (1, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Jabu Jabu's Belly",
                    "Vanilla Dungeons",
                    "Small Crates",
                ),
            ),
        ),
        # Jabu Jabu's Belly MQ
        (
            "Jabu Jabus Belly MQ Map Chest",
            (
                "Chest",
                0x02,
                0x03,
                None,
                "Map (Jabu Jabus Belly)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ First Room Side Chest",
            (
                "Chest",
                0x02,
                0x05,
                None,
                "Deku Nuts (5)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Second Room Lower Chest",
            (
                "Chest",
                0x02,
                0x02,
                None,
                "Deku Nuts (5)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Compass Chest",
            (
                "Chest",
                0x02,
                0x00,
                None,
                "Compass (Jabu Jabus Belly)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Basement Near Switches Chest",
            (
                "Chest",
                0x02,
                0x08,
                None,
                "Deku Nuts (5)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Basement Near Vines Chest",
            (
                "Chest",
                0x02,
                0x04,
                None,
                "Bombchus (10)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Boomerang Room Small Chest",
            (
                "Chest",
                0x02,
                0x01,
                None,
                "Deku Nuts (5)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Boomerang Chest",
            (
                "Chest",
                0x02,
                0x06,
                None,
                "Boomerang",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Falling Like Like Room Chest",
            (
                "Chest",
                0x02,
                0x09,
                None,
                "Deku Stick (1)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Second Room Upper Chest",
            (
                "Chest",
                0x02,
                0x07,
                None,
                "Recovery Heart",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Near Boss Chest",
            (
                "Chest",
                0x02,
                0x0A,
                None,
                "Deku Shield",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Cow",
            (
                "NPC",
                0x02,
                0x15,
                None,
                "Milk",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Cows",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ GS Boomerang Chest Room",
            (
                "GS Token",
                0x02,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ GS Tailpasaran Room",
            (
                "GS Token",
                0x02,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ GS Invisible Enemies Room",
            (
                "GS Token",
                0x02,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ GS Near Boss",
            (
                "GS Token",
                0x02,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Jabu Jabu's Belly MQ Freestanding
        (
            "Jabu Jabus Belly MQ Underwater Green Rupee 1",
            (
                "Freestanding",
                0x02,
                (1, 0, 1),
                None,
                "Rupee (1)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Underwater Green Rupee 2",
            (
                "Freestanding",
                0x02,
                (1, 0, 2),
                None,
                "Rupee (1)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Underwater Green Rupee 3",
            (
                "Freestanding",
                0x02,
                (1, 0, 3),
                None,
                "Rupee (1)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Recovery Heart 1",
            (
                "Freestanding",
                0x02,
                (1, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Recovery Heart 2",
            (
                "Freestanding",
                0x02,
                (1, 0, 10),
                None,
                "Recovery Heart",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        # Jabu Jabu's Belly MQ Pots/Crates
        (
            "Jabu Jabus Belly MQ First Room Pot 1",
            (
                "Pot",
                0x02,
                (0, 0, 16),
                None,
                "Bombs (5)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ First Room Pot 2",
            (
                "Pot",
                0x02,
                (0, 0, 17),
                None,
                "Deku Nuts (5)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Elevator Room Pot 1",
            (
                "Pot",
                0x02,
                (1, 0, 22),
                None,
                "Arrows (5)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Elevator Room Pot 2",
            (
                "Pot",
                0x02,
                (1, 0, 23),
                None,
                "Deku Nuts (5)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Small Crate Near Cow 1",
            (
                "SmallCrate",
                0x02,
                (4, 0, 12),
                None,
                "Nothing",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Small Crate Near Cow 2",
            (
                "SmallCrate",
                0x02,
                (4, 0, 13),
                None,
                "Nothing",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Near Boss Pot",
            (
                "Pot",
                0x02,
                (5, 0, 14),
                None,
                "Fairy Drop",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Hallway Small Crate 1",
            (
                "SmallCrate",
                0x02,
                (7, 0, 6),
                None,
                "Nothing",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Hallway Small Crate 2",
            (
                "SmallCrate",
                0x02,
                (7, 0, 7),
                None,
                "Nothing",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Falling Like Like Room Pot 1",
            (
                "Pot",
                0x02,
                (11, 0, 27),
                None,
                "Arrows (5)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Falling Like Like Room Pot 2",
            (
                "Pot",
                0x02,
                (11, 0, 31),
                None,
                "Bombs (5)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Boomerang Room Pot 1",
            (
                "Pot",
                0x02,
                (14, 0, 11),
                None,
                "Bombs (5)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Boomerang Room Pot 2",
            (
                "Pot",
                0x02,
                (14, 0, 15),
                None,
                "Bombs (5)",
                (
                    "Jabu Jabu's Belly MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        # Jabu Jabu's Belly MQ Wonderitems
        (
            "Jabu Jabus Belly MQ Entryway Left Cow Wonderitem",
            (
                "Wonderitem",
                0x02,
                (0, 0, 15),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Entryway Right Cow Wonderitem",
            (
                "Wonderitem",
                0x02,
                (0, 0, 14),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Elevator Room Cow Wonderitem",
            (
                "Wonderitem",
                0x02,
                (1, 0, 20),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        # ("Jabu Jabus Belly MQ Pit Room Cow Wonderitem",                  ("Wonderitem",   0x02,  (2,0,14), None,                        'Recovery Heart',                        ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"))),
        (
            "Jabu Jabus Belly MQ Basement Right Cow Wonderitem 1",
            (
                "Wonderitem",
                0x02,
                (3, 0, 14),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Basement Right Cow Wonderitem 2",
            (
                "Wonderitem",
                0x02,
                (3, 0, 15),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Basement Right Cow Wonderitem 3",
            (
                "Wonderitem",
                0x02,
                (3, 0, 16),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Basement Left Cow Wonderitem 1",
            (
                "Wonderitem",
                0x02,
                (3, 0, 17),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Basement Left Cow Wonderitem 2",
            (
                "Wonderitem",
                0x02,
                (3, 0, 18),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Basement Left Cow Wonderitem 3",
            (
                "Wonderitem",
                0x02,
                (3, 0, 19),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Wiggler Platforms Cow Wonderitem",
            (
                "Wonderitem",
                0x02,
                (4, 0, 14),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Before Boss Right Cow Wonderitem 1",
            (
                "Wonderitem",
                0x02,
                (5, 0, 10),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Before Boss Right Cow Wonderitem 2",
            (
                "Wonderitem",
                0x02,
                (5, 0, 11),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Before Boss Left Cow Wonderitem",
            (
                "Wonderitem",
                0x02,
                (5, 0, 12),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ After Big Octo Cow Wonderitem",
            (
                "Wonderitem",
                0x02,
                (6, 0, 8),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Falling Like-Like Room Right Cow Wonderitem 1",
            (
                "Wonderitem",
                0x02,
                (11, 0, 20),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Falling Like-Like Room Right Cow Wonderitem 2",
            (
                "Wonderitem",
                0x02,
                (11, 0, 21),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Falling Like-Like Room Right Cow Wonderitem 3",
            (
                "Wonderitem",
                0x02,
                (11, 0, 22),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Falling Like-Like Room Left Cow Wonderitem 1",
            (
                "Wonderitem",
                0x02,
                (11, 0, 23),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Falling Like-Like Room Left Cow Wonderitem 2",
            (
                "Wonderitem",
                0x02,
                (11, 0, 24),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Jabu Jabus Belly MQ Falling Like-Like Room Left Cow Wonderitem 3",
            (
                "Wonderitem",
                0x02,
                (11, 0, 25),
                None,
                "Recovery Heart",
                ("Jabu Jabu's Belly", "Master Quest", "Wonderitem"),
            ),
        ),
        # Jabu Jabu's Belly Shared
        (
            "Jabu Jabus Belly Barinade Heart",
            (
                "BossHeart",
                0x13,
                0x4F,
                None,
                "Heart Container",
                (
                    "Jabu Jabu's Belly",
                    "Jabu Jabu's Belly MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Barinade Pot 1",
            (
                "Pot",
                0x13,
                (1, 0, 2),
                None,
                "Recovery Heart",
                (
                    "Jabu Jabu's Belly",
                    "Jabu Jabu's Belly MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Barinade Pot 2",
            (
                "Pot",
                0x13,
                (1, 0, 3),
                None,
                "Recovery Heart",
                (
                    "Jabu Jabu's Belly",
                    "Jabu Jabu's Belly MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Barinade Pot 3",
            (
                "Pot",
                0x13,
                (1, 0, 4),
                None,
                "Recovery Heart",
                (
                    "Jabu Jabu's Belly",
                    "Jabu Jabu's Belly MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Barinade Pot 4",
            (
                "Pot",
                0x13,
                (1, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Jabu Jabu's Belly",
                    "Jabu Jabu's Belly MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Barinade Pot 5",
            (
                "Pot",
                0x13,
                (1, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Jabu Jabu's Belly",
                    "Jabu Jabu's Belly MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Jabu Jabus Belly Barinade Pot 6",
            (
                "Pot",
                0x13,
                (1, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Jabu Jabu's Belly",
                    "Jabu Jabu's Belly MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        # Bottom of the Well Vanilla
        (
            "Bottom of the Well Front Left Fake Wall Chest",
            (
                "Chest",
                0x08,
                0x08,
                None,
                "Small Key (Bottom of the Well)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well Front Center Bombable Chest",
            (
                "Chest",
                0x08,
                0x02,
                None,
                "Bombchus (10)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well Back Left Bombable Chest",
            (
                "Chest",
                0x08,
                0x04,
                None,
                "Deku Nuts (10)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well Underwater Left Chest",
            (
                "Chest",
                0x08,
                0x09,
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well Freestanding Key",
            (
                "Collectable",
                0x08,
                0x01,
                None,
                "Small Key (Bottom of the Well)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well Compass Chest",
            (
                "Chest",
                0x08,
                0x01,
                None,
                "Compass (Bottom of the Well)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well Center Skulltula Chest",
            (
                "Chest",
                0x08,
                0x0E,
                None,
                "Deku Nuts (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well Right Bottom Fake Wall Chest",
            (
                "Chest",
                0x08,
                0x05,
                None,
                "Small Key (Bottom of the Well)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well Fire Keese Chest",
            (
                "Chest",
                0x08,
                0x0A,
                None,
                "Deku Shield",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well Like Like Chest",
            (
                "Chest",
                0x08,
                0x0C,
                None,
                "Hylian Shield",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well Map Chest",
            (
                "Chest",
                0x08,
                0x07,
                None,
                "Map (Bottom of the Well)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well Underwater Front Chest",
            (
                "Chest",
                0x08,
                0x10,
                None,
                "Bombs (10)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well Invisible Chest",
            (
                "Chest",
                0x08,
                0x14,
                None,
                "Rupees (200)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well Lens of Truth Chest",
            (
                "Chest",
                0x08,
                0x03,
                None,
                "Lens of Truth",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well GS West Inner Room",
            (
                "GS Token",
                0x08,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Bottom of the Well GS East Inner Room",
            (
                "GS Token",
                0x08,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Bottom of the Well GS Like Like Cage",
            (
                "GS Token",
                0x08,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Bottom of the Well Vanilla Freestanding
        (
            "Bottom of the Well Center Room Pit Fall Blue Rupee 1",
            (
                "Freestanding",
                0x08,
                (1, 0, 27),
                None,
                "Rupees (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well Center Room Pit Fall Blue Rupee 2",
            (
                "Freestanding",
                0x08,
                (1, 0, 28),
                None,
                "Rupees (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well Center Room Pit Fall Blue Rupee 3",
            (
                "Freestanding",
                0x08,
                (1, 0, 29),
                None,
                "Rupees (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well Center Room Pit Fall Blue Rupee 4",
            (
                "Freestanding",
                0x08,
                (1, 0, 30),
                None,
                "Rupees (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well Center Room Pit Fall Blue Rupee 5",
            (
                "Freestanding",
                0x08,
                (1, 0, 31),
                None,
                "Rupees (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well Coffin Recovery Heart 1",
            (
                "Freestanding",
                0x08,
                (2, 0, 14),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well Coffin Recovery Heart 2",
            (
                "Freestanding",
                0x08,
                (2, 0, 15),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        # Bottom of the Well Vanilla Pots
        (
            "Bottom of the Well Left Side Pot 1",
            (
                "Pot",
                0x08,
                (0, 0, 23),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Left Side Pot 2",
            (
                "Pot",
                0x08,
                (0, 0, 24),
                None,
                "Rupees (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Left Side Pot 3",
            (
                "Pot",
                0x08,
                (0, 0, 25),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Near Entrance Pot 1",
            (
                "Pot",
                0x08,
                (0, 0, 27),
                None,
                "Rupees (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Near Entrance Pot 2",
            (
                "Pot",
                0x08,
                (0, 0, 28),
                None,
                "Rupees (20)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Underwater Pot",
            (
                "Pot",
                0x08,
                (0, 0, 30),
                None,
                "Bombs (10)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Pot 1",
            (
                "Pot",
                0x08,
                (1, 0, 45),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Pot 2",
            (
                "Pot",
                0x08,
                (1, 0, 46),
                None,
                "Rupees (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Pot 3",
            (
                "Pot",
                0x08,
                (1, 0, 47),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Pot 4",
            (
                "Pot",
                0x08,
                (1, 0, 48),
                None,
                "Rupees (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Pot 5",
            (
                "Pot",
                0x08,
                (1, 0, 49),
                None,
                "Rupees (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Pot 6",
            (
                "Pot",
                0x08,
                (1, 0, 50),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Pot 7",
            (
                "Pot",
                0x08,
                (1, 0, 51),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Pot 8",
            (
                "Pot",
                0x08,
                (1, 0, 52),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Pot 9",
            (
                "Pot",
                0x08,
                (1, 0, 53),
                None,
                "Deku Nuts (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Pot 10",
            (
                "Pot",
                0x08,
                (1, 0, 54),
                None,
                "Rupees (20)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Pot 11",
            (
                "Pot",
                0x08,
                (1, 0, 55),
                None,
                "Rupees (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Pot 12",
            (
                "Pot",
                0x08,
                (1, 0, 56),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well Fire Keese Pot",
            (
                "Pot",
                0x08,
                (3, 0, 7),
                None,
                "Rupees (5)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well West Inner Room Flying Pot 1",
            (
                "FlyingPot",
                0x08,
                (6, 0, 3),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well West Inner Room Flying Pot 2",
            (
                "FlyingPot",
                0x08,
                (6, 0, 4),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well West Inner Room Flying Pot 3",
            (
                "FlyingPot",
                0x08,
                (6, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        # Bottom of the Well Silver Rupees
        (
            "Bottom of the Well Basement Silver Rupee Wood Beam Front",
            (
                "SilverRupee",
                0x08,
                (1, 0, 43),
                None,
                "Silver Rupee (Bottom of the Well Basement)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Silver Rupee Wood Beam Back",
            (
                "SilverRupee",
                0x08,
                (1, 0, 42),
                None,
                "Silver Rupee (Bottom of the Well Basement)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Silver Rupee Ladders Bottom",
            (
                "SilverRupee",
                0x08,
                (1, 0, 41),
                None,
                "Silver Rupee (Bottom of the Well Basement)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Silver Rupee Ladders Middle",
            (
                "SilverRupee",
                0x08,
                (1, 0, 40),
                None,
                "Silver Rupee (Bottom of the Well Basement)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Bottom of the Well Basement Silver Rupee Ladders Top",
            (
                "SilverRupee",
                0x08,
                (1, 0, 39),
                None,
                "Silver Rupee (Bottom of the Well Basement)",
                (
                    "Bottom of the Well",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        # Bottom of the Well MQ
        (
            "Bottom of the Well MQ Map Chest",
            (
                "Chest",
                0x08,
                0x03,
                None,
                "Map (Bottom of the Well)",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ East Inner Room Freestanding Key",
            (
                "Collectable",
                0x08,
                0x01,
                None,
                "Small Key (Bottom of the Well)",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ Compass Chest",
            (
                "Chest",
                0x08,
                0x02,
                None,
                "Compass (Bottom of the Well)",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ Dead Hand Freestanding Key",
            (
                "Collectable",
                0x08,
                0x02,
                None,
                "Small Key (Bottom of the Well)",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ Lens of Truth Chest",
            (
                "Chest",
                0x08,
                0x01,
                None,
                "Lens of Truth",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ GS Coffin Room",
            (
                "GS Token",
                0x08,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ GS West Inner Room",
            (
                "GS Token",
                0x08,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ GS Basement",
            (
                "GS Token",
                0x08,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Bottom of the Well MQ Freestanding
        (
            "Bottom of the Well MQ Bombable Recovery Heart 1",
            (
                "Freestanding",
                0x08,
                (0, 0, 37),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ Bombable Recovery Heart 2",
            (
                "Freestanding",
                0x08,
                (0, 0, 38),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ Basement Recovery Heart 1",
            (
                "Freestanding",
                0x08,
                (1, 0, 28),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ Basement Recovery Heart 2",
            (
                "Freestanding",
                0x08,
                (1, 0, 29),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ Basement Recovery Heart 3",
            (
                "Freestanding",
                0x08,
                (1, 0, 30),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ Coffin Recovery Heart 1",
            (
                "Freestanding",
                0x08,
                (2, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ Coffin Recovery Heart 2",
            (
                "Freestanding",
                0x08,
                (2, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        # Bottom of the Well MQ Pots
        (
            "Bottom of the Well MQ Center Room Right Pot 1",
            (
                "Pot",
                0x08,
                (0, 0, 41),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ Center Room Right Pot 2",
            (
                "Pot",
                0x08,
                (0, 0, 43),
                None,
                "Arrows (10)",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ Center Room Right Pot 3",
            (
                "Pot",
                0x08,
                (0, 0, 45),
                None,
                "Bombs (5)",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ Perimeter Behind Gate Pot",
            (
                "Pot",
                0x08,
                (0, 0, 47),
                None,
                "Fairy Drop",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ East Inner Room Pot 1",
            (
                "Pot",
                0x08,
                (5, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ East Inner Room Pot 2",
            (
                "Pot",
                0x08,
                (5, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Bottom of the Well MQ East Inner Room Pot 3",
            (
                "Pot",
                0x08,
                (5, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Bottom of the Well MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        # Bottom of the Well MQ Wonderitems
        (
            "Bottom of the Well MQ Main Area Left Slingshot Wonderitem 1",
            (
                "Wonderitem",
                0x08,
                (0, 0, 6),
                None,
                "Rupees (20)",
                ("Bottom of the Well", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Bottom of the Well MQ Main Area Left Slingshot Wonderitem 2",
            (
                "Wonderitem",
                0x08,
                (0, 0, 7),
                None,
                "Rupees (20)",
                ("Bottom of the Well", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Bottom of the Well MQ Main Area Left Slingshot Wonderitem 3",
            (
                "Wonderitem",
                0x08,
                (0, 0, 9),
                None,
                "Deku Seeds (30)",
                ("Bottom of the Well", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Bottom of the Well MQ Main Area Left Slingshot Wonderitem 4",
            (
                "Wonderitem",
                0x08,
                (0, 0, 11),
                None,
                "Rupees (20)",
                ("Bottom of the Well", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Bottom of the Well MQ Main Area Right Slingshot Wonderitem 1",
            (
                "Wonderitem",
                0x08,
                (0, 0, 8),
                None,
                "Rupees (20)",
                ("Bottom of the Well", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Bottom of the Well MQ Main Area Right Slingshot Wonderitem 2",
            (
                "Wonderitem",
                0x08,
                (0, 0, 10),
                None,
                "Deku Seeds (30)",
                ("Bottom of the Well", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Bottom of the Well MQ Main Area Right Slingshot Wonderitem 3",
            (
                "Wonderitem",
                0x08,
                (0, 0, 12),
                None,
                "Rupees (20)",
                ("Bottom of the Well", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Bottom of the Well MQ Main Area Right Slingshot Wonderitem 4",
            (
                "Wonderitem",
                0x08,
                (0, 0, 13),
                None,
                "Rupees (20)",
                ("Bottom of the Well", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Bottom of the Well MQ East Inner Room Slingshot Wonderitem 1",
            (
                "Wonderitem",
                0x08,
                (5, 0, 1),
                None,
                "Rupees (20)",
                ("Bottom of the Well", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Bottom of the Well MQ East Inner Room Slingshot Wonderitem 2",
            (
                "Wonderitem",
                0x08,
                (5, 0, 2),
                None,
                "Rupees (20)",
                ("Bottom of the Well", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Bottom of the Well MQ East Inner Room Slingshot Wonderitem 3",
            (
                "Wonderitem",
                0x08,
                (5, 0, 3),
                None,
                "Rupees (20)",
                ("Bottom of the Well", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Bottom of the Well MQ East Inner Room Slingshot Wonderitem 4",
            (
                "Wonderitem",
                0x08,
                (5, 0, 4),
                None,
                "Rupees (20)",
                ("Bottom of the Well", "Master Quest", "Wonderitem"),
            ),
        ),
        # Forest Temple Vanilla
        (
            "Forest Temple First Room Chest",
            (
                "Chest",
                0x03,
                0x03,
                None,
                "Small Key (Forest Temple)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple First Stalfos Chest",
            (
                "Chest",
                0x03,
                0x00,
                None,
                "Small Key (Forest Temple)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple Raised Island Courtyard Chest",
            (
                "Chest",
                0x03,
                0x05,
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple Map Chest",
            (
                "Chest",
                0x03,
                0x01,
                None,
                "Map (Forest Temple)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple Well Chest",
            (
                "Chest",
                0x03,
                0x09,
                None,
                "Small Key (Forest Temple)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple Eye Switch Chest",
            (
                "Chest",
                0x03,
                0x04,
                None,
                "Arrows (30)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple Boss Key Chest",
            (
                "Chest",
                0x03,
                0x0E,
                None,
                "Boss Key (Forest Temple)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple Floormaster Chest",
            (
                "Chest",
                0x03,
                0x02,
                None,
                "Small Key (Forest Temple)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple Red Poe Chest",
            (
                "Chest",
                0x03,
                0x0D,
                None,
                "Small Key (Forest Temple)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple Bow Chest",
            (
                "Chest",
                0x03,
                0x0C,
                None,
                "Bow",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple Blue Poe Chest",
            (
                "Chest",
                0x03,
                0x0F,
                None,
                "Compass (Forest Temple)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple Falling Ceiling Room Chest",
            (
                "Chest",
                0x03,
                0x07,
                None,
                "Arrows (10)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple Basement Chest",
            (
                "Chest",
                0x03,
                0x0B,
                None,
                "Arrows (5)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple GS First Room",
            (
                "GS Token",
                0x03,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Forest Temple GS Lobby",
            (
                "GS Token",
                0x03,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Forest Temple GS Raised Island Courtyard",
            (
                "GS Token",
                0x03,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Forest Temple GS Level Island Courtyard",
            (
                "GS Token",
                0x03,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Forest Temple GS Basement",
            (
                "GS Token",
                0x03,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Forest Temple Vanilla Freestanding
        (
            "Forest Temple Courtyard Recovery Heart 1",
            (
                "Freestanding",
                0x03,
                (8, 0, 10),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Forest Temple Courtyard Recovery Heart 2",
            (
                "Freestanding",
                0x03,
                (8, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Forest Temple Well Recovery Heart 1",
            (
                "Freestanding",
                0x03,
                (9, 0, 3),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Forest Temple Well Recovery Heart 2",
            (
                "Freestanding",
                0x03,
                (9, 0, 4),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        # Forest Temple Vanilla Pots
        (
            "Forest Temple Center Room Right Pot 1",
            (
                "Pot",
                0x03,
                (2, 0, 16),
                None,
                "Arrows (10)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Center Room Right Pot 2",
            (
                "Pot",
                0x03,
                (2, 0, 12),
                None,
                "Rupees (5)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Center Room Right Pot 3",
            (
                "Pot",
                0x03,
                (2, 0, 14),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Center Room Left Pot 1",
            (
                "Pot",
                0x03,
                (2, 0, 17),
                None,
                "Arrows (10)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Center Room Left Pot 2",
            (
                "Pot",
                0x03,
                (2, 0, 13),
                None,
                "Rupees (5)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Center Room Left Pot 3",
            (
                "Pot",
                0x03,
                (2, 0, 15),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Lower Stalfos Pot 1",
            (
                "Pot",
                0x03,
                (6, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Lower Stalfos Pot 2",
            (
                "Pot",
                0x03,
                (6, 0, 7),
                None,
                "Fairy Drop",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Upper Stalfos Pot 1",
            (
                "Pot",
                0x03,
                (6, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Upper Stalfos Pot 2",
            (
                "Pot",
                0x03,
                (6, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Upper Stalfos Pot 3",
            (
                "Pot",
                0x03,
                (6, 0, 10),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Upper Stalfos Pot 4",
            (
                "Pot",
                0x03,
                (6, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Blue Poe Room Pot 1",
            (
                "Pot",
                0x03,
                (13, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Blue Poe Room Pot 2",
            (
                "Pot",
                0x03,
                (13, 0, 7),
                None,
                "Arrows (10)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Blue Poe Room Pot 3",
            (
                "Pot",
                0x03,
                (13, 0, 8),
                None,
                "Arrows (10)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Frozen Eye Switch Room Pot 1",
            (
                "Pot",
                0x03,
                (14, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Frozen Eye Switch Room Pot 2",
            (
                "Pot",
                0x03,
                (14, 0, 7),
                None,
                "Arrows (10)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Green Poe Room Pot 1",
            (
                "Pot",
                0x03,
                (16, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple Green Poe Room Pot 2",
            (
                "Pot",
                0x03,
                (16, 0, 8),
                None,
                "Arrows (10)",
                (
                    "Forest Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        # Forest Temple MQ
        (
            "Forest Temple MQ First Room Chest",
            (
                "Chest",
                0x03,
                0x03,
                None,
                "Small Key (Forest Temple)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple MQ Wolfos Chest",
            (
                "Chest",
                0x03,
                0x00,
                None,
                "Small Key (Forest Temple)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple MQ Well Chest",
            (
                "Chest",
                0x03,
                0x09,
                None,
                "Small Key (Forest Temple)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple MQ Raised Island Courtyard Lower Chest",
            (
                "Chest",
                0x03,
                0x01,
                None,
                "Small Key (Forest Temple)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple MQ Raised Island Courtyard Upper Chest",
            (
                "Chest",
                0x03,
                0x05,
                None,
                "Small Key (Forest Temple)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple MQ Boss Key Chest",
            (
                "Chest",
                0x03,
                0x0E,
                None,
                "Boss Key (Forest Temple)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple MQ Redead Chest",
            (
                "Chest",
                0x03,
                0x02,
                None,
                "Small Key (Forest Temple)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple MQ Map Chest",
            (
                "Chest",
                0x03,
                0x0D,
                None,
                "Map (Forest Temple)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple MQ Bow Chest",
            (
                "Chest",
                0x03,
                0x0C,
                None,
                "Bow",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple MQ Compass Chest",
            (
                "Chest",
                0x03,
                0x0F,
                None,
                "Compass (Forest Temple)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple MQ Falling Ceiling Room Chest",
            (
                "Chest",
                0x03,
                0x06,
                None,
                "Arrows (5)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple MQ Basement Chest",
            (
                "Chest",
                0x03,
                0x0B,
                None,
                "Arrows (5)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Forest Temple MQ GS First Hallway",
            (
                "GS Token",
                0x03,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Forest Temple MQ GS Raised Island Courtyard",
            (
                "GS Token",
                0x03,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Forest Temple MQ GS Level Island Courtyard",
            (
                "GS Token",
                0x03,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Forest Temple MQ GS Well",
            (
                "GS Token",
                0x03,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Forest Temple MQ GS Block Push Room",
            (
                "GS Token",
                0x03,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Forest Temple MQ Freestanding
        (
            "Forest Temple MQ Courtyard Recovery Heart 1",
            (
                "Freestanding",
                0x03,
                (8, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Forest Temple MQ Courtyard Recovery Heart 2",
            (
                "Freestanding",
                0x03,
                (8, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Forest Temple MQ Courtyard Recovery Heart 3",
            (
                "Freestanding",
                0x03,
                (8, 0, 13),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Forest Temple MQ Well Recovery Heart 1",
            (
                "Freestanding",
                0x03,
                (9, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Forest Temple MQ Well Recovery Heart 2",
            (
                "Freestanding",
                0x03,
                (9, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Forest Temple MQ Well Recovery Heart 3",
            (
                "Freestanding",
                0x03,
                (9, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        # Forest Temple MQ Pots
        (
            "Forest Temple MQ Center Room Right Pot 1",
            (
                "Pot",
                0x03,
                (2, 0, 10),
                None,
                "Rupees (5)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Center Room Right Pot 2",
            (
                "Pot",
                0x03,
                (2, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Center Room Right Pot 3",
            (
                "Pot",
                0x03,
                (2, 0, 14),
                None,
                "Arrows (10)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Center Room Left Pot 1",
            (
                "Pot",
                0x03,
                (2, 0, 11),
                None,
                "Rupees (5)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Center Room Left Pot 2",
            (
                "Pot",
                0x03,
                (2, 0, 13),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Center Room Left Pot 3",
            (
                "Pot",
                0x03,
                (2, 0, 15),
                None,
                "Arrows (10)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Wolfos Room Pot 1",
            (
                "Pot",
                0x03,
                (6, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Wolfos Room Pot 2",
            (
                "Pot",
                0x03,
                (6, 0, 8),
                None,
                "Fairy Drop",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Upper Stalfos Pot 1",
            (
                "Pot",
                0x03,
                (6, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Upper Stalfos Pot 2",
            (
                "Pot",
                0x03,
                (6, 0, 10),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Upper Stalfos Pot 3",
            (
                "Pot",
                0x03,
                (6, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Upper Stalfos Pot 4",
            (
                "Pot",
                0x03,
                (6, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Blue Poe Room Pot 1",
            (
                "Pot",
                0x03,
                (13, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Blue Poe Room Pot 2",
            (
                "Pot",
                0x03,
                (13, 0, 7),
                None,
                "Arrows (10)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Blue Poe Room Pot 3",
            (
                "Pot",
                0x03,
                (13, 0, 8),
                None,
                "Arrows (10)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Green Poe Room Pot 1",
            (
                "Pot",
                0x03,
                (16, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Green Poe Room Pot 2",
            (
                "Pot",
                0x03,
                (16, 0, 8),
                None,
                "Arrows (10)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Basement Pot 1",
            (
                "Pot",
                0x03,
                (17, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Basement Pot 2",
            (
                "Pot",
                0x03,
                (17, 0, 13),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Basement Pot 3",
            (
                "Pot",
                0x03,
                (17, 0, 14),
                None,
                "Bombs (5)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Basement Pot 4",
            (
                "Pot",
                0x03,
                (17, 0, 15),
                None,
                "Arrows (5)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Forest Temple MQ Frozen Eye Switch Room Small Wooden Crate 1",
            (
                "SmallCrate",
                0x03,
                (14, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Forest Temple MQ Frozen Eye Switch Room Small Wooden Crate 2",
            (
                "SmallCrate",
                0x03,
                (14, 0, 9),
                None,
                "Arrows (5)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Forest Temple MQ Frozen Eye Switch Room Small Wooden Crate 3",
            (
                "SmallCrate",
                0x03,
                (14, 0, 10),
                None,
                "Arrows (5)",
                (
                    "Forest Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        # Forest Temple Shared
        (
            "Forest Temple Phantom Ganon Heart",
            (
                "BossHeart",
                0x14,
                0x4F,
                None,
                "Heart Container",
                (
                    "Forest Temple",
                    "Forest Temple MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                ),
            ),
        ),
        # Fire Temple Vanilla
        (
            "Fire Temple Near Boss Chest",
            (
                "Chest",
                0x04,
                0x01,
                None,
                "Small Key (Fire Temple)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple Flare Dancer Chest",
            (
                "Chest",
                0x04,
                0x00,
                None,
                "Bombs (10)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple Boss Key Chest",
            (
                "Chest",
                0x04,
                0x0C,
                None,
                "Boss Key (Fire Temple)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple Big Lava Room Lower Open Door Chest",
            (
                "Chest",
                0x04,
                0x04,
                None,
                "Small Key (Fire Temple)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple Big Lava Room Blocked Door Chest",
            (
                "Chest",
                0x04,
                0x02,
                None,
                "Small Key (Fire Temple)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple Boulder Maze Lower Chest",
            (
                "Chest",
                0x04,
                0x03,
                None,
                "Small Key (Fire Temple)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple Boulder Maze Side Room Chest",
            (
                "Chest",
                0x04,
                0x08,
                None,
                "Small Key (Fire Temple)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple Map Chest",
            (
                "Chest",
                0x04,
                0x0A,
                None,
                "Map (Fire Temple)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple Boulder Maze Shortcut Chest",
            (
                "Chest",
                0x04,
                0x0B,
                None,
                "Small Key (Fire Temple)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple Boulder Maze Upper Chest",
            (
                "Chest",
                0x04,
                0x06,
                None,
                "Small Key (Fire Temple)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple Scarecrow Chest",
            (
                "Chest",
                0x04,
                0x0D,
                None,
                "Rupees (200)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple Compass Chest",
            (
                "Chest",
                0x04,
                0x07,
                None,
                "Compass (Fire Temple)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple Megaton Hammer Chest",
            (
                "Chest",
                0x04,
                0x05,
                None,
                "Megaton Hammer",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple Highest Goron Chest",
            (
                "Chest",
                0x04,
                0x09,
                None,
                "Small Key (Fire Temple)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple GS Boss Key Loop",
            (
                "GS Token",
                0x04,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Fire Temple GS Song of Time Room",
            (
                "GS Token",
                0x04,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Fire Temple GS Boulder Maze",
            (
                "GS Token",
                0x04,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Fire Temple GS Scarecrow Climb",
            (
                "GS Token",
                0x04,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Fire Temple GS Scarecrow Top",
            (
                "GS Token",
                0x04,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Fire Temple Vanilla Freestanding
        (
            "Fire Temple Elevator Room Recovery Heart 1",
            (
                "Freestanding",
                0x04,
                (21, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Fire Temple Elevator Room Recovery Heart 2",
            (
                "Freestanding",
                0x04,
                (21, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Fire Temple Elevator Room Recovery Heart 3",
            (
                "Freestanding",
                0x04,
                (21, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Fire Temple Narrow Path Room Recovery Heart 1",
            (
                "Freestanding",
                0x04,
                (6, 0, 1),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Fire Temple Narrow Path Room Recovery Heart 2",
            (
                "Freestanding",
                0x04,
                (6, 0, 2),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Fire Temple Narrow Path Room Recovery Heart 3",
            (
                "Freestanding",
                0x04,
                (6, 0, 3),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Fire Temple Moving Fire Room Recovery Heart 1",
            (
                "Freestanding",
                0x04,
                (16, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Fire Temple Moving Fire Room Recovery Heart 2",
            (
                "Freestanding",
                0x04,
                (16, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Fire Temple Moving Fire Room Recovery Heart 3",
            (
                "Freestanding",
                0x04,
                (16, 0, 10),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        # Fire Temple Vanilla Pots/Crates
        (
            "Fire Temple Big Lava Room Pot 1",
            (
                "Pot",
                0x04,
                (1, 0, 27),
                None,
                "Arrows (10)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Big Lava Room Pot 2",
            (
                "Pot",
                0x04,
                (1, 0, 28),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Big Lava Room Pot 3",
            (
                "Pot",
                0x04,
                (1, 0, 29),
                None,
                "Arrows (10)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Near Boss Pot 1",
            (
                "Pot",
                0x04,
                (2, 0, 9),
                None,
                "Fairy Drop",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Near Boss Pot 2",
            (
                "Pot",
                0x04,
                (2, 0, 10),
                None,
                "Bombs (10)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Near Boss Pot 3",
            (
                "Pot",
                0x04,
                (2, 0, 11),
                None,
                "Bombs (10)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Near Boss Pot 4",
            (
                "Pot",
                0x04,
                (2, 0, 12),
                None,
                "Fairy Drop",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Flame Maze Right Side Pot 1",
            (
                "Pot",
                0x04,
                (10, 0, 52),
                None,
                "Bombs (10)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Flame Maze Right Side Pot 2",
            (
                "Pot",
                0x04,
                (10, 0, 53),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Flame Maze Right Side Pot 3",
            (
                "Pot",
                0x04,
                (10, 0, 54),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Flame Maze Right Side Pot 4",
            (
                "Pot",
                0x04,
                (10, 0, 55),
                None,
                "Bombs (10)",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Flame Maze Left Side Pot 1",
            (
                "Pot",
                0x04,
                (10, 0, 56),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Flame Maze Left Side Pot 2",
            (
                "Pot",
                0x04,
                (10, 0, 57),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Flame Maze Left Side Pot 3",
            (
                "Pot",
                0x04,
                (10, 0, 58),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Flame Maze Left Side Pot 4",
            (
                "Pot",
                0x04,
                (10, 0, 59),
                None,
                "Recovery Heart",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple Hammer Staircase Small Wooden Crate 1",
            (
                "SmallCrate",
                0x04,
                (14, 0, 3),
                None,
                "Nothing",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Fire Temple Hammer Staircase Small Wooden Crate 2",
            (
                "SmallCrate",
                0x04,
                (14, 0, 4),
                None,
                "Nothing",
                (
                    "Fire Temple",
                    "Vanilla Dungeons",
                    "Small Crates",
                ),
            ),
        ),
        # Fire Temple MQ
        (
            "Fire Temple MQ Map Room Side Chest",
            (
                "Chest",
                0x04,
                0x02,
                None,
                "Hylian Shield",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple MQ Megaton Hammer Chest",
            (
                "Chest",
                0x04,
                0x00,
                None,
                "Megaton Hammer",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple MQ Map Chest",
            (
                "Chest",
                0x04,
                0x0C,
                None,
                "Map (Fire Temple)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple MQ Near Boss Chest",
            (
                "Chest",
                0x04,
                0x07,
                None,
                "Small Key (Fire Temple)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple MQ Big Lava Room Blocked Door Chest",
            (
                "Chest",
                0x04,
                0x01,
                None,
                "Small Key (Fire Temple)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple MQ Boss Key Chest",
            (
                "Chest",
                0x04,
                0x04,
                None,
                "Boss Key (Fire Temple)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple MQ Lizalfos Maze Side Room Chest",
            (
                "Chest",
                0x04,
                0x08,
                None,
                "Small Key (Fire Temple)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple MQ Compass Chest",
            (
                "Chest",
                0x04,
                0x0B,
                None,
                "Compass (Fire Temple)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple MQ Lizalfos Maze Upper Chest",
            (
                "Chest",
                0x04,
                0x06,
                None,
                "Bombs (10)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple MQ Lizalfos Maze Lower Chest",
            (
                "Chest",
                0x04,
                0x03,
                None,
                "Bombs (10)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple MQ Freestanding Key",
            (
                "Collectable",
                0x04,
                0x1C,
                None,
                "Small Key (Fire Temple)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Fire Temple MQ Chest On Fire",
            (
                "Chest",
                0x04,
                0x05,
                None,
                "Small Key (Fire Temple)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Fire Temple MQ GS Big Lava Room Open Door",
            (
                "GS Token",
                0x04,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Fire Temple MQ GS Skull On Fire",
            (
                "GS Token",
                0x04,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Fire Temple MQ GS Flame Maze Center",
            (
                "GS Token",
                0x04,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Fire Temple MQ GS Flame Maze Side Room",
            (
                "GS Token",
                0x04,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Fire Temple MQ GS Above Flame Maze",
            (
                "GS Token",
                0x04,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Fire Temple MQ Freestanding
        (
            "Fire Temple MQ Elevator Room Recovery Heart 1",
            (
                "Freestanding",
                0x04,
                (21, 0, 3),
                None,
                "Recovery Heart",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Fire Temple MQ Elevator Room Recovery Heart 2",
            (
                "Freestanding",
                0x04,
                (21, 0, 4),
                None,
                "Recovery Heart",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Fire Temple MQ Elevator Room Recovery Heart 3",
            (
                "Freestanding",
                0x04,
                (21, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        # Fire Temple MQ Pots/Crates
        (
            "Fire Temple MQ First Room Pot 1",
            (
                "Pot",
                0x04,
                (0, 0, 10),
                None,
                "Rupees (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ First Room Pot 2",
            (
                "Pot",
                0x04,
                (0, 0, 11),
                None,
                "Rupees (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Big Lava Room Left Pot",
            (
                "Pot",
                0x04,
                (1, 0, 18),
                None,
                "Arrows (10)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Big Lava Room Right Pot",
            (
                "Pot",
                0x04,
                (1, 0, 20),
                None,
                "Rupees (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Big Lava Room Alcove Pot",
            (
                "Pot",
                0x04,
                (1, 0, 19),
                None,
                "Rupees (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Near Boss Pot 1",
            (
                "Pot",
                0x04,
                (2, 0, 9),
                None,
                "Rupees (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Near Boss Pot 2",
            (
                "Pot",
                0x04,
                (2, 0, 10),
                None,
                "Arrows (30)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Narrow Path Room Pot 1",
            (
                "Pot",
                0x04,
                (6, 0, 3),
                None,
                "Arrows (10)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Narrow Path Room Pot 2",
            (
                "Pot",
                0x04,
                (6, 0, 4),
                None,
                "Bombs (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Narrow Path Room Pot 3",
            (
                "Pot",
                0x04,
                (6, 0, 2),
                None,
                "Fairy Drop",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Flame Maze Right Upper Pot 1",
            (
                "Pot",
                0x04,
                (10, 0, 48),
                None,
                "Bombs (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Flame Maze Right Upper Pot 2",
            (
                "Pot",
                0x04,
                (10, 0, 49),
                None,
                "Recovery Heart",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Flame Maze Right Pot 1",
            (
                "Pot",
                0x04,
                (10, 0, 50),
                None,
                "Bombs (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Flame Maze Right Pot 2",
            (
                "Pot",
                0x04,
                (10, 0, 51),
                None,
                "Recovery Heart",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Flame Maze Left Pot 2",
            (
                "Pot",
                0x04,
                (10, 0, 52),
                None,
                "Fairy Drop",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Flame Maze Left Pot 1",
            (
                "Pot",
                0x04,
                (10, 0, 53),
                None,
                "Bombs (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shoot Torch On Wall Room Pot 1",
            (
                "Pot",
                0x04,
                (16, 0, 6),
                None,
                "Arrows (10)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shoot Torch On Wall Room Pot 2",
            (
                "Pot",
                0x04,
                (16, 0, 7),
                None,
                "Arrows (10)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Iron Knuckle Room Pot 1",
            (
                "Pot",
                0x04,
                (18, 0, 10),
                None,
                "Bombs (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Iron Knuckle Room Pot 2",
            (
                "Pot",
                0x04,
                (18, 0, 12),
                None,
                "Bombs (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Iron Knuckle Room Pot 3",
            (
                "Pot",
                0x04,
                (18, 0, 13),
                None,
                "Bombs (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Iron Knuckle Room Pot 4",
            (
                "Pot",
                0x04,
                (18, 0, 14),
                None,
                "Bombs (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Iron Knuckle Room Pot 5",
            (
                "Pot",
                0x04,
                (18, 0, 9),
                None,
                "Fairy Drop",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Iron Knuckle Room Pot 6",
            (
                "Pot",
                0x04,
                (18, 0, 15),
                None,
                "Fairy Drop",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Iron Knuckle Room Pot 7",
            (
                "Pot",
                0x04,
                (18, 0, 16),
                None,
                "Fairy Drop",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Iron Knuckle Room Pot 8",
            (
                "Pot",
                0x04,
                (18, 0, 11),
                None,
                "Fairy Drop",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Boss Key Chest Room Pot 1",
            (
                "Pot",
                0x04,
                (19, 0, 15),
                None,
                "Rupees (5)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Fire Temple MQ Boss Key Chest Room Pot 2",
            (
                "Pot",
                0x04,
                (19, 0, 14),
                None,
                "Fairy Drop",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        # Fire Temple MQ Crates
        (
            "Fire Temple MQ Near Boss Left Crate 1",
            (
                "Crate",
                0x04,
                (2, 0, 14),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Near Boss Left Crate 2",
            (
                "Crate",
                0x04,
                (2, 0, 15),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Near Boss Right Lower Crate 1",
            (
                "Crate",
                0x04,
                (2, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Near Boss Right Lower Crate 2",
            (
                "Crate",
                0x04,
                (2, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Near Boss Right Mid Crate",
            (
                "Crate",
                0x04,
                (2, 0, 13),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Near Boss Right Upper Crate",
            (
                "Crate",
                0x04,
                (2, 0, 16),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shortcut Crate 1",
            (
                "Crate",
                0x04,
                (4, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shortcut Crate 2",
            (
                "Crate",
                0x04,
                (4, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shortcut Crate 3",
            (
                "Crate",
                0x04,
                (4, 0, 13),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shortcut Crate 4",
            (
                "Crate",
                0x04,
                (4, 0, 14),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shortcut Crate 5",
            (
                "Crate",
                0x04,
                (4, 0, 15),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shortcut Crate 6",
            (
                "Crate",
                0x04,
                (4, 0, 16),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Lower Lizalfos Maze Crate 1",
            (
                "Crate",
                0x04,
                (5, 0, 28),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Lower Lizalfos Maze Crate 2",
            (
                "Crate",
                0x04,
                (5, 0, 29),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Lower Lizalfos Maze Crate 3",
            (
                "Crate",
                0x04,
                (5, 0, 30),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Upper Lizalfos Maze Crate 1",
            (
                "Crate",
                0x04,
                (5, 0, 25),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Upper Lizalfos Maze Crate 2",
            (
                "Crate",
                0x04,
                (5, 0, 26),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Upper Lizalfos Maze Crate 3",
            (
                "Crate",
                0x04,
                (5, 0, 27),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Upper Lizalfos Maze Small Wooden Crate 1",
            (
                "SmallCrate",
                0x04,
                (5, 0, 33),
                None,
                "Nothing",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Upper Lizalfos Maze Small Wooden Crate 2",
            (
                "SmallCrate",
                0x04,
                (5, 0, 34),
                None,
                "Nothing",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shoot Torch On Wall Room Right Crate 1",
            (
                "Crate",
                0x04,
                (16, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shoot Torch On Wall Room Right Crate 2",
            (
                "Crate",
                0x04,
                (16, 0, 13),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shoot Torch On Wall Room Center Crate",
            (
                "Crate",
                0x04,
                (16, 0, 10),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shoot Torch On Wall Room Left Crate 1",
            (
                "Crate",
                0x04,
                (16, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shoot Torch On Wall Room Left Crate 2",
            (
                "Crate",
                0x04,
                (16, 0, 9),
                None,
                "Rupee (1)",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shoot Torch On Wall Room Small Wooden Crate 1",
            (
                "SmallCrate",
                0x04,
                (16, 0, 14),
                None,
                "Nothing",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shoot Torch On Wall Room Small Wooden Crate 2",
            (
                "SmallCrate",
                0x04,
                (16, 0, 15),
                None,
                "Nothing",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shoot Torch On Wall Room Small Wooden Crate 3",
            (
                "SmallCrate",
                0x04,
                (16, 0, 16),
                None,
                "Nothing",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shoot Torch On Wall Room Small Wooden Crate 4",
            (
                "SmallCrate",
                0x04,
                (16, 0, 17),
                None,
                "Nothing",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Fire Temple MQ Shoot Torch On Wall Room Small Wooden Crate 5",
            (
                "SmallCrate",
                0x04,
                (16, 0, 18),
                None,
                "Nothing",
                (
                    "Fire Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        # Fire Temple MQ Wonderitems
        (
            "Fire Temple MQ Shortcut Room Hammer Wonderitem 1",
            (
                "Wonderitem",
                0x04,
                (4, 0, 7),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Fire Temple MQ Shortcut Room Hammer Wonderitem 2",
            (
                "Wonderitem",
                0x04,
                (4, 0, 8),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Fire Temple MQ Shortcut Room Hammer Wonderitem 3",
            (
                "Wonderitem",
                0x04,
                (4, 0, 9),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Fire Temple MQ Maze Face On Wall Hookshot Wonderitem",
            (
                "Wonderitem",
                0x04,
                (5, 0, 20),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Fire Temple MQ Elevator Above Maze Hookshot Wonderitem 1",
            (
                "Wonderitem",
                0x04,
                (7, 0, 5),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Fire Temple MQ Elevator Above Maze Hookshot Wonderitem 2",
            (
                "Wonderitem",
                0x04,
                (7, 0, 6),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Fire Temple MQ Elevator Above Maze Hookshot Wonderitem 3",
            (
                "Wonderitem",
                0x04,
                (7, 0, 7),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Fire Temple MQ Elevator Above Maze Hookshot Wonderitem 4",
            (
                "Wonderitem",
                0x04,
                (7, 0, 8),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Fire Temple MQ Flame Maze Hookshot Wonderitem",
            (
                "Wonderitem",
                0x04,
                (10, 0, 43),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Fire Temple MQ After Upper Flare Dancer Hookshot Wonderitem",
            (
                "Wonderitem",
                0x04,
                (12, 0, 1),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Fire Temple MQ Hammer Steps Hookshot Wonderitem",
            (
                "Wonderitem",
                0x04,
                (14, 0, 2),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Fire Temple MQ Shoot Torch on Wall Room Hookshot Wonderitem",
            (
                "Wonderitem",
                0x04,
                (16, 0, 1),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Fire Temple MQ Boss Key Hookshot Wonderitem",
            (
                "Wonderitem",
                0x04,
                (19, 0, 10),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Fire Temple MQ Boss Key Arrow Wonderitem",
            (
                "Wonderitem",
                0x04,
                (19, 0, 11),
                None,
                "Rupees (20)",
                ("Fire Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        # Fire Temple Shared
        (
            "Fire Temple Volvagia Heart",
            (
                "BossHeart",
                0x15,
                0x4F,
                None,
                "Heart Container",
                (
                    "Fire Temple",
                    "Fire Temple MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                ),
            ),
        ),
        # Water Temple Vanilla
        (
            "Water Temple Compass Chest",
            (
                "Chest",
                0x05,
                0x09,
                None,
                "Compass (Water Temple)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple Map Chest",
            (
                "Chest",
                0x05,
                0x02,
                None,
                "Map (Water Temple)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple Cracked Wall Chest",
            (
                "Chest",
                0x05,
                0x00,
                None,
                "Small Key (Water Temple)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple Torches Chest",
            (
                "Chest",
                0x05,
                0x01,
                None,
                "Small Key (Water Temple)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple Boss Key Chest",
            (
                "Chest",
                0x05,
                0x05,
                None,
                "Boss Key (Water Temple)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple Central Pillar Chest",
            (
                "Chest",
                0x05,
                0x06,
                None,
                "Small Key (Water Temple)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple Central Bow Target Chest",
            (
                "Chest",
                0x05,
                0x08,
                None,
                "Small Key (Water Temple)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple Longshot Chest",
            (
                "Chest",
                0x05,
                0x07,
                None,
                "Progressive Hookshot",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple River Chest",
            (
                "Chest",
                0x05,
                0x03,
                None,
                "Small Key (Water Temple)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple Dragon Chest",
            (
                "Chest",
                0x05,
                0x0A,
                None,
                "Small Key (Water Temple)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple GS Behind Gate",
            (
                "GS Token",
                0x05,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Water Temple GS Near Boss Key Chest",
            (
                "GS Token",
                0x05,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Water Temple GS Central Pillar",
            (
                "GS Token",
                0x05,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Water Temple GS Falling Platform Room",
            (
                "GS Token",
                0x05,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Water Temple GS River",
            (
                "GS Token",
                0x05,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Water Temple Vanilla Freestanding
        (
            "Water Temple River Recovery Heart 1",
            (
                "Freestanding",
                0x05,
                (21, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Water Temple River Recovery Heart 2",
            (
                "Freestanding",
                0x05,
                (21, 0, 13),
                None,
                "Recovery Heart",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Water Temple River Recovery Heart 3",
            (
                "Freestanding",
                0x05,
                (21, 0, 16),
                None,
                "Recovery Heart",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Water Temple River Recovery Heart 4",
            (
                "Freestanding",
                0x05,
                (21, 0, 17),
                None,
                "Recovery Heart",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        # Water Temple Vanilla Pots
        (
            "Water Temple Main Room L2 Pot 1",
            (
                "Pot",
                0x05,
                (0, 0, 24),
                None,
                "Recovery Heart",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Main Room L2 Pot 2",
            (
                "Pot",
                0x05,
                (0, 0, 25),
                None,
                "Recovery Heart",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Near Boss Pot 1",
            (
                "Pot",
                0x05,
                (0, 0, 26),
                None,
                "Fairy Drop",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Near Boss Pot 2",
            (
                "Pot",
                0x05,
                (0, 0, 27),
                None,
                "Fairy Drop",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Behind Gate Pot 1",
            (
                "Pot",
                0x05,
                (3, 0, 10),
                None,
                "Bombs (5)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Behind Gate Pot 2",
            (
                "Pot",
                0x05,
                (3, 0, 11),
                None,
                "Bombs (5)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Behind Gate Pot 3",
            (
                "Pot",
                0x05,
                (3, 0, 14),
                None,
                "Arrows (10)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Behind Gate Pot 4",
            (
                "Pot",
                0x05,
                (3, 0, 15),
                None,
                "Arrows (10)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Near Compass Pot 1",
            (
                "Pot",
                0x05,
                (4, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Near Compass Pot 2",
            (
                "Pot",
                0x05,
                (4, 0, 10),
                None,
                "Recovery Heart",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Near Compass Pot 3",
            (
                "Pot",
                0x05,
                (4, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Like Like Pot 1",
            (
                "Pot",
                0x05,
                (6, 0, 7),
                None,
                "Rupees (5)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Like Like Pot 2",
            (
                "Pot",
                0x05,
                (6, 0, 8),
                None,
                "Rupees (5)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple North Basement Block Puzzle Pot 1",
            (
                "Pot",
                0x05,
                (14, 0, 12),
                None,
                "Bombs (5)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple North Basement Block Puzzle Pot 2",
            (
                "Pot",
                0x05,
                (14, 0, 13),
                None,
                "Bombs (5)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Boss Key Pot 1",
            (
                "Pot",
                0x05,
                (16, 0, 2),
                None,
                "Fairy Drop",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Boss Key Pot 2",
            (
                "Pot",
                0x05,
                (16, 0, 3),
                None,
                "Fairy Drop",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple L1 Torch Pot 1",
            (
                "Pot",
                0x05,
                (17, 0, 8),
                None,
                "Arrows (10)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple L1 Torch Pot 2",
            (
                "Pot",
                0x05,
                (17, 0, 9),
                None,
                "Arrows (10)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple River Pot 1",
            (
                "Pot",
                0x05,
                (21, 0, 14),
                None,
                "Arrows (10)",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple River Pot 2",
            (
                "Pot",
                0x05,
                (21, 0, 15),
                None,
                "Fairy Drop",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Central Bow Target Pot 1",
            (
                "Pot",
                0x05,
                (20, 0, 4),
                None,
                "Recovery Heart",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple Central Bow Target Pot 2",
            (
                "Pot",
                0x05,
                (20, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Water Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        # Water Temple MQ
        (
            "Water Temple MQ Longshot Chest",
            (
                "Chest",
                0x05,
                0x00,
                None,
                "Progressive Hookshot",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple MQ Map Chest",
            (
                "Chest",
                0x05,
                0x02,
                None,
                "Map (Water Temple)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple MQ Compass Chest",
            (
                "Chest",
                0x05,
                0x01,
                None,
                "Compass (Water Temple)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Chest",
            (
                "Chest",
                0x05,
                0x06,
                None,
                "Small Key (Water Temple)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple MQ Boss Key Chest",
            (
                "Chest",
                0x05,
                0x05,
                None,
                "Boss Key (Water Temple)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key",
            (
                "Collectable",
                0x05,
                0x01,
                None,
                "Small Key (Water Temple)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Water Temple MQ GS Lizalfos Hallway",
            (
                "GS Token",
                0x05,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Water Temple MQ GS Before Upper Water Switch",
            (
                "GS Token",
                0x05,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Water Temple MQ GS River",
            (
                "GS Token",
                0x05,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Water Temple MQ GS Freestanding Key Area",
            (
                "GS Token",
                0x05,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Water Temple MQ GS Triple Wall Torch",
            (
                "GS Token",
                0x05,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Water Temple MQ Pots
        (
            "Water Temple MQ Triple Wall Torch Pot 1",
            (
                "Pot",
                0x05,
                (3, 0, 20),
                None,
                "Arrows (10)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Triple Wall Torch Pot 2",
            (
                "Pot",
                0x05,
                (3, 0, 21),
                None,
                "Arrows (10)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Triple Wall Torch Pot 3",
            (
                "Pot",
                0x05,
                (3, 0, 26),
                None,
                "Bombs (5)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Triple Wall Torch Pot 4",
            (
                "Pot",
                0x05,
                (3, 0, 27),
                None,
                "Bombs (5)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Pot 1",
            (
                "Pot",
                0x05,
                (4, 0, 14),
                None,
                "Recovery Heart",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Pot 2",
            (
                "Pot",
                0x05,
                (4, 0, 15),
                None,
                "Recovery Heart",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Pot 3",
            (
                "Pot",
                0x05,
                (4, 0, 16),
                None,
                "Recovery Heart",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Small Wooden Crate 1",
            (
                "SmallCrate",
                0x05,
                (4, 0, 10),
                None,
                "Nothing",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Small Wooden Crate 2",
            (
                "SmallCrate",
                0x05,
                (4, 0, 11),
                None,
                "Nothing",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Small Wooden Crate 3",
            (
                "SmallCrate",
                0x05,
                (4, 0, 12),
                None,
                "Nothing",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Small Wooden Crate 4",
            (
                "SmallCrate",
                0x05,
                (4, 0, 13),
                None,
                "Nothing",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Dark Link Top Pot 1",
            (
                "Pot",
                0x05,
                (6, 0, 8),
                None,
                "Rupees (5)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Dark Link Top Pot 2",
            (
                "Pot",
                0x05,
                (6, 0, 9),
                None,
                "Rupees (5)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Dark Link Lower Pot 1",
            (
                "Pot",
                0x05,
                (6, 0, 10),
                None,
                "Deku Nuts (5)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Dark Link Lower Pot 2",
            (
                "Pot",
                0x05,
                (6, 0, 11),
                None,
                "Fairy Drop",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Dark Link Lower Pot 3",
            (
                "Pot",
                0x05,
                (6, 0, 12),
                None,
                "Fairy Drop",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Room After Dark Link Pot 1",
            (
                "Pot",
                0x05,
                (7, 0, 3),
                None,
                "Arrows (30)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Room After Dark Link Pot 2",
            (
                "Pot",
                0x05,
                (7, 0, 4),
                None,
                "Fairy Drop",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Boss Key Chest Room Pot",
            (
                "Pot",
                0x05,
                (9, 0, 16),
                None,
                "Rupees (5)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Upper Water Switch Pot 1",
            (
                "Pot",
                0x05,
                (10, 0, 18),
                None,
                "Recovery Heart",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Upper Water Switch Pot 2",
            (
                "Pot",
                0x05,
                (10, 0, 19),
                None,
                "Recovery Heart",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Upper Water Switch Pot 3",
            (
                "Pot",
                0x05,
                (10, 0, 20),
                None,
                "Recovery Heart",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Dodongo Room Pot 1",
            (
                "Pot",
                0x05,
                (14, 0, 15),
                None,
                "Bombs (5)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Dodongo Room Pot 2",
            (
                "Pot",
                0x05,
                (14, 0, 16),
                None,
                "Bombs (5)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Room Pot 1",
            (
                "Pot",
                0x05,
                (16, 0, 10),
                None,
                "Rupees (5)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Room Pot 2",
            (
                "Pot",
                0x05,
                (16, 0, 9),
                None,
                "Fairy Drop",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ L1 Torch Pot 1",
            (
                "Pot",
                0x05,
                (17, 0, 14),
                None,
                "Rupees (5)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ L1 Torch Pot 2",
            (
                "Pot",
                0x05,
                (17, 0, 15),
                None,
                "Rupees (5)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Pot 1",
            (
                "Pot",
                0x05,
                (20, 0, 18),
                None,
                "Rupees (20)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Pot 2",
            (
                "Pot",
                0x05,
                (20, 0, 19),
                None,
                "Arrows (10)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Pot 3",
            (
                "Pot",
                0x05,
                (20, 0, 20),
                None,
                "Rupees (5)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Gate Pot 1",
            (
                "Pot",
                0x05,
                (20, 0, 21),
                None,
                "Recovery Heart",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Gate Pot 2",
            (
                "Pot",
                0x05,
                (20, 0, 22),
                None,
                "Recovery Heart",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ River Pot 1",
            (
                "Pot",
                0x05,
                (21, 0, 19),
                None,
                "Arrows (10)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Water Temple MQ River Pot 2",
            (
                "Pot",
                0x05,
                (21, 0, 20),
                None,
                "Fairy Drop",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        # Water Temple MQ Crates
        (
            "Water Temple MQ Central Pillar Upper Crate 1",
            (
                "Crate",
                0x05,
                (1, 0, 4),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Upper Crate 2",
            (
                "Crate",
                0x05,
                (1, 0, 5),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 1",
            (
                "Crate",
                0x05,
                (2, 0, 10),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 2",
            (
                "Crate",
                0x05,
                (2, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 3",
            (
                "Crate",
                0x05,
                (2, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 4",
            (
                "Crate",
                0x05,
                (2, 0, 13),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 5",
            (
                "Crate",
                0x05,
                (2, 0, 14),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 6",
            (
                "Crate",
                0x05,
                (2, 0, 15),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 7",
            (
                "Crate",
                0x05,
                (2, 0, 16),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 8",
            (
                "Crate",
                0x05,
                (2, 0, 17),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 9",
            (
                "Crate",
                0x05,
                (2, 0, 18),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 10",
            (
                "Crate",
                0x05,
                (2, 0, 19),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 11",
            (
                "Crate",
                0x05,
                (2, 0, 20),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 12",
            (
                "Crate",
                0x05,
                (2, 0, 21),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 13",
            (
                "Crate",
                0x05,
                (2, 0, 22),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Central Pillar Lower Crate 14",
            (
                "Crate",
                0x05,
                (2, 0, 23),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Triple Wall Torch Submerged Crate 1",
            (
                "Crate",
                0x05,
                (3, 0, 8),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Triple Wall Torch Submerged Crate 2",
            (
                "Crate",
                0x05,
                (3, 0, 9),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Triple Wall Torch Submerged Crate 3",
            (
                "Crate",
                0x05,
                (3, 0, 10),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Triple Wall Torch Submerged Crate 4",
            (
                "Crate",
                0x05,
                (3, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Triple Wall Torch Submerged Crate 5",
            (
                "Crate",
                0x05,
                (3, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Triple Wall Torch Submerged Crate 6",
            (
                "Crate",
                0x05,
                (3, 0, 13),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Triple Wall Torch Behind Gate Crate 1",
            (
                "Crate",
                0x05,
                (3, 0, 14),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Triple Wall Torch Behind Gate Crate 2",
            (
                "Crate",
                0x05,
                (3, 0, 15),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Triple Wall Torch Behind Gate Crate 3",
            (
                "Crate",
                0x05,
                (3, 0, 16),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Crate 1",
            (
                "Crate",
                0x05,
                (4, 0, 3),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Crate 2",
            (
                "Crate",
                0x05,
                (4, 0, 4),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Crate 3",
            (
                "Crate",
                0x05,
                (4, 0, 5),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Crate 4",
            (
                "Crate",
                0x05,
                (4, 0, 6),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Crate 5",
            (
                "Crate",
                0x05,
                (4, 0, 7),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Crate 6",
            (
                "Crate",
                0x05,
                (4, 0, 8),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Storage Room Crate 7",
            (
                "Crate",
                0x05,
                (4, 0, 9),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue By Torches Crate 1",
            (
                "Crate",
                0x05,
                (8, 0, 9),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue By Torches Crate 2",
            (
                "Crate",
                0x05,
                (8, 0, 10),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue By Torches Small Wooden Crate 1",
            (
                "SmallCrate",
                0x05,
                (8, 0, 17),
                None,
                "Nothing",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue By Torches Small Wooden Crate 2",
            (
                "SmallCrate",
                0x05,
                (8, 0, 18),
                None,
                "Nothing",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue By Torches Small Wooden Crate 3",
            (
                "SmallCrate",
                0x05,
                (8, 0, 19),
                None,
                "Nothing",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue Submerged Crate 1",
            (
                "Crate",
                0x05,
                (8, 0, 13),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue Submerged Crate 2",
            (
                "Crate",
                0x05,
                (8, 0, 14),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue Submerged Crate 3",
            (
                "Crate",
                0x05,
                (8, 0, 15),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue Submerged Crate 4",
            (
                "Crate",
                0x05,
                (8, 0, 16),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue Near Door Crate 1",
            (
                "Crate",
                0x05,
                (8, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue Near Door Crate 2",
            (
                "Crate",
                0x05,
                (8, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Boss Key Chest Room Upper Crate",
            (
                "Crate",
                0x05,
                (9, 0, 3),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Boss Key Chest Room Lower Crate 1",
            (
                "Crate",
                0x05,
                (9, 0, 2),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Boss Key Chest Room Lower Crate 2",
            (
                "Crate",
                0x05,
                (9, 0, 4),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Boss Key Chest Room Lower Crate 3",
            (
                "Crate",
                0x05,
                (9, 0, 5),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Boss Key Chest Room Lower Crate 4",
            (
                "Crate",
                0x05,
                (9, 0, 6),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Upper Water Switch Lower Crate 1",
            (
                "Crate",
                0x05,
                (10, 0, 4),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Upper Water Switch Lower Crate 2",
            (
                "Crate",
                0x05,
                (10, 0, 5),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Upper Water Switch Lower Crate 3",
            (
                "Crate",
                0x05,
                (10, 0, 6),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Upper Water Switch Lower Crate 4",
            (
                "Crate",
                0x05,
                (10, 0, 7),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Upper Water Switch Lower Crate 5",
            (
                "Crate",
                0x05,
                (10, 0, 8),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Upper Water Switch Lower Crate 6",
            (
                "Crate",
                0x05,
                (10, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Upper Water Switch Lower Small Crate",
            (
                "SmallCrate",
                0x05,
                (10, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Upper Water Switch Upper Small Crate",
            (
                "SmallCrate",
                0x05,
                (10, 0, 13),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Upper Water Switch Upper Crate 1",
            (
                "Crate",
                0x05,
                (10, 0, 9),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Before Upper Water Switch Upper Crate 2",
            (
                "Crate",
                0x05,
                (10, 0, 10),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Area Behind Gate Crate 1",
            (
                "Crate",
                0x05,
                (12, 0, 10),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Area Behind Gate Crate 2",
            (
                "Crate",
                0x05,
                (12, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Area Behind Gate Crate 3",
            (
                "Crate",
                0x05,
                (12, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Area Behind Gate Crate 4",
            (
                "Crate",
                0x05,
                (12, 0, 13),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Area Front Crate 1",
            (
                "Crate",
                0x05,
                (12, 0, 14),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Area Front Crate 2",
            (
                "Crate",
                0x05,
                (12, 0, 15),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Area Submerged Crate 1",
            (
                "Crate",
                0x05,
                (12, 0, 16),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Area Submerged Crate 2",
            (
                "Crate",
                0x05,
                (12, 0, 17),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Area Submerged Crate 3",
            (
                "Crate",
                0x05,
                (12, 0, 18),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Area Submerged Crate 4",
            (
                "Crate",
                0x05,
                (12, 0, 19),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Area Submerged Crate 5",
            (
                "Crate",
                0x05,
                (12, 0, 20),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Area Submerged Crate 6",
            (
                "Crate",
                0x05,
                (12, 0, 21),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dodongo Room Lower Crate 1",
            (
                "Crate",
                0x05,
                (14, 0, 9),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dodongo Room Lower Crate 2",
            (
                "Crate",
                0x05,
                (14, 0, 10),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dodongo Room Lower Crate 3",
            (
                "Crate",
                0x05,
                (14, 0, 13),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dodongo Room Upper Crate",
            (
                "Crate",
                0x05,
                (14, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Dodongo Room Hall Crate",
            (
                "Crate",
                0x05,
                (14, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Room Crate 1",
            (
                "Crate",
                0x05,
                (16, 0, 3),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Room Crate 2",
            (
                "Crate",
                0x05,
                (16, 0, 4),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Room Crate 3",
            (
                "Crate",
                0x05,
                (16, 0, 5),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Room Crate 4",
            (
                "Crate",
                0x05,
                (16, 0, 6),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Room Crate 5",
            (
                "Crate",
                0x05,
                (16, 0, 7),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Gate Crate 1",
            (
                "Crate",
                0x05,
                (20, 0, 5),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Gate Crate 2",
            (
                "Crate",
                0x05,
                (20, 0, 6),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Room Crate 1",
            (
                "Crate",
                0x05,
                (20, 0, 7),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Room Crate 2",
            (
                "Crate",
                0x05,
                (20, 0, 8),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Room Crate 3",
            (
                "Crate",
                0x05,
                (20, 0, 9),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Room Crate 4",
            (
                "Crate",
                0x05,
                (20, 0, 10),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Room Crate 5",
            (
                "Crate",
                0x05,
                (20, 0, 11),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Hall Crate 1",
            (
                "Crate",
                0x05,
                (20, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Hall Crate 2",
            (
                "Crate",
                0x05,
                (20, 0, 13),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Hall Crate 3",
            (
                "Crate",
                0x05,
                (20, 0, 14),
                None,
                "Rupee (1)",
                (
                    "Water Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        # Water Temple MQ Wonderitems
        (
            "Water Temple MQ Below Central Pillar Hookshot Wonderitem",
            (
                "Wonderitem",
                0x05,
                (2, 0, 25),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Triple Wall Torch Hookshot/Bow Wonderitem",
            (
                "Wonderitem",
                0x05,
                (3, 0, 4),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Hookshot Waterfall Left Hookshot Wonderitem 1",
            (
                "Wonderitem",
                0x05,
                (5, 0, 10),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Hookshot Waterfall Left Hookshot Wonderitem 2",
            (
                "Wonderitem",
                0x05,
                (5, 0, 11),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Hookshot Waterfall Left Hookshot Wonderitem 3",
            (
                "Wonderitem",
                0x05,
                (5, 0, 12),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Hookshot Waterfall Right Hookshot Wonderitem 1",
            (
                "Wonderitem",
                0x05,
                (5, 0, 3),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Hookshot Waterfall Right Hookshot Wonderitem 2",
            (
                "Wonderitem",
                0x05,
                (5, 0, 4),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Hookshot Waterfall Right Hookshot Wonderitem 3",
            (
                "Wonderitem",
                0x05,
                (5, 0, 5),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ After Dark Link Hookshot Wonderitem",
            (
                "Wonderitem",
                0x05,
                (7, 0, 1),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue Eyes Hookshot Wonderitem 1",
            (
                "Wonderitem",
                0x05,
                (8, 0, 5),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue Eyes Hookshot Wonderitem 2",
            (
                "Wonderitem",
                0x05,
                (8, 0, 7),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Dragon Statue Crates Hookshot Wonderitem",
            (
                "Wonderitem",
                0x05,
                (8, 0, 6),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Upper Water Switch Hookshot Wonderitem",
            (
                "Wonderitem",
                0x05,
                (10, 0, 2),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Boss Hallway Hookshot Wonderitem 1",
            (
                "Wonderitem",
                0x05,
                (11, 0, 1),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Boss Hallway Hookshot Wonderitem 2",
            (
                "Wonderitem",
                0x05,
                (11, 0, 2),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ 3 Water Spouts Proximity Wonderitem 1",
            (
                "Wonderitem",
                0x05,
                (15, 0, 1),
                None,
                "Rupees (5)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ 3 Water Spouts Proximity Wonderitem 2",
            (
                "Wonderitem",
                0x05,
                (15, 0, 2),
                None,
                "Arrows (10)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Freestanding Key Hookshot Wonderitem",
            (
                "Wonderitem",
                0x05,
                (16, 0, 1),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Longshot Chest Hookshot Wonderitem",
            (
                "Wonderitem",
                0x05,
                (17, 0, 8),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Compass Chest Hookshot Wonderitem",
            (
                "Wonderitem",
                0x05,
                (18, 0, 4),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Map Chest Hookshot Wonderitem",
            (
                "Wonderitem",
                0x05,
                (19, 0, 6),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Water Temple MQ Lizalfos Hallway Hookshot Wonderitem",
            (
                "Wonderitem",
                0x05,
                (20, 0, 3),
                None,
                "Rupees (20)",
                ("Water Temple MQ", "Master Quest", "Wonderitem"),
            ),
        ),
        # Water Temple Shared
        (
            "Water Temple Morpha Heart",
            (
                "BossHeart",
                0x16,
                0x4F,
                None,
                "Heart Container",
                (
                    "Water Temple",
                    "Water Temple MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                ),
            ),
        ),
        # Shadow Temple Vanilla
        (
            "Shadow Temple Map Chest",
            (
                "Chest",
                0x07,
                0x01,
                None,
                "Map (Shadow Temple)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple Hover Boots Chest",
            (
                "Chest",
                0x07,
                0x07,
                None,
                "Hover Boots",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple Compass Chest",
            (
                "Chest",
                0x07,
                0x03,
                None,
                "Compass (Shadow Temple)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple Early Silver Rupee Chest",
            (
                "Chest",
                0x07,
                0x02,
                None,
                "Small Key (Shadow Temple)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple Invisible Blades Visible Chest",
            (
                "Chest",
                0x07,
                0x0C,
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple Invisible Blades Invisible Chest",
            (
                "Chest",
                0x07,
                0x16,
                None,
                "Arrows (30)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple Falling Spikes Lower Chest",
            (
                "Chest",
                0x07,
                0x05,
                None,
                "Arrows (10)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple Falling Spikes Upper Chest",
            (
                "Chest",
                0x07,
                0x06,
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple Falling Spikes Switch Chest",
            (
                "Chest",
                0x07,
                0x04,
                None,
                "Small Key (Shadow Temple)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple Invisible Spikes Chest",
            (
                "Chest",
                0x07,
                0x09,
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple Freestanding Key",
            (
                "Collectable",
                0x07,
                0x01,
                None,
                "Small Key (Shadow Temple)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple Wind Hint Chest",
            (
                "Chest",
                0x07,
                0x15,
                None,
                "Arrows (10)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple After Wind Enemy Chest",
            (
                "Chest",
                0x07,
                0x08,
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple After Wind Hidden Chest",
            (
                "Chest",
                0x07,
                0x14,
                None,
                "Small Key (Shadow Temple)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple Spike Walls Left Chest",
            (
                "Chest",
                0x07,
                0x0A,
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple Boss Key Chest",
            (
                "Chest",
                0x07,
                0x0B,
                None,
                "Boss Key (Shadow Temple)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple Invisible Floormaster Chest",
            (
                "Chest",
                0x07,
                0x0D,
                None,
                "Small Key (Shadow Temple)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple GS Invisible Blades Room",
            (
                "GS Token",
                0x07,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Shadow Temple GS Falling Spikes Room",
            (
                "GS Token",
                0x07,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Shadow Temple GS Single Giant Pot",
            (
                "GS Token",
                0x07,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Shadow Temple GS Near Ship",
            (
                "GS Token",
                0x07,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Shadow Temple GS Triple Giant Pot",
            (
                "GS Token",
                0x07,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Shadow Temple Vanilla Freestanding
        (
            "Shadow Temple Invisible Blades Recovery Heart 1",
            (
                "Freestanding",
                0x07,
                (16, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple Invisible Blades Recovery Heart 2",
            (
                "Freestanding",
                0x07,
                (16, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple Before Boat Recovery Heart 1",
            (
                "Freestanding",
                0x07,
                (21, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple Before Boat Recovery Heart 2",
            (
                "Freestanding",
                0x07,
                (21, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple After Boat Upper Recovery Heart 1",
            (
                "Freestanding",
                0x07,
                (21, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple After Boat Upper Recovery Heart 2",
            (
                "Freestanding",
                0x07,
                (21, 0, 10),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple After Boat Lower Recovery Heart",
            (
                "Freestanding",
                0x07,
                (21, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple 3 Spinning Pots Rupee 1",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 1), (12, 0, 10, 1), (12, 0, 11, 1)],
                None,
                "Rupee (1)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple 3 Spinning Pots Rupee 2",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 2), (12, 0, 10, 2), (12, 0, 11, 2)],
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple 3 Spinning Pots Rupee 3",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 3), (12, 0, 10, 3), (12, 0, 11, 3)],
                None,
                "Rupees (20)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple 3 Spinning Pots Rupee 4",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 4), (12, 0, 10, 4), (12, 0, 11, 4)],
                None,
                "Rupee (1)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple 3 Spinning Pots Rupee 5",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 5), (12, 0, 10, 5), (12, 0, 11, 5)],
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple 3 Spinning Pots Rupee 6",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 6), (12, 0, 10, 6), (12, 0, 11, 6)],
                None,
                "Rupees (20)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple 3 Spinning Pots Rupee 7",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 7), (12, 0, 10, 7), (12, 0, 11, 7)],
                None,
                "Rupee (1)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple 3 Spinning Pots Rupee 8",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 8), (12, 0, 10, 8), (12, 0, 11, 8)],
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple 3 Spinning Pots Rupee 9",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 9), (12, 0, 10, 9), (12, 0, 11, 9)],
                None,
                "Rupees (20)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        # Shadow Temple Vanilla Pots
        (
            "Shadow Temple Whispering Walls Near Dead Hand Pot",
            (
                "Pot",
                0x07,
                (0, 0, 1),
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Whispering Walls Left Pot 1",
            (
                "Pot",
                0x07,
                (0, 0, 2),
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Whispering Walls Left Pot 2",
            (
                "Pot",
                0x07,
                (0, 0, 3),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Whispering Walls Left Pot 3",
            (
                "Pot",
                0x07,
                (0, 0, 4),
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Whispering Walls Front Pot 1",
            (
                "Pot",
                0x07,
                (0, 0, 5),
                None,
                "Deku Nuts (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Whispering Walls Front Pot 2",
            (
                "Pot",
                0x07,
                (0, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Whispering Walls Flying Pot",
            (
                "FlyingPot",
                0x07,
                (0, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Map Chest Room Pot 1",
            (
                "Pot",
                0x07,
                (1, 0, 4),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Map Chest Room Pot 2",
            (
                "Pot",
                0x07,
                (1, 0, 5),
                None,
                "Arrows (10)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Falling Spikes Lower Pot 1",
            (
                "Pot",
                0x07,
                (10, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Falling Spikes Lower Pot 2",
            (
                "Pot",
                0x07,
                (10, 0, 4),
                None,
                "Bombs (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Falling Spikes Upper Pot 1",
            (
                "Pot",
                0x07,
                (10, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Falling Spikes Upper Pot 2",
            (
                "Pot",
                0x07,
                (10, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Spike Walls Pot",
            (
                "Pot",
                0x07,
                (13, 0, 3),
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Invisible Floormaster Pot 1",
            (
                "Pot",
                0x07,
                (17, 0, 2),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Invisible Floormaster Pot 2",
            (
                "Pot",
                0x07,
                (17, 0, 3),
                None,
                "Arrows (30)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple After Wind Pot 1",
            (
                "Pot",
                0x07,
                (20, 0, 3),
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple After Wind Pot 2",
            (
                "Pot",
                0x07,
                (20, 0, 4),
                None,
                "Deku Nuts (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple After Wind Flying Pot 1",
            (
                "FlyingPot",
                0x07,
                (20, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Shadow Temple After Wind Flying Pot 2",
            (
                "FlyingPot",
                0x07,
                (20, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Shadow Temple After Boat Pot 1",
            (
                "Pot",
                0x07,
                (21, 0, 17),
                None,
                "Arrows (10)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple After Boat Pot 2",
            (
                "Pot",
                0x07,
                (21, 0, 18),
                None,
                "Nothing",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Near Boss Pot 1",
            (
                "Pot",
                0x07,
                (21, 0, 19),
                None,
                "Arrows (30)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple Near Boss Pot 2",
            (
                "Pot",
                0x07,
                (21, 0, 20),
                None,
                "Rupees (5)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        # Shadow Temple Silver Rupees
        (
            "Shadow Temple Scythe Shortcut Silver Rupee Center Left",
            (
                "SilverRupee",
                0x07,
                (6, 0, 1),
                None,
                "Silver Rupee (Shadow Temple Scythe Shortcut)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Scythe Shortcut Silver Rupee Center Right",
            (
                "SilverRupee",
                0x07,
                (6, 0, 5),
                None,
                "Silver Rupee (Shadow Temple Scythe Shortcut)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Scythe Shortcut Silver Rupee Left Alcove",
            (
                "SilverRupee",
                0x07,
                (6, 0, 4),
                None,
                "Silver Rupee (Shadow Temple Scythe Shortcut)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Scythe Shortcut Silver Rupee Back Alcove",
            (
                "SilverRupee",
                0x07,
                (6, 0, 3),
                None,
                "Silver Rupee (Shadow Temple Scythe Shortcut)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Scythe Shortcut Silver Rupee Ledge",
            (
                "SilverRupee",
                0x07,
                (6, 0, 2),
                None,
                "Silver Rupee (Shadow Temple Scythe Shortcut)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Huge Pit Silver Rupee Left",
            (
                "SilverRupee",
                0x07,
                (9, 0, 8),
                None,
                "Silver Rupee (Shadow Temple Huge Pit)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Huge Pit Silver Rupee Center Front",
            (
                "SilverRupee",
                0x07,
                (9, 0, 10),
                None,
                "Silver Rupee (Shadow Temple Huge Pit)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Huge Pit Silver Rupee Center",
            (
                "SilverRupee",
                0x07,
                (9, 0, 9),
                None,
                "Silver Rupee (Shadow Temple Huge Pit)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Huge Pit Silver Rupee Center Back",
            (
                "SilverRupee",
                0x07,
                (9, 0, 11),
                None,
                "Silver Rupee (Shadow Temple Huge Pit)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Huge Pit Silver Rupee Right",
            (
                "SilverRupee",
                0x07,
                (9, 0, 7),
                None,
                "Silver Rupee (Shadow Temple Huge Pit)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Invisible Spikes Silver Rupee Right",
            (
                "SilverRupee",
                0x07,
                (11, 0, 4),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Invisible Spikes Silver Rupee Center",
            (
                "SilverRupee",
                0x07,
                (11, 0, 5),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Invisible Spikes Silver Rupee Left",
            (
                "SilverRupee",
                0x07,
                (11, 0, 6),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Invisible Spikes Silver Rupee Ledge",
            (
                "SilverRupee",
                0x07,
                (11, 0, 3),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple Invisible Spikes Silver Rupee Near Ledge",
            (
                "SilverRupee",
                0x07,
                (11, 0, 7),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        # Shadow Temple Wonderitems
        (
            "Shadow Temple 3 Spinning Pots Wonderitem",
            (
                "Wonderitem",
                0x07,
                (12, 0, 2),
                None,
                "Arrows (10)",
                ("Shadow Temple", "Vanilla Dungeons", "Wonderitem"),
            ),
        ),
        # Shadow Temple MQ
        (
            "Shadow Temple MQ Early Gibdos Chest",
            (
                "Chest",
                0x07,
                0x03,
                None,
                "Small Key (Shadow Temple)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Map Chest",
            (
                "Chest",
                0x07,
                0x02,
                None,
                "Map (Shadow Temple)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Near Ship Invisible Chest",
            (
                "Chest",
                0x07,
                0x0E,
                None,
                "Small Key (Shadow Temple)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Compass Chest",
            (
                "Chest",
                0x07,
                0x01,
                None,
                "Compass (Shadow Temple)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Hover Boots Chest",
            (
                "Chest",
                0x07,
                0x07,
                None,
                "Hover Boots",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Blades Invisible Chest",
            (
                "Chest",
                0x07,
                0x16,
                None,
                "Small Key (Shadow Temple)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Blades Visible Chest",
            (
                "Chest",
                0x07,
                0x0C,
                None,
                "Rupees (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Beamos Silver Rupees Chest",
            (
                "Chest",
                0x07,
                0x0F,
                None,
                "Arrows (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Falling Spikes Lower Chest",
            (
                "Chest",
                0x07,
                0x05,
                None,
                "Arrows (10)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Falling Spikes Upper Chest",
            (
                "Chest",
                0x07,
                0x06,
                None,
                "Rupees (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Falling Spikes Switch Chest",
            (
                "Chest",
                0x07,
                0x04,
                None,
                "Small Key (Shadow Temple)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Spikes Chest",
            (
                "Chest",
                0x07,
                0x09,
                None,
                "Rupees (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Stalfos Room Chest",
            (
                "Chest",
                0x07,
                0x10,
                None,
                "Rupees (20)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Wind Hint Chest",
            (
                "Chest",
                0x07,
                0x15,
                None,
                "Small Key (Shadow Temple)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ After Wind Hidden Chest",
            (
                "Chest",
                0x07,
                0x14,
                None,
                "Arrows (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ After Wind Enemy Chest",
            (
                "Chest",
                0x07,
                0x08,
                None,
                "Rupees (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Boss Key Chest",
            (
                "Chest",
                0x07,
                0x0B,
                None,
                "Boss Key (Shadow Temple)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Spike Walls Left Chest",
            (
                "Chest",
                0x07,
                0x0A,
                None,
                "Rupees (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Freestanding Key",
            (
                "Collectable",
                0x07,
                0x06,
                None,
                "Small Key (Shadow Temple)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Bomb Flower Chest",
            (
                "Chest",
                0x07,
                0x0D,
                None,
                "Arrows (10)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Shadow Temple MQ GS Falling Spikes Room",
            (
                "GS Token",
                0x07,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Shadow Temple MQ GS Wind Hint Room",
            (
                "GS Token",
                0x07,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Shadow Temple MQ GS After Wind",
            (
                "GS Token",
                0x07,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Shadow Temple MQ GS After Ship",
            (
                "GS Token",
                0x07,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Shadow Temple MQ GS Near Boss",
            (
                "GS Token",
                0x07,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Shadow Temple MQ Freestanding
        (
            "Shadow Temple MQ Invisible Blades Recovery Heart 1",
            (
                "Freestanding",
                0x07,
                (16, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Blades Recovery Heart 2",
            (
                "Freestanding",
                0x07,
                (16, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Before Boat Recovery Heart 1",
            (
                "Freestanding",
                0x07,
                (21, 0, 10),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Before Boat Recovery Heart 2",
            (
                "Freestanding",
                0x07,
                (21, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ After Boat Upper Recovery Heart 1",
            (
                "Freestanding",
                0x07,
                (21, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ After Boat Upper Recovery Heart 2",
            (
                "Freestanding",
                0x07,
                (21, 0, 13),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ After Boat Lower Recovery Heart",
            (
                "Freestanding",
                0x07,
                (21, 0, 14),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ 3 Spinning Pots Rupee 1",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 1), (12, 0, 10, 1), (12, 0, 11, 1)],
                None,
                "Rupee (1)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ 3 Spinning Pots Rupee 2",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 2), (12, 0, 10, 2), (12, 0, 11, 2)],
                None,
                "Rupees (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ 3 Spinning Pots Rupee 3",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 3), (12, 0, 10, 3), (12, 0, 11, 3)],
                None,
                "Rupees (20)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ 3 Spinning Pots Rupee 4",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 4), (12, 0, 10, 4), (12, 0, 11, 4)],
                None,
                "Rupee (1)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ 3 Spinning Pots Rupee 5",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 5), (12, 0, 10, 5), (12, 0, 11, 5)],
                None,
                "Rupees (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ 3 Spinning Pots Rupee 6",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 6), (12, 0, 10, 6), (12, 0, 11, 6)],
                None,
                "Rupees (20)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ 3 Spinning Pots Rupee 7",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 7), (12, 0, 10, 7), (12, 0, 11, 7)],
                None,
                "Rupee (1)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ 3 Spinning Pots Rupee 8",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 8), (12, 0, 10, 8), (12, 0, 11, 8)],
                None,
                "Rupees (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Shadow Temple MQ 3 Spinning Pots Rupee 9",
            (
                "Freestanding",
                0x07,
                [(12, 0, 9, 9), (12, 0, 10, 9), (12, 0, 11, 9)],
                None,
                "Rupees (20)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        # Shadow Temple MQ Pots/Crates
        (
            "Shadow Temple MQ Whispering Walls Pot 1",
            (
                "Pot",
                0x07,
                (0, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Whispering Walls Pot 2",
            (
                "Pot",
                0x07,
                (0, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Whispering Walls After Time Block Flying Pot 1",
            (
                "FlyingPot",
                0x07,
                (0, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Whispering Walls After Time Block Flying Pot 2",
            (
                "FlyingPot",
                0x07,
                (0, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Whispering Walls Before Time Block Flying Pot 1",
            (
                "FlyingPot",
                0x07,
                (0, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Whispering Walls Before Time Block Flying Pot 2",
            (
                "FlyingPot",
                0x07,
                (0, 0, 10),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Compass Room Pot 1",
            (
                "Pot",
                0x07,
                (1, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Compass Room Pot 2",
            (
                "Pot",
                0x07,
                (1, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Falling Spikes Lower Pot 1",
            (
                "Pot",
                0x07,
                (10, 0, 4),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Falling Spikes Lower Pot 2",
            (
                "Pot",
                0x07,
                (10, 0, 5),
                None,
                "Bombs (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Falling Spikes Upper Pot 1",
            (
                "Pot",
                0x07,
                (10, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Falling Spikes Upper Pot 2",
            (
                "Pot",
                0x07,
                (10, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ After Wind Pot 1",
            (
                "Pot",
                0x07,
                (20, 0, 4),
                None,
                "Rupees (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ After Wind Pot 2",
            (
                "Pot",
                0x07,
                (20, 0, 5),
                None,
                "Deku Nuts (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ After Wind Flying Pot 1",
            (
                "FlyingPot",
                0x07,
                (20, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ After Wind Flying Pot 2",
            (
                "FlyingPot",
                0x07,
                (20, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ After Boat Pot 1",
            (
                "Pot",
                0x07,
                (21, 0, 20),
                None,
                "Arrows (10)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ After Boat Pot 2",
            (
                "Pot",
                0x07,
                (21, 0, 21),
                None,
                "Arrows (10)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Near Boss Pot 1",
            (
                "Pot",
                0x07,
                (21, 0, 22),
                None,
                "Rupees (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Near Boss Pot 2",
            (
                "Pot",
                0x07,
                (21, 0, 23),
                None,
                "Arrows (30)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Bomb Flower Room Pot 1",
            (
                "Pot",
                0x07,
                (17, 0, 2),
                None,
                "Arrows (30)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Bomb Flower Room Pot 2",
            (
                "Pot",
                0x07,
                (17, 0, 3),
                None,
                "Bombs (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Spike Walls Pot",
            (
                "Pot",
                0x07,
                (13, 0, 9),
                None,
                "Rupees (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Truth Spinner Small Wooden Crate 1",
            (
                "SmallCrate",
                0x07,
                (2, 0, 16),
                None,
                "Arrows (10)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Truth Spinner Small Wooden Crate 2",
            (
                "SmallCrate",
                0x07,
                (2, 0, 17),
                None,
                "Rupees (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Truth Spinner Small Wooden Crate 3",
            (
                "SmallCrate",
                0x07,
                (2, 0, 18),
                None,
                "Bombs (5)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Truth Spinner Small Wooden Crate 4",
            (
                "SmallCrate",
                0x07,
                (2, 0, 19),
                None,
                "Recovery Heart",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        # Shadow Temple MQ Silver Rupees
        (
            "Shadow Temple MQ Scythe Shortcut Silver Rupee Center Left",
            (
                "SilverRupee",
                0x07,
                (6, 0, 7),
                None,
                "Silver Rupee (Shadow Temple Scythe Shortcut)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Scythe Shortcut Silver Rupee Center Right",
            (
                "SilverRupee",
                0x07,
                (6, 0, 8),
                None,
                "Silver Rupee (Shadow Temple Scythe Shortcut)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Scythe Shortcut Silver Rupee Ledge",
            (
                "SilverRupee",
                0x07,
                (6, 0, 6),
                None,
                "Silver Rupee (Shadow Temple Scythe Shortcut)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Scythe Shortcut Silver Rupee Left Alcove",
            (
                "SilverRupee",
                0x07,
                (6, 0, 5),
                None,
                "Silver Rupee (Shadow Temple Scythe Shortcut)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Scythe Shortcut Silver Rupee Back Alcove",
            (
                "SilverRupee",
                0x07,
                (6, 0, 9),
                None,
                "Silver Rupee (Shadow Temple Scythe Shortcut)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Blades Silver Rupee 1",
            (
                "SilverRupee",
                0x07,
                (16, 0, 9),
                None,
                "Silver Rupee (Shadow Temple Invisible Blades)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Blades Silver Rupee 2",
            (
                "SilverRupee",
                0x07,
                (16, 0, 10),
                None,
                "Silver Rupee (Shadow Temple Invisible Blades)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Blades Silver Rupee 3",
            (
                "SilverRupee",
                0x07,
                (16, 0, 11),
                None,
                "Silver Rupee (Shadow Temple Invisible Blades)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Blades Silver Rupee 4",
            (
                "SilverRupee",
                0x07,
                (16, 0, 12),
                None,
                "Silver Rupee (Shadow Temple Invisible Blades)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Blades Silver Rupee 5",
            (
                "SilverRupee",
                0x07,
                (16, 0, 13),
                None,
                "Silver Rupee (Shadow Temple Invisible Blades)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Blades Silver Rupee 6",
            (
                "SilverRupee",
                0x07,
                (16, 0, 14),
                None,
                "Silver Rupee (Shadow Temple Invisible Blades)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Blades Silver Rupee Back Right",
            (
                "SilverRupee",
                0x07,
                (16, 0, 15),
                None,
                "Silver Rupee (Shadow Temple Invisible Blades)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Blades Silver Rupee Back Left",
            (
                "SilverRupee",
                0x07,
                (16, 0, 16),
                None,
                "Silver Rupee (Shadow Temple Invisible Blades)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Blades Silver Rupee Like Like",
            (
                "SilverRupee",
                0x07,
                (16, 0, 17),
                None,
                "Silver Rupee (Shadow Temple Invisible Blades)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Blades Silver Rupee Song of Time Block",
            (
                "SilverRupee",
                0x07,
                (16, 0, 18),
                None,
                "Silver Rupee (Shadow Temple Invisible Blades)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Huge Pit Silver Rupee Center Front",
            (
                "SilverRupee",
                0x07,
                (9, 0, 18),
                None,
                "Silver Rupee (Shadow Temple Huge Pit)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Huge Pit Silver Rupee Center Back",
            (
                "SilverRupee",
                0x07,
                (9, 0, 14),
                None,
                "Silver Rupee (Shadow Temple Huge Pit)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Huge Pit Silver Rupee Right",
            (
                "SilverRupee",
                0x07,
                (9, 0, 17),
                None,
                "Silver Rupee (Shadow Temple Huge Pit)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Huge Pit Silver Rupee Ceiling Upper",
            (
                "SilverRupee",
                0x07,
                (9, 0, 16),
                None,
                "Silver Rupee (Shadow Temple Huge Pit)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Huge Pit Silver Rupee Ceiling Lower",
            (
                "SilverRupee",
                0x07,
                (9, 0, 15),
                None,
                "Silver Rupee (Shadow Temple Huge Pit)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Spikes Silver Rupee Center Front",
            (
                "SilverRupee",
                0x07,
                (11, 0, 15),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Spikes Silver Rupee Center Right",
            (
                "SilverRupee",
                0x07,
                (11, 0, 18),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Spikes Silver Rupee Left Hookshot Target",
            (
                "SilverRupee",
                0x07,
                (11, 0, 12),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Spikes Silver Rupee Right Hookshot Target",
            (
                "SilverRupee",
                0x07,
                (11, 0, 20),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Spikes Silver Rupee Back Right",
            (
                "SilverRupee",
                0x07,
                (11, 0, 19),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Spikes Silver Rupee Ledge",
            (
                "SilverRupee",
                0x07,
                (11, 0, 11),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Spikes Silver Rupee Near Ledge",
            (
                "SilverRupee",
                0x07,
                (11, 0, 13),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Spikes Silver Rupee Ceiling Front",
            (
                "SilverRupee",
                0x07,
                (11, 0, 17),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Spikes Silver Rupee Ceiling Middle",
            (
                "SilverRupee",
                0x07,
                (11, 0, 16),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Shadow Temple MQ Invisible Spikes Silver Rupee Ceiling Back",
            (
                "SilverRupee",
                0x07,
                (11, 0, 14),
                None,
                "Silver Rupee (Shadow Temple Invisible Spikes)",
                (
                    "Shadow Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        # Shadow Temple MQ Wonderitems
        (
            "Shadow Temple MQ 3 Spinning Pots Wonderitem",
            (
                "Wonderitem",
                0x07,
                (12, 0, 2),
                None,
                "Arrows (10)",
                ("Shadow Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        # Shadow Temple Shared
        (
            "Shadow Temple Bongo Bongo Heart",
            (
                "BossHeart",
                0x18,
                0x4F,
                None,
                "Heart Container",
                (
                    "Shadow Temple",
                    "Shadow Temple MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                ),
            ),
        ),
        # Spirit Temple Shared
        # Vanilla and MQ locations are mixed to ensure the positions of shared locations in the log are correct for both versions
        (
            "Spirit Temple Child Bridge Chest",
            (
                "Chest",
                0x06,
                0x08,
                None,
                "Deku Shield",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Child Early Torches Chest",
            (
                "Chest",
                0x06,
                0x00,
                None,
                "Small Key (Spirit Temple)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Child Climb North Chest",
            (
                "Chest",
                0x06,
                0x06,
                None,
                "Bombchus (10)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Child Climb East Chest",
            (
                "Chest",
                0x06,
                0x0C,
                None,
                "Deku Shield",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Map Chest",
            (
                "Chest",
                0x06,
                0x03,
                None,
                "Map (Spirit Temple)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Sun Block Room Chest",
            (
                "Chest",
                0x06,
                0x01,
                None,
                "Small Key (Spirit Temple)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Entrance Front Left Chest",
            (
                "Chest",
                0x06,
                0x1A,
                None,
                "Bombchus (10)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Entrance Back Right Chest",
            (
                "Chest",
                0x06,
                0x1F,
                None,
                "Bombchus (10)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Entrance Front Right Chest",
            (
                "Chest",
                0x06,
                0x1B,
                None,
                "Small Key (Spirit Temple)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Entrance Back Left Chest",
            (
                "Chest",
                0x06,
                0x1E,
                None,
                "Small Key (Spirit Temple)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Map Chest",
            (
                "Chest",
                0x06,
                0x00,
                None,
                "Map (Spirit Temple)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Map Room Enemy Chest",
            (
                "Chest",
                0x06,
                0x08,
                None,
                "Small Key (Spirit Temple)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Child Climb North Chest",
            (
                "Chest",
                0x06,
                0x06,
                None,
                "Bombchus (10)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Child Climb South Chest",
            (
                "Chest",
                0x06,
                0x0C,
                None,
                "Small Key (Spirit Temple)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Compass Chest",
            (
                "Chest",
                0x06,
                0x03,
                None,
                "Compass (Spirit Temple)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Silver Block Hallway Chest",
            (
                "Chest",
                0x06,
                0x1C,
                None,
                "Small Key (Spirit Temple)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Sun Block Room Chest",
            (
                "Chest",
                0x06,
                0x01,
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Silver Gauntlets Chest",
            (
                "Chest",
                0x5C,
                0x0B,
                None,
                "Progressive Strength Upgrade",
                (
                    "Spirit Temple",
                    "Spirit Temple MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Desert Colossus",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Compass Chest",
            (
                "Chest",
                0x06,
                0x04,
                None,
                "Compass (Spirit Temple)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Early Adult Right Chest",
            (
                "Chest",
                0x06,
                0x07,
                None,
                "Small Key (Spirit Temple)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple First Mirror Left Chest",
            (
                "Chest",
                0x06,
                0x0D,
                None,
                "Ice Trap",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple First Mirror Right Chest",
            (
                "Chest",
                0x06,
                0x0E,
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Statue Room Northeast Chest",
            (
                "Chest",
                0x06,
                0x0F,
                None,
                "Rupees (5)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Statue Room Hand Chest",
            (
                "Chest",
                0x06,
                0x02,
                None,
                "Small Key (Spirit Temple)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Near Four Armos Chest",
            (
                "Chest",
                0x06,
                0x05,
                None,
                "Small Key (Spirit Temple)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Hallway Right Invisible Chest",
            (
                "Chest",
                0x06,
                0x14,
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Hallway Left Invisible Chest",
            (
                "Chest",
                0x06,
                0x15,
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Child Hammer Switch Chest",
            (
                "Chest",
                0x06,
                0x1D,
                None,
                "Small Key (Spirit Temple)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Statue Room Lullaby Chest",
            (
                "Chest",
                0x06,
                0x0F,
                None,
                "Rupees (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Statue Room Invisible Chest",
            (
                "Chest",
                0x06,
                0x02,
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Leever Room Chest",
            (
                "Chest",
                0x06,
                0x04,
                None,
                "Rupees (50)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Symphony Room Chest",
            (
                "Chest",
                0x06,
                0x07,
                None,
                "Rupees (50)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Beamos Room Chest",
            (
                "Chest",
                0x06,
                0x19,
                None,
                "Arrows (30)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Chest Switch Chest",
            (
                "Chest",
                0x06,
                0x18,
                None,
                "Ice Trap",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Boss Key Chest",
            (
                "Chest",
                0x06,
                0x05,
                None,
                "Boss Key (Spirit Temple)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Mirror Shield Chest",
            (
                "Chest",
                0x5C,
                0x09,
                None,
                "Mirror Shield",
                (
                    "Spirit Temple",
                    "Spirit Temple MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Desert Colossus",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Boss Key Chest",
            (
                "Chest",
                0x06,
                0x0A,
                None,
                "Boss Key (Spirit Temple)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple Topmost Chest",
            (
                "Chest",
                0x06,
                0x12,
                None,
                "Bombs (20)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Mirror Puzzle Invisible Chest",
            (
                "Chest",
                0x06,
                0x12,
                None,
                "Small Key (Spirit Temple)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Spirit Temple GS Metal Fence",
            (
                "GS Token",
                0x06,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Spirit Temple GS Sun on Floor Room",
            (
                "GS Token",
                0x06,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Spirit Temple GS Hall After Sun Block Room",
            (
                "GS Token",
                0x06,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Spirit Temple GS Lobby",
            (
                "GS Token",
                0x06,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Spirit Temple GS Boulder Room",
            (
                "GS Token",
                0x06,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Spirit Temple MQ GS Sun Block Room",
            (
                "GS Token",
                0x06,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Spirit Temple MQ GS Leever Room",
            (
                "GS Token",
                0x06,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Spirit Temple MQ GS Symphony Room",
            (
                "GS Token",
                0x06,
                0x08,
                None,
                "Gold Skulltula Token",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Spirit Temple MQ GS Nine Thrones Room West",
            (
                "GS Token",
                0x06,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Spirit Temple MQ GS Nine Thrones Room North",
            (
                "GS Token",
                0x06,
                0x10,
                None,
                "Gold Skulltula Token",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Spirit Temple Twinrova Heart",
            (
                "BossHeart",
                0x17,
                0x4F,
                None,
                "Heart Container",
                (
                    "Spirit Temple",
                    "Spirit Temple MQ",
                    "Vanilla Dungeons",
                    "Master Quest",
                ),
            ),
        ),
        # Spirit Temple Freestanding
        (
            "Spirit Temple Shifting Wall Recovery Heart 1",
            (
                "Freestanding",
                0x06,
                (23, 0, 3),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Spirit Temple Shifting Wall Recovery Heart 2",
            (
                "Freestanding",
                0x06,
                (23, 0, 4),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Child Recovery Heart 1",
            (
                "Freestanding",
                0x06,
                (1, 0, 14),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Child Recovery Heart 2",
            (
                "Freestanding",
                0x06,
                (1, 0, 15),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        # Spirit Temple Vanilla Pots/Crates
        (
            "Spirit Temple Lobby Pot 1",
            (
                "Pot",
                0x06,
                (0, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Lobby Pot 2",
            (
                "Pot",
                0x06,
                (0, 0, 12),
                None,
                "Rupees (5)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Lobby Flying Pot 1",
            (
                "FlyingPot",
                0x06,
                (0, 0, 13),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Lobby Flying Pot 2",
            (
                "FlyingPot",
                0x06,
                (0, 0, 14),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Child Climb Pot",
            (
                "Pot",
                0x06,
                (4, 0, 11),
                None,
                "Deku Seeds (30)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Hall After Sun Block Room Pot 1",
            (
                "Pot",
                0x06,
                (9, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Hall After Sun Block Room Pot 2",
            (
                "Pot",
                0x06,
                (9, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Beamos Hall Pot",
            (
                "Pot",
                0x06,
                (16, 0, 6),
                None,
                "Bombs (5)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Child Anubis Pot 1",
            (
                "Pot",
                0x06,
                (27, 0, 5),
                None,
                "Nothing",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Child Anubis Pot 2",
            (
                "Pot",
                0x06,
                (27, 0, 6),
                None,
                "Nothing",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Child Anubis Pot 3",
            (
                "Pot",
                0x06,
                (27, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Child Anubis Pot 4",
            (
                "Pot",
                0x06,
                (27, 0, 8),
                None,
                "Deku Shield",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Child Bridge Flying Pot 1",
            (
                "FlyingPot",
                0x06,
                (3, 0, 5),
                None,
                "Nothing",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Child Bridge Flying Pot 2",
            (
                "FlyingPot",
                0x06,
                (3, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Before Child Climb Small Wooden Crate 1",
            (
                "SmallCrate",
                0x06,
                (1, 0, 10),
                None,
                "Deku Nuts (5)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Small Crates",
                ),
            ),
        ),  # Overwrite original flag 0x2C because it conflicts w/ Beamos hall pot
        (
            "Spirit Temple Before Child Climb Small Wooden Crate 2",
            (
                "SmallCrate",
                0x06,
                (1, 0, 11),
                None,
                "Bombs (5)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Spirit Temple Central Chamber Pot 1",
            (
                "Pot",
                0x06,
                (5, 0, 24),
                None,
                "Nothing",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Central Chamber Pot 2",
            (
                "Pot",
                0x06,
                (5, 0, 25),
                None,
                "Nothing",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Central Chamber Pot 3",
            (
                "Pot",
                0x06,
                (5, 0, 26),
                None,
                "Nothing",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Central Chamber Pot 4",
            (
                "Pot",
                0x06,
                (5, 0, 27),
                None,
                "Nothing",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Central Chamber Pot 5",
            (
                "Pot",
                0x06,
                (5, 0, 28),
                None,
                "Nothing",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Central Chamber Pot 6",
            (
                "Pot",
                0x06,
                (5, 0, 29),
                None,
                "Nothing",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Central Chamber Flying Pot 1",
            (
                "FlyingPot",
                0x06,
                (5, 0, 21),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Central Chamber Flying Pot 2",
            (
                "FlyingPot",
                0x06,
                (5, 0, 22),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Adult Climb Flying Pot 1",
            (
                "FlyingPot",
                0x06,
                (15, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Adult Climb Flying Pot 2",
            (
                "FlyingPot",
                0x06,
                (15, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Big Mirror Flying Pot 1",
            (
                "FlyingPot",
                0x06,
                (25, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Big Mirror Flying Pot 2",
            (
                "FlyingPot",
                0x06,
                (25, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Big Mirror Flying Pot 3",
            (
                "FlyingPot",
                0x06,
                (25, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Big Mirror Flying Pot 4",
            (
                "FlyingPot",
                0x06,
                (25, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Big Mirror Flying Pot 5",
            (
                "FlyingPot",
                0x06,
                (25, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple Big Mirror Flying Pot 6",
            (
                "FlyingPot",
                0x06,
                (25, 0, 10),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        # Spirit Temple Vanilla Silver Rupees
        (
            "Spirit Temple Adult Boulder Silver Rupee Ledge",
            (
                "SilverRupee",
                0x06,
                (13, 0, 11),
                None,
                "Silver Rupee (Spirit Temple Adult Boulders)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Adult Boulder Silver Rupee Front Left",
            (
                "SilverRupee",
                0x06,
                (13, 0, 8),
                None,
                "Silver Rupee (Spirit Temple Adult Boulders)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Adult Boulder Silver Rupee Front Right",
            (
                "SilverRupee",
                0x06,
                (13, 0, 9),
                None,
                "Silver Rupee (Spirit Temple Adult Boulders)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Adult Boulder Silver Rupee Back Right",
            (
                "SilverRupee",
                0x06,
                (13, 0, 10),
                None,
                "Silver Rupee (Spirit Temple Adult Boulders)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Adult Boulder Silver Rupee Back Left",
            (
                "SilverRupee",
                0x06,
                (13, 0, 7),
                None,
                "Silver Rupee (Spirit Temple Adult Boulders)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Sun Block Room Silver Rupee Left",
            (
                "SilverRupee",
                0x06,
                (8, 0, 16),
                None,
                "Silver Rupee (Spirit Temple Sun Block)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Sun Block Room Silver Rupee Center Front",
            (
                "SilverRupee",
                0x06,
                (8, 0, 15),
                None,
                "Silver Rupee (Spirit Temple Sun Block)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Sun Block Room Silver Rupee Center Back",
            (
                "SilverRupee",
                0x06,
                (8, 0, 14),
                None,
                "Silver Rupee (Spirit Temple Sun Block)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Sun Block Room Silver Rupee Right Front",
            (
                "SilverRupee",
                0x06,
                (8, 0, 17),
                None,
                "Silver Rupee (Spirit Temple Sun Block)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Sun Block Room Silver Rupee Right Back",
            (
                "SilverRupee",
                0x06,
                (8, 0, 13),
                None,
                "Silver Rupee (Spirit Temple Sun Block)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Child Early Torches Silver Rupee Top Right",
            (
                "SilverRupee",
                0x06,
                (2, 0, 13),
                None,
                "Silver Rupee (Spirit Temple Child Early Torches)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Child Early Torches Silver Rupee Bottom Right",
            (
                "SilverRupee",
                0x06,
                (2, 0, 14),
                None,
                "Silver Rupee (Spirit Temple Child Early Torches)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Child Early Torches Silver Rupee Bottom Left",
            (
                "SilverRupee",
                0x06,
                (2, 0, 15),
                None,
                "Silver Rupee (Spirit Temple Child Early Torches)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Child Early Torches Silver Rupee Top Left",
            (
                "SilverRupee",
                0x06,
                (2, 0, 16),
                None,
                "Silver Rupee (Spirit Temple Child Early Torches)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple Child Early Torches Silver Rupee Near Torch",
            (
                "SilverRupee",
                0x06,
                (2, 0, 17),
                None,
                "Silver Rupee (Spirit Temple Child Early Torches)",
                (
                    "Spirit Temple",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        # Spirit Temple MQ Silver Rupees
        (
            "Spirit Temple MQ Lobby and Lower Adult Silver Rupee Left Boulder",
            (
                "SilverRupee",
                0x06,
                (0, 0, 12),
                None,
                "Silver Rupee (Spirit Temple Lobby and Lower Adult)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Lobby and Lower Adult Silver Rupee Right Boulder",
            (
                "SilverRupee",
                0x06,
                (0, 0, 11),
                None,
                "Silver Rupee (Spirit Temple Lobby and Lower Adult)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Lobby and Lower Adult Silver Rupee Water Jet",
            (
                "SilverRupee",
                0x06,
                (0, 0, 14),
                None,
                "Silver Rupee (Spirit Temple Lobby and Lower Adult)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Lobby and Lower Adult Silver Rupee Behind Water Jet",
            (
                "SilverRupee",
                0x06,
                (0, 0, 10),
                None,
                "Silver Rupee (Spirit Temple Lobby and Lower Adult)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Lobby and Lower Adult Silver Rupee Near Door",
            (
                "SilverRupee",
                0x06,
                (0, 0, 13),
                None,
                "Silver Rupee (Spirit Temple Lobby and Lower Adult)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Adult Climb Silver Rupee 1",
            (
                "SilverRupee",
                0x06,
                (23, 0, 11),
                None,
                "Silver Rupee (Spirit Temple Adult Climb)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Adult Climb Silver Rupee 2",
            (
                "SilverRupee",
                0x06,
                (23, 0, 12),
                None,
                "Silver Rupee (Spirit Temple Adult Climb)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Adult Climb Silver Rupee 3",
            (
                "SilverRupee",
                0x06,
                (23, 0, 15),
                None,
                "Silver Rupee (Spirit Temple Adult Climb)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Adult Climb Silver Rupee 4",
            (
                "SilverRupee",
                0x06,
                (23, 0, 13),
                None,
                "Silver Rupee (Spirit Temple Adult Climb)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Adult Climb Silver Rupee 5",
            (
                "SilverRupee",
                0x06,
                (23, 0, 14),
                None,
                "Silver Rupee (Spirit Temple Adult Climb)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        # Spirit Temple MQ Pots
        (
            "Spirit Temple MQ Lobby Pot 1",
            (
                "Pot",
                0x06,
                (0, 0, 18),
                None,
                "Bombs (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Lobby Pot 2",
            (
                "Pot",
                0x06,
                (0, 0, 19),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Lobby Pot 3",
            (
                "Pot",
                0x06,
                (0, 0, 20),
                None,
                "Rupees (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Lobby Pot 4",
            (
                "Pot",
                0x06,
                (0, 0, 22),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Child Torch Slugs Room Pot",
            (
                "Pot",
                0x06,
                (1, 0, 12),
                None,
                "Bombs (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Child 3 Gibdo Room Pot 1",
            (
                "Pot",
                0x06,
                (2, 0, 13),
                None,
                "Rupees (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Child 3 Gibdo Room Pot 2",
            (
                "Pot",
                0x06,
                (2, 0, 14),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Child Stalfos Fight Pot 1",
            (
                "Pot",
                0x06,
                (27, 0, 10),
                None,
                "Rupees (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Child Stalfos Fight Pot 2",
            (
                "Pot",
                0x06,
                (27, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Child Stalfos Fight Pot 3",
            (
                "Pot",
                0x06,
                (27, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Child Stalfos Fight Pot 4",
            (
                "Pot",
                0x06,
                (27, 0, 13),
                None,
                "Fairy Drop",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Child Climb Pot",
            (
                "Pot",
                0x06,
                (4, 0, 13),
                None,
                "Rupees (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Central Chamber Flying Pot Top Left",
            (
                "FlyingPot",
                0x06,
                (5, 0, 19),
                None,
                "Nothing",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Central Chamber Flying Pot Floor",
            (
                "FlyingPot",
                0x06,
                (5, 0, 20),
                None,
                "Nothing",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Central Chamber Flying Pot Stairs",
            (
                "FlyingPot",
                0x06,
                (5, 0, 23),
                None,
                "Nothing",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Central Chamber Floor Pot 1",
            (
                "Pot",
                0x06,
                (5, 0, 31),
                None,
                "Rupees (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Central Chamber Floor Pot 2",
            (
                "Pot",
                0x06,
                (5, 0, 35),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Central Chamber Floor Pot 3",
            (
                "Pot",
                0x06,
                (5, 0, 36),
                None,
                "Rupees (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Central Chamber Top Left Pot (Left)",
            (
                "Pot",
                0x06,
                (5, 0, 34),
                None,
                "Rupees (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Central Chamber Top Left Pot (Right)",
            (
                "Pot",
                0x06,
                (5, 0, 33),
                None,
                "Arrows (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Sun Block Room Pot 1",
            (
                "Pot",
                0x06,
                (8, 0, 23),
                None,
                "Rupees (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Sun Block Room Pot 2",
            (
                "Pot",
                0x06,
                (8, 0, 25),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Below 4 Wallmasters Pot 1",
            (
                "Pot",
                0x06,
                (15, 0, 15),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Below 4 Wallmasters Pot 2",
            (
                "Pot",
                0x06,
                (15, 0, 16),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Shifting Wall Pot 1",
            (
                "Pot",
                0x06,
                (23, 0, 16),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Shifting Wall Pot 2",
            (
                "Pot",
                0x06,
                (23, 0, 17),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ After Shifting Wall Room Pot 1",
            (
                "Pot",
                0x06,
                (24, 0, 4),
                None,
                "Bombs (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ After Shifting Wall Room Pot 2",
            (
                "Pot",
                0x06,
                (24, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Big Mirror Pot 1",
            (
                "Pot",
                0x06,
                (25, 0, 10),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Big Mirror Pot 2",
            (
                "Pot",
                0x06,
                (25, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Big Mirror Pot 3",
            (
                "Pot",
                0x06,
                (25, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Big Mirror Pot 4",
            (
                "Pot",
                0x06,
                (25, 0, 13),
                None,
                "Rupees (5)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        # Spirit Temple MQ Crates
        (
            "Spirit Temple MQ Central Chamber Crate 1",
            (
                "Crate",
                0x06,
                (5, 0, 12),
                None,
                "Rupee (1)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Central Chamber Crate 2",
            (
                "Crate",
                0x06,
                (5, 0, 13),
                None,
                "Rupee (1)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Central Chamber Small Wooden Crate",
            (
                "SmallCrate",
                0x06,
                (5, 0, 14),
                None,
                "Nothing",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Beamos Room Small Wooden Crate",
            (
                "SmallCrate",
                0x06,
                (17, 0, 1),
                None,
                "Nothing",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Small Crates",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Big Mirror Crate 1",
            (
                "Crate",
                0x06,
                (25, 0, 2),
                None,
                "Rupee (1)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Big Mirror Crate 2",
            (
                "Crate",
                0x06,
                (25, 0, 3),
                None,
                "Rupee (1)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Big Mirror Crate 3",
            (
                "Crate",
                0x06,
                (25, 0, 4),
                None,
                "Rupee (1)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        (
            "Spirit Temple MQ Big Mirror Crate 4",
            (
                "Crate",
                0x06,
                (25, 0, 5),
                None,
                "Rupee (1)",
                (
                    "Spirit Temple MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        # Spirit Temple MQ Wonderitems
        (
            "Spirit Temple MQ Chest Switch Sword Wonderitem",
            (
                "Wonderitem",
                0x06,
                (18, 0, 10),
                None,
                "Recovery Heart",
                ("Spirit Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Spirit Temple MQ Chest Switch Hammer Wonderitem",
            (
                "Wonderitem",
                0x06,
                (18, 0, 9),
                None,
                "Recovery Heart",
                ("Spirit Temple", "Master Quest", "Wonderitem"),
            ),
        ),
        # Ice Cavern Vanilla
        (
            "Ice Cavern Map Chest",
            (
                "Chest",
                0x09,
                0x00,
                None,
                "Map (Ice Cavern)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ice Cavern Compass Chest",
            (
                "Chest",
                0x09,
                0x01,
                None,
                "Compass (Ice Cavern)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ice Cavern Iron Boots Chest",
            (
                "Chest",
                0x09,
                0x02,
                None,
                "Iron Boots",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ice Cavern GS Spinning Scythe Room",
            (
                "GS Token",
                0x09,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Ice Cavern GS Heart Piece Room",
            (
                "GS Token",
                0x09,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Ice Cavern GS Push Block Room",
            (
                "GS Token",
                0x09,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Ice Cavern Freestanding PoH",
            (
                "Collectable",
                0x09,
                0x01,
                None,
                "Piece of Heart",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        # Ice Cavern Vanilla Freestanding
        (
            "Ice Cavern Frozen Blue Rupee",
            (
                "Freestanding",
                0x09,
                (1, 0, 1),
                None,
                "Rupees (5)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ice Cavern Map Room Recovery Heart 1",
            (
                "Freestanding",
                0x09,
                (9, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ice Cavern Map Room Recovery Heart 2",
            (
                "Freestanding",
                0x09,
                (9, 0, 8),
                None,
                "Recovery Heart",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ice Cavern Map Room Recovery Heart 3",
            (
                "Freestanding",
                0x09,
                (9, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ice Cavern Push Block Room Red Rupee 1",
            (
                "Freestanding",
                0x09,
                (5, 0, 1),
                None,
                "Rupees (20)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ice Cavern Push Block Room Red Rupee 2",
            (
                "Freestanding",
                0x09,
                (5, 0, 2),
                None,
                "Rupees (20)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ice Cavern Push Block Room Red Rupee 3",
            (
                "Freestanding",
                0x09,
                (5, 0, 3),
                None,
                "Rupees (20)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        # Ice Cavern Vanilla Pots
        (
            "Ice Cavern Hall Pot 1",
            (
                "Pot",
                0x09,
                (2, 0, 1),
                None,
                "Recovery Heart",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern Hall Pot 2",
            (
                "Pot",
                0x09,
                (2, 0, 2),
                None,
                "Recovery Heart",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern Spinning Scythe Pot 1",
            (
                "Pot",
                0x09,
                (3, 0, 9),
                None,
                "Arrows (10)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern Spinning Scythe Pot 2",
            (
                "Pot",
                0x09,
                (3, 0, 10),
                None,
                "Rupees (5)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern Spinning Scythe Pot 3",
            (
                "Pot",
                0x09,
                (3, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern Spinning Scythe Flying Pot",
            (
                "FlyingPot",
                0x09,
                (3, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Flying Pots",
                ),
            ),
        ),
        (
            "Ice Cavern Near End Pot 1",
            (
                "Pot",
                0x09,
                (6, 0, 1),
                None,
                "Recovery Heart",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern Near End Pot 2",
            (
                "Pot",
                0x09,
                (6, 0, 2),
                None,
                "Recovery Heart",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern Frozen Pot",
            (
                "Pot",
                0x09,
                (9, 0, 10),
                None,
                "Rupees (50)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        # Ice Cavern Silver Rupees
        (
            "Ice Cavern Spinning Scythe Silver Rupee Icicles",
            (
                "SilverRupee",
                0x09,
                (3, 0, 3),
                None,
                "Silver Rupee (Ice Cavern Spinning Scythe)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ice Cavern Spinning Scythe Silver Rupee Center Left",
            (
                "SilverRupee",
                0x09,
                (3, 0, 4),
                None,
                "Silver Rupee (Ice Cavern Spinning Scythe)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ice Cavern Spinning Scythe Silver Rupee Center Back",
            (
                "SilverRupee",
                0x09,
                (3, 0, 5),
                None,
                "Silver Rupee (Ice Cavern Spinning Scythe)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ice Cavern Spinning Scythe Silver Rupee Center Right",
            (
                "SilverRupee",
                0x09,
                (3, 0, 6),
                None,
                "Silver Rupee (Ice Cavern Spinning Scythe)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ice Cavern Spinning Scythe Silver Rupee Ledge",
            (
                "SilverRupee",
                0x09,
                (3, 0, 7),
                None,
                "Silver Rupee (Ice Cavern Spinning Scythe)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ice Cavern Push Block Silver Rupee Back Left",
            (
                "SilverRupee",
                0x09,
                (5, 0, 11),
                None,
                "Silver Rupee (Ice Cavern Push Block)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ice Cavern Push Block Silver Rupee Back Center",
            (
                "SilverRupee",
                0x09,
                (5, 0, 12),
                None,
                "Silver Rupee (Ice Cavern Push Block)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ice Cavern Push Block Silver Rupee Front Center",
            (
                "SilverRupee",
                0x09,
                (5, 0, 13),
                None,
                "Silver Rupee (Ice Cavern Push Block)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ice Cavern Push Block Silver Rupee Red Ice",
            (
                "SilverRupee",
                0x09,
                (5, 0, 14),
                None,
                "Silver Rupee (Ice Cavern Push Block)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ice Cavern Push Block Silver Rupee Front Left",
            (
                "SilverRupee",
                0x09,
                (5, 0, 15),
                None,
                "Silver Rupee (Ice Cavern Push Block)",
                (
                    "Ice Cavern",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        # Ice Cavern MQ
        (
            "Ice Cavern MQ Map Chest",
            (
                "Chest",
                0x09,
                0x01,
                None,
                "Map (Ice Cavern)",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ice Cavern MQ Compass Chest",
            (
                "Chest",
                0x09,
                0x00,
                None,
                "Compass (Ice Cavern)",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ice Cavern MQ Freestanding PoH",
            (
                "Collectable",
                0x09,
                0x01,
                None,
                "Piece of Heart",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ice Cavern MQ Iron Boots Chest",
            (
                "Chest",
                0x09,
                0x02,
                None,
                "Iron Boots",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ice Cavern MQ GS Red Ice",
            (
                "GS Token",
                0x09,
                0x02,
                None,
                "Gold Skulltula Token",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Ice Cavern MQ GS Ice Block",
            (
                "GS Token",
                0x09,
                0x04,
                None,
                "Gold Skulltula Token",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        (
            "Ice Cavern MQ GS Scarecrow",
            (
                "GS Token",
                0x09,
                0x01,
                None,
                "Gold Skulltula Token",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Gold Skulltulas",
                ),
            ),
        ),
        # Ice Cavern MQ Pots
        (
            "Ice Cavern MQ First Hall Pot",
            (
                "Pot",
                0x09,
                (0, 0, 4),
                None,
                "Recovery Heart",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern MQ Tektite Room Pot 1",
            (
                "Pot",
                0x09,
                (1, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern MQ Tektite Room Pot 2",
            (
                "Pot",
                0x09,
                (1, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern MQ Center Room Pot 1",
            (
                "Pot",
                0x09,
                (3, 0, 14),
                None,
                "Rupees (5)",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern MQ Center Room Pot 2",
            (
                "Pot",
                0x09,
                (3, 0, 16),
                None,
                "Recovery Heart",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern MQ Center Room Pot 3",
            (
                "Pot",
                0x09,
                (3, 0, 13),
                None,
                "Fairy Drop",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern MQ Center Room Pot 4",
            (
                "Pot",
                0x09,
                (3, 0, 19),
                None,
                "Fairy Drop",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern MQ Near End Pot 1",
            (
                "Pot",
                0x09,
                (6, 0, 7),
                None,
                "Rupees (5)",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern MQ Near End Pot 2",
            (
                "Pot",
                0x09,
                (6, 0, 6),
                None,
                "Fairy Drop",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern MQ Compass Room Pot 1",
            (
                "Pot",
                0x09,
                (9, 0, 11),
                None,
                "Bombs (5)",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ice Cavern MQ Compass Room Pot 2",
            (
                "Pot",
                0x09,
                (9, 0, 12),
                None,
                "Bombs (5)",
                (
                    "Ice Cavern MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        # Gerudo Training Ground Vanilla
        (
            "Gerudo Training Ground Lobby Left Chest",
            (
                "Chest",
                0x0B,
                0x13,
                None,
                "Rupees (5)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Lobby Right Chest",
            (
                "Chest",
                0x0B,
                0x07,
                None,
                "Arrows (10)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Stalfos Chest",
            (
                "Chest",
                0x0B,
                0x00,
                None,
                "Small Key (Gerudo Training Ground)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Before Heavy Block Chest",
            (
                "Chest",
                0x0B,
                0x11,
                None,
                "Arrows (30)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Heavy Block First Chest",
            (
                "Chest",
                0x0B,
                0x0F,
                None,
                "Rupees (200)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Heavy Block Second Chest",
            (
                "Chest",
                0x0B,
                0x0E,
                None,
                "Rupees (5)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Heavy Block Third Chest",
            (
                "Chest",
                0x0B,
                0x14,
                None,
                "Small Key (Gerudo Training Ground)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Heavy Block Fourth Chest",
            (
                "Chest",
                0x0B,
                0x02,
                None,
                "Ice Trap",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Eye Statue Chest",
            (
                "Chest",
                0x0B,
                0x03,
                None,
                "Small Key (Gerudo Training Ground)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Near Scarecrow Chest",
            (
                "Chest",
                0x0B,
                0x04,
                None,
                "Small Key (Gerudo Training Ground)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Hammer Room Clear Chest",
            (
                "Chest",
                0x0B,
                0x12,
                None,
                "Arrows (10)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Hammer Room Switch Chest",
            (
                "Chest",
                0x0B,
                0x10,
                None,
                "Small Key (Gerudo Training Ground)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Freestanding Key",
            (
                "Collectable",
                0x0B,
                0x01,
                None,
                "Small Key (Gerudo Training Ground)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Maze Right Central Chest",
            (
                "Chest",
                0x0B,
                0x05,
                None,
                "Bombchus (5)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Maze Right Side Chest",
            (
                "Chest",
                0x0B,
                0x08,
                None,
                "Arrows (30)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Underwater Silver Rupee Chest",
            (
                "Chest",
                0x0B,
                0x0D,
                None,
                "Small Key (Gerudo Training Ground)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Beamos Chest",
            (
                "Chest",
                0x0B,
                0x01,
                None,
                "Small Key (Gerudo Training Ground)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Hidden Ceiling Chest",
            (
                "Chest",
                0x0B,
                0x0B,
                None,
                "Small Key (Gerudo Training Ground)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Maze Path First Chest",
            (
                "Chest",
                0x0B,
                0x06,
                None,
                "Rupees (50)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Maze Path Second Chest",
            (
                "Chest",
                0x0B,
                0x0A,
                None,
                "Rupees (20)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Maze Path Third Chest",
            (
                "Chest",
                0x0B,
                0x09,
                None,
                "Arrows (30)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Maze Path Final Chest",
            (
                "Chest",
                0x0B,
                0x0C,
                None,
                "Ice Arrows",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        # Gerudo Training Ground Vanilla Freestanding
        (
            "Gerudo Training Ground Beamos Recovery Heart 1",
            (
                "Freestanding",
                0x0B,
                (7, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Beamos Recovery Heart 2",
            (
                "Freestanding",
                0x0B,
                (7, 0, 12),
                None,
                "Recovery Heart",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        # Gerudo Training Ground Silver Rupees
        (
            "Gerudo Training Ground Lava Room Silver Rupee Front Left",
            (
                "SilverRupee",
                0x0B,
                (6, 0, 11),
                None,
                "Silver Rupee (Gerudo Training Ground Lava)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Lava Room Silver Rupee Front Right",
            (
                "SilverRupee",
                0x0B,
                (6, 0, 12),
                None,
                "Silver Rupee (Gerudo Training Ground Lava)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Lava Room Silver Rupee Flame Circle",
            (
                "SilverRupee",
                0x0B,
                (6, 0, 13),
                None,
                "Silver Rupee (Gerudo Training Ground Lava)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Lava Room Silver Rupee Center Right",
            (
                "SilverRupee",
                0x0B,
                (6, 0, 15),
                None,
                "Silver Rupee (Gerudo Training Ground Lava)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Lava Room Silver Rupee Hookshot Target",
            (
                "SilverRupee",
                0x0B,
                (6, 0, 14),
                None,
                "Silver Rupee (Gerudo Training Ground Lava)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Underwater Silver Rupee Top",
            (
                "SilverRupee",
                0x0B,
                (9, 0, 18),
                None,
                "Silver Rupee (Gerudo Training Ground Water)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Underwater Silver Rupee Middle",
            (
                "SilverRupee",
                0x0B,
                (9, 0, 20),
                None,
                "Silver Rupee (Gerudo Training Ground Water)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Underwater Silver Rupee Bottom Front Right",
            (
                "SilverRupee",
                0x0B,
                (9, 0, 21),
                None,
                "Silver Rupee (Gerudo Training Ground Water)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Underwater Silver Rupee Bottom Center",
            (
                "SilverRupee",
                0x0B,
                (9, 0, 17),
                None,
                "Silver Rupee (Gerudo Training Ground Water)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Underwater Silver Rupee Bottom Back Left",
            (
                "SilverRupee",
                0x0B,
                (9, 0, 19),
                None,
                "Silver Rupee (Gerudo Training Ground Water)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Boulder Room Silver Rupee Bottom Right",
            (
                "SilverRupee",
                0x0B,
                (2, 0, 10),
                None,
                "Silver Rupee (Gerudo Training Ground Slopes)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Boulder Room Silver Rupee Bottom Left",
            (
                "SilverRupee",
                0x0B,
                (2, 0, 11),
                None,
                "Silver Rupee (Gerudo Training Ground Slopes)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Boulder Room Silver Rupee Ceiling",
            (
                "SilverRupee",
                0x0B,
                (2, 0, 12),
                None,
                "Silver Rupee (Gerudo Training Ground Slopes)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Boulder Room Silver Rupee Ledge",
            (
                "SilverRupee",
                0x0B,
                (2, 0, 13),
                None,
                "Silver Rupee (Gerudo Training Ground Slopes)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground Boulder Room Silver Rupee Top Left",
            (
                "SilverRupee",
                0x0B,
                (2, 0, 14),
                None,
                "Silver Rupee (Gerudo Training Ground Slopes)",
                (
                    "Gerudo Training Ground",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        # Gerudo Training Ground Wonderitems
        (
            "Gerudo Training Ground Eye Statue Wonderitem",
            (
                "Wonderitem",
                0x0B,
                (4, 0, 3),
                None,
                "Arrows (10)",
                ("Gerudo Training Ground", "Vanilla Dungeons", "Wonderitem"),
            ),
        ),
        (
            "Gerudo Training Ground Hammer Room Wonderitem",
            (
                "Wonderitem",
                0x0B,
                (5, 0, 17),
                None,
                "Arrows (10)",
                ("Gerudo Training Ground", "Vanilla Dungeons", "Wonderitem"),
            ),
        ),
        (
            "Gerudo Training Ground Beamos Wonderitem",
            (
                "Wonderitem",
                0x0B,
                (7, 0, 13),
                None,
                "Arrows (10)",
                ("Gerudo Training Ground", "Vanilla Dungeons", "Wonderitem"),
            ),
        ),
        # Gerudo Training Ground MQ
        (
            "Gerudo Training Ground MQ Lobby Left Chest",
            (
                "Chest",
                0x0B,
                0x13,
                None,
                "Arrows (10)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Lobby Right Chest",
            (
                "Chest",
                0x0B,
                0x07,
                None,
                "Bombchus (5)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ First Iron Knuckle Chest",
            (
                "Chest",
                0x0B,
                0x00,
                None,
                "Rupees (5)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Before Heavy Block Chest",
            (
                "Chest",
                0x0B,
                0x11,
                None,
                "Arrows (10)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Heavy Block Chest",
            (
                "Chest",
                0x0B,
                0x02,
                None,
                "Rupees (50)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Eye Statue Chest",
            (
                "Chest",
                0x0B,
                0x03,
                None,
                "Bombchus (10)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Ice Arrows Chest",
            (
                "Chest",
                0x0B,
                0x04,
                None,
                "Ice Arrows",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Second Iron Knuckle Chest",
            (
                "Chest",
                0x0B,
                0x12,
                None,
                "Arrows (10)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Flame Circle Chest",
            (
                "Chest",
                0x0B,
                0x0E,
                None,
                "Small Key (Gerudo Training Ground)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Maze Right Central Chest",
            (
                "Chest",
                0x0B,
                0x05,
                None,
                "Rupees (5)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Maze Right Side Chest",
            (
                "Chest",
                0x0B,
                0x08,
                None,
                "Rupee (Treasure Chest Game) (1)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Underwater Silver Rupee Chest",
            (
                "Chest",
                0x0B,
                0x0D,
                None,
                "Small Key (Gerudo Training Ground)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Dinolfos Chest",
            (
                "Chest",
                0x0B,
                0x01,
                None,
                "Small Key (Gerudo Training Ground)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Hidden Ceiling Chest",
            (
                "Chest",
                0x0B,
                0x0B,
                None,
                "Rupees (50)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Maze Path First Chest",
            (
                "Chest",
                0x0B,
                0x06,
                None,
                "Rupee (1)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Maze Path Second Chest",
            (
                "Chest",
                0x0B,
                0x0A,
                None,
                "Rupees (20)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Maze Path Third Chest",
            (
                "Chest",
                0x0B,
                0x09,
                None,
                "Rupee (Treasure Chest Game) (1)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        # Gerudo Training Ground MQ Pots/Crates
        (
            "Gerudo Training Ground MQ Lobby Left Pot 1",
            (
                "Pot",
                0x0B,
                (0, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Lobby Left Pot 2",
            (
                "Pot",
                0x0B,
                (0, 0, 7),
                None,
                "Rupees (5)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Lobby Right Pot 1",
            (
                "Pot",
                0x0B,
                (0, 0, 8),
                None,
                "Rupees (5)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Lobby Right Pot 2",
            (
                "Pot",
                0x0B,
                (0, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Maze Crate",
            (
                "Crate",
                0x0B,
                (8, 0, 2),
                None,
                "Rupee (1)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Crates",
                ),
            ),
        ),
        # Gerudo Training Ground MQ Silver Rupees
        (
            "Gerudo Training Ground MQ Icicle Room Silver Rupee Freezard",
            (
                "SilverRupee",
                0x0B,
                (2, 0, 28),
                None,
                "Silver Rupee (Gerudo Training Ground Slopes)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Icicle Room Silver Rupee Icicles",
            (
                "SilverRupee",
                0x0B,
                (2, 0, 25),
                None,
                "Silver Rupee (Gerudo Training Ground Slopes)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Icicle Room Silver Rupee Center",
            (
                "SilverRupee",
                0x0B,
                (2, 0, 26),
                None,
                "Silver Rupee (Gerudo Training Ground Slopes)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Icicle Room Silver Rupee Ceiling",
            (
                "SilverRupee",
                0x0B,
                (2, 0, 27),
                None,
                "Silver Rupee (Gerudo Training Ground Slopes)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Icicle Room Silver Rupee Above Void",
            (
                "SilverRupee",
                0x0B,
                (2, 0, 29),
                None,
                "Silver Rupee (Gerudo Training Ground Slopes)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Lava Room Silver Rupee Front Left",
            (
                "SilverRupee",
                0x0B,
                (6, 0, 12),
                None,
                "Silver Rupee (Gerudo Training Ground Lava)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Lava Room Silver Rupee Front Center",
            (
                "SilverRupee",
                0x0B,
                (6, 0, 13),
                None,
                "Silver Rupee (Gerudo Training Ground Lava)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Lava Room Silver Rupee Front Right",
            (
                "SilverRupee",
                0x0B,
                (6, 0, 11),
                None,
                "Silver Rupee (Gerudo Training Ground Lava)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Lava Room Silver Rupee Back Left",
            (
                "SilverRupee",
                0x0B,
                (6, 0, 9),
                None,
                "Silver Rupee (Gerudo Training Ground Lava)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Lava Room Silver Rupee Back Center",
            (
                "SilverRupee",
                0x0B,
                (6, 0, 10),
                None,
                "Silver Rupee (Gerudo Training Ground Lava)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Lava Room Silver Rupee Back Right",
            (
                "SilverRupee",
                0x0B,
                (6, 0, 8),
                None,
                "Silver Rupee (Gerudo Training Ground Lava)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Underwater Silver Rupee Middle",
            (
                "SilverRupee",
                0x0B,
                (9, 0, 13),
                None,
                "Silver Rupee (Gerudo Training Ground Water)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Underwater Silver Rupee Front Right",
            (
                "SilverRupee",
                0x0B,
                (9, 0, 14),
                None,
                "Silver Rupee (Gerudo Training Ground Water)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Gerudo Training Ground MQ Underwater Silver Rupee Back Left",
            (
                "SilverRupee",
                0x0B,
                (9, 0, 12),
                None,
                "Silver Rupee (Gerudo Training Ground Water)",
                (
                    "Gerudo Training Ground MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        # Gerudo Training Ground MQ Wonderitems
        (
            "Gerudo Training Ground MQ Eye Statue Proximity Wonderitem",
            (
                "Wonderitem",
                0x0B,
                (4, 0, 5),
                None,
                "Rupees (20)",
                ("Gerudo Training Ground", "Master Quest", "Wonderitem"),
            ),
        ),
        (
            "Gerudo Training Ground MQ Dinolfos Arrow Wonderitem",
            (
                "Wonderitem",
                0x0B,
                (7, 0, 9),
                None,
                "Rupees (20)",
                ("Gerudo Training Ground", "Master Quest", "Wonderitem"),
            ),
        ),  # One of the actors in this room appears to have been deleted so this actor is #9. The 0x185 Checkable Spot actor is missing in MQU.json
        # Ganon's Castle Vanilla
        (
            "Ganons Castle Forest Trial Chest",
            (
                "Chest",
                0x0D,
                0x09,
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Water Trial Left Chest",
            (
                "Chest",
                0x0D,
                0x07,
                None,
                "Ice Trap",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Water Trial Right Chest",
            (
                "Chest",
                0x0D,
                0x06,
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Shadow Trial Front Chest",
            (
                "Chest",
                0x0D,
                0x08,
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Shadow Trial Golden Gauntlets Chest",
            (
                "Chest",
                0x0D,
                0x05,
                None,
                "Progressive Strength Upgrade",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial First Left Chest",
            (
                "Chest",
                0x0D,
                0x0C,
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Second Left Chest",
            (
                "Chest",
                0x0D,
                0x0B,
                None,
                "Ice Trap",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Third Left Chest",
            (
                "Chest",
                0x0D,
                0x0D,
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial First Right Chest",
            (
                "Chest",
                0x0D,
                0x0E,
                None,
                "Ice Trap",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Second Right Chest",
            (
                "Chest",
                0x0D,
                0x0A,
                None,
                "Arrows (30)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Third Right Chest",
            (
                "Chest",
                0x0D,
                0x0F,
                None,
                "Ice Trap",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Invisible Enemies Chest",
            (
                "Chest",
                0x0D,
                0x10,
                None,
                "Small Key (Ganons Castle)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Lullaby Chest",
            (
                "Chest",
                0x0D,
                0x11,
                None,
                "Small Key (Ganons Castle)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Spirit Trial Crystal Switch Chest",
            (
                "Chest",
                0x0D,
                0x12,
                None,
                "Bombchus (20)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Spirit Trial Invisible Chest",
            (
                "Chest",
                0x0D,
                0x14,
                None,
                "Arrows (10)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle Deku Scrub Left",
            (
                "Scrub",
                0x0D,
                0x3A,
                None,
                "Buy Green Potion",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Ganons Castle Deku Scrub Center-Left",
            (
                "Scrub",
                0x0D,
                0x37,
                None,
                "Buy Bombs (5) for 35 Rupees",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Ganons Castle Deku Scrub Center-Right",
            (
                "Scrub",
                0x0D,
                0x33,
                None,
                "Buy Arrows (30)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Ganons Castle Deku Scrub Right",
            (
                "Scrub",
                0x0D,
                0x39,
                None,
                "Buy Red Potion for 30 Rupees",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Deku Scrubs",
                ),
            ),
        ),
        # Ganon's Castle Vanilla Freestanding
        (
            "Ganons Castle Shadow Trial Recovery Heart 1",
            (
                "Freestanding",
                0x0D,
                (12, 0, 9),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ganons Castle Shadow Trial Recovery Heart 2",
            (
                "Freestanding",
                0x0D,
                (12, 0, 11),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ganons Castle Shadow Trial Recovery Heart 3",
            (
                "Freestanding",
                0x0D,
                (12, 0, 13),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ganons Castle Fire Trial Recovery Heart",
            (
                "Freestanding",
                0x0D,
                (14, 0, 20),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ganons Castle Spirit Trial Recovery Heart",
            (
                "Freestanding",
                0x0D,
                (17, 0, 28),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Freestandings",
                ),
            ),
        ),
        # Ganon's Castle Vanilla Pots
        (
            "Ganons Castle Water Trial Pot 1",
            (
                "Pot",
                0x0D,
                (4, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Water Trial Pot 2",
            (
                "Pot",
                0x0D,
                (4, 0, 6),
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Water Trial Fairy Pot Drop",
            (
                "Pot",
                0x0D,
                (3, 0, 4),
                None,
                "Fairy Drop",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Forest Trial Pot 1",
            (
                "Pot",
                0x0D,
                (7, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Forest Trial Pot 2",
            (
                "Pot",
                0x0D,
                (7, 0, 6),
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Boulder Pot",
            (
                "Pot",
                0x0D,
                (8, 0, 11),
                None,
                "Arrows (30)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Pot 1",
            (
                "Pot",
                0x0D,
                (11, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Pot 2",
            (
                "Pot",
                0x0D,
                (11, 0, 6),
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Shadow Trial Like Like Pot 1",
            (
                "Pot",
                0x0D,
                (12, 0, 15),
                None,
                "Arrows (10)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Shadow Trial Like Like Pot 2",
            (
                "Pot",
                0x0D,
                (12, 0, 16),
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Shadow Trial Pot 1",
            (
                "Pot",
                0x0D,
                (13, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Shadow Trial Pot 2",
            (
                "Pot",
                0x0D,
                (13, 0, 6),
                None,
                "Arrows (10)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Fire Trial Pot 1",
            (
                "Pot",
                0x0D,
                (15, 0, 5),
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Fire Trial Pot 2",
            (
                "Pot",
                0x0D,
                (15, 0, 6),
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Spirit Trial Pot 1",
            (
                "Pot",
                0x0D,
                (19, 0, 5),
                None,
                "Deku Nuts (5)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle Spirit Trial Pot 2",
            (
                "Pot",
                0x0D,
                (19, 0, 6),
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Pots",
                ),
            ),
        ),
        # Ganon's Castle Silver Rupees
        (
            "Ganons Castle Spirit Trial Silver Rupee Ceiling",
            (
                "SilverRupee",
                0x0D,
                (17, 0, 22),
                None,
                "Silver Rupee (Ganons Castle Spirit Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Spirit Trial Silver Rupee Front Right",
            (
                "SilverRupee",
                0x0D,
                (17, 0, 23),
                None,
                "Silver Rupee (Ganons Castle Spirit Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Spirit Trial Silver Rupee Center",
            (
                "SilverRupee",
                0x0D,
                (17, 0, 24),
                None,
                "Silver Rupee (Ganons Castle Spirit Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Spirit Trial Silver Rupee Back Left",
            (
                "SilverRupee",
                0x0D,
                (17, 0, 25),
                None,
                "Silver Rupee (Ganons Castle Spirit Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Spirit Trial Silver Rupee Back Right",
            (
                "SilverRupee",
                0x0D,
                (17, 0, 26),
                None,
                "Silver Rupee (Ganons Castle Spirit Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Silver Rupee Center Left",
            (
                "SilverRupee",
                0x0D,
                (8, 0, 9),
                None,
                "Silver Rupee (Ganons Castle Light Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Silver Rupee Center Top",
            (
                "SilverRupee",
                0x0D,
                (8, 0, 7),
                None,
                "Silver Rupee (Ganons Castle Light Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Silver Rupee Center Right",
            (
                "SilverRupee",
                0x0D,
                (8, 0, 8),
                None,
                "Silver Rupee (Ganons Castle Light Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Silver Rupee Left Alcove",
            (
                "SilverRupee",
                0x0D,
                (8, 0, 6),
                None,
                "Silver Rupee (Ganons Castle Light Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Light Trial Silver Rupee Right Alcove",
            (
                "SilverRupee",
                0x0D,
                (8, 0, 5),
                None,
                "Silver Rupee (Ganons Castle Light Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Fire Trial Silver Rupee Flamethrower",
            (
                "SilverRupee",
                0x0D,
                (14, 0, 14),
                None,
                "Silver Rupee (Ganons Castle Fire Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Fire Trial Silver Rupee Inside Pillar",
            (
                "SilverRupee",
                0x0D,
                (14, 0, 17),
                None,
                "Silver Rupee (Ganons Castle Fire Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Fire Trial Silver Rupee Right Front",
            (
                "SilverRupee",
                0x0D,
                (14, 0, 16),
                None,
                "Silver Rupee (Ganons Castle Fire Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Fire Trial Silver Rupee Right Center",
            (
                "SilverRupee",
                0x0D,
                (14, 0, 15),
                None,
                "Silver Rupee (Ganons Castle Fire Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Fire Trial Silver Rupee Right Back",
            (
                "SilverRupee",
                0x0D,
                (14, 0, 13),
                None,
                "Silver Rupee (Ganons Castle Fire Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Forest Trial Silver Rupee Front Left",
            (
                "SilverRupee",
                0x0D,
                (6, 0, 8),
                None,
                "Silver Rupee (Ganons Castle Forest Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Forest Trial Silver Rupee Front Right",
            (
                "SilverRupee",
                0x0D,
                (6, 0, 7),
                None,
                "Silver Rupee (Ganons Castle Forest Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Forest Trial Silver Rupee Center Left",
            (
                "SilverRupee",
                0x0D,
                (6, 0, 11),
                None,
                "Silver Rupee (Ganons Castle Forest Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Forest Trial Silver Rupee Back Center",
            (
                "SilverRupee",
                0x0D,
                (6, 0, 10),
                None,
                "Silver Rupee (Ganons Castle Forest Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle Forest Trial Silver Rupee Back Right",
            (
                "SilverRupee",
                0x0D,
                (6, 0, 9),
                None,
                "Silver Rupee (Ganons Castle Forest Trial)",
                (
                    "Ganon's Castle",
                    "Vanilla Dungeons",
                    "Silver Rupees",
                ),
            ),
        ),
        # Ganon's Castle MQ
        (
            "Ganons Castle MQ Forest Trial Freestanding Key",
            (
                "Collectable",
                0x0D,
                0x01,
                None,
                "Small Key (Ganons Castle)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Forest Trial Eye Switch Chest",
            (
                "Chest",
                0x0D,
                0x02,
                None,
                "Arrows (10)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Forest Trial Frozen Eye Switch Chest",
            (
                "Chest",
                0x0D,
                0x03,
                None,
                "Bombs (5)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Water Trial Chest",
            (
                "Chest",
                0x0D,
                0x01,
                None,
                "Rupees (20)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Shadow Trial Bomb Flower Chest",
            (
                "Chest",
                0x0D,
                0x00,
                None,
                "Arrows (10)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Shadow Trial Eye Switch Chest",
            (
                "Chest",
                0x0D,
                0x05,
                None,
                "Small Key (Ganons Castle)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Light Trial Lullaby Chest",
            (
                "Chest",
                0x0D,
                0x04,
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Spirit Trial First Chest",
            (
                "Chest",
                0x0D,
                0x0A,
                None,
                "Bombchus (10)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Spirit Trial Invisible Chest",
            (
                "Chest",
                0x0D,
                0x14,
                None,
                "Arrows (10)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Spirit Trial Sun Front Left Chest",
            (
                "Chest",
                0x0D,
                0x09,
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Spirit Trial Sun Back Left Chest",
            (
                "Chest",
                0x0D,
                0x08,
                None,
                "Small Key (Ganons Castle)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Spirit Trial Sun Back Right Chest",
            (
                "Chest",
                0x0D,
                0x07,
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Spirit Trial Golden Gauntlets Chest",
            (
                "Chest",
                0x0D,
                0x06,
                None,
                "Progressive Strength Upgrade",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Deku Scrub Left",
            (
                "Scrub",
                0x0D,
                0x3A,
                None,
                "Buy Green Potion",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Deku Scrub Center-Left",
            (
                "Scrub",
                0x0D,
                0x37,
                None,
                "Buy Bombs (5) for 35 Rupees",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Deku Scrub Center",
            (
                "Scrub",
                0x0D,
                0x33,
                None,
                "Buy Arrows (30)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Deku Scrub Center-Right",
            (
                "Scrub",
                0x0D,
                0x39,
                None,
                "Buy Red Potion for 30 Rupees",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Deku Scrubs",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Deku Scrub Right",
            (
                "Scrub",
                0x0D,
                0x30,
                None,
                "Buy Deku Nut (5)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Deku Scrubs",
                ),
            ),
        ),
        # Ganon's Castle MQ Freestanding
        (
            "Ganons Castle MQ Water Trial Recovery Heart",
            (
                "Freestanding",
                0x0D,
                (2, 0, 30),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Light Trial Recovery Heart 1",
            (
                "Freestanding",
                0x0D,
                (8, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Light Trial Recovery Heart 2",
            (
                "Freestanding",
                0x0D,
                (8, 0, 7),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Freestandings",
                ),
            ),
        ),
        # Ganon's Castle MQ Pots
        (
            "Ganons Castle MQ Water Trial Pot 1",
            (
                "Pot",
                0x0D,
                (4, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Water Trial Pot 2",
            (
                "Pot",
                0x0D,
                (4, 0, 6),
                None,
                "Arrows (10)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Forest Trial Pot 1",
            (
                "Pot",
                0x0D,
                (7, 0, 5),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Forest Trial Pot 2",
            (
                "Pot",
                0x0D,
                (7, 0, 6),
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Light Trial Pot 1",
            (
                "Pot",
                0x0D,
                (11, 0, 5),
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Light Trial Pot 2",
            (
                "Pot",
                0x0D,
                (11, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Shadow Trial Pot 1",
            (
                "Pot",
                0x0D,
                (13, 0, 5),
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Shadow Trial Pot 2",
            (
                "Pot",
                0x0D,
                (13, 0, 6),
                None,
                "Arrows (10)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Fire Trial Pot 1",
            (
                "Pot",
                0x0D,
                (15, 0, 5),
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Fire Trial Pot 2",
            (
                "Pot",
                0x0D,
                (15, 0, 6),
                None,
                "Recovery Heart",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Spirit Trial Pot 1",
            (
                "Pot",
                0x0D,
                (19, 0, 5),
                None,
                "Rupees (5)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Spirit Trial Pot 2",
            (
                "Pot",
                0x0D,
                (19, 0, 6),
                None,
                "Deku Nuts (5)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        # Ganon's Castle MQ Silver Rupees
        (
            "Ganons Castle MQ Fire Trial Silver Rupee Rising Platform",
            (
                "SilverRupee",
                0x0D,
                (14, 0, 22),
                None,
                "Silver Rupee (Ganons Castle Fire Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Fire Trial Silver Rupee Beamos",
            (
                "SilverRupee",
                0x0D,
                (14, 0, 19),
                None,
                "Silver Rupee (Ganons Castle Fire Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Fire Trial Silver Rupee Left Front",
            (
                "SilverRupee",
                0x0D,
                (14, 0, 23),
                None,
                "Silver Rupee (Ganons Castle Fire Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Fire Trial Silver Rupee Left Center",
            (
                "SilverRupee",
                0x0D,
                (14, 0, 20),
                None,
                "Silver Rupee (Ganons Castle Fire Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Fire Trial Silver Rupee Left Back",
            (
                "SilverRupee",
                0x0D,
                (14, 0, 21),
                None,
                "Silver Rupee (Ganons Castle Fire Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Shadow Trial Silver Rupee Moving Platform",
            (
                "SilverRupee",
                0x0D,
                (12, 0, 18),
                None,
                "Silver Rupee (Ganons Castle Shadow Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Shadow Trial Silver Rupee Bomb Flower",
            (
                "SilverRupee",
                0x0D,
                (12, 0, 14),
                None,
                "Silver Rupee (Ganons Castle Shadow Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Shadow Trial Silver Rupee First Beamos",
            (
                "SilverRupee",
                0x0D,
                (12, 0, 15),
                None,
                "Silver Rupee (Ganons Castle Shadow Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Shadow Trial Silver Rupee Last Beamos",
            (
                "SilverRupee",
                0x0D,
                (12, 0, 16),
                None,
                "Silver Rupee (Ganons Castle Shadow Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Shadow Trial Silver Rupee Guillotine",
            (
                "SilverRupee",
                0x0D,
                (12, 0, 17),
                None,
                "Silver Rupee (Ganons Castle Shadow Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Water Trial Silver Rupee Hole",
            (
                "SilverRupee",
                0x0D,
                (3, 0, 8),
                None,
                "Silver Rupee (Ganons Castle Water Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Water Trial Silver Rupee Near Blocks",
            (
                "SilverRupee",
                0x0D,
                (3, 0, 9),
                None,
                "Silver Rupee (Ganons Castle Water Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Water Trial Silver Rupee Center Left",
            (
                "SilverRupee",
                0x0D,
                (3, 0, 12),
                None,
                "Silver Rupee (Ganons Castle Water Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Water Trial Silver Rupee Red Ice",
            (
                "SilverRupee",
                0x0D,
                (3, 0, 10),
                None,
                "Silver Rupee (Ganons Castle Water Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        (
            "Ganons Castle MQ Water Trial Silver Rupee Above Void",
            (
                "SilverRupee",
                0x0D,
                (3, 0, 11),
                None,
                "Silver Rupee (Ganons Castle Water Trial)",
                (
                    "Ganon's Castle MQ",
                    "Master Quest",
                    "Silver Rupees",
                ),
            ),
        ),
        # Ganon's Castle Shared
        (
            "Ganons Tower Boss Key Chest",
            (
                "Chest",
                0x0A,
                0x0B,
                None,
                "Boss Key (Ganons Castle)",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Chests",
                ),
            ),
        ),
        # Ganon's Tower Pots
        (
            "Ganons Tower Pot 1",
            (
                "Pot",
                0x0A,
                [(8, 0, 2), (0, 0, 48)],
                None,
                "Rupees (5)",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 2",
            (
                "Pot",
                0x0A,
                [(8, 0, 3), (0, 0, 49)],
                None,
                "Recovery Heart",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 3",
            (
                "Pot",
                0x0A,
                [(8, 0, 4), (0, 0, 50)],
                None,
                "Arrows (10)",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 4",
            (
                "Pot",
                0x0A,
                [(8, 0, 5), (0, 0, 51)],
                None,
                "Rupees (5)",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 5",
            (
                "Pot",
                0x0A,
                [(8, 0, 6), (0, 0, 52)],
                None,
                "Arrows (10)",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 6",
            (
                "Pot",
                0x0A,
                [(8, 0, 7), (0, 0, 53)],
                None,
                "Recovery Heart",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 7",
            (
                "Pot",
                0x0A,
                [(8, 0, 8), (0, 0, 54)],
                None,
                "Rupees (5)",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 8",
            (
                "Pot",
                0x0A,
                [(8, 0, 9), (0, 0, 56)],
                None,
                "Recovery Heart",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 9",
            (
                "Pot",
                0x0A,
                [(8, 0, 10), (0, 0, 55)],
                None,
                "Nothing",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 10",
            (
                "Pot",
                0x0A,
                [(8, 0, 11), (0, 0, 57)],
                None,
                "Nothing",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 11",
            (
                "Pot",
                0x0A,
                [(8, 0, 12), (0, 0, 58)],
                None,
                "Arrows (10)",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 12",
            (
                "Pot",
                0x0A,
                [(8, 0, 13), (0, 0, 59)],
                None,
                "Arrows (10)",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 13",
            (
                "Pot",
                0x0A,
                [(8, 0, 14), (0, 0, 60)],
                None,
                "Recovery Heart",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 14",
            (
                "Pot",
                0x0A,
                [(8, 0, 15), (0, 0, 61)],
                None,
                "Recovery Heart",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 15",
            (
                "Pot",
                0x0A,
                [(8, 0, 16), (0, 0, 62)],
                None,
                "Recovery Heart",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 16",
            (
                "Pot",
                0x0A,
                [(8, 0, 17), (0, 0, 63)],
                None,
                "Nothing",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 17",
            (
                "Pot",
                0x0A,
                [(8, 0, 18), (0, 0, 64)],
                None,
                "Nothing",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        (
            "Ganons Tower Pot 18",
            (
                "Pot",
                0x0A,
                [(8, 0, 19), (0, 0, 65)],
                None,
                "Arrows (10)",
                (
                    "Ganon's Tower",
                    "Vanilla Dungeons",
                    "Master Quest",
                    "Pots",
                ),
            ),
        ),
        ## Events and Drops
        ("Pierre", ("Event", None, None, None, "Scarecrow Song", None)),
        ("Deliver Rutos Letter", ("Event", None, None, None, "Deliver Letter", None)),
        ("Master Sword Pedestal", ("Event", None, None, None, "Time Travel", None)),
        ("Deku Baba Sticks", ("Drop", None, None, None, "Deku Stick Drop", None)),
        ("Deku Baba Nuts", ("Drop", None, None, None, "Deku Nut Drop", None)),
        ("Stick Pot", ("Drop", None, None, None, "Deku Stick Drop", None)),
        ("Nut Pot", ("Drop", None, None, None, "Deku Nut Drop", None)),
        ("Nut Crate", ("Drop", None, None, None, "Deku Nut Drop", None)),
        ("Blue Fire", ("Drop", None, None, None, "Blue Fire", None)),
        ("Lone Fish", ("Drop", None, None, None, "Fish", None)),
        ("Fish Group", ("Drop", None, None, None, "Fish", None)),
        ("Bug Rock", ("Drop", None, None, None, "Bugs", None)),
        ("Bug Shrub", ("Drop", None, None, None, "Bugs", None)),
        ("Wandering Bugs", ("Drop", None, None, None, "Bugs", None)),
        ("Fairy Pot", ("Drop", None, None, None, "Fairy", None)),
        ("Free Fairies", ("Drop", None, None, None, "Fairy", None)),
        ("Wall Fairy", ("Drop", None, None, None, "Fairy", None)),
        ("Butterfly Fairy", ("Drop", None, None, None, "Fairy", None)),
        ("Gossip Stone Fairy", ("Drop", None, None, None, "Fairy", None)),
        ("Bean Plant Fairy", ("Drop", None, None, None, "Fairy", None)),
        ("Fairy Pond", ("Drop", None, None, None, "Fairy", None)),
        ("Big Poe Kill", ("Drop", None, None, None, "Big Poe", None)),
        ("Deku Shield Pot", ("Drop", None, None, None, "Deku Shield Drop", None)),
        ## Hints
        # These are not actual locations, but are filler spots used for hint reachability.
        # Hint location types must start with 'Hint'.
        ("DMC Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("DMT Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("Colossus Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("Dodongos Cavern Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("GV Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("GC Maze Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("GC Medigoron Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("Graveyard Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("HC Malon Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("HC Rock Wall Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("HC Storms Grotto Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("HF Cow Grotto Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("KF Deku Tree Gossip Stone (Left)", ("HintStone", None, None, None, None, None)),
        ("KF Deku Tree Gossip Stone (Right)", ("HintStone", None, None, None, None, None)),
        ("KF Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("LH Lab Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("LH Gossip Stone (Southeast)", ("HintStone", None, None, None, None, None)),
        ("LH Gossip Stone (Southwest)", ("HintStone", None, None, None, None, None)),
        ("LW Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("SFM Maze Gossip Stone (Lower)", ("HintStone", None, None, None, None, None)),
        ("SFM Maze Gossip Stone (Upper)", ("HintStone", None, None, None, None, None)),
        ("SFM Saria Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("ToT Gossip Stone (Left)", ("HintStone", None, None, None, None, None)),
        ("ToT Gossip Stone (Left-Center)", ("HintStone", None, None, None, None, None)),
        ("ToT Gossip Stone (Right)", ("HintStone", None, None, None, None, None)),
        ("ToT Gossip Stone (Right-Center)", ("HintStone", None, None, None, None, None)),
        ("ZD Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("ZF Fairy Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("ZF Jabu Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("ZR Near Grottos Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("ZR Near Domain Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("HF Near Market Grotto Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("HF Southeast Grotto Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("HF Open Grotto Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("Kak Open Grotto Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("ZR Open Grotto Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("KF Storms Grotto Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("LW Near Shortcuts Grotto Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("DMT Storms Grotto Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("DMC Upper Grotto Gossip Stone", ("HintStone", None, None, None, None, None)),
        ("ToT Child Altar Hint", ("Hint", None, None, None, None, None)),
        ("ToT Adult Altar Hint", ("Hint", None, None, None, None, None)),
        ("Dampe Diary Hint", ("Hint", None, None, None, None, None)),
        ("10 Skulltulas Reward Hint", ("Hint", None, None, None, None, None)),
        ("20 Skulltulas Reward Hint", ("Hint", None, None, None, None, None)),
        ("30 Skulltulas Reward Hint", ("Hint", None, None, None, None, None)),
        ("40 Skulltulas Reward Hint", ("Hint", None, None, None, None, None)),
        ("50 Skulltulas Reward Hint", ("Hint", None, None, None, None, None)),
        ("ZR Frogs Ocarina Minigame Hint", ("Hint", None, None, None, None, None)),
        ("Ganondorf Hint", ("Hint", None, None, None, None, None)),
    ]
)

location_sort_order: dict[str, int] = {loc: i for i, loc in enumerate(location_table.keys())}

# Business Scrub Details
business_scrubs: list[tuple[int, int, int, list[str]]] = [
    # id   price  text   text replacement
    (0x30, 20, 0x10A0, ["Deku Nuts", "a \x05\x42mysterious item\x05\x40"]),
    (0x31, 15, 0x10A1, ["Deku Sticks", "a \x05\x42mysterious item\x05\x40"]),
    (0x3E, 10, 0x10A2, ["Piece of Heart", "\x05\x42mysterious item\x05\x40"]),
    (0x33, 40, 0x10CA, ["\x05\x41Deku Seeds", "a \x05\x42mysterious item"]),
    (0x34, 50, 0x10CB, ["\x41Deku Shield", "\x42mysterious item"]),
    (0x37, 40, 0x10CC, ["\x05\x41Bombs", "a \x05\x42mysterious item"]),
    (0x38, 00, 0x10CD, ["\x05\x41Arrows", "a \x05\x42mysterious item"]),  # unused
    (0x39, 40, 0x10CE, ["\x05\x41Red Potion", "\x05\x42mysterious item"]),
    (0x3A, 40, 0x10CF, ["Green Potion", "mysterious item"]),
    (
        0x77,
        40,
        0x10DC,
        ["enable you to pick up more\x01\x05\x41Deku Sticks", "sell you a \x05\x42mysterious item"],
    ),
    (
        0x79,
        40,
        0x10DD,
        ["enable you to pick up more \x05\x41Deku\x01Nuts", "sell you a \x05\x42mysterious item"],
    ),
]

dungeons: tuple[str, ...] = (
    "Deku Tree",
    "Dodongo's Cavern",
    "Jabu Jabu's Belly",
    "Forest Temple",
    "Fire Temple",
    "Water Temple",
    "Spirit Temple",
    "Shadow Temple",
    "Ice Cavern",
    "Bottom of the Well",
    "Gerudo Training Ground",
    "Ganon's Castle",
)
location_groups: dict[str, list[str]] = {
    "Song": [name for (name, data) in location_table.items() if data[0] == "Song"],
    "Chest": [name for (name, data) in location_table.items() if data[0] == "Chest"],
    "Collectable": [name for (name, data) in location_table.items() if data[0] == "Collectable"],
    "Boss": [
        name
        for (name, data) in location_table.items()
        if data[0] == "Boss" or name == "ToT Reward from Rauru"
    ],
    "ActorOverride": [
        name for (name, data) in location_table.items() if data[0] == "ActorOverride"
    ],
    "BossHeart": [name for (name, data) in location_table.items() if data[0] == "BossHeart"],
    "CollectableLike": [
        name
        for (name, data) in location_table.items()
        if data[0] in ("Collectable", "BossHeart", "GS Token", "SilverRupee")
    ],
    "CanSee": [
        name
        for (name, data) in location_table.items()
        if data[0]
        in (
            "Collectable",
            "BossHeart",
            "GS Token",
            "Shop",
            "MaskShop",
            "Freestanding",
            "ActorOverride",
            "RupeeTower",
            "Pot",
            "Crate",
            "FlyingPot",
            "SmallCrate",
            "Beehive",
            "SilverRupee",
        )
        # Treasure Box Shop, Bombchu Bowling, Hyrule Field (OoT), Lake Hylia (RL/FA)
        or data[0:2] in [("Chest", 0x10), ("NPC", 0x4B), ("NPC", 0x51), ("NPC", 0x57)]
    ],
    "Dungeon": [
        name
        for (name, data) in location_table.items()
        if data[5] is not None and any(dungeon in data[5] for dungeon in dungeons)
    ],
}


def location_is_viewable(
    loc_name: str,
    correct_chest_appearances: str,
    fast_chests: bool,
    *,
    world: Optional[World] = None,
) -> bool:
    return (
        (
            (correct_chest_appearances in ("textures", "both", "classic") or not fast_chests)
            and loc_name in location_groups["Chest"]
        )
        or loc_name in location_groups["CanSee"]
        or (
            world is not None
            and world.bigocto_location() is not None
            and world.bigocto_location().name == loc_name
        )
    )
