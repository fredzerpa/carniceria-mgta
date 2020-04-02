from tkinter import *
from PIL import ImageTk, Image
from functions import open_window


def show_receipt(main_win, ):
    open_window(Receipt, 350, 500, main_win)


class Receipt:
    def __init__(self, main_win):
        self.root = Toplevel(main_win, bg="white")
        self.root.title("Receipt - Carniceria Margarita")
        self.root.iconbitmap("./images/favicon.ico")
        self.root.resizable(False, False)
        self.root.geometry("350x500")
        self.root.focus()

        # Images
        self.logo_32 = ImageTk.PhotoImage(Image.open("./images/logo-32x32.png"))

        # Title
        Label(self.root, image=self.logo_32, bg="white").place(x=15, y=20)
        self.title = Label(self.root, text="Formulario de Registro", font=("Sans-serif", 14), bg="white")
        self.title.place(x=52, y=25)

        # Choosing Job Widgets
        self.choosing_area = LabelFrame(self.root, text="Cargo de Trabajo", padx=10, pady=2, bg="white")
        self.choosing_area.place(x=65, y=75)

        self.job = StringVar()
        self.job.set(None)
        Radiobutton(self.choosing_area, text="Admin", variable=self.job, value="admin", bg="white") \
            .grid(row=0, column=0, padx=5)
        Radiobutton(self.choosing_area, text="Cajero", variable=self.job, value="clerk", bg="white") \
            .grid(row=0, column=1, padx=5)

        # Username
        Label(self.root, text="Usuario", font=("Sans-serif", 12), bg="white").place(x=120, y=130)
        self.username = Entry(self.root, width=30, bd=3, relief=GROOVE)
        self.username.place(x=55, y=160)

        # Password
        Label(self.root, text="Clave", font=("Sans-serif", 12), bg="white").place(x=125, y=190)
        self.password = Entry(self.root, width=30, bd=3, relief=GROOVE)
        self.password.place(x=55, y=220)

        # Re Password
        Label(self.root, text="Re-Clave", font=("Sans-serif", 12), bg="white").place(x=115, y=250)
        self.re_password = Entry(self.root, width=30, bd=3, relief=GROOVE)
        self.re_password.place(x=55, y=280)

        # Cancel Button
        Button(self.root, text="Cancelar", width=10, command=self.root.destroy).place(x=60, y=330)

        # Register Button
        Button(self.root, text="Registrar", width=10, bg="#bbbcbd", activebackground="#8c9196", command=self.register
               ).place(x=155, y=330)

