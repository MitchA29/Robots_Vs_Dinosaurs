from robot import Robot

class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet (self):
        robot1 = Robot("Brenard", 100, 0)
        self.robots.append(robot1)

        robot2 = Robot("Harry", 150, 1)
        self.robots.append(robot2)

        robot3 = Robot("Jan", 115, 2)
        self.robots.append(robot3)
