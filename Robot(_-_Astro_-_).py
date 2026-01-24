import numpy as np

class RobotIA:
    def __init__(self, nom, x, y):
        self.nom = nom
        self.position = np.array([float(x), float(y)])
        self.vitesse = 0.0

    def calcul_distance(self, cible_x, cible_y):
        cible = np.array([float(cible_x), float(cible_y)])
        return np.linalg.norm(cible - self.position)

    def scanner(self, dist_obs):
        # Cette méthode analyse la distance pour le robot
        if dist_obs < 1:
            return "STOP"
        elif 1 <= dist_obs <= 5:
            return "RALENTIR"
        else:
            return "OK"

    def piloter(self, dist_obs):
        # Cette méthode donne l'ordre au robot après un scannage
        ordre = self.scanner(dist_obs)
        if ordre == "STOP":
            print(f"!!! {self.nom} : Obstcale en vue !!!")
            self.reculer(0, 1)
        elif ordre == "RALENTIR":
            print(f"{self.nom} : Évite l'obstacle...")
            self.avancer(1, 0.5)
        else:
            print(f"{self.nom} : Route libre.")
            self.avancer(0, 2)

    def avancer(self, x, y):
        self.vitesse = 1.0
        self.position += np.array([float(x), float(y)]) * self.vitesse
        print(f"Position actuelle : {self.position}")

    def reculer(self, x, y):
        self.vitesse = 0.5
        self.position -= np.array([float(x), float(y)]) * self.vitesse
        print(f"Position actuelle : {self.position}")

print("-------------- TEST --------------")

mon_robot = RobotIA("Wall-E", 0, 0)
# Simulation d'un obstacle à 3 mètres
mon_robot.piloter(3)