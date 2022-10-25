#Edward Grau
#TP2 #2
#gr.401
from random import randint


def jeux():
    global nb_essais +
    nombre = randint(0,100)
    nb_essais = 0
    print(str(nombre))
    print("J’ai choisi un nombre au hasard entre 1 et 100. À vous de le deviner...")
    game(nombre)


def game(nombre):
    global nb_essais
    Essai = int(input("Entrez votre essai : "))
    nb_essais += 1

    if Essai > nombre:
        print("Mauvais choix, le nombre est plus petit que : " + str(Essai))
        print("Nombre d'éssais : " + str(nb_essais))
        print('réessaye')
        game(nombre)



    elif Essai < nombre:
        print("Mauvaise réponse, le nombre est plus grand que : " + str(Essai))
        print("Nombre d'éssais : " + str(nb_essais))
        print('réessaye')
        game(nombre)


    elif Essai == nombre:
        print("Bravo! Bonne réponse")
        print('Vous avez réussi en : ' + str(nb_essais))
        replay = input('Veux-tu rejouer? (y/n)')

        if replay == 'y':
           jeux()

        elif replay == 'n':
            print("Au revoir...")

        else:
            print("input invalide")


jeux()
