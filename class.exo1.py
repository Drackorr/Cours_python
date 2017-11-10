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

    def ajouter_enfant(self, enfant):
        """ Methode qui ajoute enfant a la liste des enfants de self"""
        self.enfants.append(enfant)
        return print(enfant.nom, 'a ete ajouté aux enfants de',self.nom)

adam = Humain("Adam","m")
eve = Humain("Eve","f")
abel = Humain('Abel', 'm')
adam.ajouter_enfant(abel)
print(adam.se_presenter())
print(adam.enfants[0].nom)
print(eve.se_presenter())
