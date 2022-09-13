#Edward Grau gr.401

#permet à l'utilisateur d'écrire la phrase
phrase = input("Ecrivez une phrase: ")

#afficher la phrase du input
print("votre phrase est : " + phrase)

#compteur de mot
word_count = len(phrase.split())

#afficher le nombre de mots en string
print("le nombre de mots est : " + str(word_count))
