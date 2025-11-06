import pygame
import sys

# --- Initialisation ---
pygame.init()
pygame.display.set_caption("Prototype Blue Prince")

# --- Dimensions de la fenêtre ---
WIDTH, HEIGHT = 1000, 750
LEFT_PANEL_WIDTH = 400  # zone des salles
RIGHT_PANEL_WIDTH = WIDTH - LEFT_PANEL_WIDTH
TOP_RIGHT_HEIGHT = 200
BOTTOM_RIGHT_HEIGHT = HEIGHT - TOP_RIGHT_HEIGHT

# --- Grille verticale : 9 lignes, 5 colonnes ---

ROWS, COLS = 9, 5
CELL_SIZE = LEFT_PANEL_WIDTH // COLS

# --- Couleurs ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (40, 40, 40)
LIGHT_GRAY = (100, 100, 100)
BLUE = (50, 100, 200)
GREEN = (60, 180, 75)
RED = (200, 50, 50)
YELLOW = (255, 200, 0)

# --- Fenêtre ---
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# --- Police ---
font = pygame.font.SysFont("arial", 20)

# --- Données de jeu ---
selected_cell = [0, 0]
steps = 0
keys = 0
inventory = ["Potion", "Clé d'argent"]

# Liste des types de salles avec couleurs associées
room_types = [
    ("Salle vide", LIGHT_GRAY),
    ("Salle piège", RED),
    ("Salle clé", GREEN),
    ("Salle trésor", YELLOW)
]
selected_room_index = 0

# --- Grille : chaque case = index du type de salle ---
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

# --- Fonctions ---
def draw_grid():
    """Affiche la grille des salles à gauche (verticale)."""
    for r in range(ROWS):
        for c in range(COLS):
            x = c * CELL_SIZE
            y = r * CELL_SIZE
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

            room_index = grid[r][c]
            _, color = room_types[room_index]

            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, GRAY, rect, 1)

            if [r, c] == selected_cell:
                pygame.draw.rect(screen, BLUE, rect, 3)


def draw_top_right():
    """Affiche l’inventaire et les infos."""
    x0 = LEFT_PANEL_WIDTH
    pygame.draw.rect(screen, GRAY, (x0, 0, RIGHT_PANEL_WIDTH, TOP_RIGHT_HEIGHT))
    
    text_lines = [
        f"Nombre de pas : {steps}",
        f"Clés : {keys}",
        "Inventaire :",
    ] + [f"  - {item}" for item in inventory]

    for i, txt in enumerate(text_lines):
        img = font.render(txt, True, WHITE)
        screen.blit(img, (x0 + 10, 10 + i * 25))


def draw_bottom_right():
    """Affiche la sélection de pièce à ajouter."""
    x0 = LEFT_PANEL_WIDTH
    y0 = TOP_RIGHT_HEIGHT
    pygame.draw.rect(screen, GRAY, (x0, y0, RIGHT_PANEL_WIDTH, BOTTOM_RIGHT_HEIGHT))
    
    label = font.render("Choix de la pièce :", True, WHITE)
    screen.blit(label, (x0 + 10, y0 + 10))

    for i, (name, _) in enumerate(room_types):
        color = GREEN if i == selected_room_index else WHITE
        img = font.render(f"{'>' if i == selected_room_index else ' '} {name}", True, color)
        screen.blit(img, (x0 + 20, y0 + 50 + i * 30))


def update_selection(key):
    """Déplace le curseur sur la grille."""
    global selected_cell
    r, c = selected_cell
    if key == pygame.K_UP and r > 0:
        r -= 1
    elif key == pygame.K_DOWN and r < ROWS - 1:
        r += 1
    elif key == pygame.K_LEFT and c > 0:
        c -= 1
    elif key == pygame.K_RIGHT and c < COLS - 1:
        c += 1
    selected_cell = [r, c]


def change_room_selection(key):
    """Change le type de salle choisi (4/6 ou pavé numérique)."""
    global selected_room_index
    if key in (pygame.K_4, pygame.K_KP4):
        selected_room_index = (selected_room_index - 1) % len(room_types)
    elif key in (pygame.K_6, pygame.K_KP6):
        selected_room_index = (selected_room_index + 1) % len(room_types)


def place_room():
    """Place le type de salle sélectionné dans la grille."""
    global steps
    r, c = selected_cell
    grid[r][c] = selected_room_index
    steps += 1


# --- Boucle principale ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                update_selection(event.key)
            elif event.key in (pygame.K_4, pygame.K_6, pygame.K_KP4, pygame.K_KP6):
                change_room_selection(event.key)
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                place_room()

    # --- Affichage ---
    screen.fill(BLACK)
    draw_grid()
    draw_top_right()
    draw_bottom_right()

    pygame.display.flip()
    clock.tick(30)