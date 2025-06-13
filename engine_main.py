from characters_main import MainCharacter
from characters_main import Merchant
from characters_main import DescriptiveNPC
from characters_main import Orc
from characters_main import Skeleton
from characters_main import KoboldMonster
from characters_main import LizardMen

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
from items_main import CrimsonFang
from items_main import CrimsonKey

from skills_main import RustyShiv
from skills_main import PocketFlame
from skills_main import RattleHex
from skills_main import BonePierce
from skills_main import TailWhip
from skills_main import VenomousSpit
from skills_main import Skullbreaker
from skills_main import BrutalSmash

import pandas as pd
import json
import random
import sys
import os

class WrongClass(Exception):
    pass
class WrongStat(Exception):
    pass
class NotEnough(Exception):
    pass
class InvalidInput(Exception):
    pass
# ======================================= File Handling ==================================================================

# This is the main data file which saves the Main Characters information
main_file_name = 'character_info.json'
# This is the skill file that saves skills info
skill_file_name = 'skills_info.json'


# This Func loads the json file 
def load_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            json.dump({}, file)  # Create an empty JSON file

    with open(file_name, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}  # Return empty dict if file is corrupted

# This function saves data to the JSON file
def save_to_file(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

# ====================================================== Starting scene =============================================================

def starting_scene():
    print("\n" + "="*50)
    print("            WELCOME TO DUNGEON QUEST")
    print("="*50 + "\n")
    print("You find yourself standing at the entrance of a dark and mysterious dungeon.")
    print("Two paths lie ahead of you:")
    print("  1) The winding, eerie tunnels of the Kobold Den.")
    print("  2) The chilling silence of the Graveyard.")
    print("\nWill you dare to choose your path and face the dangers within?\n")
    print("Prepare yourself, hero... Your quest begins now!\n")
    print("="*50 + "\n")


# ================================================= Create a new character ====================================================

# This func helps to create a new character if there isnt any available yet
def create_character():
    name = input("System : Select a name for your character - ") 
    while True:
        try:
            character_class = input("System : Select a name for your character (Mage/Swordsmen) - ") 
            if character_class.lower() in ["mage", "swordsman"]:
                break
            else:
                raise WrongClass("Please choose a class from the given option")
        except WrongClass as c:
            print(f"Error : {c}")
    character = MainCharacter(name, character_class) # Update the json file 
    if character.character_class == "mage":
        character.intelligence += 5
        character.max_mana += 100
        character.current_mana += 100
        skill = {"Fire Ball"}
        character.skills = list(skill)
    if character.character_class == "swordsman":
        character.strength += 5
        character.max_stamina += 100
        character.current_stamina += 100
        skill = {"Sword Slash"}
        character.skills = list(skill)
    save_to_file(main_file_name, character.to_dict())
    print("System : New Character successfully created !!")


# ======================================================= Display =============================================================

def display_syswindow(main_character):
    print("          --------------------------------------------------------------")
    print(str(main_character))
    print("          --------------------------------------------------------------")

def display_max_stats(main_character):
    print("          ----------------------------------------------")
    print(f"System : | Name : {main_character.name}",
            f"\n\t | Class : {main_character.character_class}\t\tHealth : {main_character.max_health}",
            f"\n\t | Strength : {main_character.strength}\t\tIntelligence : {main_character.intelligence}",
            f"\n\t | Stamina : {main_character.max_stamina}\t\tMana : {main_character.max_mana}\n\t | Stat Points : {main_character.stat_points}")
    print("          ----------------------------------------------")

def display_stats(main_character):
    print("          ----------------------------------------------")
    print(f"System : | Name : {main_character.name}",
            f"\n\t | Class : {main_character.character_class}\t\tHealth : {main_character.current_health}",
            f"\n\t | Strength : {main_character.strength}\t\tIntelligence : {main_character.intelligence}",
            f"\n\t | Stamina : {main_character.current_stamina}\t\tMana : {main_character.current_mana}\n\t | Stat Points : {main_character.stat_points}")
    print("          ----------------------------------------------")

def display_monsters_stats(Monster):
    print("          ----------------------------------------------")
    print(Monster)
    print("          ----------------------------------------------")

def display_skills_info(main_character):
    for i,  skill in enumerate(main_character.skills, 1):
        print("System : Which skill do you wanna use - ")
        skill_info = skill_list[skill]
        print(f"\t{i}. {skill_info}")




# ======================================================== Object defined =====================================================

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
crimson_fang = CrimsonFang()
crimson_key = CrimsonKey()

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
    "Orc Meat" : orc_meat,
    "Crimson Fang" : crimson_fang,
    "Crimson Key" : crimson_key
}

