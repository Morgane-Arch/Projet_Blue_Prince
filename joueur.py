from ObjetConso import ObjetsConsommables
from objet_permanent import ObjetPermanent
from interface_graphique import ROWS, COLS
import pygame
from pieces import salles

class Joueur:
    """
    Classe permettant de représenter le joueur dans le jeu : par sa position son inventaire 

    Paramètres : 
        position_depart : tuple(int, int)
        Position initiale du joueur sur la grille, représenté par ligne et colonne

    Attributs : 
        position : tuple(int, int)
        direction : str
        Direction de déplacement du joueur

        consommables : ObjetsConsommables
        Inventaire contenant les objets consommables (clé, gemme, etc)

        objet_permanents : list[ObjetPermanent]
        Liste des objets permanents que le joueur a

        autres_objets : list[]
        Inventaire pour les autres objets

        peut_creuser : bool
        Indique si le joueur a une pelle pour creuser (objet permanent)

        peut_briser_cadenas_coffre : bool 
        Indique si le joueur a un marteau

        peut_ouvrir_portes : bool 
        Indique le joueur a le kit de crochetage

        chance_cle_pieces = int
        Indique la chance d'obtenir des clés et des pièces (dépendance à l'objet permanent détecteur de métaux)

        chance_objets : int 
        Indique la chance d'obtenir des objets dans les pièces (dépendance à l'objet permanent patte de lapin)
    """

    def __init__(self, position_depart):
        self.position = position_depart # Initialise la position du joueur
        self.direction = None  # Initialise la direction de déplacement du joueur, pas de direction spécifique définit au tout début

        self.consommables = ObjetsConsommables() # Inventaire objets consommables
        self.objets_permanents = [] # Inventaire objets permanents 
        self.autres_objets = []

        #Effets liés aux objets permanents
        self.peut_creuser = False
        self.peut_briser_cadenas_coffre = False
        self.peut_ouvrir_portes = False

        self.chance_cle_pieces = 0
        self.chance_objets = 0

    # Ajouter un objet permanent 
    def ajouter_objet_permanent(self, objet: ObjetPermanent):
        """
        Fonction permettant d'ajouter un objet permanent à l'inventaire du joueur et d'appliquer ses effets

        Paramètre : 
            objet : ObjetPermanent
        """
        self.objets_permanents.append(objet)
        objet.appliquer(self)

    # Affichage 
    def afficher_objets_permanents(self):
        """
        Fonction permettant d'afficher les objets permanents dans l'inventaire
        """
        print("Objets permanents :")
        if not self.objets_permanents:
            print("Aucun objet permanent.")
        for obj in self.objets_permanents:
            print(f"- {obj.nom} : {obj.description}")
    


    ############## Fonctions de Déplacements du joueur ##############

    def set_direction(self, key):
        """Change la direction mise en surbrillance sans bouger.
        
        Paramètres : 
            key : int
            Code de la touche pressée par l'utilisateur
        """
        if key == pygame.K_UP:
            self.direction = "up"
        elif key == pygame.K_DOWN:
            self.direction = "down"
        elif key == pygame.K_LEFT:
            self.direction = "left"
        elif key == pygame.K_RIGHT:
            self.direction = "right"


    def move_in_direction(self, grid):
        """Déplace la sélection dans la direction choisie."""

        r, c = self.position #rows, columns
        new_r, new_c = r, c #nouvelle position

        

        #Test pour voir si on peut adopter la position (si on est au bout de la grille)
        if self.direction == "up" and r > 0 : 
            new_r -= 1
        elif self.direction == "down" and r < ROWS - 1 : 
            new_r += 1

        elif self.direction == "left" and c > 0:
            new_c -= 1
        elif self.direction == "right" and c < COLS - 1:
            new_c += 1

        #Si la position a vraiment changé (pas coincé par un bord par exemple)
        if (new_r, new_c) != (r, c) :
            encore_en_vie = self.consommables.retirer_objet("pas", 1) #on retire le pas

            #si objetconso.retirer_objet renvoie false : cela signifie qu'on n'a plus de pas
            if not encore_en_vie : 
                print("Game over !")
                return
        
        #mise à jour de la position
        self.position = (new_r, new_c)

#### à revoir : l'effet de la salle avec retire_pas
        # on applique l effet de la salle 
        #salle = salles[grid[new_r][new_c]]
        #salle.retirer_pas(self)









