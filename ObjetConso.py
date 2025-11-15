class ObjetsConsommables : 
    """ Classe représentant les objets consommables du joueur, dans son inventaire : 
    - Pas : le nombre de pas restants
    - Pièces : le nombre de pièces restantes 
    - Gemmes : le nombre de gemme restantes 
    - Clés : Le nombre de clés 
    - Dé : Le nombre de dés en la possession du joueur
    """

    def __init__(self, pas = 70, piece = 0, gemme = 2, cle = 0, de = 0) : 
        self.pas = pas
        self.piece = piece
        self.gemme = gemme
        self.cle = cle
        self.de = de
    
    #Permet d'ajouter un objet consommable à l'inventaire du joueur 
    def ajouter_objet(self, objet, quantite) : 
        """ Ajoute une certaine quantité d'un objet consommable à l'inventaire du joueur
        - Objet : str ("pas", "piece", "gemme", "cle", "de") 
        - Quantite : int : La quantité à ajouter
        """
        if not isinstance(objet, str) : 
            raise TypeError("Le nom de l'objet doit être une chaîne de caractère")

        if not isinstance(quantite, int) : 
            raise TypeError("La quantite doit etre un entier !")

        if quantite > 0 : 
            if objet == "pas" : 
                self.pas += quantite
            elif objet == "piece" : 
                self.piece += quantite
            elif objet == "gemme" : 
                self.gemme += quantite
            elif objet == "cle" : 
                self.cle += quantite
            elif objet == "de" : 
                self.de += quantite
            else : 
                raise ValueError("Type d'objet inconnu.")
        else : 
            raise ValueError("On ne veut qu'ajouter des objets, pas en consommer. Se référer à retirer_objet")
        
    #Permet de retirer un objet de l'inventaire du joueur : Il a choisit de le consommer - à marcher
    def retirer_objet(self, objet, quantite) : 
        """ Retire une certaine quantité d'un objet consommable de l'inventaire du joueur. 
        objet : str : le type d'objet à retirer ("pas", "piece", "gemme", "cle", "de")
        quantite : int : la quantité à retirer
        """
        if objet == "pas" : 
            if quantite != 1 : 
                raise ValueError("On ne peut retirer qu'un seul pas à la fois")
            if self.pas >= quantite : 
                self.pas -= quantite
                if self.pas == 0 : #GameOver si le pas atteint 0, sous forme de booléen
                    return False
                return True
            else : #Game over si on ne peut plus retirer 1 pas, cela signifie que l'on est à 0
                return False
                
        elif objet == "piece" : 
            if self.piece >= quantite : 
                self.piece -= quantite
            else : 
                raise ValueError("Pièces insuffisantes.")
        elif objet == "gemme" : 
            if self.gemme >= quantite : 
                self.gemme -= quantite
            else : 
                raise ValueError("Gemmes insuffisantes.")
        elif objet == "cle" : 
            if self.cle >= quantite : 
                self.cle -= quantite
            else : 
                raise ValueError("Clés insuffisantes.")
        elif objet == "de" : 
            if self.de >= quantite : 
                self.de -= quantite
            else : 
                raise ValueError("Dés insuffisants.")
        else : 
            raise ValueError("Type d'objet inconnu.")
        
        return True #le joueur peut continuer de joueur

    #Permet d'afficher les objets consommables présents dans l'inventaire     
    def afficher_objets(self) : 
        """
        Affiche le contenu de l'inventaire
        """
        print("Pas :", self.pas)
        print("Pièces :", self.piece)
        print("Gemmes :", self.gemme)
        print("Cles :", self.cle)
        print("De :", self.de)


        

