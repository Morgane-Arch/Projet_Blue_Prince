import pygame
from joueur import Joueur
from mansion import Mansion
import interface_graphique as ui


class Game:

    def __init__(self):
        # Création du manoir (carte 9x5)
        self.mansion = Mansion()

        # Création du joueur à la position de départ du manoir
        self.joueur = Joueur(self.mansion.selected_cell)

        # Indique si le jeu doit continuer
        self.running = True


    def play(self):
        """Boucle principale du jeu"""

        while self.running:

        
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:

                    # Déplacements

                    if event.key == pygame.K_UP:
                        self.mansion.bouger(self.joueur, "haut")

                    elif event.key == pygame.K_DOWN:
                        self.mansion.bouger(self.joueur, "bas")

                    elif event.key == pygame.K_LEFT:
                        self.mansion.bouger(self.joueur, "gauche")

                    elif event.key == pygame.K_RIGHT:
                        self.mansion.bouger(self.joueur, "droite")

                    #  Changer la salle 

                    elif event.key == pygame.K_4:
                        self.mansion.change_room_selection(4)

                    elif event.key == pygame.K_6:
                        self.mansion.change_room_selection(6)

                    # Placer une salle dans la grille

                    elif event.key == pygame.K_p:
                        self.mansion.place_selected_room()


         
            ui.screen.fill((0, 0, 0))

            # Grille de gauche
            ui.draw_grid(
                self.mansion.selected_direction,
                self.mansion.selected_cell,
                self.mansion.grid,
                ui.room_images_grid
            )

            # Panneau de droite haut 
            ui.draw_top_right(
                self.joueur.objets_permanents,
                self.joueur
            )

            # Panneau de droite bas : choix des 3 salles
            ui.draw_bottom_right(
                self.mansion.salles_affichees,
                self.mansion.room_types,
                self.mansion.selected_room_index,
                ui.room_images_large
            )

            pygame.display.flip()

        pygame.quit()
