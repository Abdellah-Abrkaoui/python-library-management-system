import tkinter as tk
from tkinter import messagebox
from .library import Library
from .book import Book

class LibraryGUI:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Library Management System")
        self.file_path = "data/books.txt"  # File path for saving/loading books

        # Title
        tk.Label(root, text="Library Management System", font=("Arial", 16, "bold")).pack(pady=10)

        # Input fields
        self.title_entry = self.create_entry("Title:")
        self.author_entry = self.create_entry("Author:")
        self.year_entry = self.create_entry("Year:")

        # Buttons
        tk.Button(root, text="Add Book", command=self.add_book, bg="green", fg="white").pack(pady=5)
        tk.Button(root, text="Remove Book", command=self.remove_book, bg="red", fg="white").pack(pady=5)
        # tk.Button(root, text="List Books", command=self.list_books).pack(pady=5)
        tk.Button(root, text="Save Books", command=self.save_books).pack(pady=5)
        tk.Button(root, text="Load Books", command=self.load_books).pack(pady=5)

        # Display area
        self.book_list = tk.Text(root, width=50, height=15)
        self.book_list.pack(pady=10)

    def create_entry(self, label_text):
        """Creates a labeled input field."""
        frame = tk.Frame(self.root)
        frame.pack(pady=5)
        tk.Label(frame, text=label_text).pack(side="left")
        entry = tk.Entry(frame)
        entry.pack(side="left")
        return entry

    def add_book(self):
        """Adds a book to the library."""
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        year = self.year_entry.get().strip()

        if not title or not author or not year:
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            book = Book(title, author, int(year))
            self.library.ajouter_livre(book)
            messagebox.showinfo("Success", f"Book '{title}' added!")
            self.clear_entries()
            self.list_books()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")

    def remove_book(self):
        """Removes a book from the library."""
        title = self.title_entry.get().strip()

        if not title:
            messagebox.showerror("Error", "Title field is required to remove a book.")
            return

        try:
            self.library.supprimer_livre(title,self.file_path)  # Remove the book from the library
            self.library.sauvegarder_books(self.file_path)  # Save the updated library to the file
            messagebox.showinfo("Success", f"Book '{title}' removed!")
            self.clear_entries()
            self.list_books()  # Refresh the book list in the interface
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")

    # def list_books(self):
    #     """Lists all books in the library."""
    #     self.book_list.delete(1.0, tk.END)
    #     if not self.library.books:
    #         self.book_list.insert(tk.END, "No books in the library.\n")
    #     else:
    #         for book in self.library.books:
    #             self.book_list.insert(tk.END, f"{book.titre} by {book.auteur} - {book.annee_publication}\n")

    def save_books(self):
        """Saves the books to the file."""
        try:
            results = self.library.sauvegarder_books(self.file_path)
            messages = []
            for result in results:
                if result["status"] == "saved":
                    messages.append(f"Book '{result['book']}' saved.")
                else:
                    messages.append(f"Book '{result['book']}' already exists.")
            messagebox.showinfo("Save Results", "\n".join(messages))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save books: {e}")

    def load_books(self):
        """Loads books from the file."""
        try:
            result = self.library.charger_book_list(self.file_path)
            if isinstance(result, str):
                messagebox.showinfo("Info", result)
            else:
                messagebox.showinfo("Success", "Books loaded from file!")
            self.list_books()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load books: {e}")

    def clear_entries(self):
        """Clears all input fields."""
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
