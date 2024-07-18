from __future__ import annotations
from typing import Optional, Any

# Progressive: True  -> Advancement
#              False -> Priority
#              None  -> Normal
#    Item:                                            (type, Progressive, GetItemID, special),
#
# special "upgrade_ids" correspond to the item IDs in item_table.c for all of the upgrade tiers
# of that item.
#
item_table: dict[str, tuple[str, Optional[bool], Optional[int], Optional[dict[str, Any]]]] = {
    "Bombs (5)": ("Item", None, 0x0001, {"junk": 8}),
    "Deku Nuts (5)": ("Item", None, 0x0002, {"junk": 5}),
    "Bombchus (10)": ("Item", True, 0x0003, None),
    "Boomerang": ("Item", True, 0x0006, None),
    "Deku Stick (1)": ("Item", None, 0x0007, {"junk": 5}),
    "Lens of Truth": ("Item", True, 0x000A, None),
    "Megaton Hammer": ("Item", True, 0x000D, None),
    "Cojiro": ("Item", True, 0x000E, {"trade": True}),
    "Bottle": ("Item", True, 0x000F, {"bottle": float("Inf")}),
    "Blue Potion": ("Item", True, 0x0012, None),  # distinct from shop item
    "Bottle with Milk": ("Item", True, 0x0014, {"bottle": float("Inf")}),
    "Rutos Letter": ("Item", True, 0x0015, None),
    "Deliver Letter": ("Item", True, None, {"bottle": float("Inf")}),
    "Sell Big Poe": ("Item", True, None, {"bottle": float("Inf")}),
    "Magic Bean": ("Item", True, 0x0016, {"progressive": 10}),
    "Skull Mask": ("Item", True, 0x0017, {"trade": True, "object": 0x0136}),
    "Spooky Mask": ("Item", True, 0x0018, {"trade": True, "object": 0x0135}),
    "Chicken": ("Item", True, 0x0019, {"trade": True}),
    "Keaton Mask": ("Item", True, 0x001A, {"trade": True, "object": 0x0134}),
    "Bunny Hood": ("Item", True, 0x001B, {"trade": True, "object": 0x0137}),
    "Mask of Truth": ("Item", True, 0x001C, {"trade": True, "object": 0x0138}),
    "Pocket Egg": ("Item", True, 0x001D, {"trade": True}),
    "Pocket Cucco": ("Item", True, 0x001E, {"trade": True}),
    "Odd Mushroom": ("Item", True, 0x001F, {"trade": True}),
    "Odd Potion": ("Item", True, 0x0020, {"trade": True}),
    "Poachers Saw": ("Item", True, 0x0021, {"trade": True}),
    "Broken Sword": ("Item", True, 0x0022, {"trade": True}),
    "Prescription": ("Item", True, 0x0023, {"trade": True}),
    "Eyeball Frog": ("Item", True, 0x0024, {"trade": True}),
    "Eyedrops": ("Item", True, 0x0025, {"trade": True}),
    "Claim Check": ("Item", True, 0x0026, {"trade": True}),
    "Kokiri Sword": ("Item", True, 0x0027, None),
    "Giants Knife": ("Item", None, 0x0028, None),
    "Deku Shield": ("Item", None, 0x0029, None),
    "Hylian Shield": ("Item", None, 0x002A, None),
    "Mirror Shield": ("Item", True, 0x002B, None),
    "Goron Tunic": ("Item", True, 0x002C, None),
    "Zora Tunic": ("Item", True, 0x002D, None),
    "Iron Boots": ("Item", True, 0x002E, None),
    "Hover Boots": ("Item", True, 0x002F, None),
    "Stone of Agony": ("Item", True, 0x0039, None),
    "Gerudo Membership Card": ("Item", True, 0x003A, None),
    "Heart Container": (
        "Item",
        True,
        0x003D,
        {"alias": ("Piece of Heart", 4), "progressive": float("Inf")},
    ),
    "Piece of Heart": ("Item", True, 0x003E, {"progressive": float("Inf")}),
    "Boss Key": ("BossKey", True, 0x003F, None),
    "Compass": ("Compass", None, 0x0040, None),
    "Map": ("Map", None, 0x0041, None),
    "Small Key": ("SmallKey", True, 0x0042, {"progressive": float("Inf")}),
    "Weird Egg": ("Item", True, 0x0047, {"trade": True}),
    "Recovery Heart": ("Item", None, 0x0048, {"junk": 0}),
    "Arrows (5)": ("Item", None, 0x0049, {"junk": 8}),
    "Arrows (10)": ("Item", None, 0x004A, {"junk": 2}),
    "Arrows (30)": ("Item", None, 0x004B, {"junk": 0}),
    "Rupee (1)": ("Item", None, 0x004C, {"junk": -1}),
    "Rupees (5)": ("Item", None, 0x004D, {"junk": 10}),
    "Rupees (20)": ("Item", None, 0x004E, {"junk": 4}),
    "Milk": ("Item", None, 0x0050, None),
    "Goron Mask": ("Item", None, 0x0051, {"trade": True, "object": 0x0150}),
    "Zora Mask": ("Item", None, 0x0052, {"trade": True, "object": 0x0151}),
    "Gerudo Mask": ("Item", None, 0x0053, {"trade": True, "object": 0x0152}),
    "Rupees (50)": ("Item", None, 0x0055, {"junk": 1}),
    "Rupees (200)": ("Item", None, 0x0056, {"junk": 0}),
    "Biggoron Sword": ("Item", None, 0x0057, None),
    "Fire Arrows": ("Item", True, 0x0058, None),
    "Ice Arrows": ("Item", True, 0x0059, None),
    "Blue Fire Arrows": ("Item", True, 0x0059, None),
    "Light Arrows": ("Item", True, 0x005A, None),
    "Gold Skulltula Token": ("Token", True, 0x005B, {"progressive": float("Inf")}),
    "Dins Fire": ("Item", True, 0x005C, None),
    "Nayrus Love": ("Item", True, 0x005E, None),
    "Farores Wind": ("Item", True, 0x005D, None),
    "Deku Nuts (10)": ("Item", None, 0x0064, {"junk": 0}),
    "Bomb (1)": ("Item", None, 0x0065, {"junk": -1}),
    "Bombs (10)": ("Item", None, 0x0066, {"junk": 2}),
    "Bombs (20)": ("Item", None, 0x0067, {"junk": 0}),
    "Deku Seeds (30)": ("Item", None, 0x0069, {"junk": 5}),
    "Bombchus (5)": ("Item", True, 0x006A, None),
    "Bombchus (20)": ("Item", True, 0x006B, None),
    "Small Key (Treasure Chest Game)": ("TCGSmallKey", True, 0x0071, {"progressive": float("Inf")}),
    "Rupee (Treasure Chest Game) (1)": ("Item", None, 0x0072, None),
    "Rupees (Treasure Chest Game) (5)": ("Item", None, 0x0073, None),
    "Rupees (Treasure Chest Game) (20)": ("Item", None, 0x0074, None),
    "Rupees (Treasure Chest Game) (50)": ("Item", None, 0x0075, None),
    "Piece of Heart (Treasure Chest Game)": (
        "Item",
        True,
        0x0076,
        {"alias": ("Piece of Heart", 1), "progressive": float("Inf")},
    ),
    "Ice Trap": ("Item", None, 0x007C, {"junk": 0}),
    "Progressive Hookshot": ("Item", True, 0x0080, {"progressive": 2}),
    "Progressive Strength Upgrade": ("Item", True, 0x0081, {"progressive": 3}),
    "Bomb Bag": ("Item", True, 0x0082, None),
    "Bow": ("Item", True, 0x0083, None),
    "Slingshot": ("Item", True, 0x0084, None),
    "Progressive Wallet": ("Item", True, 0x0085, {"progressive": 3}),
    "Progressive Scale": ("Item", True, 0x0086, {"progressive": 2}),
    "Deku Nut Capacity": ("Item", None, 0x0087, None),
    "Deku Stick Capacity": ("Item", None, 0x0088, None),
    "Bombchus": ("Item", True, 0x0089, None),
    "Magic Meter": ("Item", True, 0x008A, None),
    "Ocarina": ("Item", True, 0x008B, None),
    "Bottle with Red Potion": ("Item", True, 0x008C, {"bottle": True, "shop_object": 0x0F}),
    "Bottle with Green Potion": ("Item", True, 0x008D, {"bottle": True, "shop_object": 0x0F}),
    "Bottle with Blue Potion": ("Item", True, 0x008E, {"bottle": True, "shop_object": 0x0F}),
    "Bottle with Fairy": ("Item", True, 0x008F, {"bottle": True, "shop_object": 0x0F}),
    "Bottle with Fish": ("Item", True, 0x0090, {"bottle": True, "shop_object": 0x0F}),
    "Bottle with Blue Fire": ("Item", True, 0x0091, {"bottle": True, "shop_object": 0x0F}),
    "Bottle with Bugs": ("Item", True, 0x0092, {"bottle": True, "shop_object": 0x0F}),
    "Bottle with Big Poe": ("Item", True, 0x0093, {"shop_object": 0x0F}),
    "Bottle with Poe": ("Item", True, 0x0094, {"bottle": True, "shop_object": 0x0F}),
    "Boss Key (Forest Temple)": ("BossKey", True, 0x0095, None),
    "Boss Key (Fire Temple)": ("BossKey", True, 0x0096, None),
    "Boss Key (Water Temple)": ("BossKey", True, 0x0097, None),
    "Boss Key (Spirit Temple)": ("BossKey", True, 0x0098, None),
    "Boss Key (Shadow Temple)": ("BossKey", True, 0x0099, None),
    "Boss Key (Ganons Castle)": ("GanonBossKey", True, 0x009A, None),
    "Compass (Deku Tree)": ("Compass", False, 0x009B, None),
    "Compass (Dodongos Cavern)": ("Compass", False, 0x009C, None),
    "Compass (Jabu Jabus Belly)": ("Compass", False, 0x009D, None),
    "Compass (Forest Temple)": ("Compass", False, 0x009E, None),
    "Compass (Fire Temple)": ("Compass", False, 0x009F, None),
    "Compass (Water Temple)": ("Compass", False, 0x00A0, None),
    "Compass (Spirit Temple)": ("Compass", False, 0x00A1, None),
    "Compass (Shadow Temple)": ("Compass", False, 0x00A2, None),
    "Compass (Bottom of the Well)": ("Compass", False, 0x00A3, None),
    "Compass (Ice Cavern)": ("Compass", False, 0x00A4, None),
    "Map (Deku Tree)": ("Map", False, 0x00A5, None),
    "Map (Dodongos Cavern)": ("Map", False, 0x00A6, None),
    "Map (Jabu Jabus Belly)": ("Map", False, 0x00A7, None),
    "Map (Forest Temple)": ("Map", False, 0x00A8, None),
    "Map (Fire Temple)": ("Map", False, 0x00A9, None),
    "Map (Water Temple)": ("Map", False, 0x00AA, None),
    "Map (Spirit Temple)": ("Map", False, 0x00AB, None),
    "Map (Shadow Temple)": ("Map", False, 0x00AC, None),
    "Map (Bottom of the Well)": ("Map", False, 0x00AD, None),
    "Map (Ice Cavern)": ("Map", False, 0x00AE, None),
    "Small Key (Forest Temple)": ("SmallKey", True, 0x00AF, {"progressive": float("Inf")}),
    "Small Key (Fire Temple)": ("SmallKey", True, 0x00B0, {"progressive": float("Inf")}),
    "Small Key (Water Temple)": ("SmallKey", True, 0x00B1, {"progressive": float("Inf")}),
    "Small Key (Spirit Temple)": ("SmallKey", True, 0x00B2, {"progressive": float("Inf")}),
    "Small Key (Shadow Temple)": ("SmallKey", True, 0x00B3, {"progressive": float("Inf")}),
    "Small Key (Bottom of the Well)": ("SmallKey", True, 0x00B4, {"progressive": float("Inf")}),
    "Small Key (Gerudo Training Ground)": ("SmallKey", True, 0x00B5, {"progressive": float("Inf")}),
    "Small Key (Thieves Hideout)": ("HideoutSmallKey", True, 0x00B6, {"progressive": float("Inf")}),
    "Small Key (Ganons Castle)": ("SmallKey", True, 0x00B7, {"progressive": float("Inf")}),
    "Double Defense": ("Item", None, 0x00B8, None),
    "Buy Magic Bean": ("Item", True, 0x0016, {"alias": ("Magic Bean", 10), "progressive": 10}),
    "Magic Bean Pack": ("Item", True, 0x00C9, {"alias": ("Magic Bean", 10), "progressive": 10}),
    "Triforce Piece": ("Item", True, 0x00CA, {"progressive": float("Inf")}),
    "Zeldas Letter": ("Item", True, 0x000B, {"trade": True}),
    "Time Travel": ("Event", True, None, None),
    "Scarecrow Song": ("Event", True, None, None),
    "Triforce": ("Event", True, None, None),
    "Small Key Ring (Forest Temple)": (
        "SmallKey",
        True,
        0x00CB,
        {"alias": ("Small Key (Forest Temple)", 10), "progressive": float("Inf")},
    ),
    "Small Key Ring (Fire Temple)": (
        "SmallKey",
        True,
        0x00CC,
        {"alias": ("Small Key (Fire Temple)", 10), "progressive": float("Inf")},
    ),
    "Small Key Ring (Water Temple)": (
        "SmallKey",
        True,
        0x00CD,
        {"alias": ("Small Key (Water Temple)", 10), "progressive": float("Inf")},
    ),
    "Small Key Ring (Spirit Temple)": (
        "SmallKey",
        True,
        0x00CE,
        {"alias": ("Small Key (Spirit Temple)", 10), "progressive": float("Inf")},
    ),
    "Small Key Ring (Shadow Temple)": (
        "SmallKey",
        True,
        0x00CF,
        {"alias": ("Small Key (Shadow Temple)", 10), "progressive": float("Inf")},
    ),
    "Small Key Ring (Bottom of the Well)": (
        "SmallKey",
        True,
        0x00D0,
        {"alias": ("Small Key (Bottom of the Well)", 10), "progressive": float("Inf")},
    ),
    "Small Key Ring (Gerudo Training Ground)": (
        "SmallKey",
        True,
        0x00D1,
        {"alias": ("Small Key (Gerudo Training Ground)", 10), "progressive": float("Inf")},
    ),
    "Small Key Ring (Thieves Hideout)": (
        "HideoutSmallKey",
        True,
        0x00D2,
        {"alias": ("Small Key (Thieves Hideout)", 10), "progressive": float("Inf")},
    ),
    "Small Key Ring (Ganons Castle)": (
        "SmallKey",
        True,
        0x00D3,
        {"alias": ("Small Key (Ganons Castle)", 10), "progressive": float("Inf")},
    ),
    "Small Key Ring (Treasure Chest Game)": (
        "TCGSmallKey",
        True,
        0x00D7,
        {"alias": ("Small Key (Treasure Chest Game)", 10), "progressive": float("Inf")},
    ),
    "Silver Rupee (Dodongos Cavern Staircase)": ("SilverRupee", True, 0x00D8, {"progressive": 5}),
    "Silver Rupee (Ice Cavern Spinning Scythe)": ("SilverRupee", True, 0x00D9, {"progressive": 5}),
    "Silver Rupee (Ice Cavern Push Block)": ("SilverRupee", True, 0x00DA, {"progressive": 5}),
    "Silver Rupee (Bottom of the Well Basement)": ("SilverRupee", True, 0x00DB, {"progressive": 5}),
    "Silver Rupee (Shadow Temple Scythe Shortcut)": (
        "SilverRupee",
        True,
        0x00DC,
        {"progressive": 5},
    ),
    "Silver Rupee (Shadow Temple Invisible Blades)": (
        "SilverRupee",
        True,
        0x00DD,
        {"progressive": 10},
    ),
    "Silver Rupee (Shadow Temple Huge Pit)": ("SilverRupee", True, 0x00DE, {"progressive": 5}),
    "Silver Rupee (Shadow Temple Invisible Spikes)": (
        "SilverRupee",
        True,
        0x00DF,
        {"progressive": 10},
    ),
    "Silver Rupee (Gerudo Training Ground Slopes)": (
        "SilverRupee",
        True,
        0x00E0,
        {"progressive": 5},
    ),
    "Silver Rupee (Gerudo Training Ground Lava)": ("SilverRupee", True, 0x00E1, {"progressive": 6}),
    "Silver Rupee (Gerudo Training Ground Water)": (
        "SilverRupee",
        True,
        0x00E2,
        {"progressive": 5},
    ),
    "Silver Rupee (Spirit Temple Child Early Torches)": (
        "SilverRupee",
        True,
        0x00E3,
        {"progressive": 5},
    ),
    "Silver Rupee (Spirit Temple Adult Boulders)": (
        "SilverRupee",
        True,
        0x00E4,
        {"progressive": 5},
    ),
    "Silver Rupee (Spirit Temple Lobby and Lower Adult)": (
        "SilverRupee",
        True,
        0x00E5,
        {"progressive": 5},
    ),
    "Silver Rupee (Spirit Temple Sun Block)": ("SilverRupee", True, 0x00E6, {"progressive": 5}),
    "Silver Rupee (Spirit Temple Adult Climb)": ("SilverRupee", True, 0x00E7, {"progressive": 5}),
    "Silver Rupee (Ganons Castle Spirit Trial)": ("SilverRupee", True, 0x00E8, {"progressive": 5}),
    "Silver Rupee (Ganons Castle Light Trial)": ("SilverRupee", True, 0x00E9, {"progressive": 5}),
    "Silver Rupee (Ganons Castle Fire Trial)": ("SilverRupee", True, 0x00EA, {"progressive": 5}),
    "Silver Rupee (Ganons Castle Shadow Trial)": ("SilverRupee", True, 0x00EB, {"progressive": 5}),
    "Silver Rupee (Ganons Castle Water Trial)": ("SilverRupee", True, 0x00EC, {"progressive": 5}),
    "Silver Rupee (Ganons Castle Forest Trial)": ("SilverRupee", True, 0x00ED, {"progressive": 5}),
    "Silver Rupee Pouch (Dodongos Cavern Staircase)": (
        "SilverRupee",
        True,
        0x00EE,
        {"alias": ("Silver Rupee (Dodongos Cavern Staircase)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Ice Cavern Spinning Scythe)": (
        "SilverRupee",
        True,
        0x00EF,
        {"alias": ("Silver Rupee (Ice Cavern Spinning Scythe)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Ice Cavern Push Block)": (
        "SilverRupee",
        True,
        0x00F0,
        {"alias": ("Silver Rupee (Ice Cavern Push Block)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Bottom of the Well Basement)": (
        "SilverRupee",
        True,
        0x00F1,
        {"alias": ("Silver Rupee (Bottom of the Well Basement)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Shadow Temple Scythe Shortcut)": (
        "SilverRupee",
        True,
        0x00F2,
        {"alias": ("Silver Rupee (Shadow Temple Scythe Shortcut)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Shadow Temple Invisible Blades)": (
        "SilverRupee",
        True,
        0x00F3,
        {"alias": ("Silver Rupee (Shadow Temple Invisible Blades)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Shadow Temple Huge Pit)": (
        "SilverRupee",
        True,
        0x00F4,
        {"alias": ("Silver Rupee (Shadow Temple Huge Pit)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Shadow Temple Invisible Spikes)": (
        "SilverRupee",
        True,
        0x00F5,
        {"alias": ("Silver Rupee (Shadow Temple Invisible Spikes)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Gerudo Training Ground Slopes)": (
        "SilverRupee",
        True,
        0x00F6,
        {"alias": ("Silver Rupee (Gerudo Training Ground Slopes)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Gerudo Training Ground Lava)": (
        "SilverRupee",
        True,
        0x00F7,
        {"alias": ("Silver Rupee (Gerudo Training Ground Lava)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Gerudo Training Ground Water)": (
        "SilverRupee",
        True,
        0x00F8,
        {"alias": ("Silver Rupee (Gerudo Training Ground Water)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Spirit Temple Child Early Torches)": (
        "SilverRupee",
        True,
        0x00F9,
        {"alias": ("Silver Rupee (Spirit Temple Child Early Torches)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Spirit Temple Adult Boulders)": (
        "SilverRupee",
        True,
        0x00FA,
        {"alias": ("Silver Rupee (Spirit Temple Adult Boulders)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Spirit Temple Lobby and Lower Adult)": (
        "SilverRupee",
        True,
        0x00FB,
        {"alias": ("Silver Rupee (Spirit Temple Lobby and Lower Adult)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Spirit Temple Sun Block)": (
        "SilverRupee",
        True,
        0x00FC,
        {"alias": ("Silver Rupee (Spirit Temple Sun Block)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Spirit Temple Adult Climb)": (
        "SilverRupee",
        True,
        0x00FD,
        {"alias": ("Silver Rupee (Spirit Temple Adult Climb)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Ganons Castle Spirit Trial)": (
        "SilverRupee",
        True,
        0x00FE,
        {"alias": ("Silver Rupee (Ganons Castle Spirit Trial)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Ganons Castle Light Trial)": (
        "SilverRupee",
        True,
        0x00FF,
        {"alias": ("Silver Rupee (Ganons Castle Light Trial)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Ganons Castle Fire Trial)": (
        "SilverRupee",
        True,
        0x0100,
        {"alias": ("Silver Rupee (Ganons Castle Fire Trial)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Ganons Castle Shadow Trial)": (
        "SilverRupee",
        True,
        0x0101,
        {"alias": ("Silver Rupee (Ganons Castle Shadow Trial)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Ganons Castle Water Trial)": (
        "SilverRupee",
        True,
        0x0102,
        {"alias": ("Silver Rupee (Ganons Castle Water Trial)", 10), "progressive": 1},
    ),
    "Silver Rupee Pouch (Ganons Castle Forest Trial)": (
        "SilverRupee",
        True,
        0x0103,
        {"alias": ("Silver Rupee (Ganons Castle Forest Trial)", 10), "progressive": 1},
    ),
    "Ocarina A Button": ("Item", True, 0x0104, {"ocarina_button": True}),
    "Ocarina C up Button": ("Item", True, 0x0105, {"ocarina_button": True}),
    "Ocarina C down Button": ("Item", True, 0x0106, {"ocarina_button": True}),
    "Ocarina C left Button": ("Item", True, 0x0107, {"ocarina_button": True}),
    "Ocarina C right Button": ("Item", True, 0x0108, {"ocarina_button": True}),
    "Fairy Drop": ("Item", None, 0x0119, None),
    "Nothing": ("Item", None, 0x011A, None),
    # Event items otherwise generated by generic event logic
    # can be defined here to enforce their appearance in playthroughs.
    "Water Temple Clear": ("Event", True, None, None),
    "Forest Trial Clear": ("Event", True, None, None),
    "Fire Trial Clear": ("Event", True, None, None),
    "Water Trial Clear": ("Event", True, None, None),
    "Shadow Trial Clear": ("Event", True, None, None),
    "Spirit Trial Clear": ("Event", True, None, None),
    "Light Trial Clear": ("Event", True, None, None),
    "Epona": ("Event", True, None, None),
    "Deku Stick Drop": ("Drop", True, None, None),
    "Deku Nut Drop": ("Drop", True, None, None),
    "Blue Fire": ("Drop", True, None, None),
    "Fairy": ("Drop", True, None, None),
    "Fish": ("Drop", True, None, None),
    "Bugs": ("Drop", True, None, None),
    "Big Poe": ("Drop", True, None, None),
    "Bombchu Drop": ("Drop", True, None, None),
    "Deku Shield Drop": ("Drop", True, None, None),
    # Consumable refills defined mostly to placate 'starting with' options
    "Arrows": ("Refill", None, None, None),
    "Bombs": ("Refill", None, None, None),
    "Deku Seeds": ("Refill", None, None, None),
    "Deku Sticks": ("Refill", None, None, None),
    "Deku Nuts": ("Refill", None, None, None),
    "Rupees": ("Refill", None, None, None),
    "Minuet of Forest": (
        "Song",
        True,
        0x00BB,
        {
            "text_id": 0x73,
            "song_id": 0x02,
            "item_id": 0x5A,
        },
    ),
    "Bolero of Fire": (
        "Song",
        True,
        0x00BC,
        {
            "text_id": 0x74,
            "song_id": 0x03,
            "item_id": 0x5B,
        },
    ),
    "Serenade of Water": (
        "Song",
        True,
        0x00BD,
        {
            "text_id": 0x75,
            "song_id": 0x04,
            "item_id": 0x5C,
        },
    ),
    "Requiem of Spirit": (
        "Song",
        True,
        0x00BE,
        {
            "text_id": 0x76,
            "song_id": 0x05,
            "item_id": 0x5D,
        },
    ),
    "Nocturne of Shadow": (
        "Song",
        True,
        0x00BF,
        {
            "text_id": 0x77,
            "song_id": 0x06,
            "item_id": 0x5E,
        },
    ),
    "Prelude of Light": (
        "Song",
        True,
        0x00C0,
        {
            "text_id": 0x78,
            "song_id": 0x07,
            "item_id": 0x5F,
        },
    ),
    "Zeldas Lullaby": (
        "Song",
        True,
        0x00C1,
        {
            "text_id": 0xD4,
            "song_id": 0x0A,
            "item_id": 0x60,
        },
    ),
    "Eponas Song": (
        "Song",
        True,
        0x00C2,
        {
            "text_id": 0xD2,
            "song_id": 0x09,
            "item_id": 0x61,
        },
    ),
    "Sarias Song": (
        "Song",
        True,
        0x00C3,
        {
            "text_id": 0xD1,
            "song_id": 0x08,
            "item_id": 0x62,
        },
    ),
    "Suns Song": (
        "Song",
        True,
        0x00C4,
        {
            "text_id": 0xD3,
            "song_id": 0x0B,
            "item_id": 0x63,
        },
    ),
    "Song of Time": (
        "Song",
        True,
        0x00C5,
        {
            "text_id": 0xD5,
            "song_id": 0x0C,
            "item_id": 0x64,
        },
    ),
    "Song of Storms": (
        "Song",
        True,
        0x00C6,
        {
            "text_id": 0xD6,
            "song_id": 0x0D,
            "item_id": 0x65,
        },
    ),
    "Buy Deku Nut (5)": ("Shop", True, 0x00, {"object": 0x00BB, "price": 15}),
    "Buy Arrows (30)": ("Shop", False, 0x01, {"object": 0x00D8, "price": 60}),
    "Buy Arrows (50)": ("Shop", False, 0x02, {"object": 0x00D8, "price": 90}),
    "Buy Bombs (5) for 25 Rupees": ("Shop", False, 0x03, {"object": 0x00CE, "price": 25}),
    "Buy Deku Nut (10)": ("Shop", True, 0x04, {"object": 0x00BB, "price": 30}),
    "Buy Deku Stick (1)": ("Shop", True, 0x05, {"object": 0x00C7, "price": 10}),
    "Buy Bombs (10)": ("Shop", False, 0x06, {"object": 0x00CE, "price": 50}),
    "Buy Fish": ("Shop", True, 0x07, {"object": 0x00F4, "price": 200}),
    "Buy Red Potion for 30 Rupees": ("Shop", False, 0x08, {"object": 0x00EB, "price": 30}),
    "Buy Green Potion": ("Shop", False, 0x09, {"object": 0x00EB, "price": 30}),
    "Buy Blue Potion": ("Shop", False, 0x0A, {"object": 0x00EB, "price": 100}),
    "Buy Hylian Shield": ("Shop", True, 0x0C, {"object": 0x00DC, "price": 80}),
    "Buy Deku Shield": ("Shop", True, 0x0D, {"object": 0x00CB, "price": 40}),
    "Buy Goron Tunic": ("Shop", True, 0x0E, {"object": 0x00F2, "price": 200}),
    "Buy Zora Tunic": ("Shop", True, 0x0F, {"object": 0x00F2, "price": 300}),
    "Buy Heart": ("Shop", False, 0x10, {"object": 0x00B7, "price": 10}),
    "Buy Bombchu (10)": ("Shop", True, 0x15, {"object": 0x00D9, "price": 99}),
    "Buy Bombchu (20)": ("Shop", True, 0x16, {"object": 0x00D9, "price": 180}),
    "Buy Bombchu (5)": ("Shop", True, 0x18, {"object": 0x00D9, "price": 60}),
    "Buy Deku Seeds (30)": ("Shop", False, 0x1D, {"object": 0x0119, "price": 30}),
    "Sold Out": ("Shop", False, 0x26, {"object": 0x0148}),
    "Buy Blue Fire": ("Shop", True, 0x27, {"object": 0x0173, "price": 300}),
    "Buy Bottle Bug": ("Shop", True, 0x28, {"object": 0x0174, "price": 50}),
    "Buy Poe": ("Shop", False, 0x2A, {"object": 0x0176, "price": 30}),
    "Buy Fairy's Spirit": ("Shop", True, 0x2B, {"object": 0x0177, "price": 50}),
    "Buy Arrows (10)": ("Shop", False, 0x2C, {"object": 0x00D8, "price": 20}),
    "Buy Bombs (20)": ("Shop", False, 0x2D, {"object": 0x00CE, "price": 80}),
    "Buy Bombs (30)": ("Shop", False, 0x2E, {"object": 0x00CE, "price": 120}),
    "Buy Bombs (5) for 35 Rupees": ("Shop", False, 0x2F, {"object": 0x00CE, "price": 35}),
    "Buy Red Potion for 40 Rupees": ("Shop", False, 0x30, {"object": 0x00EB, "price": 40}),
    "Buy Red Potion for 50 Rupees": ("Shop", False, 0x31, {"object": 0x00EB, "price": 50}),
    "Kokiri Emerald": ("DungeonReward", True, 0x0127, {"stone": True, "item_id": 0x6C}),
    "Goron Ruby": ("DungeonReward", True, 0x0128, {"stone": True, "item_id": 0x6D}),
    "Zora Sapphire": ("DungeonReward", True, 0x0129, {"stone": True, "item_id": 0x6E}),
    "Light Medallion": ("DungeonReward", True, 0x012A, {"medallion": True, "item_id": 0x6B}),
    "Forest Medallion": ("DungeonReward", True, 0x012B, {"medallion": True, "item_id": 0x66}),
    "Fire Medallion": ("DungeonReward", True, 0x012C, {"medallion": True, "item_id": 0x67}),
    "Water Medallion": ("DungeonReward", True, 0x012D, {"medallion": True, "item_id": 0x68}),
    "Shadow Medallion": ("DungeonReward", True, 0x012E, {"medallion": True, "item_id": 0x6A}),
    "Spirit Medallion": ("DungeonReward", True, 0x012F, {"medallion": True, "item_id": 0x69}),
}

REWARD_COLORS: dict[str, str] = {
    "Kokiri Emerald": "Green",
    "Goron Ruby": "Red",
    "Zora Sapphire": "Blue",
    "Light Medallion": "Light Blue",
    "Forest Medallion": "Green",
    "Fire Medallion": "Red",
    "Water Medallion": "Blue",
    "Shadow Medallion": "Pink",
    "Spirit Medallion": "Yellow",
}
