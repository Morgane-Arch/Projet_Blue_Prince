class Inventaire:
    def __init__(self):
        self.objets = []

    def ajouter(self, objet):
        self.objets.append(objet)

    def retirer(self, objet):
        if objet in self.objets:
            self.objets.remove(objet)

    def utiliser(self, objet, joueur):
        if objet in self.objets:
            objet.consommer(joueur)
            self.retirer(objet)

    def lister(self):
        return [obj.nom for obj in self.objets]
