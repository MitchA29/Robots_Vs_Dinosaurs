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
        print ("Team Robots: ")
        for x in self.fleet.robots:
            print (x.name)
        print (" ")
        print ("Team Dinos: ")
        for x in self.herd.dinosaurs:
            print (x.name)
        print ("__________________________________________")
        print ("Begin battle!")
        print (" ")
        self.battle()

    def battle (self):
        while (len(self.herd.dinosaurs) > 0) and (len(self.fleet.robots) > 0):
            self.dino_turn (self.herd.dinosaurs[0])
            if self.fleet.robots [0].health <= 0:
                print (self.herd.dinosaurs[0].name + " defeated " + self.fleet.robots[0].name)
                self.fleet.robots.pop[0]
                if len(self.fleet.robots) == 0:
                    self.display_winners()
            self.robo_turn (self.fleet.robots[0])
            if self.herd.dinosaurs [0].health <= 0:
                print (self.fleet.robots[0].name + " defeated " + self.herd.dinosaurs[0].name)
                self.herd.dinosaurs.pop[0]
                if len(self.herd.dinosaurs) == 0:
                    self.display_winners()
       
        

    def dino_turn (self, dinosaur):
        print (str(dinosaur.name) + " attacks " + str(self.fleet.robots[0].name))
        self.fleet.robots[0].health = self.fleet.robots[0].health - self.herd.dinosaurs[0].attack_power


    def robo_turn (self, robot):
        print (str(robot.name) + " attacks " + str(self.herd.dinosaurs[0].name))
        self.herd.dinosaurs[0].health = self.herd.dinosaurs[0].health - self.fleet.robots[0].weapon.attack_power


    # def show_dino_opponent_options (self):
    #     pass

    # def show_robo_opponent_options (self):
    #     pass

    # def display_winners (self):
    #     if (len(self.herd.dinosaurs == 0)):
    #         print ("Robots win!")
    #     elif (len(self.fleet.robots == 0)):
    #         print ("Dinos win!")
    #     else:
    #         print ("Error with finding who wins.")
        
