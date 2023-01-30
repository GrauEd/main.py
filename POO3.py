#Edward Grau
#gr.401
#Exercises POO 2

from random import *
def de():
    variable = [random.randint(1, 6) for _ in range(4)]
    variable.sort()
    variable = variable[:3]
    return sum(variable)
class NPC:
    def __init__(self):

        #Force
        self.f = de()

        #Agilité
        self.a = de()

        #Constitution
        self.co = de()

        #Intelligence
        self.i = de()

        #Sagesse
        self.s = de()

        #Charisme
        self.ca = de()

        #classe d’armure (1d12)
        self.armure = random.randint(1, 12)

        #nom (chaîne de caractères)
        self.nom = str

        #race (chaîne de caractères)
        self.race = str

        #espèce (chaîne de caractères)
        self.espece = str

        #point de vie (d20)
        self.pv = 20

        #profession (guerrier, voleur, etc.) (chaîne de caractères)
        self.profession = str


    def printStat(self):
        print("Sa force est: ", self.f)
        print("Son agilité est: ", self.a)
        print("Sa constitution est: ", self.co)
        print("Son intelligence est: ", self.i)
        print("Sa sagesse est: ", self.s)
        print("Son charisme est: ", self.ca)
        print("Sa classe d'armure est: ", self.armure)
        print("Son nom est: ", self.nom)
        print("Sa race est: ", self.race)
        print("Son espèce est: ", self.espece)
        print("Ses pv sont: ", self.pv)
        print("Sa profession est: ", self.profession)

class Kobold(NPC):
    def __init__(self):
        super().__init__()
    def atttaque(self, cible = NPC):
        return

    def subir_des_dommages(self, dmg):
        self.pv -= dmg




class Hero(NPC):
    def __init__(self):
        super().__init__()
    def atttaque(self, cible=NPC):
        r_de = random.randint(1, 20)

        if r_de == 20:
            cible.subir_des_dommages(random.randint(1, 8))

        elif r_de(2, 19) >= cible.armure:
            cible.subir_des_dommages(random.randint(1, 6))

        else:
            cible.subir_des_dommages(0)

    def subir_des_dommages(self, dmg):
        return


h = Hero()
k = Kobold()
h.afficher_caracteristiques()
k.attaquer(h)
h.afficher_caracteristiques()
