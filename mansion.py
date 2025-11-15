import random
from pieces import salles 
from objet_permanent import PERMANENTS

class Mansion:
    def __init__(self):
        self.rows = 9
        self.cols = 5

        # un map de 9x5
        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        # on commence par la case au milieu
        self.selected_cell = [4, 2]

        self.selected_direction = None

        # on introduit toutes les salles qu'on a
        self.room_types = [(nom, piece.image) for nom, piece in salles.items()]

        # 3 salles aléatoires
        self.salles_affichees = random.sample(self.room_types[2:], 3)
        self.selected_room_index = 0

        def Afficher_nom_salle(self):
            """Obtenir le nom de la salle actuelle"""
            r, c = self.selected_cell
            if self.grid[r][c] is None:
                return None
            nom = self.room_types[self.grid[r][c]][0]
            return salles[nom]



    def set_direction(self, direction):
        self.selected_direction = direction


   
    def bouger(self, joueur, direction):
        """On fait bouger le joueur"""

        r, c = self.selected_cell
        nr, nc = r, c

        # nouvelle position
        if direction == "haut" and r > 0:
            nr -= 1
        elif direction == "bas" and r < self.rows - 1:
            nr += 1
        elif direction == "gauche" and c > 0:
            nc -= 1
        elif direction == "droite" and c < self.cols - 1:
            nc += 1
        else:
            """si on dépasse la frontière, on ne bouge pas"""
            return False  

        
        room_here_index = self.grid[r][c]
        room_next_index = self.grid[nr][nc]

        if room_here_index is None or room_next_index is None:
            """s'il n'y a pas de salle à la position actuelle/ prochaine,
            on ne bouge pas"""
            return False

        room_here = salles[self.room_types[room_here_index][0]]
        room_next = salles[self.room_types[room_next_index][0]]

       
        mapping = {"haut": "N", "bas": "S", "gauche": "W", "droite": "E"}

        if room_here.portes[mapping[direction]] == 0:
            #porte fermée, il nous faut la clé ou le kit 
            if joueur.peut_ouvrir_portes or joueur.consommables.cle > 0:
                # on utilise la clé
                if not joueur.peut_ouvrir_portes:
                    joueur.consommables.retirer_objet("cle", 1)
            else:
                return False  # on n'a rien pour ouvrir

        # on retire 1 pas
        result = joueur.consommables.retirer_objet("pas", 1)
        if not result:
            print("GAME OVER — Vous n'avez plus de pas")
            return False

        # on met à jour la nouvelle position
        self.selected_cell = [nr, nc]

        # on rentre dans la salle
        self.enter_room(joueur)

        return True


    
    def place_selected_room(self):
        r, c = self.selected_cell

        if self.grid[r][c] is not None:
            return False  # salle déjà posée

        # on obtient le nom de la salle
        nom, _ = self.salles_affichees[self.selected_room_index]

        # on trouve l'index correpondant
        room_index = next(i for i, (n, f) in enumerate(self.room_types) if n == nom)

        # on le met dans grid
        self.grid[r][c] = room_index

        # on retire aléatoirement 3 salles
        self.salles_affichees = random.sample(self.room_types[2:], 3)
        self.selected_room_index = 0

        return True


    # Navigue dans la liste des salles affichées
    def change_room_selection(self, key):
        if key == 4:
            self.selected_room_index = (self.selected_room_index - 1) % len(self.salles_affichees)
        elif key == 6:
            self.selected_room_index = (self.selected_room_index + 1) % len(self.salles_affichees)


  
    def enter_room(self, joueur):
        """on gagne les objets en fonction de la salle"""

        room = self.Afficher_nom_salle()
        if room is None:
            return

        for obj in room.objets:

        
            if obj in ("pomme", "banana", "sandwich", "gateau", "repas"):
                gains = {
                    "pomme": 2,
                    "banana": 3,
                    "sandwich": 15,
                    "gateau": 10,
                    "repas": 25
                }
                joueur.consommables.ajouter_objet("pas", gains[obj])

            elif obj == "gemme":
                joueur.consommables.ajouter_objet("gemme", 1)

            elif obj == "clé":
                joueur.consommables.ajouter_objet("cle", 1)

      
            elif obj == "permanent":
                self.give_random_permanent(joueur)

          
            elif obj == "dig":
                if joueur.peut_creuser:
             
                    joueur.consommables.ajouter_objet("piece", 1)

        




    def donne_objetspermanent(self, joueur):
        options = list(PERMANENTS.values())
        objet = random.choice(options)
        objet.appliquer(joueur)
        joueur.objets_permanents.append(objet)