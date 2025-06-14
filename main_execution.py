"""
Main execution file for Dungeon Quest game.
Handles game loop, location management, and character progression.
"""

import engine_main as game_engine
from characters_main import (
    MainCharacter, Merchant, Orc, Skeleton, KoboldMonster, 
    LizardMen, VampireLord
)
from skills_main import (
    SwordCut, SwordHeal, SwordSlash, SwordStrike, StaminaHeal,
    FireBall, IceSpike, ArcaneShot, HealingLight, ManaHeal
)
from items_main import (
    StaffOfWisdom, TitanSlayer, IronFangBlade, KnightsEdge,
    ArcaneOrb, EnchantedCloak, HealthPotion, StaminaPotion,
    ManaPotion, KoboldStone, SkeletonAsh, LizardTail, OrcMeat
)

main_file_name = "character_info.json"


# Custom exception classes for game logic
class WrongClass(Exception):
    pass

class WrongStat(Exception):
    pass

class NotEnough(Exception):
    pass

class InvalidInput(Exception):
    pass


# Lookup dictionaries for inventory and skill management
items_list = {
    "Iron Fang Blade": IronFangBlade(),
    "Knight's Edge": KnightsEdge(),
    "Titan Slayer": TitanSlayer(),
    "Staff of Wisdom": StaffOfWisdom(),
    "Arcane Orb": ArcaneOrb(),
    "Enchanted Cloak": EnchantedCloak(),
    "Health Potion": HealthPotion(),
    "Mana Potion": ManaPotion(),
    "Stamina Potion": StaminaPotion(),
    "Kobold Stone": KoboldStone(),
    "Skeleton's ash": SkeletonAsh(),
    "Lizardmen's scales": LizardTail(),
    "Orc Meat": OrcMeat()
}

skill_list = {
    "Sword Cut": SwordCut(),
    "Sword Strike": SwordStrike(),
    "Sword Slash": SwordSlash(),
    "Sword Heal": SwordHeal(),
    "Fire Ball": FireBall(),
    "Ice Spike": IceSpike(),
    "Arcane Shot": ArcaneShot(),
    "Healing Light": HealingLight(),
    "Mana Heal": ManaHeal(),
    "Stamina Heal": StaminaHeal()
}


# Location configuration for game flow
LOCATION_CONFIG = {
    "Main Entrance": {
        "type": "safe_zone",
        "routes": {
            "First Route": "Kobold's Den",
            "Second Route": "Graveyard"
        }
    },
    "Kobold's Den": {
        "type": "battle",
        "monster": KoboldMonster,
        "previous": "Main Entrance",
        "next": "Sanctuary of Solace"
    },
    "Sanctuary of Solace": {
        "type": "safe_zone",
        "routes": {
            "Kobold's Den": "Kobold's Den",
            "Next Room": "LizardMen's Lair"
        }
    },
    "LizardMen's Lair": {
        "type": "battle",
        "monster": LizardMen,
        "previous": "Sanctuary of Solace",
        "next": "Chamber of the Forsaken"
    },
    "Graveyard": {
        "type": "battle",
        "monster": Skeleton,
        "previous": "Main Entrance",
        "next": "The Whispering Hearth"
    },
    "The Whispering Hearth": {
        "type": "safe_zone",
        "routes": {
            "Graveyard": "Graveyard",
            "Next Room": "Orc Village"
        }
    },
    "Orc Village": {
        "type": "battle",
        "monster": Orc,
        "previous": "The Whispering Hearth",
        "next": "Chamber of the Forsaken"
    }
}


