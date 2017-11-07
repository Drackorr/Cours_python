#Déterminer si un mot est un palindrome
mon_mot = input("votre mot : ")
mon_mot_inverse = "" #mot inverser

for lettre in reversed(mon_mot):
    mon_mot_inverse += lettre

if mon_mot == mon_mot_inverse:
    print(mon_mot,"est un palindrome")
else:
    print(mon_mot,"n'est pas un palindrome")


