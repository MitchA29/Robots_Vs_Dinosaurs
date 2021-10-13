from robot import Robot
from weapons import Weapon

class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet (self):
        robot1 = Robot("Brenard")
        robot1.heath = 100
        robot1.weapon = Weapon("sword", 50)
        Fleet.robots.append(robot1)

        robot2 = Robot("Harry")
        robot2.heath = 100
        robot2.weapon = Weapon("Lazer", 50)
        Fleet.robots.append(robot2)

        robot3 = Robot("Jan")
        robot3.heath = 100
        robot3.weapon = Weapon("chainsaw", 50)
        Fleet.robots.append(robot3)
