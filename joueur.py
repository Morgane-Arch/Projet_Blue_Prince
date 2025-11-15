from ObjetConso import ObjetsConsommables
from objet_permanent import ObjetPermanent

class Joueur:
    def __init__(self):
      

        # objets consommables (Sofia)
        self.consommables = ObjetsConsommables()

        # les objets permanents 
        self.objets_permanents = []

        # effets liés aux objets permanents
        self.peut_creuser = False
        self.peut_briser_cadenas_coffre = False
        self.peut_ouvrir_portes = False

        self.chance_cle_pieces = 0
        self.chance_objets = 0

    # ajouter un objet permanent 
    def ajouter_objet_permanent(self, objet: ObjetPermanent):
        self.objets_permanents.append(objet)
        objet.appliquer(self)

    # affichage 
    def afficher_objets_permanents(self):
        print("Objets permanents :")
        if not self.objets_permanents:
            print("Aucun objet permanent.")
        for obj in self.objets_permanents:
            print(f"- {obj.nom} : {obj.description}")
