from weapons import Weapon

class Robot:
    def __init__(self, name, health, num):
        self.name = name
        self.health = health
        self.weapons = []
        self.make_weapons()
        self.weapon = self.weapons[num]
        
    def attack (self, dinosaur):
        pass

    def make_weapons (self):
        weapon1 = Weapon("sword", 40)
        weapon2 = Weapon("Lazer", 60)
        weapon3 = Weapon("chainsaw", 35)
        self.weapons.append(weapon1)
        self.weapons.append(weapon2)
        self.weapons.append(weapon3) 