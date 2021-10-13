from dinosaur import Dinosaur
class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd (self):
        dino1 = Dinosaur ("Gertie", 25)
        self.dinosaurs.append(dino1)
        dino2 = Dinosaur ("Bruce", 40)
        self.dinosaurs.append(dino1)
        dino3 = Dinosaur ("Greg", 30)
        self.dinosaurs.append(dino1)