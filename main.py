from interface_graphique import *


# --- Boucle principale ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT):
                set_direction(event.key)
            elif event.key in (pygame.K_4, pygame.K_6, pygame.K_KP4, pygame.K_KP6):
                change_room_selection(event.key)
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                move_in_direction()
                place_room()

    # --- Affichage ---
    screen.fill(BLACK)
    draw_grid()
    draw_top_right()
    draw_bottom_right()

    pygame.display.flip()
    clock.tick(30)