def handle_boss_encounter(main_character):
    """Handle the boss encounter sequence."""
    print("System : The chamber trembles as you insert the Crimson Key...")
    print("System : The scent of iron fills the air. A cold presence watches you from the shadows.")

    monster = VampireLord()
    print("Vehraxis : Another breath-bound soul dares trespass... how quaint.")
    print("\t   Your scent betrays courage, but your eyes whisper fear.")
    print("Vehraxis : Do you think you are the first to raise steel against the Crimson Wane?")
    print("\t   Their bones paved my throne, and their names... forgotten.")
    print("Vehraxis : Come then. Bleed. Break. Belong.")
    print("\t   I'll sip your strength like vintage sorrow, and wear your heart like a medal.")
    
    game_engine.battle(main_character, monster)
    
    if main_character.current_health == 0:
        main_character.location = "Main Entrance"
        game_engine.restore_stats(main_character)
        return
        
    print("System : Silence falls like a curtain. The air grows still. Vehraxis the Crimson Wane... is no more.")
    print("System : His body dissolves into crimson mist, leaving behind only ash and a faint whisper — 'Not... the end...'")
    print("System : A distant echo — as if the dungeon itself exhales in relief.")
    print("System : You feel a surge of power course through your veins. Something inside you... has changed.")
    print("System : Boss Defeated!")
    print(f"System : {main_character.name} has triumphed over the Crimson Wane and proven their might.")
    print("System : The key fragment shimmers in the remains... you may now proceed.")
    
    main_character.boss_defeated = "defeated"


def handle_post_boss_victory(main_character):
    """Handle post-boss victory dialogue."""
    print("Ravemir : ...So it is done.")
    print("\t  The silence... it feels foreign. No more whispers in the dark corners of my helm.")
    print("\t  You've shattered the curse that bound this threshold. Vehraxis is no more.")
    print("Ravemir : I have waited lifetimes for a blade brave enough... a soul bold enough...")
    print("\t  You are both.")
    print("\t  Go now, bearer of fate. My watch is over.")
    print("System : Ravemir lowers his halberd one final time. His armor crumbles into crimson dust, carried away by a wind that was never there before.")
    
    main_character.boss_defeated = "story ends"


def handle_location(main_character, location):
    """Handle location-specific logic using configuration."""
    config = LOCATION_CONFIG.get(location)
    
    if not config:
        return handle_special_location(main_character, location)
    
    if config["type"] == "safe_zone":
        routes = config["routes"]
        route_keys = list(routes.keys())
        game_engine.safe_zones_menu(
            main_character, location, 
            route_keys[0], routes[route_keys[0]],
            route_keys[1], routes[route_keys[1]]
        )
    elif config["type"] == "battle":
        monster = config["monster"]()
        game_engine.Battle_rooms(
            main_character, location, monster,
            config["previous"], config["next"]
        )


def handle_special_location(main_character, location):
    """Handle special locations like the boss room."""
    if location == "Chamber of the Forsaken":
        if "Crimson Key" not in main_character.inventory:
            game_engine.boss_room_menu_no_key(main_character, location, main_character.previous_room)
        elif main_character.boss_defeated == "undefeated":
            handle_boss_encounter(main_character)
        elif main_character.boss_defeated == "defeated":
            handle_post_boss_victory(main_character)
        elif main_character.boss_defeated == "story ends":
            game_engine.boss_room_menu_end(main_character, location, VampireLord(), "Orc Village", "LizardMen's Lair")


# Main game execution
if __name__ == "__main__":
    # Load or create character data
    chr_info = game_engine.load_file(main_file_name)
    if not chr_info or "name" not in chr_info:
        game_engine.starting_scene()
        game_engine.create_character()
        chr_info = game_engine.load_file(main_file_name)

    main_character = MainCharacter.from_dict(chr_info)

    # Main game loop
    while True:
        # Set initial location if character is new
        if main_character.location is None:
            main_character.location = "Main Entrance"
            main_character.location_discovered.append(main_character.location)
            game_engine.save_to_file(main_file_name, main_character.to_dict())
            continue

        # Handle current location
        handle_location(main_character, main_character.location)
        game_engine.save_to_file(main_file_name, main_character.to_dict())