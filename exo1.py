score = 0
verif = True

nom_joueur = input('saisissez votre nom : ')

while verif:

    score = input('saisir dernier score : ')

    if score.isdigit():
        score = int(score) + 1
        print(nom_joueur, "a obtenu", score, "points.")
        verif = False
    else:
        print("erreur !!!!")
        verif = True
