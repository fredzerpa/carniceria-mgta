from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from functions import open_window, center_window
from receipt import Receipt, show_receipt


def show_main(name, job, prev_win):
    open_window(MainSystem, 1280, 800, name, job, prev_win)


class MainSystem:
    def __init__(self, name, job, prev_win):
        self.root = Toplevel()
        self.root.title(f"Bienvenido {name.capitalize()}, Carniceria Margarita")
        self.root.iconbitmap("./images/favicon.ico")
        self.root.resizable(False, False)

        self.login_win = prev_win

        self.receipt = Receipt

        # User
        self.name = name
        self.job = job

        # Images
        self.bg_image = ImageTk.PhotoImage(Image.open("./images/main-logo.png"))
        self.products = {
            "ribs": {
                "name": "Baby Back Ribs",
                "price": 3,
                "image": PhotoImage(file=r"./images/products/ribs.png").subsample(4, 4),
                "stock": 20
            },
            "groundBeef": {
                "name": "Carne Molida",
                "price": 2.5,
                "image": PhotoImage(file=r"./images/products/carne-molida.png").subsample(4, 4),
                "stock": 20
            },
            "chicken": {
                "name": "Muslo de Pollo",
                "price": 1.5,
                "image": PhotoImage(file=r"./images/products/muslo.png").subsample(4, 4),
                "stock": 20
            },
            "steak": {
                "name": "Bistec",
                "price": 3.5,
                "image": PhotoImage(file=r"./images/products/bistec.png").subsample(4, 4),
                "stock": 20
            },
            "chorizo": {
                "name": "Chorizo",
                "price": 10,
                "image": PhotoImage(file=r"./images/products/chorizo.png").subsample(4, 4),
                "stock": 20
            },
            "bacon": {
                "name": "Tocineta",
                "price": 5,
                "image": PhotoImage(file=r"./images/products/tocineta.png").subsample(4, 4),
                "stock": 20
            },
            "meatRoast": {
                "name": "Carne para Mechar",
                "price": 2,
                "image": PhotoImage(file=r"./images/products/mechada.png").subsample(4, 4),
                "stock": 20
            },
            "porkLeg": {
                "name": "Pernil",
                "price": 3.5,
                "image": PhotoImage(file=r"./images/products/pernil.png").subsample(4, 4),
                "stock": 20
            },
            "cheese": {
                "name": "Queso Blanco",
                "price": 3,
                "image": PhotoImage(file=r"./images/products/queso.png").subsample(4, 4),
                "stock": 0
            },
            "ham": {
                "name": "Jamon Precocido",
                "price": 2.5,
                "image": PhotoImage(file=r"./images/products/jamon.png").subsample(4, 4),
                "stock": 0
            }
        }
        # Working Area
        self.working_bg = Label(self.root, image=self.bg_image, bg="black")
        self.working_bg.grid(row=0, column=0, columnspan=3)

        self.working_frame = Frame(self.working_bg, bd=4, bg="white", relief=RIDGE,
                                   width=950, height=550, padx=10, pady=10)
        self.working_frame.pack(pady=25, padx=25)

        Button(self.working_frame, image=self.products["ribs"]["image"], activebackground="#ccc", command=lambda: self.selected_product("ribs")) \
            .place(x=0, y=0)
        Button(self.working_frame, image=self.products["groundBeef"]["image"], activebackground="#ccc") \
            .place(x=150, y=0)
        Button(self.working_frame, image=self.products["chicken"]["image"], activebackground="#ccc") \
            .place(x=300, y=0)
        Button(self.working_frame, image=self.products["steak"]["image"], activebackground="#ccc") \
            .place(x=450, y=0)
        Button(self.working_frame, image=self.products["chorizo"]["image"], activebackground="#ccc") \
            .place(x=600, y=0)
        Button(self.working_frame, image=self.products["bacon"]["image"], activebackground="#ccc") \
            .place(x=750, y=0)
        Button(self.working_frame, image=self.products["meatRoast"]["image"], activebackground="#ccc") \
            .place(x=0, y=150)
        Button(self.working_frame, image=self.products["porkLeg"]["image"], activebackground="#ccc") \
            .place(x=150, y=150)
        Button(self.working_frame, image=self.products["cheese"]["image"], state=DISABLED, bg="#808080") \
            .place(x=300, y=150)
        Button(self.working_frame, image=self.products["ham"]["image"], state=DISABLED, bg="#808080") \
            .place(x=450, y=150)

        # Menu
        self.menu_frame = Frame(self.root, bd=2, relief=GROOVE, width=278)
        self.menu_frame.grid(row=0, column=3, rowspan=2, sticky=N + S)

        Label(self.menu_frame, text=f"Encargado:  {self.name.upper()}", font=("Calibri", 14), wraplength=200).place(x=30, y=50)

        self.data_frame = Frame(self.menu_frame, bg="white", relief=RIDGE, bd=3)
        self.data_frame.place(x=30, y=100)

        scrollbar_products = Scrollbar(self.data_frame)
        scrollbar_products.pack(side=RIGHT, fill=Y)

        # List Products Selected
        self.list_items = Listbox(self.data_frame, yscrollcommand=scrollbar_products.set, width=30, height=30)
        self.list_items.pack(side=LEFT, fill=BOTH)


        scrollbar_products.config(command=self.list_items.yview)

        # SubTotal Label
        Label(self.menu_frame, text=f"Sub-Total: ", font=("Calibri", 12, "bold")) \
            .place(x=30, y=600)
        # IVA Label
        Label(self.menu_frame, text=f"I.V.A: ", font=("Calibri", 11, "bold")) \
            .place(x=30, y=630)
        # Total Label
        Label(self.menu_frame, text=f"Total a Pagar: ".upper(), fg="red", font=("Calibri", 14, "bold")) \
            .place(x=30, y=660)

        self.total_purchase = Label(self.menu_frame, text=f"2225,00 $", font=("Calibri",  14, "bold"), fg="green")
        self.total_purchase.place(x=170, y=660)

        Button(self.menu_frame, text="Log Out", width=10, height=2, command=self.logout) \
            .place(x=175, y=725)

        Button(self.menu_frame, text="Imprimir", command=self.print_purchase,
               width=15, height=2, bg="#bbbcbd", activebackground="#8c9196") \
            .place(x=25, y=725)

        # Terminal
        self.terminal_bg = Frame(self.root, bd=2, bg="#b7b7b7")
        self.terminal_bg.grid(row=1, column=0, columnspan=3)

        self.terminal_frame = Frame(self.terminal_bg, bd=6, relief=GROOVE, bg="white", width=970, height=170)
        self.terminal_frame.pack(padx=9, pady=10)

        scrollbar_terminal = Scrollbar(self.terminal_frame)
        scrollbar_terminal.pack(side=RIGHT, fill=Y)
        self.terminal_data = Listbox(self.terminal_frame, yscrollcommand=scrollbar_terminal.set, height=10, width=158,
                                     bg="black", fg="white", selectbackground="#3c3c3c")
        self.terminal_data.insert(END, "Bienvenido a Carniceria Margarita C.A - Fred, Cindy & Dayana 🎃")
        self.terminal_data.insert(END, f"{self.name.upper()}: ..")

        self.terminal_data.pack(side=LEFT, fill=BOTH)
        scrollbar_terminal.config(command=self.terminal_data.yview)

    def logout(self):
        self.login_win.deiconify()
        self.root.destroy()

    def print_purchase(self):
        center_window(self.receipt().root, 350, 500)

    def selected_product(self, prod_name):
        self.terminal_data.insert(END, f"{self.name.upper()} ~ Selected {self.products[prod_name]['name']}")
