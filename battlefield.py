from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game (self):
        self.display_welcome()

    def display_welcome (self):
        print (" ")
        print ("Welcome to Robots Vs. Dinosaurs")
        print ("__________________________________________")
        print (" ")
        print ("Team Robots: ")
        print (" ")
        for x in self.fleet.robots:
            print (x.name)
            print ("Health: " + str(x.health))
            print ("Attack Power: " + str(x.weapon.attack_power))
            print (" ")
        print (" ")
        print ("Team Dinos: ")
        print (" ")
        for x in self.herd.dinosaurs:
            print (x.name)
            print ("Health: " + str(x.health))
            print ("Attack Power: " + str(x.attack_power))
            print (" ")
        print ("__________________________________________")
        print ("Begin battle!")
        print (" ")
        self.battle()

    def battle (self):
        while (len(self.herd.dinosaurs) > 0) and (len(self.fleet.robots) > 0):
            self.dino_turn (self.herd.dinosaurs[0])
            if self.fleet.robots [0].health <= 0:
                print (" ")
                print (self.herd.dinosaurs[0].name + " defeated " + self.fleet.robots[0].name)
                self.fleet.robots.pop(0)
                print (" ")
                if len(self.fleet.robots) == 0:
                    self.display_winners()
            self.robo_turn (self.fleet.robots[0])
            if self.herd.dinosaurs [0].health <= 0:
                print (" ")
                print (self.fleet.robots[0].name + " defeated " + self.herd.dinosaurs[0].name)
                self.herd.dinosaurs.pop(0)
                print (" ")
                if len(self.herd.dinosaurs) == 0:
                    self.display_winners()

    def dino_turn (self, dinosaur):
        print (str(dinosaur.name) + " attacks " + str(self.fleet.robots[0].name) + " for " + str(dinosaur.attack_power) + " damage!")
        self.fleet.robots[0].health = self.fleet.robots[0].health - dinosaur.attack_power

    def robo_turn (self, robot):
        print (str(robot.name) + " attacks " + str(self.herd.dinosaurs[0].name) + " for " + str(robot.weapon.attack_power) + " damage!")
        self.herd.dinosaurs[0].health = self.herd.dinosaurs[0].health - robot.weapon.attack_power

    def display_winners (self):
        if (len(self.herd.dinosaurs) == 0):
            print ("__________________________________________")
            print ("Robots win!")
            print (" ")
            exit()
        elif (len(self.fleet.robots) == 0):
            print ("__________________________________________")
            print ("Dinos win!")
            print (" ")
            exit()
        
