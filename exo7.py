#Ecrire un algorithme qui demande successivement 5 nombres à l’utilisateur, et qui lui dise ensuite quel était le plus grand parmi ces 5 nombres et sa position

a = int(input('veuillez ecrire le premier nombre : '))
b = int(input('veuillez ecrire le deuxieme nombre : '))
c = int(input('veuillez ecrire le troisieme nombre : '))
d = int(input('veuillez ecrire le quatrieme nombre : '))
e = int(input('veuillez ecrire le cinquieme nombre : '))

ma_liste = [a, b, c, d, e]
ma_liste2 = sorted(ma_liste, reverse=True)
print(ma_liste2[0])
