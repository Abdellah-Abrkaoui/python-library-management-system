# library class

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


    def supprimer_livre(self,titre):
            for book in self.books:
                if book.titre == titre:
                    self.books.remove(book)
                    print("book deleted")
                else:
                    # print("book not exist")
                    raise ValueError("Book not exists")
                

    def lister_livres(self):
        if not self.books:
            print("No books available.")
        else:
            for b in self.books:
                print(f"{b.titre} by {b.auteur} - {b.annee_publication}")



l1 = Library()
b1 = Book("ali","med",1000)
b2 = Book("book 2","med",1000)

l1.ajouter_livre(b1)
l1.lister_livres()
try:
    l1.supprimer_livre("aklsdj")
except ValueError as e :
    print(e)
l1.lister_livres()
