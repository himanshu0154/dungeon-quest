from items_main import StaffOfWisdom
from items_main import TitanSlayer
from items_main import IronFangBlade
from items_main import KnightsEdge
from items_main import ArcaneOrb
from items_main import EnchantedCloak
from items_main import HealthPotion
from items_main import StaminaPotion
from items_main import ManaPotion
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

# =============================== Character Class ====================================================================================

# This is the character class which is the base class from which MainCharacter and Enemies Classes will inherit
class Character():
    def __init__(self, name, character_class, max_health, current_health, strength, intelligence, max_mana, current_mana, max_stamina, current_stamina ):
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


# ============================== Main Character Class ==================================================================================  

# This is the MainCharacter Class which inherites from Character Class
class MainCharacter(Character):
    def __init__(self, name, character_class):
        super().__init__(name, character_class, max_health = 100, current_health = 100, strength = 0, intelligence = 0, max_mana=0, current_mana= 0, max_stamina  = 0, current_stamina = 0  )
        self.lvl = 1
        self.experience = 0
        self.inventory = []
        self.skills = set()
        self.stat_points = 0
        self.gold = 0
        self.status_effect = None
        self.status_duration = 0
        self.weapon = None
        self.location = None
        self.location_discovered = []
        self.chest = []
        self.boss_defeated = "undefeated"
        self.previous_room = None


    @classmethod
    def from_dict(cls, data):
        # This func sets the info from the data_main.json
        obj = cls(data["name"], data['character_class'])
        obj.max_health = data["max health"]
        obj.current_health = data["current health"]
        obj.strength = data["strength"]
        obj.intelligence = data['intelligence']
        obj.max_mana = data['max mana']
        obj.current_mana = data['current mana']
        obj.max_stamina = data["max stamina"]
        obj.current_stamina = data["current stamina"]
        obj.inventory = data["inventory"]
        obj.skills = set(data.get('skills', []))  # Convert list to set
        obj.lvl = data['lvl']
        obj.experience = data['experience']
        obj.stat_points = data['stat_points']
        obj.gold = data['gold']
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
        # This func is used to update the data_main.json
        return {
            "name": self.name,
            "character_class": self.character_class,
            "max health": self.max_health,
            "current health": self.current_health,
            "strength": self.strength,
            "intelligence" : self.intelligence,
            "max mana" : self.max_mana,
            "current mana" : self.current_mana,
            "max stamina": self.max_stamina,
            "current stamina": self.current_stamina,
            "inventory": self.inventory,
            "skills": list(self.skills),
            "lvl" : self.lvl,
            "experience" : self.experience,
            "stat_points" : self.stat_points,
            "gold" : self.gold,
            "status_effect" : self.status_effect,
            "status_duration" : self.status_duration,
            "weapon" : self.weapon,
            "location" : self.location,
            "location discovered" : self.location_discovered,
            "chest founded" : self.chest,
            "boss defeated" : self.boss_defeated,
            "previous room" : self.previous_room
        }
    def __str__(self):
        return f"System : | Name : {self.name}\n\t | Class : {self.character_class}\t\t\tgold : {self.gold}\n\t | Level : {self.lvl}\t\t\tExperience Points : {self.experience}\n\t | Health : {self.current_health}\t\t\tMana : {self.current_mana}\n\t | Strength : {self.strength}\t\t\tSkills : {list(self.skills)}\n\t | Intelligence : {self.intelligence}\t\tInventory : {self.inventory}\n\t | Stamina : {self.current_stamina}\t\t\tStat Points : {self.stat_points}"
    

# ==================================================== Enemies Class ==================================================================
#This is the Enemies Class which also inherites from the Character Class
class Enemies(Character):
    def __init__(self, name, strength, health, mana, drop, drop_price):
        super().__init__(name,strength, health, mana)
        self.drop = drop
        self.drop_price = drop_price

# =================================================== Monster class ===================================================================

class Monsters():
    def __init__(self, name, health, drop, exp):
        self.name = name
        self.health = health
        self.drop = drop
        self.exp = exp

    def __str__(self):
        return f"System : | Name : {self.name}\n\t | Health : {self.health}"

# =================================================== Kobold ==========================================================================

rusty_shiv = RustyShiv()
pocket_flame = PocketFlame()

class KoboldMonster(Monsters):
    def __init__(self):
        super().__init__(name = "Kobold", health = 100, drop = "Kobold Stone", exp = 200)
        self.skills = [rusty_shiv, pocket_flame]

# ================================================== Skeleton ========================================================================

bone_pierce = BonePierce()
rattle_hex = RattleHex()

class Skeleton(Monsters):
    def __init__(self):
        super().__init__(name = "Skeleton", health = 100, drop = "Skeleton's ash", exp = 100)
        self.skills = [bone_pierce, rattle_hex]

# ==================================================== Lizardmen =====================================================================

tail_whip = TailWhip()
venomous_spit = VenomousSpit()

class LizardMen(Monsters):
    def __init__(self):
        super().__init__(name = "Lizard Men",  health = 100 , drop = "Lizardmen's scales", exp = 400)
        self. skills = [tail_whip, venomous_spit]

# ==================================================== Orc ===========================================================================

brutal_smash = BrutalSmash()
skull_breaker = Skullbreaker()

class Orc(Monsters):
    def __init__(self):
        super().__init__(name = "Orc", health = 100, drop = "Orc Meat",  exp = 500)
        self.skills = [brutal_smash, skull_breaker]

# =================================================== Boss Monster ===================================================================

blood_drain = BloodDrain()
crimson_howl = CrimsonHowl()
shadow_burst = ShadowBurst()

class VampireLord(Monsters):
    def __init__(self):
        super().__init__(name = "Vehraxis the Crimson Wane", health = 200, drop = "Crimson Fang", exp = 1000)
        self.skills = [blood_drain, crimson_howl, shadow_burst]

# ==================================================== NPC's Class ====================================================================
#This is a NPC class it doesnt inherites from any class

class NPC():
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

# ==================================================== Items for merchant to sell =====================================================

iron_fang_blade = IronFangBlade()
knights_edge = KnightsEdge()
titan_slayer = TitanSlayer()
staff_of_wisdom = StaffOfWisdom()
arcane_orb = ArcaneOrb()
enchanted_cloak = EnchantedCloak()
health_potion = HealthPotion()
stamina_potion = StaminaPotion()
mana_potion = ManaPotion()

# ====================================================== Merchant ======================================================================

class Merchant(NPC):
    def __init__(self):
        super().__init__(name = "Merchant Todd", occupation = "Merchant")
        self.goods = {
            1: iron_fang_blade,
            2: knights_edge,
            3: titan_slayer,
            4: staff_of_wisdom,
            5: arcane_orb,
            6: enchanted_cloak,
            7: health_potion,
            8: mana_potion,
            9: stamina_potion
        }

    def show_items(self):
        print("Merchant : Here you go, these are my masterpieces - ")
        for key, value in self.goods.items():
            print(f"\t{key} - {value.name} - {value.price} golds")

    def __str__(self):
        return f"Name : {self.name}\nOccupation : {self.occupation}\ndescription : All ways eager to sell something"


class DescriptiveNPC(NPC):
    def __init__(self):
        super().__init__(name = "Unkown", occupation = "Unknown")

class QuestNPC(NPC):
    def __init__(self):
        super().__init__(name = "Ravemir, the Crimson Vowkeeper", occupation = "Eternal Sentinel of the Blood Gate")


     
