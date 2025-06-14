"""
Item system for Dungeon Quest game.
Contains all weapon, potion, and drop item classes with their stats and effects.
"""

from base_classes import BaseItem


# Weapon factory functions to reduce repetition
def create_swordsman_weapon(name, attack_increase, heal, stamina_replenish, price):
    """Factory function for creating swordsman weapons."""
    return BaseItem(
        name=name,
        class_of_weapon="weapon",
        class_required="swordsman",
        attack_increase=attack_increase,
        heal=heal,
        intelligence_increase=0,
        mana_replenish=0,
        stamina_replenish=stamina_replenish,
        price=price
    )


def create_mage_weapon(name, heal, intelligence_increase, mana_replenish, price):
    """Factory function for creating mage weapons."""
    return BaseItem(
        name=name,
        class_of_weapon="weapon",
        class_required="mage",
        attack_increase=0,
        heal=heal,
        intelligence_increase=intelligence_increase,
        mana_replenish=mana_replenish,
        stamina_replenish=0,
        price=price
    )


def create_potion(name, class_required, heal=0, mana_replenish=0, stamina_replenish=0, price=0):
    """Factory function for creating potions."""
    return BaseItem(
        name=name,
        class_of_weapon="potion",
        class_required=class_required,
        attack_increase=0,
        heal=heal,
        intelligence_increase=0,
        mana_replenish=mana_replenish,
        stamina_replenish=stamina_replenish,
        price=price
    )


def create_drop_item(name, price):
    """Factory function for creating drop items."""
    return BaseItem(
        name=name,
        class_of_weapon="drop",
        class_required=None,
        attack_increase=0,
        heal=0,
        intelligence_increase=0,
        mana_replenish=0,
        stamina_replenish=0,
        price=price
    )


# Swordsman weapon classes
class IronFangBlade(BaseItem):
    """Basic swordsman weapon with balanced stats."""
    
    def __init__(self):
        weapon = create_swordsman_weapon("Iron Fang Blade", 10, 10, 5, 500)
        super().__init__(weapon.name, weapon.class_of_weapon, weapon.class_required, weapon.attack_increase, weapon.heal, weapon.intelligence_increase, weapon.mana_replenish, weapon.stamina_replenish, weapon.price)


class KnightsEdge(BaseItem):
    """Mid-tier swordsman weapon with improved stats."""
    
    def __init__(self):
        weapon = create_swordsman_weapon("Knight's Edge", 15, 15, 10, 800)
        super().__init__(weapon.name, weapon.class_of_weapon, weapon.class_required, weapon.attack_increase, weapon.heal, weapon.intelligence_increase, weapon.mana_replenish, weapon.stamina_replenish, weapon.price)


class TitanSlayer(BaseItem):
    """High-tier swordsman weapon with powerful stats."""
    
    def __init__(self):
        weapon = create_swordsman_weapon("Titan Slayer", 25, 13, 15, 1500)
        super().__init__(weapon.name, weapon.class_of_weapon, weapon.class_required, weapon.attack_increase, weapon.heal, weapon.intelligence_increase, weapon.mana_replenish, weapon.stamina_replenish, weapon.price)


# Mage weapon classes        
class StaffOfWisdom(BaseItem):
    """Basic mage weapon focusing on intelligence and mana."""
    
    def __init__(self):
        weapon = create_mage_weapon("Staff of Wisdom", 10, 10, 20, 600)
        super().__init__(weapon.name, weapon.class_of_weapon, weapon.class_required, weapon.attack_increase, weapon.heal, weapon.intelligence_increase, weapon.mana_replenish, weapon.stamina_replenish, weapon.price)


class ArcaneOrb(BaseItem):
    """Mid-tier mage weapon with enhanced magical properties."""
    
    def __init__(self):
        weapon = create_mage_weapon("Arcane Orb", 15, 15, 30, 1000)
        super().__init__(weapon.name, weapon.class_of_weapon, weapon.class_required, weapon.attack_increase, weapon.heal, weapon.intelligence_increase, weapon.mana_replenish, weapon.stamina_replenish, weapon.price)


