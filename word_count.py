#Edward Grau gr.401
#word_count

#permet à l'utilisateur d'écrire la phrase
phrase = input("Ecrivez une phrase: ")

#afficher la phrase du input
print("votre phrase est : " + phrase)

#prend l`input et envoit le nombre de mots des mots à l'utilisateur
def word_count(phrase):
    return len(phrase.split())

#imprime le nombre de mots en string
mots = word_count(phrase)
print("le nombre de mots est : " + str(mots))