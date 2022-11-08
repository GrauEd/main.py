#Edward Grau
#TP2 #2
#gr.401
from random import randint

#loop qui recommence le jeux
def jeux():
    #donner le choix de choisir les bornes de la devinette
    bornes = int(input ("Voulez-vous choisir vos bornes de la devinette? 1(oui) 2(non)"))
    if bornes == 1:
        #borne 1
        C1 = int(input("inscrivez votre première borne"))
        #borne 2
        C2 = int(input("inscrivez votre deuxième borne"))
        nombre = randint(C1,C2)
        print("J’ai choisi un nombre au hasard entre " + str(C1) + " et " + str(C2) + ". À vous de le deviner...")
    elif bornes != 1:
        nombre = randint(0, 100)
        print("J’ai choisi un nombre au hasard entre 1 et 100. À vous de le deviner...")
    #réinitialiser le nombre de "guess" après chaque partie
    global nb_essais
    nb_essais = 0

    game(nombre)

#loop qui commence une devinette
def game(nombre):
    global nb_essais
    # prendre l'input de l'utilisateur
    Essai = int(input("Entrez votre essai : "))
    # augmenter le nombre d'essais
    nb_essais += 1
    # si la devinette est trop grand
    if Essai > nombre:
        print("Mauvais choix, le nombre est plus petit que : " + str(Essai))
        print("Nombre d'éssais : " + str(nb_essais))
        print('réessaye')
        # redeviner
        game(nombre)


    # l'essais est trop petit
    elif Essai < nombre:
        print("Mauvaise réponse, le nombre est plus grand que : " + str(Essai))
        print("Nombre d'éssais : " + str(nb_essais))
        print('réessaye')
        # redeviner
        game(nombre) #redeviner

    #bonne réponse
    elif Essai == nombre:
        print("Bravo! Bonne réponse")
        print('Vous avez réussi en : ' + str(nb_essais))
        replay = input('Veux-tu rejouer? (y/n)')

        # refaire le jeux avec un nouveau chiffre
        if replay == 'y':
           jeux()

        # terminer la partie
        elif replay == 'n':
            print("Au revoir...")

        #réponse invalide
        else:
            print("input invalide")


jeux()
