#Demander à l'utilisateur un nom de balise et un contenu de cette balise, et afficher le code html : ex: balise : "i", texte : "mot" --> <i>mot</i>
balise = input("ecrire nom de balise : ")
contenu_balise = input('ecrire le contenu de votre balise : ')

print('<',balise,'>',contenu_balise,'<','/',balise,'>')