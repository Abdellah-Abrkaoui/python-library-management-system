# this is book class 

class Book():
    def __init__(self,titre,auteur,annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def affiche_livre(self):
        print(f"{self.titre} by {self.auteur} - year of pub : {self.annee_publication}")

    



# b1 = Book("abdellah","abrkaoui",2000)
# b1.affiche_livre()