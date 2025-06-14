"""
Skill system for Dungeon Quest game.
Contains all player and monster skills with their effects and damage values.
"""

from base_classes import BaseSkill, BaseMonsterSkill, load_json_file, save_json_file

main_file_name = 'skills_info.json'


# Skill factory functions to reduce repetition
def create_swordsman_skill(name, lvl, attack, heal, stamina_heal, health_usage, stamina_usage):
    """Factory function for creating swordsman skills."""
    return BaseSkill(
        name=name, species="Main", lvl=lvl, attack=attack, heal=heal,
        mana_heal=0, stamina_heal=stamina_heal, mana_usage=0,
        health_usage=health_usage, stamina_usage=stamina_usage
    )


def create_mage_skill(name, lvl, attack, heal, mana_heal, mana_usage, health_usage):
    """Factory function for creating mage skills."""
    return BaseSkill(
        name=name, species="Main", lvl=lvl, attack=attack, heal=heal,
        mana_heal=mana_heal, stamina_heal=0, mana_usage=mana_usage,
        health_usage=health_usage, stamina_usage=0
    )


def create_monster_skill(name, attack, status_effect=None, status_apply_chance=None, status_effect_damage=None, status_effect_duration=None):
    """Factory function for creating monster skills."""
    return BaseMonsterSkill(
        name=name, species="Monster", attack=attack,
        status_effect=status_effect, status_apply_chance=status_apply_chance,
        status_effect_damage=status_effect_damage, status_effect_duration=status_effect_duration
    )


# Swordsman skill classes
class SwordSlash(BaseSkill):
    """Basic swordsman attack skill."""
    
    def __init__(self):
        skill = create_swordsman_skill("Sword Slash", 1, 15, 0, 0, 0, 10)
        super().__init__(skill.name, skill.species, skill.lvl, skill.attack, skill.heal, skill.mana_heal, skill.stamina_heal, skill.mana_usage, skill.health_usage, skill.stamina_usage)


class SwordStrike(BaseSkill):
    """Powerful swordsman attack with high stamina cost."""
    
    def __init__(self):
        skill = create_swordsman_skill("Sword Strike", 1, 25, 0, 0, 0, 20)
        super().__init__(skill.name, skill.species, skill.lvl, skill.attack, skill.heal, skill.mana_heal, skill.stamina_heal, skill.mana_usage, skill.health_usage, skill.stamina_usage)


class SwordCut(BaseSkill):
    """Light swordsman attack with low stamina cost."""
    
    def __init__(self):
        skill = create_swordsman_skill("Sword Cut", 1, 5, 0, 0, 0, 5)
        super().__init__(skill.name, skill.species, skill.lvl, skill.attack, skill.heal, skill.mana_heal, skill.stamina_heal, skill.mana_usage, skill.health_usage, skill.stamina_usage)


class SwordHeal(BaseSkill):
    """Swordsman healing skill that also deals minor damage."""
    
    def __init__(self):
        skill = create_swordsman_skill("Sword Heal", 1, 5, 40, 0, 0, 30)
        super().__init__(skill.name, skill.species, skill.lvl, skill.attack, skill.heal, skill.mana_heal, skill.stamina_heal, skill.mana_usage, skill.health_usage, skill.stamina_usage)


class StaminaHeal(BaseSkill):
    """Stamina restoration skill using health as cost."""
    
    def __init__(self):
        skill = create_swordsman_skill("Stamina Heal", 1, 0, 0, 40, 20, 0)
        super().__init__(skill.name, skill.species, skill.lvl, skill.attack, skill.heal, skill.mana_heal, skill.stamina_heal, skill.mana_usage, skill.health_usage, skill.stamina_usage)


# Mage skill classes
class FireBall(BaseSkill):
    """Mage fire attack spell."""
    
    def __init__(self):
        skill = create_mage_skill("Fire Ball", 1, 20, 0, 0, 10, 0)
        super().__init__(skill.name, skill.species, skill.lvl, skill.attack, skill.heal, skill.mana_heal, skill.stamina_heal, skill.mana_usage, skill.health_usage, skill.stamina_usage)


class IceSpike(BaseSkill):
    """Mage ice attack spell."""
    
    def __init__(self):
        skill = create_mage_skill("Ice Spike", 1, 15, 0, 0, 10, 0)
        super().__init__(skill.name, skill.species, skill.lvl, skill.attack, skill.heal, skill.mana_heal, skill.stamina_heal, skill.mana_usage, skill.health_usage, skill.stamina_usage)


class ArcaneShot(BaseSkill):
    """Mage arcane attack spell with higher mana cost."""
    
    def __init__(self):
        skill = create_mage_skill("Arcane Shot", 1, 25, 0, 0, 15, 0)
        super().__init__(skill.name, skill.species, skill.lvl, skill.attack, skill.heal, skill.mana_heal, skill.stamina_heal, skill.mana_usage, skill.health_usage, skill.stamina_usage)


