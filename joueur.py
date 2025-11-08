class Joueur:
    def __init__(self):
        # nombre de pas initial
        self.pas = 70

        # Inventaire consommable (sofia)
        self.consommable = []

        # les objets permanents
        self.objets_permanents = []

        # les effets des objets permanents
        self.peut_creuser = False                # Pelle
        self.peut_briser_cadenas_coffre = False  # Marteau
        self.peut_ouvrir_portes = False       # Kit de crochetage

        self.chance_cle_pieces = 0                # Détecteur 
        self.chance_objets = 0                     # Patte de lapin 

    # ajouter les objets permanents
    def ajouter_objet_permanent(self, objet):
        self.objets_permanents.append(objet)
        objet.appliquer(self)  

    def afficher_objets_permanents(self):
        for obj in self.objets_permanents:
            print(f"- {obj.nom} : {obj.description}")
