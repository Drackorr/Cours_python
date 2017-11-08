#Supprimer toutes les voyelles d'un chaîne de caractères

def vid_var(phrase):
    phrase = (phrase.replace("a", ""))
    phrase = (phrase.replace("e", ""))
    phrase = (phrase.replace("y", ""))
    phrase = (phrase.replace("u", ""))
    phrase = (phrase.replace("i", ""))
    phrase = (phrase.replace("o", ""))
    phrase = (phrase.replace("A", ""))
    phrase = (phrase.replace("E", ""))
    phrase = (phrase.replace("Y", ""))
    phrase = (phrase.replace("U", ""))
    phrase = (phrase.replace("I", ""))
    phrase = (phrase.replace("O", ""))

    return phrase

var1 = input('ecrire votre phrase : ')


print(vid_var(var1))