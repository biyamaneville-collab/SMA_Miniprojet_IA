#Partie 1 : La classe Parente(Véhicule)

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

    def klaxonner(self):
        print("Tuut Tuut Pi Piiii !!!")

#Partie 2 : La classe Enfant(héritage)

        class Camion(Vehicule):

            def __init__(self, marque, annee, capacite_tonnes):
                super().__init__(marque, annee)
                self.capacite_tonnes = capacite_tonnes
                self.charqement_actuel = 0

            def charger(self, poids):
                if (self.chargement_actuel + poids) <= self.capacite_tonnes:
                    self.charqement_actuel += poids
                    print(f"Chargé : {poids}t")
                    print(f"Total : {self.chargement_actuel}t")
                else:
                    print("Erreur : Trop lourd !")

#Partie 3 : Exécution(Le Main)

if names == "main"

print("----------- SIMULATION ------------")

ma_ferrari = Vehicule("Ferrari",2024, "black")
mon_volo = Camion("Volvo",2020,20)

ma_ferrari.accelerer(100)
ma_ferrari.avancer(50,30)

mon_volo.accelerer(50)

ma_ferrari.klaxonner()
mon_volo.charger(15)
mon_volo.charger(10)