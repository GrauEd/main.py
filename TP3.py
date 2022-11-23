#Edward Grau
#Groupe 401.
#TP3 - combat des monstres
from random import randint

def settings():

    global streak
    #commencer la suite de combats a 0
    streak = 0
    global  niveau_vie
    #commencer avec 20 pv
    niveau_vie = 20




def jeu(niveau_vie):
    #force du monstre aléatoire
    force_adversaire = randint(1,6)
    #indiquer la fifficulté a l'utilisateur
    print("Vous tombez face à face avec un adversaire de difficulté :" + str(force_adversaire))

    #donner le chiox d'actions a l'utilisater
    menu = int(input("""Que voulez-vous faire ? 
            1- Combattre cet adversaire
	        2- Contourner cet adversaire et aller ouvrir une autre porte
	        3- Afficher les règles du jeu
	        4- Quitter la partie"""))


        #premier choix
    if menu == 1:
        print(str(niveau_vie))

        #dé entre 1 et 6
        de = randint(1,6)


            #echoe
            if de <= force_adversaire:
                print("Le monstre vous a gravement blessé. Vous perdez 4 points de vie")
                niveau_vie -= 4
                streak = 0


                print(str(niveau_vie))
                #victoire
            elif de >= force_adversaire:
                print("Vous avez vaincu le monstre. Vous buvez son élixir magique et gagnez 4 points de vie")
                niveau_vie += 4
                streak += 1
                print("Vous avez maintenant " + str(niveau_vie) + " poinnts de vie")
                print("Vous avez gagné" + str(streak) + "combat(s) de suite")

        #deuxième choix
    elif menu == 2:
        print("Votre honneur est blessé. En conséquence, vous perdez un point de vie")
        niveau_vie =-1
        print(niveau_vie)

        #troisième choix
    elif menu == 3:
        print("""Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas,
            le niveau de vie de l’usager est augmenté de la force de l’adversaire.
            Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.
            Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.
            La partie se termine lorsque les points de vie de l’usager tombent sous 0.
            L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.""")



        #quatrième choix
    elif menu == 4:
        print("Merci et au revoir... ")

jeu(niveau_vie)