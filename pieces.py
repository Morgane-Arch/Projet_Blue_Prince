class Piece:
    """
    Classe représentant une pièce du manoir

    Paramètres : 
        nom : str
            Nom de la salle
        image : str
            Nom du fichier qui contient l'image de la pièce 
        portes : List[str]
            Direction dans lesquelles la salle possède une sortie
        cout : int 
            Coût pour entrer dans la pièce
        objets : list[str]
            Liste des objets pouvant apparaître dans la salle
        rarete : int
            Indice de rareté de la pièce 
        couleur : str
            Couleur de la pièce
    Attributs : 
        objets_restants : list[str]
            Permet de gérer la non réaparition des objets une fois qu'on a visité une salle
    """

    def __init__(self, nom, image, portes, cout, objets, rarete, couleur):
        self.nom = nom
        self.image = image
        self.portes = portes
        self.cout = cout
        self.objets = objets
        self.rarete = rarete
        self.couleur = couleur

        self.objets_restants = objets[:]

    #Méthode retire_pas - pour les pièces qui ont l'attribut spécial de retirer des pas en entrant
    def retirer_pas(self, joueur):
        """
        Fonction permettant de retirer des pas au joueur lorsqu'il entre dans une pièce qui possède cet 'objet'

        Paramètre : 
            joueur : Joueur
        """
        if "retire_pas" in self.objets:
            joueur.consommables.retirer_objet("pas", 1)
            print(f"La pièce {self.nom} retire un pas supplémentaire au joueur.")

