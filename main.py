from interface_graphique import *
from joueur import Joueur
from pieces import *
import pygame
import sys
import os
import random




############ Chargement des images des salles ############

# Nom du dossier contenant les images des salles
ROOM_IMAGE_FOLDER = "Images_salles"

# Salles disponibles (FAIRE UNE PIOCHE DANS LAQUELLE ON ENLEVE DES SALLES DISPO TOUT AU LONG DE LA PARTIE)
# Format : (nom affiché, nom_fichier)

selected_room_index = 0

# Chargement des images
# Listes pour stocker les images
room_images_grid = []   # petites images pour la grille
room_images_large = []  # grandes images pour la sélection à droite

IMG_SIZE_GRID = int(CELL_SIZE * 0.9)
IMG_SIZE_LARGE = 160

for piece in salles:
    path = os.path.join(ROOM_IMAGE_FOLDER, piece.image)
    if os.path.exists(path):
        original = pygame.image.load(path).convert_alpha()
        img_grid = pygame.transform.smoothscale(original, (IMG_SIZE_GRID, IMG_SIZE_GRID))
        img_large = pygame.transform.smoothscale(original, (IMG_SIZE_LARGE, IMG_SIZE_LARGE))
    else:
        img_grid = pygame.Surface((IMG_SIZE_GRID, IMG_SIZE_GRID))
        img_grid.fill((150, 0, 150))
        img_large = pygame.Surface((IMG_SIZE_LARGE, IMG_SIZE_LARGE))
        img_large.fill((170, 0, 170))

    room_images_grid.append(img_grid)
    room_images_large.append(img_large)





############ Initialisation des données du jeu ############

# Création du joueur
joueur = Joueur([8, 2]) # création d'un joueur à la position initiale [8,2]

# Données du jeu
salles_affichees = random.sample(salles[2:], 3) # Séléction aléatoire initiale des 3 images de droite
inventory = ["Potion", "Clé d'argent"]  # Objets contenu dans l'inventaire situé à gauche, objets permanents posséder par le joueur
# VOIR COMMENT INCLURE OBJETS PERMANENTS ICI

# Grille de gauche : chaque contient soit un index correspondant à la salle soit None (ATTENTION SI L'ON MODIFIE LA PIOCHE A CHAQUE TOUR PEUT ETRE CREER 2 LISTES)
grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
grid[8][2] = 0  # Mise en place de Entrance room sur la case du milieu du bas (0 = index de Entrance room)
grid[0][2] = 1  # Mise en place de Antechamber sur la case du milieu du haut (1 = index de Antechamber)




############ Boucle de jeu ############

# Boucle principale
mode_selection = False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT) and mode_selection==False:
                joueur.set_direction(event.key)
            elif event.key in (pygame.K_4, pygame.K_6, pygame.K_KP4, pygame.K_KP6):
                selected_room_index = change_room_selection(event.key, selected_room_index, salles_affichees)
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                r, c = joueur.position
                if joueur.direction == "up" and r > 0:
                    r -= 1
                elif joueur.direction == "down" and r < ROWS - 1:
                    r += 1
                elif joueur.direction == "left" and c > 0:
                    c -= 1
                elif joueur.direction == "right" and c < COLS - 1:
                    c += 1
                name, _ = (salles_affichees[selected_room_index].nom, salles_affichees[selected_room_index].image)

                # Trouver l'index correspondant dans room_types
                room_index = next(idx for idx, piece in enumerate(salles) if piece.nom == name)

                if not mode_selection and grid[r][c] == None:
                    # Passe en mode sélection
                    mode_selection = True
                    draw_bottom_right(salles_affichees, salles, selected_room_index, room_images_large)
                else:
                    mode_selection = False # Sortir du mode sélection
                    joueur.move_in_direction(grid)
                    grid, salles_affichees, selected_room_index = place_room(salles_affichees, selected_room_index, joueur.position, salles, grid)

    # Affichage
    screen.fill(BLACK)
    draw_grid(joueur.direction, joueur.position, grid, room_images_grid)
    draw_top_right(inventory, joueur)

    if mode_selection:
        draw_bottom_right(salles_affichees, salles, selected_room_index, room_images_large)

    
    pygame.display.flip()
    clock.tick(30)