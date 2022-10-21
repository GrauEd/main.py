#Edward Grau
#TP2 #2
#gr.401
from random import randint
nb_essais = 0
def jeux():
    nombre = randint(0,100)
    Essai = int(input("Entrez votre essai : "))
    print(str(nombre) + str(Essai))

    def game():
       print("J’ai choisi un nombre au hasard entre 1 et 100. À vous de le deviner...")

    global nb_essais
    if Essai != nombre:

        nb_essais += 1


        if Essai > nombre:
            print("Mauvais choix, le nombre est plus petit que : " + str(Essai))
            print("Nombre d'éssais : " + str(nb_essais))


        elif Essai < nombre:
            print("Mauvaise réponse, le nombre est plus grand que : " + str(Essai))
            print("Nombre d'éssais : " + str(nb_essais))

        elif Essai == nombre:
            print("Bravo! Bonne réponse")
            print('Vous avez réussi en : ' + str(nb_essais))

        replay = input('Veux-tu rejouer? (y/n)')

        if replay == 'y':
            game()

        elif replay == 'n':
            print("Au revoir...")

        else:
            print("input invalide")

jeux()