#-- coding: utf-8 --
class Humain:
    """Classe qui regroupe les humains"""
    espece = 'Homo Sapiens Sapien'

    def __init__(self,nom, sexe):
        self.nom = nom
        self.sexe = sexe
        self.enfants = list()

    def se_presenter(self):
        """Méthode qui dit a l'objet de se présenter """
        genre = 'un homme' if self.sexe == 'm' else 'une femme'
        pres = "Je m'appelle " + self.nom + " et je suis " + genre
        return pres

    def add_enfnats(self,liste_enfants):
        self.enfants.append(liste_enfants)

    def set_mensurations(self,liste_mens):
        self.set_mensurations = liste_mens

    def rencontrer(self, humain):
        dialogue1 = self.nom + " dit : bonjour " + humain.nom + " !"
        dialogue2 = humain.nom + " repond : Bonjour " + self.nom + " !"
        return print(dialogue1,"\n",dialogue2)


class Piece:
    """Classe qui regroupe les humains dans la piece"""
    def __init__(self,nom):
        self.nom = nom
        self.humains = list()

    def ajouter_humains(self,liste_humains):
        self.humains += liste_humains
        print("Humains ajoutés dans le", self.nom)



liste_dimension = [10, 7, 3]



adam = Humain("Adam","m")
eve = Humain("Eve","f")
abel = Humain('Abel', 'm')
salon = Piece('salon')
print('Cette pièce est un '+ salon.nom)
salon.ajouter_humains([adam,abel])


print(adam.rencontrer(eve))





