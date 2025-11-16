import random 
from ObjetConso import ObjetsConsommables
from objet_permanent import PERMANENTS
from AutresObjets import AutresObjets

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



    # Génerer des objets présents dans les salles

    def generer_objet_salle(self, piece, joueur) : 
        """
        Prend une piece et renvoie une liste d'objets pouvant apparaître dans cette pièce
        Piece : instance de la classe Piece
        Joueur : instance de la classe Joueur
        Retourne le nom de l'objet généré ou None s'il n'y a pas d'objet à générer.
        """
        objets_trouve = {} #tous les objets qu'on aura trouvé à la fin

        #ON parcourt tous les types d'objets pouvant apparaître dans la piece 

        for objet in piece.objets : 

            proba_apparition = self.proba_base_apparition #Probabilite de base d'apparition des objets dans la pièce

            proba_apparition += self.bonus_chance * joueur.chance_objets  #si le joueur a une patte de lapin : sa chance augmente de 5%

            if objet in ["cle", "piece"] : #pour le detecteur des metaux
                proba_apparition += self.bonus_chance * joueur.chance_cle_pieces 

            #on tire un nb aléatoire entre 0 et 1, si il est inferieur a la proba d'apparition, on ajoute l'objet à la liste des objets trouvés
            if random.random() < proba_apparition :

                # Pour les objets permanents, on ajoute l'objet permanent correspondant
                if objet == "permanent" : 

                    #on choisit un objet permanent au hasard parmi les objets permanents disponibles
                    nom_obj_permanent = random.choice(list(PERMANENTS.keys()))
                    objets_trouve[nom_obj_permanent] = objets_trouve.get(nom_obj_permanent, 0) + 1

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
       
       
       
       
       
        