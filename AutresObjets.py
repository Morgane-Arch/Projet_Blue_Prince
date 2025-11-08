from joueur import Joueur
from ObjetConso import ObjetsConsommables

class AutresObjets : 
    """
    Classe représentant les autres objets que le joueur peut posséder - non consommable et différent des objets permanents
    - nom_objet : str : le nom de l'objet (pomme, banane, gateau, sandiwch, repas, coffres, casiers, endroit à creuser)
    - contenu : str : ce que contient l'objet (par exemple pour un coffre, on a 10 pommes)
    - est_ouvert : bool : indique si l'objet a deja ete ouvert ou deja ete utilisé 
    """
    def __init__(self, nom_objet, contenu=None, est_utilise=False) : 
        self.nom_objet = nom_objet
        self.contenu = contenu
        self.est_utilise = est_utilise


    #attention, la classe joueur n'est pas encore définie !!!! 
    def utiliser_objet_mangeable(self, joueur) :
        """ Permet d'utiliser un objet mangeable 
        Joueur : instance de la classe Joueur
        """
        if not isinstance(joueur, Joueur): 
            raise TypeError("L'argument doit être une instance de la classe Joueur")
        
        #Maintenant on va regarder quel objet le joueur utilise
        if self.nom_objet == "pomme" : 
            joueur.objets.ajouter_objet("pas", 2) 
            print(" Bonne nouvelle !!! Vous avez mangé une pomme, 2 pas ont été ajoutés à votre inventaire !")

        elif self.nom_objet == "banane" : 
            joueur.objets.ajouter_objet("pas", 3) 
            print(" Bonne nouvelle !!! Vous avez mangé une banane, 2 pas ont été ajoutés à votre inventaire !")

        elif self.nom_objet == "gateau" : 
            joueur.objets.ajouter_objet("pas", 10) 
            print(" Bonne nouvelle !!! Vous avez mangé un gateau, 10 pas ont été ajoutés à votre inventaire !")
        
        elif self.nom_objet == "sandwich" :
            joueur.objets.ajouter_objet("pas", 15) 
            print(" Bonne nouvelle !!! Vous avez mangé un sandiwch au saumon, 15 pas ont été ajoutés à votre inventaire !")

        elif self.nom_objet == "repas" :
            joueur.objets.ajouter_objet("pas", 25) 
            print(" Bonne nouvelle !!! Vous avez mangé un repas, 25 pas ont été ajoutés à votre inventaire !")

        else : 
            raise ValueError("L'objet n'est pas mangeable ! Se référer à utiliser_objet_interactif pour les autres objet")

    def utiliser_objet_interactif(self, joueur) : 
        """ Permet d'interagir avec un objet dit interactif 
        joueur : instance de la classe Joueur 
        """

        if not isinstance(joueur, Joueur): 
            raise TypeError("L'argument doit être une instance de la classe Joueur")
        
        #verification que l'objet est bien interactif
        if self.nom_objet not in ["coffre", "casiers", "endroit_a_creuser"] : 
            raise ValueError("L'objet n'est pas interactif ! Se référer à utiliser_objet_mangeable pour les objets mangeables")
        
        if self.est_utilise == True : #Si l'objet a deja ete ouvert
            print("L'objet a déjà été utilisé !")
            return
        else : 
            #Pour un casier, et un coffre il faut une clé pour l'ouvrir : 
            if self.nom_objet == "casier" : 
                if joueur.objets.cle == 0 : #joueur a un attribut objet qui est une instance de objetconsommable
                    print(f"Le {self.nom_objet} est verrouillé... Vous n'avez pas assez de clé pour l'ouvrir...")
                    return
                else : 
                    joueur.objets.retirer_objet("cle", 1)
                    print(f"Vous utilisez une clé pour ouvrir le {self.nom_objet}")

            #Pour un endroit à creuser, il faut une pelle pour creuser
            if self.nom_objet == "endroit_a_creuser" :
                if joueur.peut_creuser == False :
                    print("Vous n'avez pas de pelle pour creuser ici...")
                    return
                else : 
                    print("vous utilisez votre pelle et creusez ici")

            #Pour le coffre avec marteau ou une cle
            if self.nom_objet == "coffre" :
                if joueur.peut_briser_cadenas_coffre == True or joueur.objets.cle > 0 :
                    print("Vous avez ouvert le coffre !")

                else : 
                    print("Vous n'avez pas de marteau pour briser le cadenas du coffre ni de clé pour l'ouvrir")
                    return
                
            #Un coffre ne peut jamais etre vide d apres la consigne. Alors on met une condition 
            if self.nom_objet == "coffre" and self.contenu == None :
                raise ValueError("un coffre ne peut pas etre vide !")
            
            #une fois qu'on a passé toutes les conditions, on peut ouvrir l'objet 
            if self.contenu == None : 
                print(f"Feinte... {self.nom_objet} est vide")
            else : 
                print(f"Bonne nouvelle ! Le {self.nom_objet} contient : {self.contenu}")
                self.est_utilise = True

                # Le contenu du coffre est ajouté à l'inventaire du joueur si c'est un objet consommable
                if isinstance(self.contenu, ObjetsConsommables) :
                    joueur.objets.ajouter_objet("pas", self.contenu.pas)
                    joueur.objets.ajouter_objet("piece", self.contenu.piece)
                    joueur.objets.ajouter_objet("gemme", self.contenu.gemme)
                    joueur.objets.ajouter_objet("cle", self.contenu.cle)
                    joueur.objets.ajouter_objet("de", self.contenu.de)
                else : 
                    self.utiliser_objet_mangeable(joueur)
    

        
       
