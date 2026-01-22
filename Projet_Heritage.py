import numpy as np

class Vehicule:

    def __init__(self, marque, annee, nombre_porte):
        self.marque = marque
        self.annee = annee
        self.nombre_porte = nombre_porte

    super().__init__(marque,annee)

    def klaxonner(self):
        print("Tuut Tuut Pi Piiii !!!")

    class Camion(Vehicule):

        def __init__(self, marque, annee, capacite_tonnes):
            super().__init__(marque,annee)
            self.capacite_tonnes
            self.charqement_actuel = 0

        def charger(self,poids):
            if(self.chargement_actuel + poids) <= self.capacite_tonnes:
                self.charqement_actuel += poids
                print(f"Chargé : {poids}t")
                print(f"Total : {self.chargement_actuel}t")
            else:
                print("Erreur : Trop lourd !")