class HealingLight(BaseSkill):
    """Mage healing spell."""
    
    def __init__(self):
        skill = create_mage_skill("Healing Light", 1, 0, 50, 0, 10, 0)
        super().__init__(skill.name, skill.species, skill.lvl, skill.attack, skill.heal, skill.mana_heal, skill.stamina_heal, skill.mana_usage, skill.health_usage, skill.stamina_usage)


class ManaHeal(BaseSkill):
    """Mana restoration skill using health as cost."""
    
    def __init__(self):
        skill = create_mage_skill("Mana Heal", 1, 0, 0, 40, 0, 20)
        super().__init__(skill.name, skill.species, skill.lvl, skill.attack, skill.heal, skill.mana_heal, skill.stamina_heal, skill.mana_usage, skill.health_usage, skill.stamina_usage)


# Kobold monster skills
class RustyShiv(BaseMonsterSkill):
    """Kobold attack with bleed status effect."""
    
    def __init__(self):
        skill = create_monster_skill("Rusty Shiv", 23, "Bleed", 0.25, 2, 3)
        super().__init__(skill.name, skill.species, skill.attack, skill.status_effect, skill.status_apply_chance, skill.status_effect_damage, skill.status_effect_duration)


class PocketFlame(BaseMonsterSkill):
    """Kobold fire attack with burn status effect."""
    
    def __init__(self):
        skill = create_monster_skill("Pocket Flame", 20, "Burn", 0.4, 2, 3)
        super().__init__(skill.name, skill.species, skill.attack, skill.status_effect, skill.status_apply_chance, skill.status_effect_damage, skill.status_effect_duration)


# Skeleton monster skills
class BonePierce(BaseMonsterSkill):
    """Skeleton piercing attack without status effects."""
    
    def __init__(self):
        skill = create_monster_skill("Bone Pierce", 24)
        super().__init__(skill.name, skill.species, skill.attack, skill.status_effect, skill.status_apply_chance, skill.status_effect_damage, skill.status_effect_duration)


class RattleHex(BaseMonsterSkill):
    """Skeleton magical attack without status effects."""
    
    def __init__(self):
        skill = create_monster_skill("Rattle Hex", 26)
        super().__init__(skill.name, skill.species, skill.attack, skill.status_effect, skill.status_apply_chance, skill.status_effect_damage, skill.status_effect_duration)


# Lizardmen monster skills
class TailWhip(BaseMonsterSkill):
    """Lizardmen physical attack without status effects."""
    
    def __init__(self):
        skill = create_monster_skill("Tail Whip", 34)
        super().__init__(skill.name, skill.species, skill.attack, skill.status_effect, skill.status_apply_chance, skill.status_effect_damage, skill.status_effect_duration)


class VenomousSpit(BaseMonsterSkill):
    """Lizardmen poison attack with poison status effect."""
    
    def __init__(self):
        skill = create_monster_skill("Venomous Spit", 30, "Poison", 0.4, 3, 2)
        super().__init__(skill.name, skill.species, skill.attack, skill.status_effect, skill.status_apply_chance, skill.status_effect_damage, skill.status_effect_duration)


# Orc monster skills
class BrutalSmash(BaseMonsterSkill):
    """Orc heavy physical attack without status effects."""
    
    def __init__(self):
        skill = create_monster_skill("Brutal Smash", 30)
        super().__init__(skill.name, skill.species, skill.attack, skill.status_effect, skill.status_apply_chance, skill.status_effect_damage, skill.status_effect_duration)


class Skullbreaker(BaseMonsterSkill):
    """Orc devastating physical attack without status effects."""
    
    def __init__(self):
        skill = create_monster_skill("Skull Breaker", 33)
        super().__init__(skill.name, skill.species, skill.attack, skill.status_effect, skill.status_apply_chance, skill.status_effect_damage, skill.status_effect_duration)


# Vampire Lord boss skills
class BloodDrain(BaseMonsterSkill):
    """Vampire Lord life-draining attack."""
    
    def __init__(self):
        skill = create_monster_skill("Blood Drain", 43)
        super().__init__(skill.name, skill.species, skill.attack, skill.status_effect, skill.status_apply_chance, skill.status_effect_damage, skill.status_effect_duration)


class CrimsonHowl(BaseMonsterSkill):
    """Vampire Lord fear-inducing attack."""
    
    def __init__(self):
        skill = create_monster_skill("Crimson Howl", 40)
        super().__init__(skill.name, skill.species, skill.attack, skill.status_effect, skill.status_apply_chance, skill.status_effect_damage, skill.status_effect_duration)


class ShadowBurst(BaseMonsterSkill):
    """Vampire Lord most powerful shadow attack."""
    
    def __init__(self):
        skill = create_monster_skill("Shadow Burst", 50)
        super().__init__(skill.name, skill.species, skill.attack, skill.status_effect, skill.status_apply_chance, skill.status_effect_damage, skill.status_effect_duration)


# Initialize skills data in JSON file if it doesn't exist
skill_info = load_json_file(main_file_name)
if not skill_info:
    skills = [
        SwordCut(), SwordStrike(), SwordSlash(), SwordHeal(), StaminaHeal(),
        FireBall(), IceSpike(), ArcaneShot(), HealingLight(), ManaHeal()
    ]
    
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
    save_json_file(main_file_name, skill_info)