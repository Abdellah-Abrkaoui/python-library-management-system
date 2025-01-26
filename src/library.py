# library class

from .book import Book


class Library:
    def __init__(self):
        self.books = []  # Initialize an empty list of books

    def ajouter_livre(self, book):
        # Check if the book already exists in the library
        if any(b.titre == book.titre for b in self.books):
            raise ValueError("This book already exists.")
        else:
            self.books.append(book)
            print(f"Book '{book.titre}' added.")

    def supprimer_livre(self, titre, pathfile=None):
        for book in self.books:
            if book.titre == titre:
                self.books.remove(book)
                print(f"Book '{titre}' deleted.")
                
                # If a file path is provided, update the file to reflect the change
                if pathfile:
                    try:
                        with open(pathfile, "r") as file:
                            lines = file.readlines()
                        
                        # Rewrite the file excluding the deleted book
                        with open(pathfile, "w") as file:
                            for line in lines:
                                # Check if the current line matches the deleted book
                                if line.strip() != f"{book.titre} - {book.auteur} - {book.annee_publication}":
                                    file.write(line)
                    except Exception as e:
                        raise Exception(f"Failed to update the file: {e}")
                
                return  # Exit after removing the book
        # Raise an error if the book is not found
        raise ValueError("Book does not exist.")


    def lister_livres(self):
        # List all the books in the library
        if not self.books:
            print("No books available.")
        else:
            for b in self.books:
                print(f"{b.titre} by {b.auteur} - {b.annee_publication}")

    def sauvegarder_books(self, pathfile):
        # Save the library's books to a file
        results = []  # To store the save status of each book
        try:
            # Read existing books from the file
            try:
                with open(pathfile, "r") as file:
                    existing_books = set(file.readlines())  # Use a set for quick lookups
            except FileNotFoundError:
                existing_books = set()  # Handle the case where the file doesn't exist

            # Append new books to the file if they don't already exist
            with open(pathfile, "a") as file:
                for b in self.books:
                    book_data = f"{b.titre} - {b.auteur} - {b.annee_publication}\n"
                    if book_data not in existing_books:
                        file.write(book_data)
                        results.append({"book": b.titre, "status": "saved"})
                    else:
                        results.append({"book": b.titre, "status": "exists"})

        except Exception as e:
            raise e  # Raise any unexpected errors to the caller

        return results

    def charger_book_list(self, pathfile):
        # Load books from a file into the library
        try:
            with open(pathfile, "r") as file:
                content = file.readlines()
                for line in content:
                    # Parse each line and create a Book object
                    titre, auteur, annee = line.strip().split(" - ")
                    annee = int(annee)  # Convert year to integer
                    self.ajouter_livre(Book(titre, auteur, annee))
        except FileNotFoundError:
            return f"File '{pathfile}' does not exist."
        except Exception as e:
            raise e  # Raise unexpected errors
