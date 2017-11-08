#Demander à l'utilisateur un nom de balise et un contenu de cette balise, et afficher le code html : ex: balise : "i", texte : "mot" --> <i>mot</i>
def html(bal, cont):
    text = '<'+bal+'>'+cont+'<'+'/'+bal+'>'
    return text

balise = input("ecrire nom de balise : ")
contenu_balise = input('ecrire le contenu de votre balise : ')

print(html(balise, contenu_balise))