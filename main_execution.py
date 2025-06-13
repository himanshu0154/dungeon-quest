import engine_main as game_engine
main_file_name = "character_info.json"

from characters_main import MainCharacter
from characters_main import Merchant
from characters_main import Orc
from characters_main import Skeleton
from characters_main import KoboldMonster
from characters_main import LizardMen
from characters_main import VampireLord

from skills_main import SwordCut
from skills_main import SwordHeal
from skills_main import SwordSlash
from skills_main import SwordStrike
from skills_main import StaminaHeal
from skills_main import FireBall
from skills_main import IceSpike
from skills_main import ArcaneShot
from skills_main import HealingLight
from skills_main import ManaHeal

from items_main import StaffOfWisdom
from items_main import TitanSlayer
from items_main import IronFangBlade
from items_main import KnightsEdge
from items_main import ArcaneOrb
from items_main import EnchantedCloak
from items_main import HealthPotion
from items_main import StaminaPotion
from items_main import ManaPotion
from items_main import KoboldStone
from items_main import SkeletonAsh
from items_main import LizardTail
from items_main import OrcMeat

from skills_main import RustyShiv
from skills_main import PocketFlame
from skills_main import RattleHex
from skills_main import BonePierce
from skills_main import TailWhip
from skills_main import VenomousSpit
from skills_main import Skullbreaker
from skills_main import BrutalSmash
from skills_main import CrimsonHowl
from skills_main import ShadowBurst
from skills_main import BloodDrain

class WrongClass(Exception):
    pass
class WrongStat(Exception):
    pass
class NotEnough(Exception):
    pass
class InvalidInput(Exception):
    pass

# This are the main character's skills as of now
sword_cut = SwordCut()
sword_strike = SwordStrike()
sword_slash = SwordSlash()
sword_heal = SwordHeal()
stamina_heal = StaminaHeal()

fire_ball = FireBall()
ice_spike = IceSpike()
arcane_shot = ArcaneShot()
healing_light = HealingLight()
mana_heal = ManaHeal()

# This are the monster's skills as of now 

rusty_shiv = RustyShiv()
pocket_flame = PocketFlame()
bone_pierce = BonePierce()
rattle_hex = RattleHex()
tail_whip = TailWhip()
venomous_spit = VenomousSpit()
brutal_smash = BrutalSmash()
skull_breaker = Skullbreaker()
blood_drain = BloodDrain()
crimson_howl = CrimsonHowl()
shadow_burst = ShadowBurst()

# These are the items 

iron_fang_blade = IronFangBlade()
knights_edge = KnightsEdge()
titan_slayer = TitanSlayer()
staff_of_wisdom = StaffOfWisdom()
arcane_orb = ArcaneOrb()
enchanted_cloak = EnchantedCloak()
health_potion = HealthPotion()
mana_potion = ManaPotion()
stamina_potion = StaminaPotion()
kobold_stone = KoboldStone()
skeleton_ash = SkeletonAsh()
lizard_tail = LizardTail()
orc_meat = OrcMeat()


items_list = {
    "Iron Fang Blade" : iron_fang_blade,
    "Knights Edge" : knights_edge,
    "Titan Slayer" : titan_slayer,
    "Staff of Wisdom" : staff_of_wisdom,
    "Arcane Orb" : arcane_orb,
    "Enchanted Cloak" : enchanted_cloak,
    "Health Potion" : health_potion,
    "Mana Potion" : mana_potion,
    "Stamina Potion" : stamina_potion,
    "Kobold Stone" : kobold_stone,
    "Skeleton's ash" : skeleton_ash,
    "Lizardmen's scales" : lizard_tail,
    "Orc Meat" : orc_meat
}

skill_list = {
    "Sword Cut" : sword_cut,
    "Sword Strike" : sword_cut,
    "Sword Slash" : sword_slash,
    "Sword Heal" : sword_heal,
    "Fire Ball" : fire_ball,
    "Ice Spike" : ice_spike,
    "Arcane Shot" : arcane_shot,
    "Healing Light" : healing_light,
    "Mana Heal" : mana_heal,
    "Stamina Heal" : stamina_heal
}

# Enemies
kobold = KoboldMonster()
skeleton = Skeleton()
lizardmen = LizardMen()
orc = Orc()
vampire_lord = VampireLord()