# Définition de chaque pièce en fonction de tous leurs paramètres
Antechamber = Piece("Antechamber", "Antechamber_Icon.png", ["N","S","E","W"], 0, [], 0, "bleu")
Attic = Piece("Attic", "Attic_Icon.png", ["S"], 0, ["gemme","cle", "coffre"], 0, "bleu")
Billiard_room = Piece("Billiard room", "Billiard_Room_Icon.png", ["S","W"], 2, ["gemme","gateau","permanent", "coffre"], 2, "bleu")
Closet = Piece("Closet", "Closet_Icon.png", ["S"], 1, ["pas","gemme","pomme", "coffre"], 1, "bleu")
Entrance_Hall = Piece("Entrance Hall", "Entrance_Hall_Icon.png", ["N","E","W"], 0, ["sandwich","pomme"], 1, "bleu")
Gallery = Piece("Gallery","Gallery_Icon.png", ["N","S"], 1, ["permanent", "coffre"], 1, "bleu")
Parlor = Piece("Parlor", "Parlor_Icon.png", ["S","W"], 0, [], 0, "bleu")
Room_8 = Piece("Room 8","Room_8_Icon.png", ["S","W"], 1, ["gemme"], 1, "bleu")
Rotunda = Piece("Rotunda","Rotunda_Icon.png", ["W","S"], 2, [], 2, "bleu")
Spare_Room = Piece("Spare Room","Spare_Room_Icon.png", ["N","S"], 0, ["repas", "gemme"], 2, "bleu")
Storeroom = Piece("Storeroom","Storeroom_Icon.png", ["S"], 0, ["permanent","pomme"], 1, "bleu")
The_foundation = Piece("The foundation","The_Foundation_Icon.png", ["S","W","E"], 0, ["permanent", "cle", "gemme", "repas"], 3, "bleu")
Walk_in_closet = Piece("Walk in closet","Walk-in_Closet_Icon.png", ["S"], 1, ["permanent", "permanent"], 3, "bleu")
Locker_room = Piece("Locker room","Locker_Room_Icon.png", ["N","S"], 0, ["casier"], 3, "bleu")
Bookshop = Piece("Bookshop", "Bookshop_Icon.png", ["S","W"], 0, ["pomme","gateau","sandwich","cle", "coffre"], 1, "yellow")
Kitchen = Piece("Kitchen", "Kitchen_Icon.png", ["W","S"], 2, ["pomme","gateau","sandwich","cle"], 2, "yellow")
Showroom = Piece("Showroom", "Showroom_Icon.png", ["N","S"], 0, ["pomme","gateau","sandwich","cle"], 0, "yellow")
Bunk_room = Piece("Bunk room", "Bunk_Room_Icon.png", ["S"], 1, ["pas"], 2, "purple")
Secret_Garden = Piece("Secret Garden", "Secret_Garden_Icon.png", ["W","S","E"], 0, ["gemme","permanent", "creuser"], 2, "green")
Great_hall = Piece("Great hall", "Great_Hall_Icon.png", ["S","N","W","E"], 0, [], 1, "orange")
Chapel = Piece("Chapel", "Chapel_Icon.png", ["E","W","S"], 0, ["retire_pas"], 0, "red")
Weight_room = Piece("Weight room", "Weight_Room_Icon.png", ["E","W","S","N"], 0, ["retire_pas"], 1, "red")
Archives = Piece("Archives", "Archives_Icon.png", ["E","W","N","S"], 1, ["retire_pas"], 1, "red")
Cloister = Piece("Cloister", "Cloister_Icon.png", ["N","S","E","W"], 1, ["gemme","permanent"], 1, "green")
Commissary = Piece("Commissary", "Commissary_Icon.png", ["W","S"], 1, ["pomme","gateau","sandwich","cle"], 1, "yellow")
Corridor = Piece("Corridor", "Corridor_Icon.png", ["N","S"], 1, ["creuser"], 1, "orange")
Courtyard = Piece("Courtyard", "Courtyard_Icon.png", ["W","E","S"], 1, ["gemme","permanent"], 1, "green")
Foyer = Piece("Foyer", "Foyer_Icon.png", ["N","S"], 1, [], 1, "orange")
Furnace = Piece("Furnace", "Furnace_Icon.png", ["S"], 1, ["retire_pas"], 1, "red")
Gymnasium = Piece("Gymnasium", "Gymnasium_Icon.png", ["E","W","S"], 1, ["retire_pas"], 1, "red")
Laundry_Room = Piece("Laundry_Room", "Laundry_Room_Icon.png", ["S"], 1, ["pomme","gateau","sandwich","cle"], 1, "yellow")
Lavatory = Piece("Lavatory", "Lavatory_Icon.png", ["S"], 1, ["retire_pas"], 1, "red")
Locksmith = Piece("Locksmith", "Locksmith_Icon.png", ["S"], 1, ["pomme","gateau","sandwich","cle"], 1, "yellow")
Morning_Room = Piece("Morning_Room", "Morning_Room_Icon.png", ["W","S"], 1, ["gemme","permanent"], 1, "green")
Nursery = Piece("Nursery", "Nursery_Icon.png", ["S"], 1, ["pas"], 1, "purple")
Patio = Piece("Patio", "Patio_Icon.png", ["W","S"], 1, ["gemme","permanent", "creuser", "coffre"], 1, "green")
Veranda = Piece("Veranda", "Veranda_Icon.png", ["N","S"], 1, ["gemme","permanent", "coffre"], 1, "green")

#Liste du nom de toutes les salles
salles = [
    Entrance_Hall,
    Antechamber,
    Attic,
    Billiard_room,
    Closet,
    Gallery,
    Parlor,
    Room_8,
    Rotunda,
    Spare_Room,
    Storeroom,
    The_foundation,
    Walk_in_closet,
    Locker_room,
    Bookshop,
    Bunk_room,
    Chapel,
    Great_hall,
    Kitchen,
    Secret_Garden,
    Showroom,
    Weight_room,
    Archives,
    Cloister,
    Commissary,
    Corridor,
    Courtyard,
    Foyer,
    Furnace,
    Gymnasium,
    Laundry_Room,
    Lavatory,
    Locksmith,
    Morning_Room,
    Nursery,
    Patio,
    Veranda
]