class EnchantedCloak(BaseItem):
    """High-tier mage equipment with powerful magical enhancements."""
    
    def __init__(self):
        weapon = create_mage_weapon("Enchanted Cloak", 20, 25, 15, 1600)
        super().__init__(weapon.name, weapon.class_of_weapon, weapon.class_required, weapon.attack_increase, weapon.heal, weapon.intelligence_increase, weapon.mana_replenish, weapon.stamina_replenish, weapon.price)


# Consumable potion classes
class HealthPotion(BaseItem):
    """Universal healing potion usable by any class."""
    
    def __init__(self):
        potion = create_potion("Health Potion", None, heal=50, price=500)
        super().__init__(potion.name, potion.class_of_weapon, potion.class_required, potion.attack_increase, potion.heal, potion.intelligence_increase, potion.mana_replenish, potion.stamina_replenish, potion.price)


class StaminaPotion(BaseItem):
    """Stamina restoration potion for swordsman class."""
    
    def __init__(self):
        potion = create_potion("Stamina Potion", "swordsman", stamina_replenish=40, price=300)
        super().__init__(potion.name, potion.class_of_weapon, potion.class_required, potion.attack_increase, potion.heal, potion.intelligence_increase, potion.mana_replenish, potion.stamina_replenish, potion.price)


class ManaPotion(BaseItem):
    """Mana restoration potion for mage class."""
    
    def __init__(self):
        potion = create_potion("Mana Potion", "mage", mana_replenish=50, price=300)
        super().__init__(potion.name, potion.class_of_weapon, potion.class_required, potion.attack_increase, potion.heal, potion.intelligence_increase, potion.mana_replenish, potion.stamina_replenish, potion.price)


# Monster drop items for selling
class KoboldStone(BaseItem):
    """Drop item from Kobold monsters."""
    
    def __init__(self):
        drop = create_drop_item("Kobold Stone", 400)
        super().__init__(drop.name, drop.class_of_weapon, drop.class_required, drop.attack_increase, drop.heal, drop.intelligence_increase, drop.mana_replenish, drop.stamina_replenish, drop.price)


class SkeletonAsh(BaseItem):
    """Drop item from Skeleton monsters."""
    
    def __init__(self):
        drop = create_drop_item("Skeleton's ash", 300)
        super().__init__(drop.name, drop.class_of_weapon, drop.class_required, drop.attack_increase, drop.heal, drop.intelligence_increase, drop.mana_replenish, drop.stamina_replenish, drop.price)


class LizardTail(BaseItem):
    """Drop item from Lizardmen monsters."""
    
    def __init__(self):
        drop = create_drop_item("Lizardmen's scales", 600)
        super().__init__(drop.name, drop.class_of_weapon, drop.class_required, drop.attack_increase, drop.heal, drop.intelligence_increase, drop.mana_replenish, drop.stamina_replenish, drop.price)


class OrcMeat(BaseItem):
    """Drop item from Orc monsters."""
    
    def __init__(self):
        drop = create_drop_item("Orc Meat", 1000)
        super().__init__(drop.name, drop.class_of_weapon, drop.class_required, drop.attack_increase, drop.heal, drop.intelligence_increase, drop.mana_replenish, drop.stamina_replenish, drop.price)


# Special quest items
class CrimsonKey(BaseItem):
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


class CrimsonFang(BaseItem):
    """Rare drop from the final boss."""
    
    def __init__(self):
        drop = create_drop_item("Crimson Fang", 5000)
        super().__init__(drop.name, drop.class_of_weapon, drop.class_required, drop.attack_increase, drop.heal, drop.intelligence_increase, drop.mana_replenish, drop.stamina_replenish, drop.price)