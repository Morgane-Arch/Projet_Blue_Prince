class Piece:

    def __init__(self, nom, image, portes, cout, objets, rarete, couleur):
        self.nom = nom
        self.image = image
        self.portes = portes
        self.cout = cout
        self.objets = objets
        self.rarete = rarete
        self.couleur = couleur



Antechamber = Piece("Antechamber", "Antechamber_Icon.png", ["N","S","E","W"], 0, [], 0, "bleu")
Attic = Piece("Attic", "Attic_Icon.png", ["S"], 0, ["gemme","clé"], 0, "bleu")
Billiard_room = Piece("Billiard room", "Billiard_Room_Icon.png", ["S","W"], 2, ["gemme","gateau","permanent"], 2, "bleu")
Closet = Piece("Closet", "Closet_Icon.png", ["S"], 1, ["pas","gemme","pomme"], 1, "bleu")
Entrance_Hall = Piece("Entrance Hall", "Entrance_Hall_Icon.png", ["N","E","W"], 0, ["sandwich","pomme"], 1, "bleu")
Gallery = Piece("Gallery","Gallery_Icon.png", ["N","S"], 1, ["permanent"], 1, "bleu")
Parlor = Piece("Parlor", "Parlor_Icon.png", ["S","W"], 0, [], 0, "bleu")
Room_8 = Piece("Room 8","Room_8_Icon.png", ["S","W"], 1, ["gemme"], 1, "bleu")
Rotunda = Piece("Rotunda","Rotunda_Icon.png", ["W","S"], 0, [], 2, "bleu")
Spare_Room = Piece("Spare Room","Spare_Room_Icon.png", ["N","S"], 0, ["repas", "gemme"], 2, "bleu")
Storeroom = Piece("Storeroom","Storeroom_Icon.png", ["S"], 0, ["permanent","pomme"], 1, "bleu")
The_foundation = Piece("The foundation","The_Foundation_Icon.png", ["S","W","E"], 0, ["parmenant", "clé", "gemme", "repas"], 3, "bleu")
Walk_in_closet = Piece("Walk in closet","Walk-in_Closet_Icon.png", ["S"], 0, ["parmenant", "parmenant"], 3, "bleu")



salles = [Entrance_Hall, Antechamber, Attic, Billiard_room, Closet, Gallery, Parlor, Room_8, Rotunda, Spare_Room, Storeroom, The_foundation, Walk_in_closet]



#salles_est = [nom for nom, piece in salles.items() if "E" in piece.portes]