from ObjetConso import ObjetsConsommables
from objet_permanent import ObjetPermanent
from interface_graphique import ROWS, COLS
import pygame



class Joueur:

    def __init__(self, position_depart):
        self.position = position_depart # Initialise la position du joueur
        self.direction = None  # Initialise la direction de déplacement du joueur, pas de direction spécifique définit au tout début

        self.consommables = ObjetsConsommables() # Inventaire objets consommables
        self.objets_permanents = [] # Inventaire objets permanents 

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
    


    ############## Fonctions de Déplacements du joueur ##############

    def set_direction(self, key):
        """Change la direction mise en surbrillance sans bouger."""
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
        
        #### Fonction modifiée, regarder ancien commit si pas validé

        r, c = self.position #rows, columns
        new_r, new_c = r, c #nouvelle position

        #Test pour vois si on peut adopter la position (si on est au bout de la grille)
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
        self.position = [new_r, new_c]





