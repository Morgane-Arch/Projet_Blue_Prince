from interface_graphique import *
from joueur import Joueur
from pieces import *
import pygame
import sys
import os
import random
from AleatoireObjet import AleatoireObjet
from objet_permanent import PERMANENTS




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
joueur = Joueur((8, 2)) # création d'un joueur à la position initiale [8,2]


##### AJOUT
# Initialisation de la gestion des objets 
objet_aleatoire = AleatoireObjet()

# Données du jeu
salles_affichees = random.sample(salles[2:], 3) # Séléction aléatoire initiale des 3 images de droite


# VOIR COMMENT INCLURE OBJETS PERMANENTS ICI
#### AJOUT OBJET PERMANENY
for nom_objet_de_depart in inventory :                                                   # on parcourt chaque élément de inventaire
    if nom_objet_de_depart in PERMANENTS :                                               # si l'objet est un objet permanent
        joueur.ajouter_objet_permanent(PERMANENTS[nom_objet_de_depart])                  # on ajoute aux objets permanents du joueur

# Grille de gauche : chaque contient soit un index correspondant à la salle soit None (ATTENTION SI L'ON MODIFIE LA PIOCHE A CHAQUE TOUR PEUT ETRE CREER 2 LISTES)
grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
grid[8][2] = 0  # Mise en place de Entrance room sur la case du milieu du bas (0 = index de Entrance room)
grid[0][2] = 1  # Mise en place de Antechamber sur la case du milieu du haut (1 = index de Antechamber)