status_effects_list = {
    "Bleed" : rusty_shiv,
    "Burn" : pocket_flame,
    "Poison" : venomous_spit,
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

# ======================================================== LVL up system ========================================================

# This dict gives the stats and exp given and required respectively during and for the level up respectively
stat_exp_cap = {
    1 : [10, 100],
    2 : [13, 200],
    3 : [15, 250],
    4 : [17, 450],
    5 : [20, 600]
}

# This func levels up the character when the exp reaches a certain point
def lvlup(main_character):
    while True:
        stat_point = stat_exp_cap[main_character.lvl][0]
        exp_cap_lvl = stat_exp_cap[main_character.lvl][1]
        if main_character.experience >= exp_cap_lvl: 
            if main_character.lvl >= 5:
                main_character.experience -= exp_cap_lvl
                main_character.stat_points += stat_point
                print("System : You're level is maxed out!!")
            else:
                main_character.lvl += 1
                main_character.experience -= exp_cap_lvl
                main_character.stat_points += stat_point
                print("System : You leveled up!!!")
            
            print(f"System : Stat gained {stat_point}")

            save_to_file(main_file_name, main_character.to_dict())
        else:
            return


# ======================================================== Stat distribution ===================================================


# This func is for stat distribution
def stat_distribute(main_character):
    while True:
        try:
            if main_character.stat_points == 0:
                raise NotEnough("System : No available stat points for distribution")
            display_max_stats(main_character)
            while True:
                stats_dict = {
                    1 : "Strength",
                    2 : "Intelligence",
                    3 : "Mana",
                    4 : "Stamina",
                    5 : "Health",
                    6 : "Exit"         
                }
                print("System : Which stat do you want to improve -")
                for key, value in stats_dict.items():
                    print(f"\t{key}. {value}")
                try:
                    index = int(input(f"{main_character.name}  : "))
                    if index in stats_dict.keys():
                        try:
                            stat_increase = int(input(f"System : How much do you want to put in {stats_dict[index]} - "))
                            if stat_increase > main_character.stat_points:
                                raise NotEnough(f"System : Not enough Stat points for distribution")
                            else:
                                if index == 1:
                                    main_character.strength += stat_increase
                                elif index == 2:
                                    main_character.intelligence += stat_increase
                                elif index == 3:
                                    main_character.current_mana += stat_increase
                                elif index == 4:
                                    main_character.current_stamina +=  stat_increase
                                elif index == 5:
                                    main_character.current_health += stat_increase
                                elif index == 6:
                                    print("System : Returning to main interface...")
                                    return
                                main_character.stat_points -= stat_increase
                                save_to_file(main_file_name, main_character.to_dict())
                                print(f"System : attribute {stats_dict[index]} increased by {stat_increase}")
                                break
                        except NotEnough as ne:
                            print(ne)
                        except ValueError:
                            print("System: Allocation failed. Please input a valid number of points")
                    else:
                        raise WrongStat("System: No such attribute exists")
                except ValueError:
                        print(f"System: Allocation failed. Please input a valid int value")
                except WrongStat as ws:
                    print(ws)      
        except NotEnough as ne:
            print(ne)  
            return    

# ======================================================== Skills equisition ===================================================

# Gives out skills as per the required level
def Skill_equisition(main_character):
    new_skills = set(main_character.skills)  # start with existing skills

    if main_character.character_class.lower() == "swordsman":
        if main_character.lvl >= 1:
            new_skills.add(sword_cut.name)
        if main_character.lvl >= 2:
            new_skills.add(stamina_heal.name)
        if main_character.lvl >= 3:
            new_skills.add(sword_slash.name)
        if main_character.lvl >= 4:
            new_skills.update([sword_strike.name, sword_heal.name])
    else:
        if main_character.lvl >= 1:
            new_skills.add(fire_ball.name)
        if main_character.lvl >= 2:
            new_skills.add(mana_heal.name)
        if main_character.lvl >= 3:
            new_skills.add(ice_spike.name)
        if main_character.lvl >= 4:
            new_skills.update([arcane_shot.name, healing_light.name])

    added = new_skills - set(main_character.skills) # skills that are just added means are new
    main_character.skills = list(new_skills) # converting set to list

    for skill in added:
        print(f"System : You gained {skill}!") # showing only newly added skills

    save_to_file(main_file_name, main_character.to_dict())  # Save right after

# ======================================================== Skills level up ===================================================

# Func to act as a frame work to upgrade specific skill
def update_specific_skill(skill_name, **updates): # takes skill name and a dict - stats you want to level up as an argument
    skill_info = load_file(skill_file_name)
    
    if skill_name not in skill_info:
        print(f"System : Skill '{skill_name}' not found!")
        return

    for key, value in updates.items():
        if key in skill_info[skill_name]:
            skill_info[skill_name][key] = value # in the skill info the skill with the name skill_name make its chosen key equal to value
        else:
            print(f"System : '{key}' not found in '{skill_name}' data!")
    print(f"System : {skill_name} leveled up !!")

    save_to_file(skill_file_name, skill_info)

# Func to level up skills when reached a certain level
def skills_level_up(main_character):
    if main_character.character_class.lower() == "mage":
        if main_character.lvl == 3:
            update_specific_skill("Fire Ball", **{"level" : 2, "Attack" : 30})
            update_specific_skill("Mana Heal", **{"level" : 2, "Mana heal" : 50})

        if main_character.lvl == 4:
            update_specific_skill("Fire Ball", **{"level" : 3, "Attack" : 40, "Stamina usage" : 35})
            update_specific_skill("Ice Spike", **{"level" : 2, "Attack" : 20})

        if main_character.lvl == 5:
            update_specific_skill("Mana Heal", **{"level" : "Max", "Mana heal" : 70, "Health usage" : 30})
            update_specific_skill("Fire Ball", **{"level" : "Max", "Attack" : 50, "Stamina usage" : 40})
            update_specific_skill("Ice Spike", **{"level" : "Max", "Attack" : 30, "Stamina usage" : 20})
            update_specific_skill("Arcane Shot", **{"level" : 2, "Attack" : 35})
            update_specific_skill("Healing Light", **{"level" : 2, "Heal" : 70, "Stamina usage" : 40})
    else:
        if main_character.lvl == 3:
            update_specific_skill("Stamina Heal", level=2, stamina_heal=50)
            update_specific_skill("Sword Cut", level=2, Attack=10)

        if main_character.lvl == 4:
            update_specific_skill("Sword Cut", **{"level" : 3, "Attack" : 20, "Stamina usage" : 10})
            update_specific_skill("Sword Slash", **{"level" : 2, "Attack" : 25})

        if main_character.lvl == 5:
            update_specific_skill("Stamina Heal", **{"level" : "Max", "Stamina heal" : 70, "Health usage" : 30})
            update_specific_skill("Sword Cut", **{"level" : "Max", "Attack" : 25, "Stamina usage" : 15})
            update_specific_skill("Sword Slash", **{"level" : "Max", "Attack" : 35, "Stamina usage" : 20})
            update_specific_skill("Sword Strike", **{"level" : 2, "Attack" : 35})
            update_specific_skill("Sword Cut", **{"level" : 2, "Heal" : 60, "Stamina usage" : 25})



# ======================================================== Merchant Npc ===============================================================

# ======================================================== Buy from Merchant ===========================================================

# This is the func to buy from merchant
def buy_from_merchant(main_character):
    merchant = Merchant() 
    try:
        user = int(input(f"{main_character.name} :  "))
        if user in merchant.goods.keys(): 
            if main_character.character_class == merchant.goods[user].class_required or merchant.goods[user].class_required == None:
                try:
                    if main_character.gold >= merchant.goods[user].price:
                        main_character.inventory.append(f"{merchant.goods[user].name}")
                        main_character.gold -= merchant.goods[user].price
                        save_to_file(main_file_name, main_character.to_dict())
                        print(f"system : Successfully purchased {merchant.goods[user].name}")
                    else:
                        raise NotEnough("You dont have enough gold to buy this item!")
                except NotEnough as ne:
                    print(f"Error : {ne}")
                    return
            else:
                print("System : you dont meet the the class requirement!")
                return  
        else:
            raise InvalidInput("The merchant raises an eyebrow. That's not something I'm selling.")
    except InvalidInput as i:
        print(f"System : {i}")
    except ValueError:
        print(f"System: Allocation failed. Please input a valid number of points")

# ================================================ Sell to Merchant ====================================================================

# This is the func to sell to the merchant
def sell_to_merchant(main_character):
    item_dict = {} # to save item obj as value 
    print("Merchant : Okay, let me look at your stuff then")
    if not main_character.inventory:
        print("Merchant : Looks like you're traveling light. Nothing to sell, eh?")
        print("Merchant : No worries, just come back when you got something for me.")
        return
    print(f"{main_character.name} :  These are the items, I have -")
    for i, item in enumerate(main_character.inventory, 1):
            if item == "Crimson Key":
                continue
            item = items_list[item]
            item_dict[i] = item
            print(f"\t{i}. {item.name} - {item.price} gold")
    print("Merchant : hmm, what do you wanna sell?")
    try : 
        user = int(input(f"{main_character.name} :  "))
        if user in item_dict.keys():
            print("Merchant : Are you sure?")
            print("\t1. Yes\n\t2. No")  
            try:
                user_response = int(input(f"{main_character.name} :  "))
                if user_response == 1:
                    main_character.gold += item_dict[user].price
                    main_character.inventory.remove(f"{item_dict[user].name}")
                    print(f"System : Successfully sold {item_dict[user].name}")
                    save_to_file(main_file_name, main_character.to_dict())
                elif user_response == 2:
                    print("Merchant : Okay, well. see you around!")
                    return
                else:
                    raise InvalidInput("The merchant raises an eyebrow. Please give a valid input")
            except InvalidInput as ie:
                print(f"System : {ie}")
            except ValueError:
                print("System : The merchant stares at your strange words. please give a int value")
        else: 
            raise InvalidInput("The merchant raises an eyebrow. Please give a valid input")
    except InvalidInput as ie:
        print(f"System : {ie}")
    except ValueError:
        print("System : The merchant stares at your strange words. please give a int value")

# ================================================== Merchant NPC main program ==========================================================

# Main merchant execution program
def merchant_npc(main_character):
    while True:
        merchant_convo_choice = {
            1 : "Hello, whats up",
            2 : "Can you show me your goods?",
            3 : "I wanna sell some suff",
            4 : "Bye!"
        }
        merchant = Merchant() 
        print(f"System : This is {merchant.occupation} {merchant.name}, always eager to sell something !!")
        for key , value in merchant_convo_choice.items():
            print(f"\t{key} - {value}")
        try:
            user = int(input(f"{main_character.name} : "))
            if user == 1 :
                print("Merchant : nothing much, what about you ?")
            elif user == 2:
                print("Merchant : Oh sure, why not? Dear customer!")
                merchant.show_items()
                while True:
                    print(f"Merchant : do you wanna buy something?\t\t Gold available - {main_character.gold}")
                    print("\t1. Yes\n\t2. No")
                    try:
                        user_response = int(input(f"{main_character.name} :  "))
                        if user_response == 1:
                            print(f"Merchant : What do you wanna buy ?")
                            buy_from_merchant(main_character)
                            break
                        elif user_response == 2:
                            print("Merchant : Okay, have a nice day")
                            break
                        else:
                            raise InvalidInput("Merchant Todd narrows his eyes. That option doesnt exist, traveler. Speak clearly — 1 or 2.")
                    except InvalidInput as i:
                        print(f"System : {i}")
                    except ValueError:
                        print("System :Merchant Todd frowns. Words are fine, but I need a number this time — 1 or 2.")
            elif user == 3: 
                sell_to_merchant(main_character)
            elif user == 4:
                print("Merchant : Bye, have a good day!")
                return
            else: 
                raise InvalidInput("Merchant Todd looks confused. Try choosing a valid option")
        except InvalidInput as i:
            print(f"System : {i}")
        except ValueError:
            print("System : Input invalid. Only numerical commands are accepted")

# ======================================================== Battle ===============================================================

# this is the func to use weapon
def use_weapon(main_character, weapon):
    main_character.weapon = weapon.name
    print(f"System : You are using {weapon.name}")
    main_character.intelligence += weapon.intelligence_increase
    main_character.current_health += weapon.heal
    main_character.current_mana += weapon.mana_replenish
    main_character.strength += weapon.attack_increase
    main_character.current_stamina += weapon.stamina_replenish
    if weapon.class_required ==  "mage":
        print(f"System : Your Intelligence Temporarily increased by {weapon.intelligence_increase}")
        print(f"System : Your Mana temporarily increased by {weapon.mana_replenish}")
        print(f"System : Your Health temporarily increased by {weapon.heal}")
    elif weapon.class_required == "swordsman": 
        print(f"System : Your Strength Temporarily increased by {weapon.attack_increase}")
        print(f"System : Your Stamina temporarily increased by {weapon.stamina_replenish}")
        print(f"System : Your Health temporarily increased by {weapon.heal}")
    save_to_file(main_file_name, main_character.to_dict())

# This is the func to unequip the weapon after the battle
def unequip_weapon(main_character, weapon):
    print(f"System : Unequipping {weapon.name}")
    main_character.intelligence -= weapon.intelligence_increase
    main_character.current_mana -= weapon.mana_replenish
    main_character.strength -= weapon.attack_increase
    main_character.current_stamina -= weapon.stamina_replenish
    if weapon.class_required ==  "mage":
        print(f"System : Your Intelligence decreased by {weapon.intelligence_increase}")
        print(f"System : Your Mana decreased by {weapon.mana_replenish}")
    elif weapon.class_required == "swordsman": 
        print(f"System : Your Strength decreased by {weapon.attack_increase}")
        print(f"System : Your Stamina decreased by {weapon.stamina_replenish}")
    main_character.weapon = None
    save_to_file(main_file_name, main_character.to_dict())

# This is the func to use the potion
def use_Potion(main_character, potion):
    print(f"System : You used a {potion.name}")
    if potion.name == "Health Potion":
        main_character.current_health += potion.heal
        print(f"System : Your Health increased by {potion.heal} ")
        main_character.inventory.remove(potion.name)
    elif potion.name == "Stamina Potion":
        main_character.current_stamina += potion.stamina_replenish
        print(f"System : Your Stamina increased by {potion.stamina_replenish} ")
        main_character.inventory.remove(potion.name)
    elif potion.name == "Mana Potion":
        main_character.current_mana += potion.mana_replenish
        print(f"System : Your Mana increased by {potion.mana_replenish} ")
        main_character.inventory.remove(potion.name)
    else:
        print("System : This option is not available yet")
    save_to_file(main_file_name, main_character.to_dict())

# This is the func to choose the weapon
def choose_weapon(main_character):
    item_dict = {}
    while True:
        print("System : These are the weapons, you currently owns - ")
        j = 1
        for i, item in enumerate(main_character.inventory, 1):
            if item == "Crimson Key":
                continue
            item_obj = items_list[item]
            if item_obj.class_of_weapon == "drop":
                continue
            item_dict[i] = item_obj
            j += 1
            print(f"\t{i}. {item_obj.name}")
        print(f"\t{j}. unarmed")
        if not item_dict:
            print("System : No weapon available!")
            return
        try:
            user = int(input(f"{main_character.name} :  "))
            if user == j:
                print("System : proceeding unarmed")
                return
            elif user in item_dict.keys():
                weapon = items_list[item_dict[user].name]
                if weapon.class_of_weapon == "weapon":
                    use_weapon(main_character, weapon)
                    return
                elif weapon.class_of_weapon == "potion":
                    use_Potion(main_character, weapon)
                else:
                    print("System : This option is not available yet!")
            else:
                print("System : No such weapon exist.")
        except InvalidInput:
            print("System : Hurry up, its not time to play around. choose a valid input")
        except ValueError:
            print("System : Hurry up, its not time to text now. Choose a valid int input")

# this is the func which helps the monster use skills
def use_skill_by_monster(skill, main_character,  monster):
        main_character.current_health -= skill.attack
        if main_character.current_health <= 0:
            main_character.current_health = 0
        print(f"System : {monster.name} used {skill.name}!")
        print(f"System : You are struck by {monster.name}'s {skill.name} and loses {skill.attack} Health!")
        if skill.status_effect:
            if main_character.status_effect is None and random.random() < skill.status_apply_chance:
                main_character.status_effect = skill.status_effect
                main_character.status_duration = skill.status_effect_duration
                print(f"System : You are afflicted with {skill.status_effect} for {skill.status_effect_duration} turns!")
            else:
                print(f"System : You resisted the status effect!")

# This is the func that helps the user to use skill 
def user_skill_by_user(skill, main_character, monster):
    if skill.name in ["Sword Heal", "Stamina Heal", "Healing Light", "Mana Heal"]:
        if skill.heal > 0:
            if main_character.character_class ==  "mage":
                if main_character.current_mana >= skill.mana_usage:
                    main_character.current_health += skill.heal
                    print(f"System : Health restored by {skill.heal}")
                    main_character.current_mana -= skill.mana_usage
                    print(f"System : Mana dropped by {skill.mana_usage}") 

                else:
                    print(f"System : Not enough Mana to use {skill.name}")

            elif main_character.character_class == "swordsman":
                if main_character.current_stamina >= skill.stamina_usage:
                    main_character.current_health += skill.heal
                    print(f"System : Health restored by {skill.heal}")
                    main_character.current_stamina -= skill.stamina_usage
                    print(f"System : Stamina dropped by {skill.stamina_usage}")
                else:
                    print(f"System : Not enough stamina to use {skill.name}")

        elif skill.mana_heal > 0:
            if main_character.current_health > skill.health_usage + 20:
                main_character.current_mana += skill.mana_heal
                print(f"System : mana restored by {skill.mana_heal}")
                main_character.current_health -= skill.health_usage
                print(f"System : Health dropped by {skill.health_usage}")

        elif skill.stamina_heal > 0:
            if main_character.current_health > skill.health_usage + 20:
                main_character.current_stamina += skill.stamina_heal
                print(f"Stamina recovered by {skill.stamina_heal}")
                main_character.current_health -= skill.health_usage
                print(f"System : Health dropped by {skill.health_usage}")
        else:
            print("System : This feature is not available yet")

    else:
        if main_character.character_class == 'mage':
            if main_character.current_mana >= skill.mana_usage:
                monster.health -= skill.attack + main_character.intelligence
                main_character.current_mana -= skill.mana_usage
                print(f"System : You used {skill.name} ")
                print(f"System : Mana dropped by {skill.mana_usage}")
                print(f"System : {monster.name} is hit by {skill.name}. It grunts in pain. (-{skill.attack + main_character.intelligence} HP)")
            else:
                print(f"System : Not enough Mana to use {skill.name}")

        elif main_character.character_class == 'swordsman':
            if main_character.current_stamina >= skill.stamina_usage:
                monster.health -= skill.attack + main_character.strength
                main_character.current_stamina -= skill.stamina_usage
                print(f"System : You used {skill.name} ")
                print(f"System : Stamina dropped by {skill.stamina_usage}")
                print(f"System : {monster.name} is hit by {skill.name}. It grunts in pain. (-{skill.attack + main_character.strength} HP)")
            else:
                print("System : This feature is not available yet")
    save_to_file(main_file_name, main_character.to_dict())

# This is the func to apply status effect   
def status_effect_apply(main_character):
    if main_character.status_effect:
        skill = status_effects_list[main_character.status_effect]
        print(f"System : You are affected by {main_character.status_effect}! ({main_character.status_duration} turns left)")
        
        if main_character.status_effect:
            main_character.current_health -= skill.status_effect_damage
            if main_character.current_health <= 0:
                main_character.current_health = 0
            print(f"System : You takes {skill.status_effect_damage} {skill.status_effect} damage! Health is now {main_character.current_health}")

        main_character.status_duration -= 1        

        if main_character.status_duration <= 0:
            print(f"System : You are no longer affected by {main_character.status_effect}.")
            main_character.status_effect = None
            main_character.status_duration = 0
    else:
        print(f"System : You are not under any status effect.")
    save_to_file(main_file_name, main_character.to_dict())

# This is the func to intitiate battle 
def battle(main_character, Monster):
    print(f"System : You have encountered a {Monster.name}")
    choose_weapon(main_character)
    display_stats(main_character)
    display_monsters_stats(Monster)
    while main_character.current_health > 0 and Monster.health > 0:
        if main_character.current_health > 0 and Monster.health > 0:
            skill_dict = {}
            print("System : Choose a skill to attack!!")
            for i , skill in enumerate(main_character.skills, 1):
                skill_dict[i] = skill
                print(f"\t{i}. {skill}")
            while True:
                try:
                    user_skill_select = int(input(f"{main_character.name} :  "))
                    if user_skill_select in skill_dict.keys():
                        skill_use = skill_list[skill_dict[user_skill_select]]
                        user_skill_by_user(skill_use, main_character,  Monster)
                        status_effect_apply(main_character)
                        display_monsters_stats(Monster)
                        save_to_file(main_file_name, main_character.to_dict())
                        break
                    else:
                        raise InvalidInput("System : No Such skill exist!! Choose a skill!!")
                except ValueError:
                    print("System : its not time to play around, be serioius and put in a valid int input! Choose a skill!!")
                except InvalidInput as i:
                    print(i)
            if main_character.current_health > 0 and Monster.health > 0:
                skill = random.choice(Monster.skills)
                use_skill_by_monster(skill, main_character,  Monster)
                status_effect_apply(main_character)
                display_stats(main_character)
                save_to_file(main_file_name, main_character.to_dict())

    if main_character.current_health <= 0:
        print("System : Your health reached 0. You died")
        print("System : Returning to the Main Entrace....")
    else:
        print(f"System : You defeated the {Monster.name}")
        print(f"System : {Monster.name} dropped {Monster.drop}")
        main_character.inventory.append(Monster.drop)
        main_character.status_effect = None
        main_character.status_duration = 0
        print(f"System : You gained {Monster.exp} exp")
        main_character.experience += Monster.exp
        print(f"System : Putting {Monster.drop} in the Inventory ..... done.")
        save_to_file(main_file_name, main_character.to_dict())
        lvlup(main_character)
        Skill_equisition(main_character)
        skills_level_up(main_character)
        if main_character.weapon is None:
            pass
        else:
            weapon = items_list[main_character.weapon]
            unequip_weapon(main_character, weapon)
    save_to_file(main_file_name, main_character.to_dict())


# ========================================================= Check Inventory ===================================================

# Func to check the inventory
def check_inventory(main_character):
    if main_character.inventory:
        print("System : Opening the inventory...... opened.")
        item_dict = {}
        while True:
            print("System : these are the items in your inventory - ")
            for i, item in enumerate(main_character.inventory, 1):
                item_dict[i] = item
                print(f"\t {i}. {item}")
            print("System : Enter 1 to check item's description\n\t Enter 2 to close the inventory")
            try:
                user = int(input(f"{main_character.name} :  "))
                if user in [1, 2]:
                    if user == 1:
                        print("System : Enter the weapon you want to view - ")
                        user_request = int(input(f"{main_character.name} :  "))
                        view_item = items_list[item_dict[user_request]]
                        print(view_item)
                    else:
                        print("System : Closing the inventory.... closed.")
                        return
                else:
                    raise InvalidInput("System : Not a valid option. Try Again!")
            except InvalidInput as i:
                print(i)
            except ValueError:
                print("System : Not a Valid input. Try a int value!")

    else:
        print("System : Your inventory is empty")
        print("System : closing the Inventory..... closed.")

# Func to check the skills
def check_skills(main_character):
    if main_character.skills:
        print("System : loading the skills.... loaded.")
        skill_dict = {}
        while True:
            print("System : these are the skills in your arsenal - ")
            for i, skill in enumerate(main_character.skills, 1):
                skill_dict[i] = skill
                print(f"\t {i}. {skill}")
            print("System : Enter 1 to check skill's description\n\t Enter 2 to close the skill section")
            try:
                user = int(input(f"{main_character.name} :  "))
                if user in [1, 2]:
                    if user == 1:
                        print("System : Enter the skill you want to view - ")
                        user_request = int(input(f"{main_character.name} :  "))
                        view_skill = skill_list[skill_dict[user_request]]
                        print(view_skill)
                    else:
                        print("System : Closing the aresenal.... closed.")
                        return
                else:
                    raise InvalidInput("System : Not a valid option. Try Again!")
            except InvalidInput as i:
                print(i)
            except ValueError:
                print("System : Not a Valid input. Try a int value!")

    else:
        print("System : You dont own any skill yet")
        print("System : closing the arsenal..... closed.")


# Func to restore health when the user die or rest in safe zones   
def restore_stats(main_character):
    main_character.current_health = main_character.max_health
    main_character.current_mana = main_character.max_mana
    main_character.current_stamina = main_character.max_stamina
    print("System: You settle down by the flickering light of the safe zone.",
        "\nSystem: As your eyes close, a gentle aura surrounds you...",
        "\nSystem: HP, Mana, and Stamina fully restored.",
        "\nSystem: You awaken feeling refreshed and ready for adventure!")
    save_to_file(main_file_name, main_character.to_dict())

# Open chest func
def chest(main_character):
    chest = ["Health Potion", "Mana Potion", "Stamina Potion", "Gold Bag"]
    loot = random.choice(chest)
    if loot == "Gold Bag":
        gold = random.randrange(100, 2001, 100)
        print(f"System : Inside, you discover: {gold} gold coins")
        main_character.gold += gold
        save_to_file(main_file_name, main_character.to_dict())
    else:
        main_character.inventory.append(loot)
        print(f"System : Inside, you discovered: {loot}")
        print("System : storing it in the inventory..... stored.")
        save_to_file(main_file_name, main_character.to_dict())

def open_chest(main_character):
    print("System : You found a mysterious chest")
    print("System : Opening the chest....")
    if main_character.location == "Kobold's Den":
        if "chest1 opened" not in main_character.chest:
            chest(main_character)
            main_character.chest.append("chest1 opened")
            save_to_file(main_file_name, main_character.to_dict())
        else:
            print("System : Its empty.")
    elif main_character.location == "LizardMen's Lair":
        if "chest2 opened" not in main_character.chest:
            chest(main_character)
            main_character.chest.append("chest2 opened")
            save_to_file(main_file_name, main_character.to_dict())
        else:
            print("System : Its empty.")
    elif main_character.location == "Graveyard":
        if "chest3 opened" not in main_character.chest:
            chest(main_character)
            main_character.chest.append("chest3 opened")
            save_to_file(main_file_name, main_character.to_dict())
        else:
            print("System : Its empty.")
    elif main_character.location == "Orc Village":
        if "chest4 opened" not in main_character.chest:
            chest(main_character)
            main_character.chest.append("chest4 opened")
            save_to_file(main_file_name, main_character.to_dict())
        else:
            print("System : Its empty.")
    elif main_character.location == "Chamber of the Forsaken":
        if "chest5 opened" not in main_character.chest:
            loot = random.randrange(2000, 5001, 1000)
            print(f"System : Inside, you discover: {loot} gold coins")
            main_character.gold += loot
            main_character.chest.append("chest5 opened")
            save_to_file(main_file_name, main_character.to_dict())
        else:
            print("System : Its empty")

# ===================================================== NPC funcs ==============================================================
# Descriptive npc funcs 
def descriptive_npc(main_character):
    NPC = DescriptiveNPC()
    if main_character.location == "Kobold's Den":
        print("System : In the dim glow of a flickering lantern stands a frail old man ",
        "\n\t draped in tattered robes. His eyes shimmer with the weight of forgotten years, ",
        "\n\t and his voice creaks like old wood.")
        print("System : I am Eldrin Hollowshade, Warden of Forgotten Paths, he murmurs. ",
              "\n\t These halls remember... and so do I.")
        while True:
            print("System : 1. Talk to Eldrin\n\t 2. Ask about Kobolds\n\t 3. Ask about the next room\n\t 4. Say bye to Eldrin")
            try:
                user_response = int(input(f"{main_character.name} :  "))
                if user_response == 1:
                    print("Eldrin : Ah... a traveler with curiosity in their step and blood on their boots. ",
                        "\n\t You've faced the Kobolds, haven't you? Brave… or foolish.")
                    continue
                elif user_response == 2:
                    print("Eldrin : The kobolds weren't always like this. There was order once. A priestess, I think. " 
                    "\n\t Or a curse. Hard to say when you've lived too long in the dark.")
                    continue
                elif user_response == 3:
                    print("Eldrin : If your bones still ache, take the left passage. There lies the Room of Sighs… they say even the walls rest there.")
                elif user_response == 4:
                    print("Eldrin : The deeper you go, the louder the past whispers. Listen well")
                    break
                else:
                    raise InvalidInput("Eldrin narrows his eyes. That option doesnt exist, traveler. Speak clearly — 1 or 2.")
            except InvalidInput as i:
                print(f"System : {i}")
            except ValueError:
                print("System :Eldrin frowns. Words are fine, but I need a number this time — 1 or 2.")
                
    elif main_character.location == "LizardMen's Lair":
        print("System : Ezirak is a half-human, half-reptilian sage who was exiled from the surface world centuries ago. "
        "\n\t He roams the LizardMen's Lair, gathering rare herbs and venomous glands to brew forbidden elixirs.")

        while True:
            print("System : 1. Talk to Ezirak\n\t 2. Ask about LizardMen\n\t 3. Ask about the next room\n\t 4. Say bye to Ezirak")
            try:
                user_response = int(input(f"{main_character.name} :  "))
                if user_response == 1:
                    print("Ezirak : Ahh... a soft-skinned wanderer in the pit of scaled secrets..."
                        "\n\t You may call me Ezirak the Moltwise, last of the Scaleborn Alchemists."
                        "\n\t I distill wisdom from venom and memory from bones..."
                        "\n\t What brings you, warmblood, to this forgotten coil of the world?")
                    continue
                elif user_response == 2:
                    print("Ezirak : The LizardMen weren't always beasts."
                        "\n\t They listened to whispers in the dark... now they molt with madness, not nature."
                        "\n\t Don’t follow their path. It's not scales they shed — it's their sanity..")
                    continue
                elif user_response == 3:
                    print("Eizark : Beyond that door? That's no room... it's a graveyard of glory")
                elif user_response == 4:
                    print("Ezirak : Stay sharp, wanderer. The lair remembers")
                    break
                else:
                    raise InvalidInput("Eizark narrows his eyes. That option doesnt exist, traveler. Speak clearly — 1 or 2.")
            except InvalidInput as i:
                print(f"System : {i}")
            except ValueError:
                print("System :Eizark frowns. Words are fine, but I need a number this time — 1 or 2.")

    elif main_character.location == "Graveyard":
        print("System : Vahl is a cloaked figure draped in tattered priestly robes, face hidden behind a cracked porcelain mask."
            "\n\t He tends to the forgotten graves and speaks to bones as though they whisper back.")

        while True:
            print("System : 1. Talk to Vahl\n\t 2. Ask about the skeletons\n\t 3. Ask about the next room\n\t 4. Say bye to Vahl")
            try:
                user_response = int(input(f"{main_character.name} :  "))
                if user_response == 1:
                    print("Vahl  : Another breath among the dead... curious."
                        "\n\t I am Vahl, last mourner of the Nameless."
                        "\n\t I keep watch so the buried do not forget they once lived.")
                    continue
                elif user_response == 2:
                    print("Vahl  : These skeletons remember pain but not peace."
                        "\n\t Bound by rage, not necromancy... they rise not for vengeance — but habit.")
                    continue
                elif user_response == 3:
                    print("Vahl  : This circle of stillness? It's the one breath the grave allows."
                    "\n\t No claws, no curses — just time... borrowed, not owned."
                    "\n\t Rest while the dead forget you're here.")
                elif user_response == 4:
                    print("Vahl  : Leave no shadow behind, wanderer. The dead count even those.")
                    break
                else:
                    raise InvalidInput("Vahl tilts his head. That number means nothing in the tongue of the dead.")
            except InvalidInput as i:
                print(f"System : {i}")
            except ValueError:
                print("System : Vahl sighs through his mask. 'Try numbers, not riddles, child.'")
    

    elif main_character.location == "Orc Village":
        print("System : Gorvak stands by the anvil where once he stood on the battlefield."
            "\n\t His tusks are chipped, his eyes sharper than ever. Smoke and steel cling to him like old war songs.")

        while True:
            print("System : 1. Talk to Gorvak\n\t 2. Ask about the Orcs\n\t 3. Ask about the next room\n\t 4. Say bye to Gorvak")
            try:
                user_response = int(input(f"{main_character.name} :  "))
                if user_response == 1:
                    print("Gorvak : Hmph... not many softskins brave these fires."
                        "\n\t I am Gorvak Ironsnout. Warchief no longer — I forge, not fight."
                        "\n\t But don't test me. My hammer still remembers your kind.")
                    continue
                elif user_response == 2:
                    print("Gorvak : The young ones howl and swing steel like it’s a game."
                        "\n\t They forget the cost. We weren’t always savages — once, we stood for something.")
                    continue
                elif user_response == 3:
                    print("Gorvak : Beyond that gate lies the Bloodfire Pit — where rage burns hotter than the forge."
                        "\n\t If you enter, leave your mercy behind.")
                elif user_response == 4:
                    print("Gorvak : Walk tall, outsider. Cowards die before the blade even falls.")
                    break
                else:
                    raise InvalidInput("Gorvak growls: 'Speak plain. 1, 2, 3, or be gone.'")
            except InvalidInput as i:
                print(f"System : {i}")
            except ValueError:
                print("System : Gorvak scowls. 'Bah! Words ain't steel. Try again with numbers.'")


    elif main_character.location == "Chamber of the Forsaken":
        if main_character.boss_defeated == "undefeated":
            print("System : You approach a motionless knight clad in rusted crimson armor, eyes glowing faint red beneath a shattered helm."
            "\n\t His massive halberd rests like a grave marker in front of the sealed boss door.")

            while True:
                print("System : 1. Talk to Ravemir\n\t 2. Ask for the Crimson Key\n\t 3. Ask about the boss\n\t 4. Say bye to Ravemir")
                try:
                    user_response = int(input(f"{main_character.name} : "))
                    if user_response == 1:
                        print("Ravemir : You tread where few dare, mortal. I am Ravemir — knight once, vowkeeper forever."
                            "\n\t  I guard the gate to Vehraxis's dominion… a place where blood dares not boil.")
                        continue

                    elif user_response == 2:
                        if "Crimson Key" in main_character.inventory:
                            print("Ravemir : The key is already yours, warmblood. Fate now lies ahead.")
                            continue
                        # Stat check condition here — customize as needed
                        if main_character.character_class == "mage":
                            if main_character.intelligence >= 10 and main_character.current_mana >= 50 and main_character.current_health >= 50:
                                print("Ravemir : Intellect... endurance... and life. You carry them well."
                                    "\n\t  Take the Crimson Key. May your courage outlast your heartbeat.")
                                main_character.inventory.append("Crimson Key")
                                save_to_file(main_file_name, main_character.to_dict())
                                continue
                            else:
                                print("Ravemir : Your soul is not yet forged for what lies beyond."
                                    "\n\t  Return when your body and mind rise above fear.")
                                continue
                        elif main_character.character_class == "swordsman":
                            if main_character.strength >= 10 and main_character.current_stamina >= 50 and main_character.current_health >= 50:
                                print("Ravemir : Strength… endurance... and life. You carry them well."
                                    "\n\t  Take the Crimson Key. May your courage outlast your heartbeat.")
                                main_character.inventory.append("Crimson Key")
                                save_to_file(main_file_name, main_character.to_dict())
                                continue
                            else:
                                print("Ravemir : Your soul is not yet forged for what lies beyond."
                                    "\n\t  Return when your body and mind rise above fear.")
                                continue

                    elif user_response == 3:
                        print("Ravemir : Vehraxis was once a prince — now, a plague with a crown."
                            "\n\t  He feasts not on blood alone, but on forgotten memories and broken wills."
                            "\n\t  If you fall, no song will find you.")
                        continue

                    elif user_response == 4:
                        print("Ravemir :  Steel your heart, wanderer. The Blood Gate watches.")
                        return

                    else:
                        raise InvalidInput("System : Ravemir does not flinch. 'Choose clearly, traveler — one path at a time.'")

                except InvalidInput as i:
                    print(f"System : {i}")
                except ValueError:
                    print("System : Ravemir's eyes narrow. 'Speak in numbers, not riddles.'")
        

    


# Func to exit program
def exit_program(main_character):
    while True:
        choice = input("System : Do you want to save your progress before exiting? (yes/no): ").strip().lower()
        if choice == "yes":
            save_to_file(main_file_name, main_character.to_dict())
            print("System : Progress saved successfully.")
            print("System : The dungeon grows quiet... until you return.")
            sys.exit()
        elif choice == "no":
            print("System : Your legacy will be lost... for now.")
            print("System : The shadows swallow your steps as you vanish into the mist.")
            with open("character_info.json", "w") as file:
                json.dump({}, file) # To delete the json files if user want to reset
            with open("skills_info.json", "w") as file:
                json.dump({}, file) # To delete the skills files
            sys.exit()
        else:
            print("System : Please type 'yes' or 'no'.")

# Merchant random spawns func
def merchant_spawn(main_character): 
    if main_character.current_health < 0.3 * main_character.max_health:
        merchant_spawn_rate = 0.4
        if random.random() < merchant_spawn_rate:
            print("System : You hear the jingling of coins and the rustling of satchels... A Merchant approaches!")
            merchant_npc(main_character)
        else:
            print("System : The silence continues... No help in sight.")
    else:
        merchant_spawn_rate = 0.1
        if random.random() < merchant_spawn_rate:
            print("System : You hear the jingling of coins and the rustling of satchels... A Merchant approaches!")
            merchant_npc(main_character)


def safe_zones_menu(main_character, name, first_route_name, first_room, second_route_name, second_room):
    print(f"System : === You have entered the {name} ===")
    while True:
        print("System : What would you like to do now?")
        print("\t1. Rest in the safe zone (restore HP, Mana, and Stamina)")
        print("\t2. Check Inventory")
        print("\t3. Check Skills")
        print("\t4. Open Status window")
        print("\t5. Distribute stat points")
        print(f"\t6. Proceed to the {first_route_name}")
        print(f"\t7. Proceed to the {second_route_name}")
        print("\t8. Exit game")
        try:
            user = int(input(f"{main_character.name} : "))
            if user == 1:
                restore_stats(main_character)
                continue
            elif user == 2:
                check_inventory(main_character)
                continue
            elif user == 3:
                check_skills(main_character)
                continue
            elif user == 4:
                display_syswindow(main_character)
            elif user == 5:
                stat_distribute(main_character)
            elif user == 6:
                if first_room not in main_character.location_discovered:
                    print(f"System: You step into unfamiliar territory... {first_room} added to map.")
                    main_character.location_discovered.append(first_room)
                main_character.location = first_room
                save_to_file(main_file_name, main_character.to_dict())
                restart = True
                break
            elif user == 7:
                if second_room not in main_character.location_discovered:
                    print(f"System: You step into unfamiliar territory... {second_room} added to map.")
                    main_character.location_discovered.append(second_room)
                main_character.location = second_room
                save_to_file(main_file_name, main_character.to_dict())
                restart = True
                break
            elif user == 8:
                exit_program(main_character)
            else:
                raise InvalidInput("System: That didn't work. Try selecting a valid choice.")
        except InvalidInput as i:
            print(i)
        except ValueError:
            print("System : Invalid input, Try again!!")
    
def Battle_rooms(main_character, name, monster, previous_room, next_room):
    merchant_spawn(main_character)
    print(f"System : === You have entered the {name} ===")
    while True:
        print("System : What would you like to do?")
        print(f"\t1. Fight the lurking {monster.name}")
        print("\t2. Open the suspicious-looking chest")
        print(f"\t3. Go back to the {previous_room}")
        print(f"\t4. Move forward to the Next Room")
        print("\t5. Talk to the mysterious NPC in the shadows")
        print("\t6. Exit Game")
        try:
            user = int(input(f"{main_character.name} : "))
            if user == 1:
                battle(main_character, monster)
                save_to_file(main_file_name, main_character.to_dict())
                if main_character.current_health == 0:
                    main_character.location = "Main Entrance"
                    restore_stats(main_character)
                    save_to_file(main_file_name, main_character.to_dict())
                    restart = True
                    break
                continue
            elif user == 2:
                open_chest(main_character)
            elif user == 3:
                if previous_room not in main_character.location_discovered:
                    print(f"System: You step into unfamiliar territory... {previous_room} added to map.")
                    main_character.location_discovered.append(previous_room)
                main_character.location = previous_room
                save_to_file(main_file_name, main_character.to_dict())
                restart = True
                break
            elif user == 4:
                if next_room not in main_character.location_discovered:
                    print(f"System: You step into unfamiliar territory... {next_room} added to map.")
                    main_character.location_discovered.append(next_room)
                main_character.location = next_room
                main_character.previous_room = name
                save_to_file(main_file_name, main_character.to_dict())
                restart = True
                break
            elif user == 5:
                descriptive_npc(main_character)
                continue
            elif user == 6:
                exit_program(main_character)

            else:
                raise InvalidInput("System: That didn't work. Try selecting a valid choice.")
        except InvalidInput as i:
            print(i)
        except ValueError:
            print("System : Invalid input, Try again!!")

def boss_room_menu_no_key(main_character, name, previous_room):
    print(f"System : === You have entered the {name} ===")
    while True:
        print("System : What would you like to do?")
        print(f"\t1. Go back to the {previous_room}")
        print("\t2. Talk to the Gate Keeper")
        print("\t3. Exit Game")
        try:
            user = int(input(f"{main_character.name} : "))
            if user == 1:
                if previous_room not in main_character.location_discovered:
                    print(f"System: You step into unfamiliar territory... {previous_room} added to map.")
                    main_character.location_discovered.append(previous_room)
                main_character.location = previous_room
                save_to_file(main_file_name, main_character.to_dict())
                restart = True
                break
            elif user == 2:
                descriptive_npc(main_character)
                restart = True
                break
            elif user == 3:
                exit_program(main_character)
            else:
                raise InvalidInput("System: That didn't work. Try selecting a valid choice.")
        except InvalidInput as i:
            print(i)
        except ValueError:
            print("System : Invalid input, Try again!!")

def boss_room_menu_end(main_character, name, monster, previous_room, next_room):
    print(f"System : === You have entered the {name} ===")
    while True:
        print("System : What would you like to do?")
        print(f"\t1. Fight {monster.name}")
        print("\t2. Open the suspicious-looking chest")
        print(f"\t3. Go back to the {previous_room}")
        print(f"\t4. Move forward to the {next_room}")
        print("\t5. Exit Game")
        try:
            user = int(input(f"{main_character.name} : "))
            if user == 1:
                battle(main_character, monster)
                save_to_file(main_file_name, main_character.to_dict())
                if main_character.current_health == 0:
                    main_character.location = "Main Entrance"
                    restore_stats(main_character)
                    save_to_file(main_file_name, main_character.to_dict())
                    restart = True
                    break
                continue
            elif user == 2:
                open_chest(main_character)
            elif user == 3:
                if previous_room not in main_character.location_discovered:
                    print(f"System: You step into unfamiliar territory... {previous_room} added to map.")
                    main_character.location_discovered.append(previous_room)
                main_character.location = previous_room
                save_to_file(main_file_name, main_character.to_dict())
                restart = True
                break
            elif user == 4:
                if next_room not in main_character.location_discovered:
                    print(f"System: You step into unfamiliar territory... {next_room} added to map.")
                    main_character.location_discovered.append(next_room)
                main_character.location = next_room
                save_to_file(main_file_name, main_character.to_dict())
                restart = True
                break
            elif user == 5:
                exit_program(main_character)
            else:
                raise InvalidInput("System: That didn't work. Try selecting a valid choice.")
        except InvalidInput as i:
            print(i)
        except ValueError:
            print("System : Invalid input, Try again!!")


