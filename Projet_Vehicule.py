#La class véhicule
import numpy as np

class Vehicule:

    def __init__(self, marque, annee):
        self.marque = marque
        self.annee = annee
        self.vitesse = 0
        self.position = np.array([0, 0])

    def accelerer(self, augmentation):
        self.vitesse += augmentation
        print(f"{self.marque} accélère à {self.vitesse} km/h")

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

jimny = Vehicule("Suzuki Jimny", 2024)

jimny.accelerer(40)
jimny.avancer(10, 5)
jimny.activer_4x4()
jimny.afficher_etat()
