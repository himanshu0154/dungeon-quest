import json


# This is the main data file which saves the skills information
main_file_name = 'skills_info.json'

# This Func loads the json file 
def load_file(file_name):
    with open(file_name, 'r') as file:
        try:
             return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        
# This func saves data to the json file
def save_to_file(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

# =============================================== Items base class ==============================================================

# This is the base class 
class Item():
    def __init__(self, class_of_weapon, name,class_required, attack_increase, heal, intelligence_increase, mana_replenish, stamina_replenish, price):
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

# ============================================= Swordsman's items =================================================================

class IronFangBlade(Item):
    def __init__(self):
        super().__init__(
            name="Iron Fang Blade",
            class_of_weapon = "weapon",
            class_required="swordsman",
            attack_increase=10,
            heal=10,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=5,
            price = 500
        )

class KnightsEdge(Item):
    def __init__(self):
        super().__init__(
            name="Knight's Edge",
            class_of_weapon = "weapon",
            class_required="swordsman",
            attack_increase=15,
            heal=15,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=10,
            price = 800
        )

class TitanSlayer(Item):
    def __init__(self):
        super().__init__(
            name="Titan Slayer",
            class_of_weapon = "weapon",
            class_required="swordsman",
            attack_increase=25,
            heal=13,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=15,
            price = 1500
        )

#===================================================== Mage's items ===============================================================
        
class StaffOfWisdom(Item):
    def __init__(self):
        super().__init__(
            name="Staff of Wisdom",
            class_of_weapon = "weapon",
            class_required="mage",
            attack_increase=0,
            heal=10,
            intelligence_increase=10,
            mana_replenish=20,
            stamina_replenish=0,
            price = 600
        )


class ArcaneOrb(Item):
    def __init__(self):
        super().__init__(
            name="Arcane Orb",
            class_of_weapon = "weapon",
            class_required="mage",
            attack_increase=0,
            heal=15,
            intelligence_increase=15,
            mana_replenish=30,
            stamina_replenish=0,
            price = 1000
        )


class EnchantedCloak(Item):
    def __init__(self):
        super().__init__(
            name="Enchanted Cloak",
            class_of_weapon = "weapon",
            class_required="mage",
            attack_increase=0,
            heal=20,
            intelligence_increase=25,
            mana_replenish=15,
            stamina_replenish=0,
            price = 1600
        )

# ====================================================== potions =====================================================================

class HealthPotion(Item):
    def __init__(self):
        super().__init__(
            name="Health Potion",
            class_of_weapon= "potion",
            class_required=None,  # No class restriction
            attack_increase=0,
            heal=50,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price = 500
        )


class StaminaPotion(Item):
    def __init__(self):
        super().__init__(
            name="Stamina Potion",
            class_of_weapon= "potion",
            class_required="swordsman",
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=40,
            price = 300
        )


class ManaPotion(Item):
    def __init__(self):
        super().__init__(
            name="Mana Potion",
            class_of_weapon= "potion",
            class_required="mage",
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=50,
            stamina_replenish=0,
            price = 300
        )
        
class KoboldStone(Item):
    def __init__(self):
        super().__init__(
            name="Kobold Stone",
            class_of_weapon= "drop",
            class_required=None,
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price = 400
        )
class SkeletonAsh(Item):
    def __init__(self):
        super().__init__(
            name="Skeleton's ash",
            class_of_weapon= "drop",
            class_required=None,
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price = 300
        )
class LizardTail(Item):
    def __init__(self):
        super().__init__(
            name="Lizardmen's scales",
            class_of_weapon= "drop",
            class_required=None,
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price = 600
        )
class OrcMeat(Item):
    def __init__(self):
        super().__init__(
            name="Orc Meat",
            class_of_weapon= "drop",
            class_required=None,
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price = 1000
        )

class CrimsonKey(Item):
    def __init__(self):
        super().__init__(
            name="Crimson Key",
            class_of_weapon= "key",
            class_required=None,
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price = None
        )
class CrimsonFang(Item):
    def __init__(self):
        super().__init__(
            name="Crimson Fang",
            class_of_weapon= "drop",
            class_required=None,
            attack_increase=0,
            heal=0,
            intelligence_increase=0,
            mana_replenish=0,
            stamina_replenish=0,
            price = 5000
        )