# Excecute the program
if __name__=="__main__":
    game_engine.starting_scene()
    chr_info = game_engine.load_file(main_file_name)
    if not chr_info or "name" not in chr_info:
        game_engine.create_character()
        chr_info = game_engine.load_file(main_file_name)

    main_character = MainCharacter.from_dict(chr_info)

    while True:
        restart = False
        if main_character.location is None:
            main_character.location = "Main Entrance"
            main_character.location_discovered.append(main_character.location)
            game_engine.save_to_file(main_file_name, main_character.to_dict())
            continue

        elif main_character.location == "Main Entrance":
            game_engine.safe_zones_menu(main_character, "Main Entrance", "First Route", "Kobold's Den", "Second Route", "Graveyard")
            if restart:
                continue

        elif main_character.location == "Kobold's Den":
            game_engine.Battle_rooms(main_character, "Kobold's Den", kobold, "Main Entrance", "Sanctuary of Solace")
            if restart:
                continue

        elif main_character.location == "Sanctuary of Solace":
            game_engine.safe_zones_menu(main_character, "Sanctuary of solace", "Kobold's Den", "Kobold's Den", "Next Room", "LizardMen's Lair")
            if restart:
                continue
        elif main_character.location == "LizardMen's Lair":
            game_engine.Battle_rooms(main_character, "LizardMen's Lair", lizardmen, "Sanctuary of Solace", "Chamber of the Forsaken")
            if restart:
                continue

        elif main_character.location == "Graveyard":
            game_engine.Battle_rooms(main_character, "Graveyard", skeleton, "Main Entrance", "The Whispering Hearth")
            if restart:
                continue

        elif main_character.location == "The Whispering Hearth":
            game_engine.safe_zones_menu(main_character, "The Whispering Hearth", "Graveyard", "Graveyard", "Next Room", "Orc Village")
            if restart:
                continue

        elif main_character.location == "Orc Village":
            game_engine.Battle_rooms(main_character, "Orc Village", orc, "The Whispering Hearth", "Chamber of the Forsaken")
            if restart:
                continue

        elif main_character.location == "Chamber of the Forsaken":
            if "Crimson Key" not in main_character.inventory:
                game_engine.boss_room_menu_no_key(main_character, "Chamber of the Forsaken", main_character.previous_room)
                if restart:
                    continue

            elif "Crimson Key" in main_character.inventory:
                if main_character.boss_defeated == "undefeated":
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
                    game_engine.save_to_file(main_file_name, main_character.to_dict())
                    if main_character.current_health == 0:
                        main_character.location = "Main Entrance"
                        game_engine.restore_stats(main_character)
                        game_engine.save_to_file(main_file_name, main_character.to_dict())
                        restart = True
                        
                    print("System : Silence falls like a curtain. The air grows still. Vehraxis the Crimson Wane... is no more.")
                    print("System : His body dissolves into crimson mist, leaving behind only ash and a faint whisper — 'Not... the end...'")

                    print("System : A distant echo — as if the dungeon itself exhales in relief.")
                    print("System : You feel a surge of power course through your veins. Something inside you... has changed.")

                    print("System : Boss Defeated!")
                    print(f"System : {main_character.name} has triumphed over the Crimson Wane and proven their might.")
                    print("System : The key fragment shimmers in the remains... you may now proceed.")
                    main_character.boss_defeated = "defeated"
                    game_engine.save_to_file(main_file_name, main_character.to_dict())
                    restart = True
                    if restart:
                        continue

                elif main_character.boss_defeated == "defeated":
                    print("Ravemir : ...So it is done.")
                    print("\t  The silence... it feels foreign. No more whispers in the dark corners of my helm.")
                    print("\t  You’ve shattered the curse that bound this threshold. Vehraxis is no more.")

                    print("Ravemir : I have waited lifetimes for a blade brave enough... a soul bold enough...")
                    print("\t  You are both.")
                    print("\t  Go now, bearer of fate. My watch is over.")

                    print("System : Ravemir lowers his halberd one final time. His armor crumbles into crimson dust, carried away by a wind that was never there before.")
                    main_character.boss_defeated = "story ends"
                    game_engine.save_to_file(main_file_name, main_character.to_dict())
                    restart = True
                    if restart:
                        continue
                
                elif main_character.boss_defeated == "story ends":
                    game_engine.boss_room_menu_end(main_character, "Chamber of the Forsaken", vampire_lord, "Orc Village", "LizardMen's Lair")
        
        if restart:
            continue


                