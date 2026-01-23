import numpy as np

class RobotIA :
    def __init__(self, nom, x, y):
        self.nom = nom
        self.position = np.array(float(x), float(y))

    def calcul_distance(self,cible_x, cible_y):
        cible = np.array(float(cible_x), float(cible_y))
        vecteur_distance = cible - self.position
        distance_reelle = np.linalg.norm(vecteur_distance)

        return distance_reelle

print("--------------TEST--------------")

mon_robot = RobotIA("Wall-E",0, 0)
dist = mon_robot.calcul_distance(10, 10)

print(f"Le robot se nomme {mon_robot} est à {dist:2f} mètres de la cible")