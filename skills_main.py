"""
Skill system for Dungeon Quest game.
Contains all player and monster skills with their effects and damage values.
"""

import json
import os

main_file_name = 'skills_info.json'

def load_file(file_name):
    """Load JSON file, create empty one if it doesn't exist."""
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            json.dump({}, file)

    with open(file_name, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}


def save_to_file(file_name, data):
    """Save data to JSON file with proper formatting."""
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


class Skills:
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
        if self.mana_usage:
            return f"\tSkill Name : {self.name}\n\tSkill Level : {self.lvl}\t\tAttack : {self.attack}\n\tHeal : {self.heal}\t\tHealth Usage : {self.health_usage}\n\tMana Heal : {self.mana_heal}\t\tMana Usage : {self.mana_usage}"
        elif self.stamina_usage:
            return f"\tSkill Name : {self.name}\n\tSkill Level : {self.lvl}\t\tAttack : {self.attack}\n\tHeal : {self.heal}\t\tHealth Usage : {self.health_usage}\n\tStamina Heal : {self.stamina_heal}\t\tStamina Usage : {self.stamina_usage}"


class MonsterSkills:
    """Base skill class for monster abilities with status effects."""
    
    def __init__(self, name, species, attack, status_effect, status_apply_chance, status_effect_damage, status_effect_duration):
        self.name = name
        self.species = species
        self.attack = attack
        self.status_effect = status_effect
        self.status_apply_chance = status_apply_chance
        self.status_effect_damage = status_effect_damage
        self.status_effect_duration = status_effect_duration


# Swordsman skill classes
class SwordSlash(Skills):
    """Basic swordsman attack skill."""
    
    def __init__(self):
        super().__init__(
            name="Sword Slash", lvl=1, species="Main",
            attack=15, heal=0, mana_heal=0,
            stamina_heal=0, mana_usage=0, 
            health_usage=0, stamina_usage=10
        )


class SwordStrike(Skills):
    """Powerful swordsman attack with high stamina cost."""
    
    def __init__(self):
        super().__init__(
            name="Sword Strike", lvl=1, species="Main",
            attack=25, heal=0, mana_heal=0,
            stamina_heal=0, mana_usage=0, 
            health_usage=0, stamina_usage=20
            )


class SwordCut(Skills):
    """Light swordsman attack with low stamina cost."""
    
    def __init__(self):
        super().__init__(
            name="Sword Cut", lvl=1, species="Main",
            attack=5, heal=0, mana_heal=0,
            stamina_heal=0, mana_usage=0, 
            health_usage=0, stamina_usage=5
            )


class SwordHeal(Skills):
    """Swordsman healing skill that also deals minor damage."""
    
    def __init__(self):
        super().__init__(
            name="Sword Heal", lvl=1, species="Main",
            attack=5, heal=40, mana_heal=0,
            stamina_heal=0, mana_usage=0, 
            health_usage=0, stamina_usage=30
            )


class StaminaHeal(Skills):
    """Stamina restoration skill using health as cost."""
    
    def __init__(self):
        super().__init__(
            name="Stamina Heal", lvl=1, species="Main",
            attack=0, heal=0, mana_heal=0, 
            stamina_heal=40, mana_usage=0, 
            health_usage=20, stamina_usage=0
            )


# Mage skill classes
class FireBall(Skills):
    """Mage fire attack spell."""
    
    def __init__(self):
        super().__init__(
            name="Fire Ball", lvl=1, species="Main",
            attack=20, heal=0, mana_heal=0,
            stamina_heal=0, mana_usage=10,
            health_usage=0, stamina_usage=0
        )


class IceSpike(Skills):
    """Mage ice attack spell."""
    
    def __init__(self):
        super().__init__(
            name="Ice Spike", lvl=1, species="Main",
            attack=15, heal=0, mana_heal=0,
            stamina_heal=0, mana_usage=10,
            health_usage=0, stamina_usage=0
        )


class ArcaneShot(Skills):
    """Mage arcane attack spell with higher mana cost."""
    
    def __init__(self):
        super().__init__(
            name="Arcane Shot", lvl=1, species="Main",
            attack=25, heal=0, mana_heal=0,
            stamina_heal=0, mana_usage=15,
            health_usage=0, stamina_usage=0
        )


class HealingLight(Skills):
    """Mage healing spell."""
    
    def __init__(self):
        super().__init__(
            name="Healing Light", lvl=1, species="Main",
            attack=0, heal=50, mana_heal=0,
            stamina_heal=0, mana_usage=10,
            health_usage=0, stamina_usage=0
        )


