import pygame
import sys
import os
import random

# --- Initialisation ---
pygame.init()
pygame.display.set_caption("Prototype Blue Prince")

# --- Dimensions de la fenêtre ---
WIDTH, HEIGHT = 1000, 750
LEFT_PANEL_WIDTH = 400  # zone des salles
RIGHT_PANEL_WIDTH = WIDTH - LEFT_PANEL_WIDTH
TOP_RIGHT_HEIGHT = 200
BOTTOM_RIGHT_HEIGHT = HEIGHT - TOP_RIGHT_HEIGHT

# --- Grille : 9 lignes, 5 colonnes ---
ROWS, COLS = 9, 5
CELL_SIZE = LEFT_PANEL_WIDTH // COLS

# --- Couleurs ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)
BLUE = (50, 100, 200)
CYAN = (0, 255, 255)
GREEN = (60, 180, 75)

# --- Fenêtre ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 20)

# --- Dossier contenant les images des salles ---
ROOM_IMAGE_FOLDER = "Images_salles"

# --- Types de salles disponibles ---
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

# --- Chargement des images (deux tailles) ---
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

# --- Sélection aléatoire initiale ---
salles_affichees = random.sample(room_types[2:], 3)


# --- Données de jeu ---
selected_cell = [8, 2]  # départ au centre bas
selected_direction = None
steps = 0
keys = 0
inventory = ["Potion", "Clé d'argent"]

# --- Grille : chaque case contient un index de salle ou None ---
grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
# Placer "Entrance Hall" sur la case de départ
grid[8][2] = 0  # 0 = index de "Entrance Hall" dans room_types
grid[0][2] = 1  # 1 = index de "Antechamber" dans room_types


# --- Fonctions d'affichage ---
def draw_direction_highlight(rect, direction):
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
    


def draw_grid():
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
                    draw_direction_highlight(rect, selected_direction)


def draw_top_right():
    """Affiche les infos du joueur."""
    x0 = LEFT_PANEL_WIDTH
    pygame.draw.rect(screen, GRAY, (x0, 0, RIGHT_PANEL_WIDTH, TOP_RIGHT_HEIGHT))

    # --- Texte des compteurs ---
    steps_text = font.render(f"Pas : {steps}", True, WHITE)
    keys_text = font.render(f"Clés : {keys}", True, WHITE)

    # Position alignée à droite
    right_margin = WIDTH - 20
    screen.blit(steps_text, (right_margin - steps_text.get_width(), 10))
    screen.blit(keys_text, (right_margin - keys_text.get_width(), 40))

    # --- Inventaire (à gauche, inchangé) ---
    inv_x = x0 + 10
    inv_y = 10
    inv_title = font.render("Inventaire :", True, WHITE)
    screen.blit(inv_title, (inv_x, inv_y))

    for i, item in enumerate(inventory):
        item_text = font.render(f"  - {item}", True, WHITE)
        screen.blit(item_text, (inv_x, inv_y + 25 * (i + 1)))


def draw_bottom_right():
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

    for i, (name, filename) in enumerate(salles_affichees):
        # Trouver l'index correspondant pour afficher la bonne image
        room_index = next(idx for idx, (n, f) in enumerate(room_types) if n == name)

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


# --- Fonctions de jeu ---
def change_room_selection(key):
    """Navigue dans la liste des salles affichées."""
    global selected_room_index
    if key in (pygame.K_4, pygame.K_KP4):
        selected_room_index = (selected_room_index - 1) % len(salles_affichees)
    elif key in (pygame.K_6, pygame.K_KP6):
        selected_room_index = (selected_room_index + 1) % len(salles_affichees)


def set_direction(key):
    """Change la direction mise en surbrillance sans bouger."""
    global selected_direction
    if key == pygame.K_UP:
        selected_direction = "up"
    elif key == pygame.K_DOWN:
        selected_direction = "down"
    elif key == pygame.K_LEFT:
        selected_direction = "left"
    elif key == pygame.K_RIGHT:
        selected_direction = "right"


def move_in_direction():
    """Déplace la sélection dans la direction choisie."""
    global selected_cell, steps
    if not selected_direction:
        return
    r, c = selected_cell
    if selected_direction == "up" and r > 0:
        r -= 1
    elif selected_direction == "down" and r < ROWS - 1:
        r += 1
    elif selected_direction == "left" and c > 0:
        c -= 1
    elif selected_direction == "right" and c < COLS - 1:
        c += 1
    selected_cell = [r, c]
    steps += 1


def place_room():
    """Place la salle sélectionnée dans la case actuelle, puis renouvelle le choix aléatoire."""
    global salles_affichees, selected_room_index

    r, c = selected_cell
    name, _ = salles_affichees[selected_room_index]

    # Trouver l'index correspondant dans room_types
    room_index = next(idx for idx, (n, f) in enumerate(room_types) if n == name)
    if grid[r][c] == None :
        grid[r][c] = room_index
        # --- Nouveau tirage aléatoire ---
        salles_affichees = random.sample(room_types[2:], 3)
        selected_room_index = 0  # réinitialise la sélection

    