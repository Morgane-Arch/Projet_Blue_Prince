class ObjetPermanent:
    def __init__(self, nom):
        self.nom = nom

    def appliquer(self, joueur):
        if self.nom == "pelle":
            joueur.peut_creuser = True

        elif self.nom == "marteau":
            joueur.peut_briser_cadenas_coffre = True

        elif self.nom == "kit_de_crochetage":
            joueur.peut_ouvrir_portes = True

        elif self.nom == "détecteur_de_métaux":
            joueur.chance_cle_pieces += 1

        elif self.nom == "patte_de_lapin":
            joueur.chance_objets += 1

