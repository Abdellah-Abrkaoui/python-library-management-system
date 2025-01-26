

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


<<<<<<< HEAD
    def supprimer_livre(self,book):
        if any(b.titre == book.titre for b in self.books):
            self.books.remove(book)
            print("book deleted")
        else:
            raise ValueError("book not exist")
        
        

=======
    def supprimer_livre(self,titre):
            for book in self.books:
                if book.titre == titre:
                    self.books.remove(book)
                    print("book deleted")
                else:
                    # print("book not exist")
                    raise ValueError("Book not exists")
                
>>>>>>> e36097ad6900e4e3a3b574be9423ee3c101bd848

    def lister_livres(self):
        if not self.books:
            print("No books available.")
        else:
            for b in self.books:
                print(f"{b.titre} by {b.auteur} - {b.annee_publication}")



l1 = Library()
b1 = Book("ali","med",1000)
<<<<<<< HEAD
b3 = Book("ali","med",1000)
l1.ajouter_livre(b1)
l1.lister_livres()
try:
    l1.supprimer_livre(b3)
except ValueError as e:
    print(e)    

=======
b2 = Book("book 2","med",1000)

l1.ajouter_livre(b1)
l1.lister_livres()
try:
    l1.supprimer_livre("aklsdj")
except ValueError as e :
    print(e)
>>>>>>> e36097ad6900e4e3a3b574be9423ee3c101bd848
l1.lister_livres()
