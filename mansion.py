import random
from pieces import salles
from objet_permanent import PERMANENTS


class Mansion:
    def __init__(self):
        self.rows = 9
        self.cols = 5

        # Carte 9x5
        self.grille = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        # Position initiale du joueur
        self.case_selectionnee = [4, 2]

        # Direction sélectionnée 
        self.direction_selectionnee = None

        # Liste de toutes les salles
        self.types_salles = [(nom, piece.image) for nom, piece in salles.items()]

        # 3 salles tirées au hasard
        self.salles_affichees = random.sample(self.types_salles[2:], 3)
        self.index_salle_selectionnee = 0


    # ======================
    # Obtenir la salle actuelle
    # ======================
    def afficher_nom_salle(self):
        r, c = self.case_selectionnee
        if self.grille[r][c] is None:
            return None
        nom = self.types_salles[self.grille[r][c]][0]
        return salles[nom]


    # ======================
    # Déplacement du joueur
    # ======================
    def bouger(self, joueur, direction):
        r, c = self.case_selectionnee
        nr, nc = r, c

        if direction == "haut" and r > 0:
            nr -= 1
        elif direction == "bas" and r < self.rows - 1:
            nr += 1
        elif direction == "gauche" and c > 0:
            nc -= 1
        elif direction == "droite" and c < self.cols - 1:
            nc += 1
        else:
            return False

        # Vérification de salle destination
        if self.grille[r][c] is None or self.grille[nr][nc] is None:
            return False

        salle_actuelle = salles[self.types_salles[self.grille[r][c]][0]]

        mapping = {"haut": "N", "bas": "S", "gauche": "W", "droite": "E"}

        # Porte fermée 
        if salle_actuelle.portes[mapping[direction]] == 0:

            # joueur peut ouvrir ?
            if joueur.peut_ouvrir_portes or joueur.consommables.cle > 0:

                # s'il utilise une clé, on la retire
                if not joueur.peut_ouvrir_portes:
                    joueur.consommables.retirer_objet("cle", 1)

            else:
                return False

        # Sinon consommer 1 pas
        if not joueur.consommables.retirer_objet("pas", 1):
            print("GAME OVER — plus de pas")
            return False

        # Nouvelle position
        self.case_selectionnee = [nr, nc]

        # Entrer dans la salle
        self.entrer_dans_salle(joueur)

        return True


    # ======================
    # Placer une salle
    # ======================
    def placer_salle_selectionnee(self):
        r, c = self.case_selectionnee

        if self.grille[r][c] is not None:
            return False

        nom, _ = self.salles_affichees[self.index_salle_selectionnee]
        index = next(i for i, (n, f) in enumerate(self.types_salles) if n == nom)

        self.grille[r][c] = index

        # Nouveau tirage des salles
        self.salles_affichees = random.sample(self.types_salles[2:], 3)
        self.index_salle_selectionnee = 0

        return True


    # ======================
    # Naviguer dans les salles proposées
    # ======================
    def changer_selection_salle(self, key):
        if key == 4:
            self.index_salle_selectionnee = (self.index_salle_selectionnee - 1) % len(self.salles_affichees)
        elif key == 6:
            self.index_salle_selectionnee = (self.index_salle_selectionnee + 1) % len(self.salles_affichees)


    # ======================
    # Entrer → obtenir objets
    # ======================
    def entrer_dans_salle(self, joueur):

        salle = self.afficher_nom_salle()
        if salle is None:
            return

        for obj in salle.objets:

            # ===== nourriture : donne des pas =====
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
                self.donner_permanent_aleatoire(joueur)

          
           


    # ======================
    # Obtenir un objet permanent
    # ======================
    def donner_permanent_aleatoire(self, joueur):
        options = list(PERMANENTS.values())
        objet = random.choice(options)
        objet.appliquer(joueur)
        joueur.objets_permanents.append(objet)
