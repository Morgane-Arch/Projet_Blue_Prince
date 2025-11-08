class ObjetPermanent:
    def __init__(self, nom, description):
        self.nom = nom
        self.description = description

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

# ===== Instances d'objets permanents utilisables dans le jeu =====

PELLE = ObjetPermanent(
    "pelle",
    "Permet de creuser à certains endroits, permettant de trouver certains objets"
)

MARTEAU = ObjetPermanent(
    "marteau",
    "Permet de briser les cadenas des coffres sans dépenser la clé."
)

KIT_CROCHETAGE = ObjetPermanent(
    "kit_de_crochetage",
    "Permet d'ouvrir certaines portes sans dépenser la clé."
)

DETECTEUR = ObjetPermanent(
    "détecteur_de_métaux",
    "Augmente la chance de trouver des clés et des pièces."
)

PATTE_LAPIN = ObjetPermanent(
    "patte_de_lapin",
    "Augmente la chance de trouver des objets."
)
