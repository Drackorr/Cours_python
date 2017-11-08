#Ecrire un algorithme qui demande successivement 5 nombres à l’utilisateur, et qui lui dise ensuite quel était le plus grand parmi ces 5 nombres et sa position

ma_liste = list()
i=0
while i<5:
      ma_liste.append(input("Nombre : " ))
      i += 1

print(ma_liste)
ma_liste2 = sorted(ma_liste, reverse=True)
print(ma_liste2)
print("Le plus grand nombre est : ",ma_liste2[0])
