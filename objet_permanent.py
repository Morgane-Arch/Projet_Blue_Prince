class ObjetPermanent:
    """
    Classe représentant un objet permanent

    Paramètres : 
        nom : str
            Nom de l'objet permanent
        description : str
            Description de l'objet
        peut_creuser : bool
            Indique si l'objet permet de creuser, par défaut false
        peut_briser_cadenas : bool 
            Indique si l'objet permet de briser un cadenas, par défaut False
        peut_ouvrir_portes : bool 
            Indique si le joueur peut ouvrir certaines portes sans clé, par défaut False
        chance_cle_pieces : int 
            Bonus de chance pour trouver des clés et des pièces, par défaut 0
        chance_objet : int
            Bonus de chance pour trouver des objets, par défaut 0
    """
    def __init__(self, nom, description, peut_creuser = False, peut_briser_cadenas = False,
                peut_ouvrir_portes = False, chance_cle_pieces = 0, chance_objets = 0):
        self.peut_creuser = peut_creuser
        self.peut_briser_cadenas = peut_briser_cadenas
        self.peut_ouvrir_portes = peut_ouvrir_portes
        self.chance_cle_pieces = chance_cle_pieces
        self.chance_objets = chance_objets
        self.nom = nom
        self.description = description

    def appliquer(self, joueur):
        """
        Fonction permettant d'appliquer les effets des objets permanents au joueur 

        Paramètre : 
            joueur : Joueur
        """
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


# Dictionnaire permettant de regrouper tous les objets permanents
# On associe un nom à une instance d'ObjetPermanent
PERMANENTS = {
    "pelle": ObjetPermanent(
        "pelle",
        "Permet de creuser à certains endroits, permettant de trouver certains objets."
    ),

    "marteau": ObjetPermanent(
        "marteau",
        "Permet de briser les cadenas des coffres sans dépenser la clé."
    ),

    "kit_de_crochetage": ObjetPermanent(
        "kit_de_crochetage",
        "Permet d'ouvrir certaines portes sans dépenser la clé."
    ),

    "détecteur_de_métaux": ObjetPermanent(
        "détecteur_de_métaux",
        "Augmente la chance de trouver des clés et des pièces."
    ),

    "patte_de_lapin": ObjetPermanent(
        "patte_de_lapin",
        "Augmente la chance de trouver des objets."
    )
}