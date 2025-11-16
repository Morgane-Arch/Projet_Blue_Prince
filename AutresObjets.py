from joueur import Joueur
from ObjetConso import ObjetsConsommables

class AutresObjets : 
    """
    Classe représentant les autres objets que le joueur peut posséder : des objets différents de consommables et permanents
    Par exemple, des pommes, des coffres....
    
    Attribut : 
        - nom_objet : str
        Le nom de l'objet (pomme, banane, gateau, sandiwch, repas, coffre, casier, endroit_à_creuser)
        - contenu : str 
        Ce que contient l'objet (par exemple pour un coffre, on a 10 pommes)
        - est_ouvert : bool 
        Indique si l'objet a déjà été ouvert ou déjà été utilisé 
    """
    def __init__(self, nom_objet, contenu, est_utilise = False) : 
        self.nom_objet = nom_objet
        self.contenu = contenu
        self.est_utilise = est_utilise


    
    def utiliser_objet_mangeable(self, joueur) :
        """ 
        Fonction permettant d'utiliser un objet mangeable 

        Attribut : 
            joueur : instance de la classe Joueur
        """
        if not isinstance(joueur, Joueur): 
            raise TypeError("L'argument doit être une instance de la classe Joueur")
        
        #On regarde quel objet le joueur utilise et on applique son effet
        if self.nom_objet == "pomme" : 
            joueur.consommables.ajouter_objet("pas", 2) 
            print(" Bonne nouvelle !!! Vous avez mangé une pomme, 2 pas ont été ajoutés à votre inventaire !")

        elif self.nom_objet == "banane" : 
            joueur.consommables.ajouter_objet("pas", 3) 
            print(" Bonne nouvelle !!! Vous avez mangé une banane, 3 pas ont été ajoutés à votre inventaire !")

        elif self.nom_objet == "gateau" : 
            joueur.consommables.ajouter_objet("pas", 10) 
            print(" Bonne nouvelle !!! Vous avez mangé un gateau, 10 pas ont été ajoutés à votre inventaire !")
        
        elif self.nom_objet == "sandwich" :
            joueur.consommables.ajouter_objet("pas", 15) 
            print(" Bonne nouvelle !!! Vous avez mangé un sandiwch au saumon, 15 pas ont été ajoutés à votre inventaire !")

        elif self.nom_objet == "repas" :
            joueur.consommables.ajouter_objet("pas", 25) 
            print(" Bonne nouvelle !!! Vous avez mangé un repas, 25 pas ont été ajoutés à votre inventaire !")

        else : 
            raise ValueError("L'objet n'est pas mangeable ! Se référer à utiliser_objet_interactif pour les autres objet")

    def utiliser_objet_interactif(self, joueur) : 
        """ 
        Fonction permettant d'intéragir avec un objet dit intéractif 

        Attribut : 
            joueur : instance de la classe Joueur 
        """

        if not isinstance(joueur, Joueur): 
            raise TypeError("L'argument doit être une instance de la classe Joueur")
        
        #Vérification que l'objet soit bien intéractif
        if self.nom_objet not in ["coffre", "casier", "endroit_a_creuser"] : 
            raise ValueError("L'objet n'est pas interactif ! Se référer à utiliser_objet_mangeable pour les objets mangeables")
        
        if self.est_utilise == True : #Si l'objet a déjà été ouvert
            print("L'objet a déjà été utilisé !")
            return
        else : # Si l'objet n'a pas été utilisé

            #Pour un casier, il faut une clé pour l'ouvrir : 
            if self.nom_objet == "casier" : 
                if joueur.consommables.cle == 0 : 
                    print(f"Le {self.nom_objet} est verrouillé... Vous n'avez pas assez de clé pour l'ouvrir...")
                    return
                else : 
                    joueur.consommables.retirer_objet("cle", 1)
                    print(f"Vous utilisez une clé pour ouvrir le {self.nom_objet}")

            #Pour un endroit à creuser, il faut une pelle pour creuser
            elif self.nom_objet == "endroit_a_creuser" :
                if joueur.peut_creuser == False :
                    print("Vous n'avez pas de pelle pour creuser ici...")
                    return
                else : 
                    print("vous utilisez votre pelle et creusez ici")

            #Pour le coffre : s'ouvre avec un marteau ou une clé
            elif self.nom_objet == "coffre" :
                if joueur.peut_briser_cadenas_coffre == True :
                    print("Vous avez ouvert le cadenas grâce au marteau !!!")
                elif joueur.consommables.cle > 0 :
                    joueur.consommables.retirer_objet("cle", 1)
                    print("Vous avez utilisé une clé pour ouvrir le coffre!!!!!")
                else :
                    print("Vous n'avez ni clé ni marteau pour ouvrir le coffre.")
                    return

            #Un coffre ne peut jamais être vide. Alors on met une condition 
            if self.nom_objet == "coffre" and (self.contenu == None or self.contenu == {}) :
                raise ValueError("un coffre ne peut pas etre vide !")
            
            #Une fois qu'on a passé toutes les conditions, on peut ouvrir l'objet 
            if self.contenu == None : 
                print(f"Feinte... {self.nom_objet} est vide")
                self.est_utilise = True

            else:
                print(f"Bonne nouvelle ! Le {self.nom_objet} contient : {self.contenu}")
                
                #maintenant on gère les dictionnaires - donc on converti les contenus en dictionnaire
                if not isinstance(self.contenu, dict) :
                    self.contenu = {self.contenu: 1} 

                #Parcourt du dictionnaire des contenus
                for nom_objet, quantite in self.contenu.items() : 

                    # Cas 1 : Si le contenu est un objet consommable
                    if nom_objet in ["pas", "piece", "gemme", "cle", "de"] :
                        joueur.consommables.ajouter_objet(nom_objet, quantite)

                    # Cas 2 : si le contenu est mangeable : 
                    elif nom_objet in ["pomme", "banane", "gateau", "sandwich", "repas"] : 
                        for i in range(quantite) : 
                            contenu = AutresObjets(nom_objet, None)
                            contenu.utiliser_objet_mangeable(joueur) #le joueur utilise le contenu 

                    else : 
                        print(f"L'objet {nom_objet} n'est pas mangeable ni consommable.")

                self.est_utilise = True