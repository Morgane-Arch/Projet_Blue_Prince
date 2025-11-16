import random 
from ObjetConso import ObjetsConsommables
from objet_permanent import PERMANENTS
from AutresObjets import AutresObjets
from joueur import Joueur
from pieces import Piece

class AleatoireObjet : 
    """
    Classe permettant de gérer le taux d'apparition des objets dans le jeu : 
    - Le taux d'apparition des coffres/casiers/endroits à creuser
    - Le taux d'apparition des objets consommables/mangeables/permanents

    Attributs : 

        - proba_base_apparition : float 
        La probabilité initiale d'apparition des objets dans la pièce (sans influence tel que couleur de la pièce, effet des objets permanents)
        
        - objet_mangeables : list[str]
        La liste des noms des objets mangeables 

        - objets_consommables : list[str]
        La liste des objets consommables 

        - self.bonus_chance : float
        Probabilité supplémentaire donné par les objets permanents

        - lot_casier : list[dict(str : int)]
        Liste des lots possibles dans le casier

        - lot_creuser : lst[dict(str : float)]
        Dictionnaire des lots possibles dans les endroits à creuser

        - proba_bonus_couleur : dict(str : float)
        La probabilité d'apparition en plus selon la couleur de la pièce

        - proba_objets : dict(str : float)
        La probabilité d'apparition de chaque objet (coffre/pomme/clé, etc)

    """

    def __init__(self) : 
        
        self.proba_base_apparition = 0.3 #Probabilite de base d'apparition des objets dans la pièce
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


        self.proba_objets = { "pomme": 0.15,
                             "banane" : 0.12,
                             "gateau" : 0.24,
                             "sandwich" : 0.10,
                             "repas" : 0.05, 
                             "pas" : 0.35, 
                             "cle" : 0.2,
                             "piece" : 0.5,
                             "gemme" : 0.2, 
                             "de" : 0.4, 
                             "casier" : 0.1, 
                             "creuser" : 0.1,
                             "coffre" : 0.1
                             }

    # Génerer des objets présents dans les salles
    def generer_objet_salle(self, piece, joueur) : 
        """
        Fonction regarde la probabilité d'apparition de chaque objet et décide des objets apparaissant à la fin dans une pièce
        
        Attributs : 
            piece : Piece
            joueur : Joueur

        return : 
            objet_trouve : dict(str, int)
            Les objets générés et leur valeur associée - None s'il n'y a as d'objet à générer
        """

        # Vérification d'appartenance des attributs
        if not isinstance(piece, Piece) : 
            raise ValueError("L'argument doit être une instance de la classe pièce")
        
        if not isinstance(joueur, Joueur) : 
            raise ValueError("Joueur doit être une instance de la classe joueur")


        objets_trouve = {}                                                              #tous les objets qu'on aura trouvé à la fin

        bonus_piece = self.proba_bonus_couleur.get(piece.couleur, 0)                    #On cherche la valeur de la probabilité associée à la pièce

        #On parcourt tous les types d'objets pouvant apparaître dans la pièce 
        for objet in piece.objets : 

            #on récupère la proba propre à l'objet - si elle n'existe pas : devient 1
            proba_type_objet = self.proba_objets.get(objet, 1.0)

            proba_apparition = (self.proba_base_apparition + self.bonus_chance * joueur.chance_objets + bonus_piece)*proba_type_objet

            if objet in ["cle", "piece"] : #pour le détecteur des métaux
                proba_apparition += self.bonus_chance * joueur.chance_cle_pieces 


            #on tire un nombre aléatoire entre 0 et 1, si il est inferieur à la proba d'apparition, on ajoute l'objet à la liste des objets trouvés
            if random.random() < proba_apparition :

                # Pour les objets permanents, on ajoute l'objet permanent correspondant
                if objet == "permanent" : 

                    #on choisit un objet permanent au hasard parmi les objets permanents disponibles
                    nom_obj_permanent = random.choice(list(PERMANENTS.keys()))
                    objets_trouve[nom_obj_permanent] = objets_trouve.get(nom_obj_permanent, 0) + 1
                
                elif objet in PERMANENTS :                                          #au cas où on n'a pas rentré 'permanent' mais le nom de l'objet permanent
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
        Fonction permettant de générer le contenu d'un coffre en fonction de la 'chance' du joueur

        Attributs : 
            joueur : Joueur

        Return : 
            dict(str : float)
            Les objets contenus dans le coffre
        """

        #On stock le contenu du coffre dans un dictionnaire
        contenu = {}

        #Combien d'objets différents on peut avoir dans le coffre (ici entre 1 à 3)
        nb_objets_differents = random.randint(1, 3)

        #Objets possibles dans le coffre 
        objets_possibles = self.objets_consommables + self.objet_mangeables

        #chance_objet influence le nombre d'objets 
        nb_objets_differents += joueur.chance_objets // 2                           #1 objet supplémentaire tous les 2 points de chance
        nb_objets_differents = min(nb_objets_differents, len(objets_possibles))     #on ne peut pas avoir plus d'objets différents que d'objets possibles

        #On réutilise les probabilités correspondant aux objets possibles
        poids = []
        for objet in objets_possibles : 
            poids.append(self.proba_objets[objet])
        
        #Normalisation de la somme (c'est une proabibilité donc sa valeur maximum est 1)
        somme = sum(poids)
        for i in range(len(poids)) : 
            poids[i] = poids[i]/somme

        #Tirage au sort des objets à mettre dans le coffre
        objets_choisis = random.choices(objets_possibles, weights=poids, k=nb_objets_differents)

        for objet in objets_choisis :
            quantite = random.randint(1, 3)  #quantité entre 1 et 3
            contenu[objet] = quantite


        return contenu
       
       #Générer le contenu d'un casier
    def contenu_casier(self, piece, joueur) :
        """
        Fonction permettant de générer le contenu d'un casier en fonction de la 'chance' du joueur

        Attributs : 
            joueur : Joueur
            piece : Piece

        Return : 
            dict(str : float)
            Les objets contenus dans le casier
        """

        if piece.nom != "Locker room" :
            raise ValueError("Le contenu du casier ne peut être généré que dans la pièce 'Locker room")

        #proba que le casier soit vide 
        proba_vide = 0.2 
        proba_vide -= self.bonus_chance * joueur.chance_objets  # si le joueur a par exemple une patte de lapin, moins de chance d'être vide
        proba_vide = max(0.05, proba_vide)  # toujours au moins 5% de chance d'être vide

        # génération du contenu du casier : 
        if random.random() < proba_vide:
            return {}   # casier vide
        
        #En prenant en compte la probabilité de chaque objet dans les lots
        poids = []
        for lot in self.lot_casier : 
            nom_objet = list(lot.keys())[0]
            poids.append(self.proba_objets.get(nom_objet, 0.1))
        
        #Normalisation des poids
        somme = sum(poids)
        for i in range(len(poids)) : 
            poids[i] = poids[i]/somme
        
        # Tirage d'un des lots prédéfinis selon le poids
        lot = random.choices(self.lot_casier, weights=poids, k=1)[0]
        return lot.copy()  
    
    #générer le contenu d'un endroit à creuser
    def contenu_endroit_a_creuser(self, joueur) :
        """
        Fonction permettant de générer le contenu d'un endroit à creuser en fonction de la 'chance' du joueur

        Attributs : 
            joueur : Joueur

        Return : 
            dict(str : float)
            Les objets contenus dans l'endroit à creuser
        """

        #proba que l'endroit à creuser soit vide 
        proba_vide = 0.3 
        proba_vide -= self.bonus_chance * joueur.chance_objets  # si le joueur a par exemple une patte de lapin, moins de chance d'etre vide
        proba_vide = max(0.1, proba_vide)  # toujours au moins 10% de chance d'être vide

        # génération du contenu du casier : 
        if random.random() < proba_vide:
            return {}   # casier vide
        
        #En prenant en compte la probabilité de chaque objet dans les lots
        poids = []
        for lot in self.lot_creuser : 
            nom_objet = list(lot.keys())[0]
            poids.append(self.proba_objets.get(nom_objet, 0.1))

        #Normalisation des poids
        somme = sum(poids)
        for i in range(len(poids)) : 
            poids[i] = poids[i]/somme
        
        # Tirage d'un des lots prédéfinis 
        lot = random.choices(self.lot_creuser, weights=poids, k=1)[0]
        return lot.copy()  



       
        