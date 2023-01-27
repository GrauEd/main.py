#Edward Grau
#gr.401
#Exercises POO 2

from random import *

class NPC:
    def __init__(self):

        #Force
        self.f = (random.randint(1, 6) for _ in range(4))
        self.f.sort()
        self.f = self.f[:3]
        self.f = sum(self.f)

        #Agilité
        self.a = (random.randint(1, 6) for _ in range(4))
        self.a.sort()
        self.a = self.a[:3]
        self.a = sum(self.a)

        #Constitution
        self.co = (random.randint(1, 6) for _ in range(4))
        self.co.sort()
        self.co = self.co[:3]
        self.co = sum(self.co)

        #Intelligence
        self.i =  self.i = (random.randint(1, 6) for _ in range(4))
        self.i.sort()
        self.i = self.i[:3]
        self.i = sum(self.i)

        #Sagesse
        self.s = (random.randint(1, 6) for _ in range(4))
        self.s.sort()
        self.s = self.s[:3]
        self.s = sum(self.s)

        #Charisme
        self.ca = (random.randint(1, 6) for _ in range(4))
        self.ca.sort()
        self.ca = self.ca[:3]
        self.ca = sum(self.ca)

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
    def atttaque(self, cible = NPC):
        r_de = random.randint(1,20)

        if r_de == 20
            cible.subir_des_dommages(random.randint(0,8))

        elif r_de =>
    def subir_des_dommages(self, qte_dommage):
        self.d = random.randint(0,6)


class Hero(NPC):
    def atttaque(self, cible = NPC):
        self.cible = NPC

    def subir_des_dommages(self, dmg):
        self.pv -= dmg


hero1 = Hero("Bob", "Humain", "Homo sapiens", "Etudiant")
hero1.afficher_caracteristiques()

kobold1  = Kobold("Kob", "Kobold", "Monstre", "Joueur")
kobold1.afficher_caracteristiques()

kobold.attaquer(hero1)
hero1.subir_des_dommages()

hero1.attaquer(kobold)
kobold1.subir_des_dommages()