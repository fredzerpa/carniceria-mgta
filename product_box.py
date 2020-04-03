from tkinter import *
from PIL import ImageTk, Image


class Product:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Product Info - Carniceria Margarita")
        self.root.iconbitmap("./images/favicon.ico")
        self.root.resizable(False, False)
        self.root.focus()