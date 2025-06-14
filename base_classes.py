"""
Base classes and shared utilities for Dungeon Quest game.
Contains common functionality to eliminate code repetition.
"""

import json
import os


def load_json_file(file_name):
    """Load JSON file, create empty one if it doesn't exist."""
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            json.dump({}, file)

    with open(file_name, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def save_json_file(file_name, data):
    """Save data to JSON file with proper formatting."""
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


class BaseCharacter:
    """Base character class with common attributes for all character types."""
    
    def __init__(self, name, character_class, max_health, current_health, strength, intelligence, max_mana, current_mana, max_stamina, current_stamina):
        self.name = name
        self.character_class = character_class
        self.strength = strength
        self.intelligence = intelligence
        self.max_health = max_health
        self.current_health = current_health
        self.max_mana = max_mana
        self.current_mana = current_mana
        self.max_stamina = max_stamina
        self.current_stamina = current_stamina


class BaseMonster:
    """Base monster class for combat encounters."""
    
    def __init__(self, name, health, drop, exp, skills):
        self.name = name
        self.health = health
        self.drop = drop
        self.exp = exp
        self.skills = skills

    def __str__(self):
        return f"System : | Name : {self.name}\n\t | Health : {self.health}"


class BaseNPC:
    """Base NPC class for non-combat characters."""
    
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation


class BaseItem:
    """Base item class with common attributes for all items."""
    
    def __init__(self, name, class_of_weapon, class_required, attack_increase, heal, intelligence_increase, mana_replenish, stamina_replenish, price):
        self.name = name
        self.class_of_weapon = class_of_weapon
        self.class_required = class_required
        self.attack_increase = attack_increase
        self.heal = heal
        self.intelligence_increase = intelligence_increase
        self.mana_replenish = mana_replenish
        self.stamina_replenish = stamina_replenish
        self.price = price

    def _format_class_specific_info(self):
        """Format item information based on class requirements."""
        if self.class_required == "mage":
            if self.class_of_weapon == "weapon":
                return f"Intelligence increase : {self.intelligence_increase}\tMana replenish : {self.mana_replenish}\n\tHeal : {self.heal}\t\t\tPrice : {self.price}"
            elif self.class_of_weapon == "potion":
                return f"Mana replenish : {self.mana_replenish}\t\tPrice : {self.price}"
        elif self.class_required == "swordsman":
            if self.class_of_weapon == "weapon":
                return f"Strength increase : {self.attack_increase}\t\tStamina replenish : {self.stamina_replenish}\n\tHeal : {self.heal}\t\t\tPrice : {self.price}"
            elif self.class_of_weapon == "potion":
                return f"Stamina replenish : {self.stamina_replenish}\t\tPrice : {self.price}"
        elif self.class_required is None:
            if self.class_of_weapon == "potion":
                return f"Heal : {self.heal}\t\tPrice : {self.price}"
            elif self.class_of_weapon == "drop":
                return f"Price : {self.price}"
        return "Unknown Item - No Info Available"

    def __str__(self):
        """Display item information based on class requirements and type."""
        base_info = f"\tName : {self.name}\n\tWeapon class : {self.class_of_weapon}"
        if self.class_required:
            base_info += f"\t\tClass Requirement : {self.class_required}"
        
        specific_info = self._format_class_specific_info()
        if specific_info == "Unknown Item - No Info Available":
            return f"\t{specific_info}"
        
        return f"{base_info}\n\t{specific_info}"


class BaseSkill:
    """Base skill class for player character abilities."""
    
    def __init__(self, name, species, lvl, attack, heal, mana_heal, stamina_heal, mana_usage, health_usage, stamina_usage):
        self.name = name
        self.species = species
        self.lvl = lvl
        self.attack = attack
        self.heal = heal
        self.mana_heal = mana_heal
        self.stamina_heal = stamina_heal
        self.mana_usage = mana_usage
        self.health_usage = health_usage
        self.stamina_usage = stamina_usage

    def __str__(self):
        """Display skill information based on resource usage type."""
        base_info = f"\tSkill Name : {self.name}\n\tSkill Level : {self.lvl}\t\tAttack : {self.attack}"
        
        if self.mana_usage:
            return f"{base_info}\n\tHeal : {self.heal}\t\tMana Usage : {self.mana_usage}"
        elif self.stamina_usage:
            return f"{base_info}\n\tHeal : {self.heal}\t\tStamina Usage : {self.stamina_usage}"
        elif self.health_usage : 
            return f"{base_info}\n\tMana Heal : {self.mana_heal}\t\tStamina Heal : {self.stamina_heal}"


class BaseMonsterSkill:
    """Base skill class for monster abilities with status effects."""
    
    def __init__(self, name, species, attack, status_effect=None, status_apply_chance=None, status_effect_damage=None, status_effect_duration=None):
        self.name = name
        self.species = species
        self.attack = attack
        self.status_effect = status_effect
        self.status_apply_chance = status_apply_chance
        self.status_effect_damage = status_effect_damage
        self.status_effect_duration = status_effect_duration