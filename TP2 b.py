#Edward Grau
#TP2 #2
#gr.401
from random import randint

while True:
    print("J’ai choisi un nombre au hasard entre 1 et 100. À vous de le deviner...")
    nb_essais = 0
    nombre = randint(0,100)
    Essai = int(input("Entrez votre essai : "))
    nb_essais = nb_essais+1

    print(str(nombre)+str(Essai))
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
        continue

    elif replay == 'n':
        print("Au revoir...")
        break
    else:
        print("input invalide")
        break