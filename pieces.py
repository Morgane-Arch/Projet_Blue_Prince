class Piece:

    def __init__(self, nom, image, portes, cout, objets, rarete, condition_place):
        self.nom = nom
        self.image = image
        self.portes = portes
        self.cout = cout
        self.objets = objets
        self.rarete = rarete
        self.condition_place = condition_place


salles = {
    "Antechamber": Piece("Antechamber", "Antechamber_Icon.png",
                           {"N":0,"S":0,"E":0,"W":0}, 0, [], 0, "bleu"),

    "Attic": Piece("Attic", "Attic_Icon.png",
                        {"N":0,"S":0}, 0, ["gemme","clé"], 0, "bleu"),

    "Billiard room": Piece("Billiard room", "Billiard_Room_Icon.png",
                     {"N":0,"S":1,"E":0}, 2,
                     ["gemme","gateau","permanent"], 2, "bleu", "bordure"),

    "Closet": Piece("Closet", "Closet_Icon.png",
                        {"N":0,"S":0}, 1,
                        ["pas","gemme","pomme"], 1, "bleu"),

    "Entrance Hall": Piece("Entrance Hall", "Entrance_Hall_Icon.png",
                     {"N":0,"S":0,"E":0,"W":0}, 0,
                     ["sandwich","pomme"], 1, "bleu"),

    "Gallery": Piece("Gallery","Gallery_Icon.png",
                            {"N":0,"W":0,"E":0}, 1,
                            ["permanent"], 1, "bleu"),

    "Parlor": Piece("Parlor", "Parlor_Icon.png",
                      {"N":0,"S":0,"E":0,"W":0}, 0, [], 0, "bleu"),

    "Room 8": Piece("Room 8","Room_8_Icon.png",
                     {"E":0,"W":0}, 1, ["gemme"], 1, "bleu"),

    "Rotunda": Piece("Rotunda","Rotunda_Icon.png",
                     {"N":0,"S":1}, 0, [], 2, "bleu"),

    "Spare Room": Piece("Spare Room","Spare_Room_Icon.png",
                       {"N":1,"S":1,"E":1}, 0, ["repas", "gemme"], 2, "bleu"),

    "Storeroom": Piece("Storeroom","Storeroom_Icon.png",
                  {"N":0,"S":0}, 0,
                  ["permanent","pomme"], 1, "bleu"),

    "The foundation": Piece("The foundation","The_Foundation_Icon.png",
                         {"S":2}, 0, ["parmenant", "clé", "gemme", "repas"], 3, "bleu", "haut"),

    "Walk in closet": Piece("Walk in closet","Walk_in_Closet_Icon.png",
                         {"S":2}, 0, ["parmenant", "parmenant"], 3, "bleu", "haut")
}
