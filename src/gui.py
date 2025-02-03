import tkinter as tk
from tkinter import messagebox
from .library import Library
from .book import Book
import os

class LibraryGUI:
    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Gestion de la Bibliothèque")
        self.root.geometry("600x600")
        self.root.configure(bg="#F0F8FF")
        self.file_path = "data/books.txt"

        # Title Frame
        title_frame = tk.Frame(root, bg="#F0F8FF")
        title_frame.pack(pady=15)

        tk.Label(title_frame, text="📚", font=("Segoe UI Emoji", 24), 
                bg="#F0F8FF").pack(side="left", padx=5)
        tk.Label(title_frame, text="Gestion de la Bibliothèque", 
                font=("Arial", 18, "bold"), fg="blue", bg="#F0F8FF").pack(side="left")

        # Input Fields
        self.title_entry = self.create_entry("Titre : ")
        self.author_entry = self.create_entry("Auteur : ")
        self.year_entry = self.create_entry("Année : ")

        # Button Container
        button_frame = tk.Frame(self.root, bg="#F0F8FF")
        button_frame.pack(pady=10, padx=10)

        # Action Buttons
        self.create_button(button_frame, "📥 Ajouter Livre", self.add_book, "#4CAF50")
        self.create_button(button_frame, "🗑️ Supprimer Livre", self.remove_book, "#FF5733")
        self.create_button(button_frame, "💾 Sauvegarder", self.save_books, "#008CBA")
        self.create_button(button_frame, "📂 Lister Livres", self.load_books, "#555555")

        # Book List Display
        self.book_list = tk.Text(root, width=50, height=10, font=("Arial", 12), 
                               bg="white", fg="black", padx=10, pady=10)
        self.book_list.pack(pady=10)

    def create_entry(self, label_text):
        # Create consistent entry fields with aligned labels
        frame = tk.Frame(self.root, bg="#F0F8FF")
        frame.pack(pady=8)
        tk.Label(frame, text=label_text, font=("Arial", 12), 
                bg="#F0F8FF", width=8, anchor="w").pack(side="left")
        entry = tk.Entry(frame, font=("Arial", 12), width=25)
        entry.pack(side="left")
        return entry

    def create_button(self, parent, text, command, color):
        # Create buttons with fixed size: 250px width and 30px height
        btn = tk.Button(
            parent,
            text=text,
            command=command,
            bg=color,
            fg="white",
            font=("Segoe UI Emoji", 10, "bold"),  # Adjusted font size
            padx=10,
            pady=5,
            borderwidth=0,
            relief="flat",
            anchor="center",
            width=25,  # Width in characters (approximately 250px)
            height=1   # Height in lines (approximately 30px)
        )
        btn.pack(side="top", pady=4, padx=20)

        # Hover effects
        btn.bind("<Enter>", lambda e: btn.config(
            bg=self.lighten_color(color), 
            relief="raised"
        ))
        btn.bind("<Leave>", lambda e: btn.config(
            bg=color, 
            relief="flat"
        ))

    def lighten_color(self, color, factor=0.2):
        # Create hover effect by lightening colors
        color = color.lstrip('#')
        rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        lighter = tuple(min(255, int(c + (255 - c) * factor)) for c in rgb)
        return f'#{lighter[0]:02x}{lighter[1]:02x}{lighter[2]:02x}'

    def add_book(self):
        # Add book to library
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        year = self.year_entry.get().strip()

        if not all([title, author, year]):
            messagebox.showerror("Erreur", "Tous les champs sont requis.")
            return

        try:
            book = Book(title, author, int(year))
            self.library.ajouter_livre(book)
            messagebox.showinfo("Succès", f"Le livre '{title}' a été ajouté !")
            self.clear_entries()
            self.list_books()
        except ValueError:
            messagebox.showerror("Erreur", "Année invalide - doit être un nombre.")

    def remove_book(self):
        # Remove book from library
        title = self.title_entry.get().strip()
        if not title:
            messagebox.showerror("Erreur", "Titre requis pour suppression.")
            return

        try:
            self.library.supprimer_livre(title, self.file_path)
            self.library.sauvegarder_books(self.file_path)
            messagebox.showinfo("Succès", f"Livre '{title}' supprimé !")
            self.clear_entries()
            self.list_books()
        except ValueError:
            messagebox.showerror("Erreur", "Livre non trouvé.")

    def save_books(self):
        # Save books to file
        try:
            results = self.library.sauvegarder_books(self.file_path)
            messages = [
                f"Livre '{result['book']}' {'sauvegardé' if result['status'] == 'saved' else 'existe déjà'}"
                for result in results
            ]
            messagebox.showinfo("Sauvegarde", "\n".join(messages))
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec sauvegarde: {e}")

    def load_books(self):
        # Load books from file
        try:
            result = self.library.charger_book_list(self.file_path)
            message = result if isinstance(result, str) else "Livres chargés avec succès!"
            messagebox.showinfo("Chargement", message)
            self.list_books()
        except Exception as e:
            messagebox.showerror("Erreur", f"Échec chargement: {e}")

    def list_books(self):
        # Display all books in library
        self.book_list.delete(1.0, tk.END)
        if not self.library.books:
            self.book_list.insert(tk.END, "Aucun livre dans la bibliothèque.\n")
        else:
            for book in self.library.books:
                self.book_list.insert(tk.END, 
                    f"• {book.titre} par {book.auteur} ({book.annee_publication})\n")

    def clear_entries(self):
        # Clear input fields
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)


