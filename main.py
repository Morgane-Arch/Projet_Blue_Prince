from interface_graphique import *
import pygame
import sys
import os
import random




############ Chargement des images des salles ############

# Nom du dossier contenant les images des salles
ROOM_IMAGE_FOLDER = "Images_salles"

# Salles disponibles (FAIRE UNE PIOCHE DANS LAQUELLE ON ENLEVE DES SALLES DISPO TOUT AU LONG DE LA PARTIE)
# Format : (nom affiché, nom_fichier)
room_types = [
    ("Entrance Hall", "Entrance_Hall_Icon.png"),
    ("Antechamber", "Antechamber_Icon.png"),
    ("The Foundation", "The_Foundation_Icon.png"),
    ("Spare Room", "Spare_Room_Icon.png"),
    ("Rotunda", "Rotunda_Icon.png"),
    ("Attic", "Attic_Icon.png"),
    ("Billiard Room", "Billiard_Room_Icon.png")
]
selected_room_index = 0

# Chargement des images
room_images_grid = []   # petites images pour la grille
room_images_large = []  # grandes images pour la sélection à droite

IMG_SIZE_GRID = int(CELL_SIZE * 0.9)  # ~72px si CELL_SIZE=80
IMG_SIZE_LARGE = 160                  # affichage à droite

for name, filename in room_types:
    path = os.path.join(ROOM_IMAGE_FOLDER, filename)
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

# Données du jeu
salles_affichees = random.sample(room_types[2:], 3) # Séléction aléatoire initiale des 3 images de droite
selected_cell = [8, 2]  # position de départ du joueur (A INCLURE DANS CLASSE JOUEUR ?)
selected_direction = None  # pas de direction spécifique définit au tout début
steps = 0  # Nombre de pas (PARTIE A MODIFIER AVEC OBJET CONSO)
keys = 0  # Nombre de clés (PARTIE A MODIFIER AVEC OBJET CONSO)
inventory = ["Potion", "Clé d'argent"]  # Objets contenu dans l'inventaire situé à gauche, objets permanents posséder par le joueur
# VOIR COMMENT INCLURE OBJETS PERMANENTS ICI

# Grille de gauche : chaque contient soit un index correspondant à la salle soit None (ATTENTION SI L'ON MODIFIE LA PIOCHE A CHAQUE TOUR PEUT ETRE CREER 2 LISTES)
grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
grid[8][2] = 0  # Mise en place de Entrance room sur la case du milieu du bas (0 = index de Entrance room)
grid[0][2] = 1  # Mise en place de Antechamber sur la case du milieu du haut (1 = index de Antechamber)





############ Boucle de jeu ############

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                selected_direction = set_direction(event.key, selected_direction)
            elif event.key in (pygame.K_4, pygame.K_6, pygame.K_KP4, pygame.K_KP6):
                selected_room_index = change_room_selection(event.key, selected_room_index, salles_affichees)
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                selected_cell, steps = move_in_direction(selected_cell, steps, selected_direction)
                grid = place_room(salles_affichees, selected_room_index, selected_cell, room_types, grid)

                # Nouveau tirage des salles aléatoire
                salles_affichees = random.sample(room_types[2:], 3)
                selected_room_index = 0  # réinitialise la sélection de la salle

    # Affichage
    screen.fill(BLACK)
    draw_grid(selected_direction, selected_cell, grid, room_images_grid)
    draw_top_right(inventory, steps, keys)
    draw_bottom_right(salles_affichees, room_types, selected_room_index, room_images_large)

    pygame.display.flip()
    clock.tick(30)