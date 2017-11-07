score = 0
nom_joueur = input('saisissez votre nom : ')
score = input('saisir dernier score : ')
verif = True

while verif:
    if score.isdigit():
        score = int(score) + 1
        print(nom_joueur, "a obtenu", score, "points.")
        verif = False
    else:
        print("erreur !!!!")

