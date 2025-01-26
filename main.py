from tkinter import Tk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.gui import LibraryGUI

if __name__ == "__main__":
    root = Tk()
    app = LibraryGUI(root)
    root.mainloop()
