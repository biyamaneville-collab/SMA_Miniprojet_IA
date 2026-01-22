#La class véhicule
import numpy as np

class Vehicule:

    def __init__(self, marque, annee,color):
        self.marque = marque
        self.annee = annee
        self.vitesse = 0
        self.position = np.array([0, 0])
        self.color = color

    def accelerer(self, augmentation):
        self.vitesse += augmentation
        print(f"{self.marque} accélère à {self.vitesse} km/h")

    def freiner(self, frein):
        self.vitesse -= frein
        if self.vitesse < 0:
            self.vitesse = 0
        print(f"{self.marque} freine de {frein} km/h")

    def avancer(self, x, y):
        mouvement = np.array([x, y])
        self.position += mouvement
        print(f"Position actuelle : {self.position}")

    def activer_4x4(self):
        print(f"{self.marque} active le mode 4x4")

    def afficher_etat(self):
        print(f"{self.marque} ({self.annee})")
        print(f"Vitesse : {self.vitesse} km/h")
        print(f"Position : {self.position}")
        print(f"Couleur : {self.color}")

suzuki_jimmy = Vehicule("Suzuki Jimny", 2024, "Blue")

suzuki_jimmy.accelerer(40)
suzuki_jimmy.avancer(10, 5)
suzuki_jimmy.activer_4x4()
suzuki_jimmy.afficher_etat()
suzuki_jimmy.freiner(10)