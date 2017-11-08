#Ecrire un algorithme qui demande successivement 5 nombres à l’utilisateur, et qui lui dise ensuite quel était le plus grand parmi ces 5 nombres et sa position
def decroissant_max(liste):
    ma_liste2 = sorted(liste, reverse=True)
    text = ma_liste2[0]
    return text

ma_liste = list()
i=0
while i<5:
      ma_liste.append(input("Nombre : "))
      i += 1

print("Le plus grand nombre est : ",decroissant_max(ma_liste))
