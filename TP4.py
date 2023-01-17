#Edward Grau
#Groupe 401
#TP3 Combat des monstres 1


from random import randint
#établir les variables
streak = 0
niveau_vie = 20
wincount = 0
losscount = 0
monsternumber = 1
numeropartie = 0


def jeu():
    global wincount,streak,monsternumber,niveau_vie,numeropartie,losscount
    #force du monstre difficile
    if streak > 3:
        print("Attention! Le boss approche!")
        force_adversaire =  randint(6,12)
    #force du monstre normal
    else:
        force_adversaire = randint(1, 12)

    #indiquer la fifficulté a l'utilisateur
    print("Vous tombez face à face avec un adversaire de difficulté :" + str(force_adversaire))

    #donner le chiox d'actions a l'utilisater
    menu = input("""Que voulez-vous faire ? 
            1- Combattre cet adversaire
	        2- Contourner cet adversaire et aller ouvrir une autre porte
	        3- Afficher les règles du jeu
	        4- Quitter la partie
	        input: """)


    #premier choix
    if menu == '1':
        # dé entre 1 et 6
        #premier de
        de = randint(1, 6)
        #deuxieme de
        dedeux = randint(1,6)
        #les deux des ensemble
        definal = de + dedeux

        print("Adversaire: " + str(monsternumber) +
              " Force de l'adversaire: " + str(force_adversaire) +
              " Niveau de vie de l'utilisateur: " + str(niveau_vie) +
              " Record de combat: Pertes:" + str(losscount) + " Victoires: " + str(wincount) + " Nombre de parties: " + str(numeropartie))
        print("Lancer du dé : " + str(definal))




        #echoue

        if definal <= force_adversaire:
            print("Le monstre vous a gravement blessé. Vous perdez 4 points de vie")
            # modifie les variables en accordanceavec le résultat
            niveau_vie -= 4
            monsternumber = monsternumber + 1
            numeropartie = numeropartie + 1
            losscount = losscount + 1
            streak = 0
            print("Vous avez maintenant " + str(niveau_vie) + " poinnts de vie")
            if niveau_vie == 0:
                print("La partie est terminé, vous avez vaincu " + str(wincount) + " monstres(s)")
            else:
                jeu()

        #victoire
        elif definal > force_adversaire:
            print("Vous avez vaincu le monstre. Vous buvez son élixir magique et gagnez 4 points de vie")
            # modifie les variables en accordanceavec le résultat
            niveau_vie += 4
            monsternumber = monsternumber + 1
            numeropartie = numeropartie + 1
            streak += 1
            print("Vous avez maintenant " + str(niveau_vie) + " poinnts de vie")
            print("Vous avez gagné " + str(streak) + " combat(s) de suite")

            jeu()


    #deuxième choix
    elif menu == '2':
        print("Votre honneur est blessé. En conséquence, vous perdez un point de vie")
        #modifie les variables en accordanceavec le résultat
        niveau_vie = niveau_vie - 1
        monsternumber = monsternumber + 1
        numeropartie = numeropartie + 1
        streak = 0
        print(niveau_vie)
        #terminer la partie
        if niveau_vie == 0:
            print("La partie est terminé, vous avez vaincu " + str(wincount) + " monstres(s)")
        #recommencer le jeu
        else:
            jeu()


    #troisième choix
    elif menu == '3':
        print("""Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas,
            le niveau de vie de l’usager est augmenté de la force de l’adversaire.
            Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.
            Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
            La partie se termine lorsque les points de vie de l’usager tombent sous 0.
            L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.""")
        jeu()



    #quatrième choix
    elif menu == '4':
        print("Merci et au revoir... ")





jeu()

class StringFoo:
    def __init__(self):
        self.string = string

    def set_string(self, string):
        self.string = string

    def print_string(self):
        print(self.string.upper())


StringFoo.print_string()




















from dataclases import dataclass

class Person:
    def __init__(self):
        self.name = ''

ornel = Person()
ornel.name = "Ornel"
ornel = Person()
audrey.name = "Audrey"

print(ornel.name)
print(audrey.name)

class NPC:
    def __init__(self):
        self.stats = NPCStats(9,1)

t = NPC(
    print()
)