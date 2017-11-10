#-- coding: utf-8 --
with open('20000.txt','r',encoding='utf8') as fichier:
    f = fichier.read()
    #print(f)


def nettoyer_texte(texte):
    texte = texte.lower()
    car_spec = ",.!?()_\";:"
    for lettre in texte:
        if lettre in car_spec:
            texte = texte.replace(lettre,'')
    for car in ['\n',"'",'-','--']:
        texte = texte.replace(car,' ')
    texte = texte.replace('\n',' ')
    texte = texte.replace("'", ' ')
    return texte

def texte_en_liste(texte):
    liste_de_mots = texte.split(' ')
    liste_de_mots = list(filter(None,liste_de_mots))
    return liste_de_mots

def compter_mots_unique(liste):
    liste_de_mots_uniques = list(set(liste))
    return len(liste_de_mots_uniques)


texte_nettoyer = nettoyer_texte(f)
liste_de_mots = texte_en_liste(texte_nettoyer)
nb_mots = len(liste_de_mots)
nb_mots_uniques = compter_mots_unique(liste_de_mots)

print(nb_mots)
print(nb_mots_uniques)