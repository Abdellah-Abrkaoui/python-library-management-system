

from book import Book
class Library():

    def __init__(self):
        self.books = [] 

    
    def ajouter_livre(self,book):
        if any(b.titre == book.titre for b in self.books):
            print("This book already exists.")
        else :
            self.books.append(book)
            print(f"Book '{book.titre}' added.")


    def supprimer_livre(self,book):
        if any(b.titre == book.titre for b in self.books):
            self.books.remove(book)
            print("book deleted")
        else:
            raise ValueError("book not exist")
        
        


    def lister_livres(self):
        if not self.books:
            print("No books available.")
        else:
            for b in self.books:
                print(f"{b.titre} by {b.auteur} - {b.annee_publication}")



l1 = Library()
b1 = Book("ali","med",1000)
b3 = Book("ali","med",1000)
l1.ajouter_livre(b1)
l1.lister_livres()
try:
    l1.supprimer_livre(b3)
except ValueError as e:
    print(e)    

l1.lister_livres()
