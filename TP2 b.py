#Edward Grau
#TP2 #2
#gr.401
from random import randint


def jeux(): #loop qui recommence le jeux
    global nb_essais
    nombre = randint(0,100)
    nb_essais = 0
    print("J’ai choisi un nombre au hasard entre 1 et 100. À vous de le deviner...")
    game(nombre)


def game(nombre): #loop qui commence une devinette
    global nb_essais
    Essai = int(input("Entrez votre essai : ")) #prendre l'input de l'utilisateur
    nb_essais += 1 #augmenter le nombre d'essais

    if Essai > nombre: #si la devinette est trop grand
        print("Mauvais choix, le nombre est plus petit que : " + str(Essai))
        print("Nombre d'éssais : " + str(nb_essais))
        print('réessaye')
        game(nombre) #redeviner



    elif Essai < nombre: #l'essais est trop petit
        print("Mauvaise réponse, le nombre est plus grand que : " + str(Essai))
        print("Nombre d'éssais : " + str(nb_essais))
        print('réessaye')
        game(nombre) #redeviner


    elif Essai == nombre:
        print("Bravo! Bonne réponse")
        print('Vous avez réussi en : ' + str(nb_essais))
        replay = input('Veux-tu rejouer? (y/n)')

        if replay == 'y':
           jeux() #refaire le jeux avec un nouveau chiffre

        elif replay == 'n':
            print("Au revoir...")

        else:
            print("input invalide")


jeux()
