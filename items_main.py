"""
Item system for Dungeon Quest game.
Contains all weapon, potion, and drop item classes with their stats and effects.
"""

import json


main_file_name = 'skills_info.json'

def load_file(file_name):
    """Load JSON data from file, return empty dict if file doesn't exist."""
    with open(file_name, 'r') as file:
        try:
             return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
def save_to_file(file_name, data):
    """Save data to JSON file with proper formatting."""
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


class Item:
    """Base item class with common attributes for all items."""
    
    def __init__(self, class_of_weapon, name, class_required, attack_increase, heal, intelligence_increase, mana_replenish, stamina_replenish, price):
        self.name = name
        self.class_of_weapon = class_of_weapon
        self.class_required = class_required
        self.attack_increase = attack_increase
        self.heal = heal
        self.intelligence_increase = intelligence_increase
        self.mana_replenish = mana_replenish
        self.stamina_replenish = stamina_replenish
        self.price = price

    def __str__(self):
        """Display item information based on class requirements and type."""
        if self.class_required == "mage":
            if self.class_of_weapon == "weapon":
                return f"\tName : {self.name}\n\tWeapon class : {self.class_of_weapon}\t\tClass Requirement : {self.class_required}\n\tIntelligence increase : {self.intelligence_increase}\tMana replenish : {self.mana_replenish}\n\tHeal : {self.heal}\t\t\tPrice : {self.price}"
            elif self.class_of_weapon == "potion":
                return f"\tName : {self.name}\n\tWeapon class : {self.class_of_weapon}\t\tClass Requirement : {self.class_required}\n\tMana replenish : {self.mana_replenish}\t\tPrice : {self.price}"
        elif self.class_required == "swordsman":
            if self.class_of_weapon == "weapon":
                return f"\tName : {self.name}\n\tWeapon class : {self.class_of_weapon}\t\tClass Requirement : {self.class_required}\n\tStrenght increase : {self.attack_increase}\t\tStamina replenish : {self.stamina_replenish}\n\tHeal : {self.heal}\t\t\tPrice : {self.price}"
            elif self.class_of_weapon == "potion":
                return f"\tName : {self.name}\n\tWeapon class : {self.class_of_weapon}\t\tClass Requirement : {self.class_required}\n\Stamina replenish : {self.stamina_replenish}\t\tPrice : {self.price}"
        elif self.class_required is None:
            if self.class_of_weapon == "potion":
                return f"\tName : {self.name}\n\tWeapon class : {self.class_of_weapon}\n\tHeal : {self.heal}\t\tPrice : {self.price}"
            elif self.class_of_weapon == "drop":
                return f"\tName : {self.name}\n\tWeapon class : {self.class_of_weapon}\n\tPrice : {self.price}"
            else:
                return "\tUnknown Item - No Info Available"
        else:
            return f"System : Unknown Item - {self.name}"


# Swordsman weapon classes
class IronFangBlade(Item):
    """Basic swordsman weapon with balanced stats."""
    
    def __init__(self):
        super().__init__(
            name="Iron Fang Blade",
            class_of_weapon="weapon",
            class_required="swordsman",
            attack_increase=10,
            heal=10,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=5,
            price=500
        )


class KnightsEdge(Item):
    """Mid-tier swordsman weapon with improved stats."""
    
    def __init__(self):
        super().__init__(
            name="Knight's Edge",
            class_of_weapon="weapon",
            class_required="swordsman",
            attack_increase=15,
            heal=15,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=10,
            price=800
        )


class TitanSlayer(Item):
    """High-tier swordsman weapon with powerful stats."""
    
    def __init__(self):
        super().__init__(
            name="Titan Slayer",
            class_of_weapon="weapon",
            class_required="swordsman",
            attack_increase=25,
            heal=13,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=15,
            price=1500
        )


# Mage weapon classes        
class StaffOfWisdom(Item):
    """Basic mage weapon focusing on intelligence and mana."""
    
    def __init__(self):
        super().__init__(
            name="Staff of Wisdom",
            class_of_weapon="weapon",
            class_required="mage",
            attack_increase=0,
            heal=10,
            intelligence_increase=10,
            mana_replenish=20,
            stamina_replenish=0,
            price=600
        )


class ArcaneOrb(Item):
    """Mid-tier mage weapon with enhanced magical properties."""
    
    def __init__(self):
        super().__init__(
            name="Arcane Orb",
            class_of_weapon="weapon",
            class_required="mage",
            attack_increase=0,
            heal=15,
            intelligence_increase=15,
            mana_replenish=30,
            stamina_replenish=0,
            price=1000
        )


class EnchantedCloak(Item):
    """High-tier mage equipment with powerful magical enhancements."""
    
    def __init__(self):
        super().__init__(
            name="Enchanted Cloak",
            class_of_weapon="weapon",
            class_required="mage",
            attack_increase=0,
            heal=20,
            intelligence_increase=25,
            mana_replenish=15,
            stamina_replenish=0,
            price=1600
        )


# Consumable potion classes
class HealthPotion(Item):
    """Universal healing potion usable by any class."""
    
    def __init__(self):
        super().__init__(
            name="Health Potion",
            class_of_weapon="potion",
            class_required=None,
            attack_increase=0,
            heal=50,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price=500
        )


class StaminaPotion(Item):
    """Stamina restoration potion for swordsman class."""
    
    def __init__(self):
        super().__init__(
            name="Stamina Potion",
            class_of_weapon="potion",
            class_required="swordsman",
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=40,
            price=300
        )


class ManaPotion(Item):
    """Mana restoration potion for mage class."""
    
    def __init__(self):
        super().__init__(
            name="Mana Potion",
            class_of_weapon="potion",
            class_required="mage",
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=50,
            stamina_replenish=0,
            price=300
        )


# Monster drop items for selling
class KoboldStone(Item):
    """Drop item from Kobold monsters."""
    
    def __init__(self):
        super().__init__(
            name="Kobold Stone",
            class_of_weapon="drop",
            class_required=None,
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price=400
        )


class SkeletonAsh(Item):
    """Drop item from Skeleton monsters."""
    
    def __init__(self):
        super().__init__(
            name="Skeleton's ash",
            class_of_weapon="drop",
            class_required=None,
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price=300
        )


class LizardTail(Item):
    """Drop item from Lizardmen monsters."""
    
    def __init__(self):
        super().__init__(
            name="Lizardmen's scales",
            class_of_weapon="drop",
            class_required=None,
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price=600
        )


class OrcMeat(Item):
    """Drop item from Orc monsters."""
    
    def __init__(self):
        super().__init__(
            name="Orc Meat",
            class_of_weapon="drop",
            class_required=None,
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price=1000
        )


# Special quest items
class CrimsonKey(Item):
    """Special key item required for boss room access."""
    
    def __init__(self):
        super().__init__(
            name="Crimson Key",
            class_of_weapon="key",
            class_required=None,
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price=None
        )


class CrimsonFang(Item):
    """Rare drop from the final boss."""
    
    def __init__(self):
        super().__init__(
            name="Crimson Fang",
            class_of_weapon="drop",
            class_required=None,
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price=5000
        )