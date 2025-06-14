"""
Character system for Dungeon Quest game.
Contains all character classes including main character, enemies, monsters, and NPCs.
"""

from items_main import (
    StaffOfWisdom, TitanSlayer, IronFangBlade, KnightsEdge, 
    ArcaneOrb, EnchantedCloak, HealthPotion, StaminaPotion, ManaPotion
)
from skills_main import (
    RustyShiv, PocketFlame, RattleHex, BonePierce, TailWhip, 
    VenomousSpit, Skullbreaker, BrutalSmash, CrimsonHowl, 
    ShadowBurst, BloodDrain
)


class Character:
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


class MainCharacter(Character):
    """Player character class with progression system and inventory management."""
    
    def __init__(self, name, character_class):
        super().__init__(name, character_class, max_health=100, current_health=100, strength=0, intelligence=0, max_mana=0, current_mana=0, max_stamina=0, current_stamina=0)
        # Progression attributes
        self.lvl = 1
        self.experience = 0
        self.stat_points = 0
        
        # Inventory and equipment
        self.inventory = []
        self.skills = set()
        self.weapon = None
        self.gold = 0
        
        # Status effects
        self.status_effect = None
        self.status_duration = 0
        
        # World state tracking
        self.location = None
        self.location_discovered = []
        self.chest = []
        self.boss_defeated = "undefeated"
        self.previous_room = None

    @classmethod
    def from_dict(cls, data):
        """Create MainCharacter instance from saved JSON data."""
        obj = cls(data["name"], data['character_class'])
        
        # Load character stats
        obj.max_health = data["max health"]
        obj.current_health = data["current health"]
        obj.strength = data["strength"]
        obj.intelligence = data['intelligence']
        obj.max_mana = data['max mana']
        obj.current_mana = data['current mana']
        obj.max_stamina = data["max stamina"]
        obj.current_stamina = data["current stamina"]
        
        # Load progression and inventory
        obj.inventory = data["inventory"]
        obj.skills = set(data.get('skills', []))
        obj.lvl = data['lvl']
        obj.experience = data['experience']
        obj.stat_points = data['stat_points']
        obj.gold = data['gold']
        
        # Load status and world state
        obj.status_effect = data['status_effect']
        obj.status_duration = data['status_duration']
        obj.weapon = data['weapon']
        obj.location = data['location']
        obj.location_discovered = data['location discovered']
        obj.chest = data['chest founded']
        obj.boss_defeated = data['boss defeated']
        obj.previous_room = data['previous room']
        
        return obj
    
    def to_dict(self):
        """Convert MainCharacter instance to dictionary for JSON saving."""
        return {
            "name": self.name,
            "character_class": self.character_class,
            "max health": self.max_health,
            "current health": self.current_health,
            "strength": self.strength,
            "intelligence": self.intelligence,
            "max mana": self.max_mana,
            "current mana": self.current_mana,
            "max stamina": self.max_stamina,
            "current stamina": self.current_stamina,
            "inventory": self.inventory,
            "skills": list(self.skills),
            "lvl": self.lvl,
            "experience": self.experience,
            "stat_points": self.stat_points,
            "gold": self.gold,
            "status_effect": self.status_effect,
            "status_duration": self.status_duration,
            "weapon": self.weapon,
            "location": self.location,
            "location discovered": self.location_discovered,
            "chest founded": self.chest,
            "boss defeated": self.boss_defeated,
            "previous room": self.previous_room
        }
    
    def __str__(self):
        """Display formatted character information."""
        return f"System : | Name : {self.name}\n\t | Class : {self.character_class}\t\t\tgold : {self.gold}\n\t | Level : {self.lvl}\t\t\tExperience Points : {self.experience}\n\t | Health : {self.current_health}\t\t\tMana : {self.current_mana}\n\t | Strength : {self.strength}\t\t\tSkills : {list(self.skills)}\n\t | Intelligence : {self.intelligence}\t\tInventory : {self.inventory}\n\t | Stamina : {self.current_stamina}\t\t\tStat Points : {self.stat_points}"


class Monsters:
    """Base monster class for combat encounters."""
    
    def __init__(self, name, health, drop, exp):
        self.name = name
        self.health = health
        self.drop = drop
        self.exp = exp

    def __str__(self):
        return f"System : | Name : {self.name}\n\t | Health : {self.health}"


class KoboldMonster(Monsters):
    """Kobold enemy with bleed and burn attacks."""
    
    def __init__(self):
        super().__init__(name="Kobold", health=100, drop="Kobold Stone", exp=200)
        self.skills = [RustyShiv(), PocketFlame()]


class Skeleton(Monsters):
    """Skeleton enemy with bone-based attacks."""
    
    def __init__(self):
        super().__init__(name="Skeleton", health=100, drop="Skeleton's ash", exp=100)
        self.skills = [BonePierce(), RattleHex()]


class LizardMen(Monsters):
    """Lizardmen enemy with poison attacks."""
    
    def __init__(self):
        super().__init__(name="Lizard Men", health=100, drop="Lizardmen's scales", exp=400)
        self.skills = [TailWhip(), VenomousSpit()]


class Orc(Monsters):
    """Orc enemy with powerful physical attacks."""
    
    def __init__(self):
        super().__init__(name="Orc", health=100, drop="Orc Meat", exp=500)
        self.skills = [BrutalSmash(), Skullbreaker()]


class VampireLord(Monsters):
    """Final boss with devastating vampire abilities."""
    
    def __init__(self):
        super().__init__(name="Vehraxis the Crimson Wane", health=200, drop="Crimson Fang", exp=1000)
        self.skills = [BloodDrain(), CrimsonHowl(), ShadowBurst()]


class NPC:
    """Base NPC class for non-combat characters."""
    
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation


class Merchant(NPC):
    """Merchant NPC for buying and selling items."""
    
    def __init__(self):
        super().__init__(name="Merchant Todd", occupation="Merchant")
        self.goods = {
            1: IronFangBlade(),
            2: KnightsEdge(),
            3: TitanSlayer(),
            4: StaffOfWisdom(),
            5: ArcaneOrb(),
            6: EnchantedCloak(),
            7: HealthPotion(),
            8: ManaPotion(),
            9: StaminaPotion()
        }

    def show_items(self):
        """Display merchant's available items with prices."""
        print("Merchant : Here you go, these are my masterpieces - ")
        for key, value in self.goods.items():
            print(f"\t{key} - {value.name} - {value.price} golds")

    def __str__(self):
        return f"Name : {self.name}\nOccupation : {self.occupation}\ndescription : All ways eager to sell something"


class DescriptiveNPC(NPC):
    """Generic NPC for room descriptions and hints."""
    
    def __init__(self):
        super().__init__(name="Unknown", occupation="Unknown")


class QuestNPC(NPC):
    """Special quest-related NPC for boss room access."""
    
    def __init__(self):
        super().__init__(name="Ravemir, the Crimson Vowkeeper", occupation="Eternal Sentinel of the Blood Gate")