#Ecrire un programme qui demande à l'utilisateur un nombre entier et lui affiche si ce nombre est un nombre pair
def pair_impair(entier):
    """Fonction qui verifie si le le nombre est pair ou impair"""
    if nbre % 2:
        text ='nombre impair'
        return text
    else:
        text ='nombre pair'
        return text
    return

nbre = int(input('ecrire un nombre entier : '))

print(pair_impair(nbre))