class ManaHeal(Skills):
    """Mana restoration skill using health as cost."""
    
    def __init__(self):
        super().__init__(
            name="Mana Heal", lvl=1, species="Main",
            attack=0, heal=0, mana_heal=40, 
            stamina_heal=0, mana_usage=0, 
            health_usage=20, stamina_usage=0
            )


# Kobold monster skills
class RustyShiv(MonsterSkills):
    """Kobold attack with bleed status effect."""
    
    def __init__(self):
        super().__init__(
            name="Rusty Shiv", species="Monster", attack=23,
            status_effect="Bleed", status_apply_chance=0.25,
            status_effect_damage=2, status_effect_duration=3
            )


class PocketFlame(MonsterSkills):
    """Kobold fire attack with burn status effect."""
    
    def __init__(self):
        super().__init__(
            name="Pocket Flame", species="Monster", attack=20,
            status_effect="Burn", status_apply_chance=0.4,
            status_effect_damage=2, status_effect_duration=3
            )


# Skeleton monster skills
class BonePierce(MonsterSkills):
    """Skeleton piercing attack without status effects."""
    
    def __init__(self):
        super().__init__(
            name="Bone Pierce", species="Monster", attack=24,
            status_effect=None, status_apply_chance=None, 
            status_effect_damage=None, status_effect_duration=None
            )


class RattleHex(MonsterSkills):
    """Skeleton magical attack without status effects."""
    
    def __init__(self):
        super().__init__(
            name="Rattle Hex", species="Monster", attack=26,
            status_effect=None, status_apply_chance=None, 
            status_effect_damage=None, status_effect_duration=None
            )


# Lizardmen monster skills
class TailWhip(MonsterSkills):
    """Lizardmen physical attack without status effects."""
    
    def __init__(self):
        super().__init__(
            name="Tail Whip", species="Monster", attack=34,
            status_effect=None, status_apply_chance=None,
            status_effect_damage=None, status_effect_duration=None
            )


class VenomousSpit(MonsterSkills):
    """Lizardmen poison attack with poison status effect."""
    
    def __init__(self):
        super().__init__(
            name="Venomous Spit", species="Monster", attack=30, 
            status_effect="Poison", status_apply_chance=0.4, 
            status_effect_damage=3, status_effect_duration=2
            )


# Orc monster skills
class BrutalSmash(MonsterSkills):
    """Orc heavy physical attack without status effects."""
    
    def __init__(self):
        super().__init__(
            name="Brutal Smash", species="Monster", attack=30, 
            status_effect=None, status_apply_chance=None, 
            status_effect_damage=None, status_effect_duration=None
            )


class Skullbreaker(MonsterSkills):
    """Orc devastating physical attack without status effects."""
    
    def __init__(self):
        super().__init__(
            name="Skull Breaker", species="Monster", attack=33, 
            status_effect=None, status_apply_chance=None, 
            status_effect_damage=None, status_effect_duration=None
            )


# Vampire Lord boss skills
class BloodDrain(MonsterSkills):
    """Vampire Lord life-draining attack."""
    
    def __init__(self):
        super().__init__(
            name="Blood Drain", species="Monster", attack=43, 
            status_effect=None, status_apply_chance=None, 
            status_effect_damage=None, status_effect_duration=None
            )


class CrimsonHowl(MonsterSkills):
    """Vampire Lord fear-inducing attack."""
    
    def __init__(self):
        super().__init__(
            name="Crimson Howl", species="Monster", attack=40, 
            status_effect=None, status_apply_chance=None, 
            status_effect_damage=None, status_effect_duration=None
            )


class ShadowBurst(MonsterSkills):
    """Vampire Lord most powerful shadow attack."""
    
    def __init__(self):
        super().__init__(
            name="Shadow Burst", species="Monster", attack=50, 
            status_effect=None, status_apply_chance=None, 
            status_effect_damage=None, status_effect_duration=None
            )


# Initialize skill instances for JSON saving
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

skills = [sword_cut, sword_strike, sword_slash, sword_heal, stamina_heal, fire_ball, ice_spike, arcane_shot, healing_light, mana_heal]

# Initialize skills data in JSON file if it doesn't exist
skill_info = load_file(main_file_name)
if not skill_info:
    for skill in skills:
        skill_info[skill.name] = {
            "level": skill.lvl,
            "Attack": skill.attack,
            "Heal": skill.heal,
            "Mana heal": skill.mana_heal,
            "Stamina heal": skill.stamina_heal,
            "Mana usage": skill.mana_usage,
            "Health usage": skill.health_usage,
            "Stamina usage": skill.stamina_usage
        }
    save_to_file(main_file_name, skill_info)