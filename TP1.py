#Edward Grau gr.401
#word_count

#permet à l'utilisateur d'écrire la phrase
phrase = input("Ecrivez une phrase: ")

#afficher la phrase du input
print("votre phrase est : " + phrase)

#compteur de mot
def word_count():
    return len(phrase.split())

#imprime le nombre de mots en string-
mots = wo+rd_count()
print("le nombre de mots est : " + str(mots))