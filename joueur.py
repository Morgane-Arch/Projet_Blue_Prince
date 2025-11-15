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
        if not self.direction:
            return
        r, c = self.position
        if self.direction == "up" and r > 0:
            r -= 1
            self.consommables.pas -= 1
        elif self.direction == "down" and r < ROWS - 1:
            r += 1
            self.consommables.pas -= 1
        elif self.direction == "left" and c > 0:
            c -= 1
            self.consommables.pas -= 1
        elif self.direction == "right" and c < COLS - 1:
            c += 1
            self.consommables.pas -= 1
        self.position = [r, c]
