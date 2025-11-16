import random 
from ObjetConso import ObjetsConsommables
from objet_permanent import PERMANENTS
from AutresObjets import AutresObjets
from joueur import Joueur

class AleatoireObjet : 
    """
    Classe permettant de gérer le t'apparition des objets dans le jeu (consommaables et permanents)
    """

    def __init__(self) : 
        
        self.proba_base_apparition = 0.3 #Probabilite de base d'apparition des objets dans la pièce
        self.proba_base_coffre = 0.5 #Probabilité de base d'obtenir des objets consommables dans un coffre
        self.objet_mangeables = ["pomme", "banane", "gateau", "sandwich", "repas"]
        self.objets_consommables = ["pas", "cle", "piece", "gemme", "de"]
        self.bonus_chance = 0.05 #bonus de chance par points de chance du joueur - patte de lapin, detecteur de metaux


        #lot possible pour un casier -- on pourra le faire pour coffre aussi 
        self.lot_casier = [ {"pas" : 8, "pomme": 3},
                            {"banane": 5, "piece": 2},
                            {"cle" : 2, "sandwich" : 1, "gemme" : 3}, 
                            {"gateau" :1, "repas":1, "de":1}
            ]
        
        #lot possible pour un endroit à creuser -- on pourra le faire pour coffre aussi 
        self.lot_creuser = [ {"pas" : 1, "repas": 1},
                            {"gemme": 2, "piece": 5},
                            {"cle" : 2, "sandwich" : 1, "de" : 3}, 
                            {"gateau" :1, "repas":1, "de":1}
            ]

        # la proba d'apparition dépend de la couleur de la salle 
        self.proba_bonus_couleur = {
            "green": 0.2,
            "purple": 0.1,
            "yellow": 0.05,
            "bleu": 0.0,
            "orange": -0.1,
            "red": -0.15
        }

    # Génerer des objets présents dans les salles
    def generer_objet_salle(self, piece, joueur) : 
        """
        Prend une piece et renvoie une liste d'objets pouvant apparaître dans cette pièce
        Piece : instance de la classe Piece
        Joueur : instance de la classe Joueur
        Retourne le nom de l'objet généré ou None s'il n'y a pas d'objet à générer.
        """
        objets_trouve = {} #tous les objets qu'on aura trouvé à la fin

        bonus_piece = self.proba_bonus_couleur.get(piece.couleur, 0)
        #ON parcourt tous les types d'objets pouvant apparaître dans la piece 

        for objet in piece.objets : 

            proba_apparition = self.proba_base_apparition + self.bonus_chance * joueur.chance_objets + bonus_piece #Probabilite de base d'apparition des objets dans la pièce

            if objet in ["cle", "piece"] : #pour le detecteur des metaux
                proba_apparition += self.bonus_chance * joueur.chance_cle_pieces 


            #on tire un nb aléatoire entre 0 et 1, si il est inferieur a la proba d'apparition, on ajoute l'objet à la liste des objets trouvés
            if random.random() < proba_apparition :

                # Pour les objets permanents, on ajoute l'objet permanent correspondant
                if objet == "permanent" : 

                    #on choisit un objet permanent au hasard parmi les objets permanents disponibles
                    nom_obj_permanent = random.choice(list(PERMANENTS.keys()))
                    objets_trouve[nom_obj_permanent] = objets_trouve.get(nom_obj_permanent, 0) + 1
                
                elif objet in PERMANENTS : 
                    objets_trouve[objet] = objets_trouve.get(objet, 0) + 1

                elif objet == "creuser" : 
                    objets_trouve["endroit_a_creuser"] = objets_trouve.get("endroit_a_creuser", 0) + 1

                elif objet == "casier" : 
                    objets_trouve["casier"] = objets_trouve.get("casier", 0) + 1
                
                elif objet == "coffre" : 
                    objets_trouve["coffre"] = objets_trouve.get("coffre", 0) + 1

                # Pour les objets mangeables 
                elif objet in ["pomme", "banane", "gateau", "sandwich", "repas"] : 
                    objets_trouve[objet] = objets_trouve.get(objet, 0) + 1

                # Pour les objets consommables : 
                elif objet in ["pas", "cle", "piece", "gemme", "de"] :
                    objets_trouve[objet] = objets_trouve.get(objet, 0) + 1

                #Autres     
                else : 
                    objets_trouve[objet] = objets_trouve.get(objet, 0) + 1
        return objets_trouve
    
    # Génerer les objets dans un coffre 
    def contenu_coffre(self, joueur) : 
        """
        Génère le contenu d'un coffre en fonction des chances du joueur.
        Retourne un dictionnaire d'objets contenus dans le coffre.
        """

        #on stock le contenu du coffre dans un dictionnaire
        contenu = {}

        #combien d'objets différents on peut avoir dans le coffre (1 à 3)
        nb_objets_differents = random.randint(1, 3)

        #objet possible dans le coffre 
        objets_possibles = self.objets_consommables + self.objet_mangeables

        #chance objet influence le nombre d'objets 
        nb_objets_differents += joueur.chance_objets // 2  #1 objet supplémentaire tous les 2 points de chance
        nb_objets_differents = min(nb_objets_differents, len(objets_possibles))  #on ne peut pas avoir plus d'objets différents que d'objets possibles

        #tirage au sort des objets à mettre dans le coffre
        objets_choisis = random.sample(objets_possibles, nb_objets_differents)

        for objet in objets_choisis :
            quantite = random.randint(1, 3)  #quantité entre 1 et 3
            contenu[objet] = quantite


        return contenu
       
       
       
       #générer le contenu d'un casier
    def contenu_casier(self, piece, joueur) :
        """
        Génère le contenu d'un casier 
        """

        if piece.nom != "Locker room" :
            raise ValueError("Le contenu du casier ne peut être généré que dans la pièce 'Locker room")

        #proba que le casier soit vide 
        proba_vide = 0.2 
        proba_vide -= self.bonus_chance * joueur.chance_objets  # si le joueur a par exemple une patte de lapin, moins de chance d'etre vide
        proba_vide = max(0.05, proba_vide)  # toujours au moins 5% de chance d'être vide

        # génération du contenu du casier : 
        if random.random() < proba_vide:
            return {}   # casier vide
        
        # Tirage d'un des lots prédéfinis 
        lot = random.choice(self.lot_casier)
        return lot.copy()  
    
    #générer le contenu d'un endroit à creuser
    def contenu_endroit_a_creuser(self, piece, joueur) :
        """
        Génère le contenu d'un endroit à creuser 
        """

        #proba que l'endroit à creuser soit vide 
        proba_vide = 0.3 
        proba_vide -= self.bonus_chance * joueur.chance_objets  # si le joueur a par exemple une patte de lapin, moins de chance d'etre vide
        proba_vide = max(0.1, proba_vide)  # toujours au moins 10% de chance d'être vide

        # génération du contenu du casier : 
        if random.random() < proba_vide:
            return {}   # casier vide
        
        # Tirage d'un des lots prédéfinis 
        lot = random.choice(self.lot_creuser)
        return lot.copy()  



       
        