print("N" in salles[grid[8][2]].portes)



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

                if joueur.direction == "up" and r > 0 and "N" in salles[grid[r][c]].portes:
                    r -= 1
                    if salles_affichees == []:
                        salles_affichees = random.sample([piece for piece in salles[2:] if "S" in piece.portes],3)
                    if not mode_selection and grid[r][c] == None:
                        # Passe en mode sélection
                        mode_selection = True
                        draw_bottom_right(salles_affichees, salles, selected_room_index, room_images_large)
                    else:
                        mode_selection = False # Sortir du mode sélection
                        joueur.move_in_direction(grid)
                        grid, selected_room_index = place_room(salles_affichees, selected_room_index, joueur.position, salles, grid)

                        ###### AJOUT (pour chaque bloc de déplacement)
                        #ajout des objets aléatoires dans la salle
                        nouvelle_piece_indice = grid[joueur.position[0]][joueur.position[1]]                # On récupère l'indice de la nouvelle pièce
                        if nouvelle_piece_indice is not None:                                               # On vérifie que la pièce existe    
                            nouvelle_piece = salles[nouvelle_piece_indice]                                  # On récupère la nouvelle pièce
                            objets_trouve = objet_aleatoire.generer_objet_salle(nouvelle_piece, joueur)     # On génère les objets aléatoires dans la salle
                            if objets_trouve :                                                              # Si on a trouvé des objets (dictinnaire non vide)
                                print(f"Objets trouvés dans la salle {nouvelle_piece.nom} : {objets_trouve}")           # Affichage
                                for nom_objet, quantite in objets_trouve.items():                                       # Pour chaque objet trouvé  
                                    if nom_objet in ["cle", "de", "pas", "piece", "gemme"]:                             # Si l'objet est consommable       
                                        joueur.consommables.ajouter_objet(nom_objet, quantite)                          # On l'ajoute aux consommables du joueur
                                        inventory.append(f"{nom_objet.capitalize()} x{quantite}")                       # Affichage dans l'inventaire
                                    elif nom_objet in PERMANENTS :                                                      # Si l'objet est permanent      
                                        joueur.ajouter_objet_permanent(PERMANENTS[nom_objet])                           # On l'ajoute aux objets permanents du joueur
                                        inventory.append(PERMANENTS[nom_objet].nom)                                     # On l'ajoute à l'inventaire pour l'affichage   
                        salles_affichees = []

                elif joueur.direction == "down" and r < ROWS - 1 and "S" in salles[grid[r][c]].portes:
                    r += 1
                    if salles_affichees == []:
                        salles_affichees = random.sample([piece for piece in salles[2:] if "N" in piece.portes],3)
                    if not mode_selection and grid[r][c] == None:
                        # Passe en mode sélection
                        mode_selection = True
                        draw_bottom_right(salles_affichees, salles, selected_room_index, room_images_large)
                    else:
                        mode_selection = False # Sortir du mode sélection
                        joueur.move_in_direction(grid)
                        grid, selected_room_index = place_room(salles_affichees, selected_room_index, joueur.position, salles, grid)
                        ###### AJOUT (pour chaque bloc de déplacement)
                        #ajout des objets aléatoires dans la salle
                        nouvelle_piece_indice = grid[joueur.position[0]][joueur.position[1]]                # On récupère l'indice de la nouvelle pièce
                        if nouvelle_piece_indice is not None:                                               # On vérifie que la pièce existe    
                            nouvelle_piece = salles[nouvelle_piece_indice]                                  # On récupère la nouvelle pièce
                            objets_trouve = objet_aleatoire.generer_objet_salle(nouvelle_piece, joueur)     # On génère les objets aléatoires dans la salle
                            if objets_trouve :                                                              # Si on a trouvé des objets (dictinnaire non vide)
                                print(f"Objets trouvés dans la salle {nouvelle_piece.nom} : {objets_trouve}")           # Affichage
                                for nom_objet, quantite in objets_trouve.items():                                       # Pour chaque objet trouvé  
                                    if nom_objet in ["cle", "de", "pas", "piece", "gemme"]:                             # Si l'objet est consommable       
                                        joueur.consommables.ajouter_objet(nom_objet, quantite)                          # On l'ajoute aux consommables du joueur
                                        inventory.append(f"{nom_objet.capitalize()} x{quantite}")                       # Affichage dans l'inventaire
                                    elif nom_objet in PERMANENTS :                                                      # Si l'objet est permanent      
                                        joueur.ajouter_objet_permanent(PERMANENTS[nom_objet])                           # On l'ajoute aux objets permanents du joueur
                                        inventory.append(PERMANENTS[nom_objet].nom) 
                        salles_affichees = []

                elif joueur.direction == "left" and c > 0 and "W" in salles[grid[r][c]].portes:
                    c -= 1
                    if salles_affichees == []:
                        salles_affichees = random.sample([piece for piece in salles[2:] if "E" in piece.portes],3)
                    if not mode_selection and grid[r][c] == None:
                        # Passe en mode sélection
                        mode_selection = True
                        draw_bottom_right(salles_affichees, salles, selected_room_index, room_images_large)
                    else:
                        mode_selection = False # Sortir du mode sélection
                        joueur.move_in_direction(grid)
                        grid, selected_room_index = place_room(salles_affichees, selected_room_index, joueur.position, salles, grid)
                        ###### AJOUT (pour chaque bloc de déplacement)
                        #ajout des objets aléatoires dans la salle
                        nouvelle_piece_indice = grid[joueur.position[0]][joueur.position[1]]                # On récupère l'indice de la nouvelle pièce
                        if nouvelle_piece_indice is not None:                                               # On vérifie que la pièce existe    
                            nouvelle_piece = salles[nouvelle_piece_indice]                                  # On récupère la nouvelle pièce
                            objets_trouve = objet_aleatoire.generer_objet_salle(nouvelle_piece, joueur)     # On génère les objets aléatoires dans la salle
                            if objets_trouve :                                                              # Si on a trouvé des objets (dictinnaire non vide)
                                print(f"Objets trouvés dans la salle {nouvelle_piece.nom} : {objets_trouve}")           # Affichage
                                for nom_objet, quantite in objets_trouve.items():                                       # Pour chaque objet trouvé  
                                    if nom_objet in ["cle", "de", "pas", "piece", "gemme"]:                             # Si l'objet est consommable       
                                        joueur.consommables.ajouter_objet(nom_objet, quantite)                          # On l'ajoute aux consommables du joueur
                                        inventory.append(f"{nom_objet.capitalize()} x{quantite}")                       # Affichage dans l'inventaire
                                    elif nom_objet in PERMANENTS :                                                      # Si l'objet est permanent      
                                        joueur.ajouter_objet_permanent(PERMANENTS[nom_objet])                           # On l'ajoute aux objets permanents du joueur
                                        inventory.append(PERMANENTS[nom_objet].nom) 
                        salles_affichees = []

                elif joueur.direction == "right" and c < COLS - 1 and "E" in salles[grid[r][c]].portes:
                    c += 1
                    if salles_affichees == []:
                        salles_affichees = random.sample([piece for piece in salles[2:] if "W" in piece.portes],3)
                    if not mode_selection and grid[r][c] == None:
                        # Passe en mode sélection
                        mode_selection = True
                        draw_bottom_right(salles_affichees, salles, selected_room_index, room_images_large)
                    else:
                        mode_selection = False # Sortir du mode sélection
                        joueur.move_in_direction(grid)
                        grid, selected_room_index = place_room(salles_affichees, selected_room_index, joueur.position, salles, grid)
                        ###### AJOUT (pour chaque bloc de déplacement)
                        #ajout des objets aléatoires dans la salle
                        nouvelle_piece_indice = grid[joueur.position[0]][joueur.position[1]]                # On récupère l'indice de la nouvelle pièce
                        if nouvelle_piece_indice is not None:                                               # On vérifie que la pièce existe    
                            nouvelle_piece = salles[nouvelle_piece_indice]                                  # On récupère la nouvelle pièce
                            objets_trouve = objet_aleatoire.generer_objet_salle(nouvelle_piece, joueur)     # On génère les objets aléatoires dans la salle
                            if objets_trouve :                                                              # Si on a trouvé des objets (dictinnaire non vide)
                                print(f"Objets trouvés dans la salle {nouvelle_piece.nom} : {objets_trouve}")           # Affichage
                                for nom_objet, quantite in objets_trouve.items():                                       # Pour chaque objet trouvé  
                                    if nom_objet in ["cle", "de", "pas", "piece", "gemme"]:                             # Si l'objet est consommable       
                                        joueur.consommables.ajouter_objet(nom_objet, quantite)                          # On l'ajoute aux consommables du joueur
                                        inventory.append(f"{nom_objet.capitalize()} x{quantite}")                       # Affichage dans l'inventaire
                                    elif nom_objet in PERMANENTS :                                                      # Si l'objet est permanent      
                                        joueur.ajouter_objet_permanent(PERMANENTS[nom_objet])                           # On l'ajoute aux objets permanents du joueur
                                        inventory.append(PERMANENTS[nom_objet].nom) 
                        salles_affichees = []
                
                


    # Affichage
    screen.fill(BLACK)
    draw_grid(joueur.direction, joueur.position, grid, room_images_grid)
    draw_top_right(joueur)

    if mode_selection:
        draw_bottom_right(salles_affichees, salles, selected_room_index, room_images_large)

    
    pygame.display.flip()
    clock.tick(30)
