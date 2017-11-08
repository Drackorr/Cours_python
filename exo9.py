#Déterminer si un mot est un palindrome
def palin_ou_pas(mot):
    mon_mot_inverse = ""  # mot inverser
    for lettre in reversed(mot):
        mon_mot_inverse += lettre

    if mon_mot == mon_mot_inverse:
        text = mot + " est un palindrome"
        return text
    else:
        text = mot + " n'est pas un palindrome"
        return text


mon_mot = input("votre mot : ")

print(palin_ou_pas(mon_mot))

