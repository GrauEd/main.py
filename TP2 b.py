#Edward Grau
#TP2 #2
#gr.401

print("J’ai choisi un nombre au hasard entre 1 et 100. À vous de le deviner...")

nombre = randint(0,100)
Essai = input("Entrez votre essai : ")

if devine < nombre:
    print("Mauvais choix, le nombre est plus petit que" + Essai)
    input("Entrez votre essai : ")

elif devine > nombre:
    print("Mauvaise réponse, le nombre est plus grand que" + Essai)
    input("Entrez votre essai : ")

elif devine == nombre