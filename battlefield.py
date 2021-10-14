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
            print (x)
        print (" ")
        print ("Team Dinos: ")
        for x in self.herd.dinosaurs:
            print (x)
        print ("__________________________________________")
        print ("Begin battle!")
        print (" ")
        self.battle()

    # def battle (self):
    #     while (len(self.herd.dinosaurs) > 0) and (len(self.fleet.robots) > 0):
    #         self.dino_turn (self.herd.dinosaurs[0])
    #         self.robo_turn (self.fleet.robots[0])
    #         pass
       
        

    def dino_turn (self, dinosaur):
        print (str(dinosaur) + " attacks " + str(self.fleet.robots[0]))


    def robo_turn (self, robot):
        print (str(robot) + " attacks " + str(self.herd.dinosaurs[0]))

    def show_dino_opponent_options (self):
        pass

    def show_robo_opponent_options (self):
        pass

    def display_winners (self):
        if (len(self.herd.dinosaurs == 0)):
            print ("Robots win!")
        elif (len(self.fleet.robots == 0)):
            print ("Dinos win!")
        else:
            print ("Error with finding who wins.")
