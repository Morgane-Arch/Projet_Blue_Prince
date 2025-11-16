class Piece:

    def __init__(self, nom, image, portes, cout, objets, rarete, couleur):
        self.nom = nom
        self.image = image
        self.portes = portes
        self.cout = cout
        self.objets = objets
        self.rarete = rarete
        self.couleur = couleur


salles = {
    "Antechamber": Piece("Antechamber", "Antechamber_Icon.png",
                           ["N","S","E","W"], 0, [], 0, "bleu"),

    "Attic": Piece("Attic", "Attic_Icon.png",
                        ["S"], 0, ["gemme","clé"], 0, "bleu"),

    "Billiard room": Piece("Billiard room", "Billiard_Room_Icon.png",
                     ["S","W"], 2,
                     ["gemme","gateau","permanent"], 2, "bleu"),

    "Closet": Piece("Closet", "Closet_Icon.png",
                        ["S"], 1,
                        ["pas","gemme","pomme"], 1, "bleu"),

    "Entrance Hall": Piece("Entrance Hall", "Entrance_Hall_Icon.png",
                     ["N","E","W"], 0,
                     ["sandwich","pomme"], 1, "bleu"),

    "Gallery": Piece("Gallery","Gallery_Icon.png",
                            ["N","S"], 1,
                            ["permanent"], 1, "bleu"),

    "Parlor": Piece("Parlor", "Parlor_Icon.png",
                      ["S","W"], 0, [], 0, "bleu"),

    "Room 8": Piece("Room 8","Room_8_Icon.png",
                     ["S","W"], 1, ["gemme"], 1, "bleu"),

    "Rotunda": Piece("Rotunda","Rotunda_Icon.png",
                     ["W","S"], 0, [], 2, "bleu"),

    "Spare Room": Piece("Spare Room","Spare_Room_Icon.png",
                       ["N","S"], 0, ["repas", "gemme"], 2, "bleu"),

    "Storeroom": Piece("Storeroom","Storeroom_Icon.png",
                  ["S"], 0,
                  ["permanent","pomme"], 1, "bleu"),

    "The foundation": Piece("The foundation","The_Foundation_Icon.png",
                         ["S","W","E"], 0, ["parmenant", "clé", "gemme", "repas"], 3, "bleu"),

    "Walk in closet": Piece("Walk in closet","Walk_in_Closet_Icon.png",
                         ["S"], 0, ["parmenant", "parmenant"], 3, "bleu")
}


#salles_est = [nom for nom, piece in salles.items() if "E" in piece.portes]