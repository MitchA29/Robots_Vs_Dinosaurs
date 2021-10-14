from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd (self):
        dino1 = Dinosaur("Greg", 50, 100)
        self.dinosaurs.append(dino1)

        dino2 = Dinosaur("Susan", 50, 100)
        self.dinosaurs.append(dino2)

        dino3 = Dinosaur("Beatrice", 50, 100)
        self.dinosaurs.append(dino3)