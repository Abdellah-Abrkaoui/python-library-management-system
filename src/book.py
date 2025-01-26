# this is book class 

class Book():
    def __init__(self,titre,auteur,annee_publication):
        if not titre or not auteur:
            raise ValueError("title and author can't be empty")
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def affiche_livre(self):
        print(f"{self.titre} by {self.auteur} - year of pub : {self.annee_publication}")

    




# try:
#     b1 = Book("book 1","auteur 1",2000)
#     b1.affiche_livre()
# except ValueError as e :
#     print(e)