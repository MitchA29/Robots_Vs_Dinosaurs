from weapons import Weapon

class Robot:
    def __init__(self, name) -> None:
        self.name = ""
        self.health = 0
        self.weapon = Weapon()

    def attack (self, dinosaur):
        pass