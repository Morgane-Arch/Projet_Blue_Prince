import pygame
import sys
import os
import random


############ Définition des paramètres d'affichage ############

# Initialisation de la fenêtre d'affichage
pygame.init()
pygame.display.set_caption("Prototype Blue Prince")

# Dimensions de la fenêtre
WIDTH, HEIGHT = 1000, 750
LEFT_PANEL_WIDTH = 400  # zone des salles
RIGHT_PANEL_WIDTH = WIDTH - LEFT_PANEL_WIDTH
TOP_RIGHT_HEIGHT = 200
BOTTOM_RIGHT_HEIGHT = HEIGHT - TOP_RIGHT_HEIGHT

# Grille de gauche (9 lignes et 5 colonnes)
ROWS, COLS = 9, 5
CELL_SIZE = LEFT_PANEL_WIDTH // COLS

# Définitions de certaines couleurs utiles par la suite pour l'affichage
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)
BLUE = (50, 100, 200)
CYAN = (0, 255, 255)
GREEN = (60, 180, 75)

# Paramètres de la fenêtre pour réglage de l'affichage du jeu
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 20)





############ Définition des fonctions d'affichage ############

def draw_direction_highlight(rect, direction, selected_cell):
    """Dessine un surlignage sur le bord de la case selon la direction choisie."""
    margin = 4
    thickness = 6
    if direction == "up" and selected_cell[0] != 0:
        area = pygame.Rect(rect.x + margin, rect.y, CELL_SIZE - 2 * margin, thickness)
        pygame.draw.rect(screen, CYAN, area)
    elif direction == "down"  and selected_cell[0] != 8:
        area = pygame.Rect(rect.x + margin, rect.bottom - thickness, CELL_SIZE - 2 * margin, thickness)
        pygame.draw.rect(screen, CYAN, area)
    elif direction == "left" and selected_cell[1] != 0:
        area = pygame.Rect(rect.x, rect.y + margin, thickness, CELL_SIZE - 2 * margin)
        pygame.draw.rect(screen, CYAN, area)
    elif direction == "right" and selected_cell[1] != 4:
        area = pygame.Rect(rect.right - thickness, rect.y + margin, thickness, CELL_SIZE - 2 * margin)
        pygame.draw.rect(screen, CYAN, area)
    

def draw_grid(selected_direction, selected_cell, grid, room_images_grid):
    """Affiche la grille principale des salles."""
    for r in range(ROWS):
        for c in range(COLS):
            x = c * CELL_SIZE
            y = r * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            room_index = grid[r][c]
            if room_index is not None:
                img = room_images_grid[room_index]
                img_rect = img.get_rect(center=rect.center)
                screen.blit(img, img_rect)
            else:
                pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, (20, 20, 20), rect, 1)

            if [r, c] == selected_cell:
                pygame.draw.rect(screen, BLUE, rect, 3)
                if selected_direction:
                    draw_direction_highlight(rect, selected_direction, selected_cell)


def draw_top_right(inventory, joueur):
    """Affiche les infos du joueur."""
    x0 = LEFT_PANEL_WIDTH
    pygame.draw.rect(screen, GRAY, (x0, 0, RIGHT_PANEL_WIDTH, TOP_RIGHT_HEIGHT))

    # --- Texte des compteurs ---
    steps_text = font.render(f"Pas : {joueur.consommables.pas}", True, WHITE)
    pieces_text = font.render(f"Pièces : {joueur.consommables.piece}", True, WHITE)
    gemme_text = font.render(f"Gemmes : {joueur.consommables.gemme}", True, WHITE)
    keys_text = font.render(f"Clés : {joueur.consommables.cle}", True, WHITE)
    des_text = font.render(f"Dés : {joueur.consommables.de}", True, WHITE)

    # Position alignée à droite
    right_margin = WIDTH - 20
    screen.blit(steps_text, (right_margin - steps_text.get_width(), 10))
    screen.blit(pieces_text, (right_margin - pieces_text.get_width(), 40))
    screen.blit(gemme_text, (right_margin - gemme_text.get_width(), 70))
    screen.blit(keys_text, (right_margin - keys_text.get_width(), 100))
    screen.blit(des_text, (right_margin - des_text.get_width(), 130))

    # --- Inventaire (à gauche, inchangé) ---
    inv_x = x0 + 10
    inv_y = 10
    inv_title = font.render("Inventaire :", True, WHITE)
    screen.blit(inv_title, (inv_x, inv_y))

    for i, item in enumerate(inventory):
        item_text = font.render(f"  - {item}", True, WHITE)
        screen.blit(item_text, (inv_x, inv_y + 25 * (i + 1)))


def draw_bottom_right(salles_affichees, salles, selected_room_index, room_images_large):
    """Affiche 3 salles choisies aléatoirement (renouvelées après chaque placement)."""
    x0 = LEFT_PANEL_WIDTH
    y0 = TOP_RIGHT_HEIGHT
    pygame.draw.rect(screen, GRAY, (x0, y0, RIGHT_PANEL_WIDTH, BOTTOM_RIGHT_HEIGHT))
    label = font.render("Choix de la salle :", True, WHITE)
    screen.blit(label, (x0 + 10, y0 + 10))

    # Paramètres d'affichage
    img_size = 160
    spacing = 180
    start_x = x0 + 40
    base_y = y0 + 60

    for i, piece in enumerate(salles_affichees):
        name = piece.nom
        filename = piece.image
        # Trouver l'index correspondant pour afficher la bonne image
        room_index = next(idx for idx, piece in enumerate(salles) if piece.nom == name)

        x = start_x + i * spacing

        # Surlignage vert autour de la salle sélectionnée
        if i == selected_room_index:
            pygame.draw.rect(screen, GREEN, (x - 5, base_y - 5, img_size + 10, img_size + 40), 2)

        # Image
        screen.blit(room_images_large[room_index], (x, base_y))

        # Nom centré sous l'image
        text_img = font.render(name, True, WHITE)
        text_rect = text_img.get_rect(center=(x + img_size // 2, base_y + img_size + 20))
        screen.blit(text_img, text_rect)


############ Définition des fonctions de jeu (A INCLURE DANS LES CLASSES JOUEUR ET PIECE ?) ############

def change_room_selection(key, selected_room_index, salles_affichees):
    """Navigue dans la liste des salles affichées."""
    if key in (pygame.K_4, pygame.K_KP4):
        selected_room_index = (selected_room_index - 1) % len(salles_affichees)
    elif key in (pygame.K_6, pygame.K_KP6):
        selected_room_index = (selected_room_index + 1) % len(salles_affichees)
    return selected_room_index


def place_room(salles_affichees, selected_room_index, selected_cell, salles, grid):
    """Place la salle sélectionnée dans la case actuelle, puis renouvelle le choix aléatoire."""
    r, c = selected_cell
    name, _ = (salles_affichees[selected_room_index].nom, salles_affichees[selected_room_index].image)

    # Trouver l'index correspondant dans room_types
    room_index = next(idx for idx, piece in enumerate(salles) if piece.nom == name)
    if grid[r][c] == None :
        grid[r][c] = room_index
        # Nouveau tirage des salles aléatoire
        salles_affichees = random.sample(salles[2:], 3)
        selected_room_index = 0  # réinitialise la sélection de la salle

    return grid, salles_affichees, selected_room_index