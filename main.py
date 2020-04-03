from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from functions import center_window
from receipt import Receipt, show_receipt
from product_box import Product, show_product
from delete_box import show_delete_box


def show_main(name, job, prev_win):
    global window
    try:
        if window.root.state() == "normal": window.root.focus()
    except:
        window = MainSystem(name, job, prev_win)
        center_window(window.root, 1280, 800)


class MainSystem:
    def __init__(self, name, job, prev_win):
        self.root = Toplevel()
        self.root.title(f"Bienvenido {name.capitalize()}, Carniceria Margarita")
        self.root.iconbitmap("./images/favicon.ico")
        self.root.resizable(False, False)
        self.root.focus()

        self.login_win = prev_win

        self.receipt = Receipt

        self.product_box = Product

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
                "stock": 100
            },
            "groundBeef": {
                "name": "Carne Molida",
                "price": 2.5,
                "image": PhotoImage(file=r"./images/products/carne-molida.png").subsample(4, 4),
                "stock": 100
            },
            "chicken": {
                "name": "Muslo de Pollo",
                "price": 1.5,
                "image": PhotoImage(file=r"./images/products/muslo.png").subsample(4, 4),
                "stock": 100
            },
            "steak": {
                "name": "Bistec",
                "price": 3.5,
                "image": PhotoImage(file=r"./images/products/bistec.png").subsample(4, 4),
                "stock": 100
            },
            "chorizo": {
                "name": "Chorizo",
                "price": 10,
                "image": PhotoImage(file=r"./images/products/chorizo.png").subsample(4, 4),
                "stock": 100
            },
            "bacon": {
                "name": "Tocineta",
                "price": 5,
                "image": PhotoImage(file=r"./images/products/tocineta.png").subsample(4, 4),
                "stock": 100
            },
            "meatRoast": {
                "name": "Carne para Mechar",
                "price": 2,
                "image": PhotoImage(file=r"./images/products/mechada.png").subsample(4, 4),
                "stock": 100
            },
            "porkLeg": {
                "name": "Pernil",
                "price": 3.5,
                "image": PhotoImage(file=r"./images/products/pernil.png").subsample(4, 4),
                "stock": 100
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

        Button(self.working_frame, image=self.products["ribs"]["image"], activebackground="#ccc",
               command=lambda: self.select_product(self.products["ribs"])) \
            .place(x=0, y=0)
        Button(self.working_frame, image=self.products["groundBeef"]["image"], activebackground="#ccc",
               command=lambda: self.select_product(self.products["groundBeef"])) \
            .place(x=150, y=0)
        Button(self.working_frame, image=self.products["chicken"]["image"], activebackground="#ccc",
               command=lambda: self.select_product(self.products["chicken"])) \
            .place(x=300, y=0)
        Button(self.working_frame, image=self.products["steak"]["image"], activebackground="#ccc",
               command=lambda: self.select_product(self.products["steak"])) \
            .place(x=450, y=0)
        Button(self.working_frame, image=self.products["chorizo"]["image"], activebackground="#ccc",
               command=lambda: self.select_product(self.products["chorizo"])) \
            .place(x=600, y=0)
        Button(self.working_frame, image=self.products["bacon"]["image"], activebackground="#ccc",
               command=lambda: self.select_product(self.products["bacon"])) \
            .place(x=750, y=0)
        Button(self.working_frame, image=self.products["meatRoast"]["image"], activebackground="#ccc",
               command=lambda: self.select_product(self.products["meatRoast"])) \
            .place(x=0, y=150)
        Button(self.working_frame, image=self.products["porkLeg"]["image"], activebackground="#ccc",
               command=lambda: self.select_product(self.products["porkLeg"])) \
            .place(x=150, y=150)
        Button(self.working_frame, image=self.products["cheese"]["image"], state=DISABLED, bg="#808080") \
            .place(x=300, y=150)
        Button(self.working_frame, image=self.products["ham"]["image"], state=DISABLED, bg="#808080") \
            .place(x=450, y=150)

        # Menu
        self.menu_frame = Frame(self.root, bd=2, relief=GROOVE, width=278)
        self.menu_frame.grid(row=0, column=3, rowspan=2, sticky=N + S)

        Label(self.menu_frame, text=f"Encargado:  {self.name.upper()}", font=("Calibri", 14), wraplength=200).place(
            x=30, y=30)

        Button(self.menu_frame, text=f"Borrar producto", font=("Calibri", 10), fg="blue", bd=0,
               activeforeground="purple", command=lambda: show_delete_box(self)) \
            .place(x=120, y=80)

        self.data_frame = Frame(self.menu_frame, bg="white", relief=RIDGE, bd=3)
        self.data_frame.place(x=30, y=100)

        # Scrollbar
        scrollbar_products = Scrollbar(self.data_frame)
        scrollbar_products.pack(side=RIGHT, fill=Y)

        # List Products Selected
        self.list_items = Listbox(self.data_frame, yscrollcommand=scrollbar_products.set, width=23, height=27,
                                  selectbackground="white", selectforeground="black",
                                  activestyle=NONE, font=("Sans-serif", 11))
        self.list_items.pack(side=LEFT, fill=BOTH)

        # Inserting Scrollbar with Listbox
        scrollbar_products.config(command=self.list_items.yview)

        # SubTotal Label
        Label(self.menu_frame, text=f"Sub-Total: ", font=("Calibri", 12, "bold")) \
            .place(x=30, y=600)
        self.subtotal_value = 0
        self.subtotal_input = Label(self.menu_frame, text=f"0.00 $", font=("Calibri", 12))
        self.subtotal_input.place(x=100, y=600)
        # IVA Label
        Label(self.menu_frame, text=f"I.V.A: ", font=("Calibri", 11, "bold")) \
            .place(x=30, y=630)
        Label(self.menu_frame, text=f"12%", font=("Calibri", 11)) \
            .place(x=70, y=630)
        # Total Label
        self.total_value = 0
        Label(self.menu_frame, text=f"Total a Pagar: ".upper(), fg="red", font=("Calibri", 14, "bold")) \
            .place(x=30, y=660)

        self.total_input = Label(self.menu_frame, text=f"0.00 $", font=("Calibri", 14, "bold"), fg="green")
        self.total_input.place(x=170, y=660)

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
        if self.list_items.size() > 0:
            response = messagebox.askyesno("Pending Bill", "Quedan productos por facturar, desea continuar?")
            if response:
                self.login_win.deiconify()
                self.root.destroy()
        else:
            self.login_win.deiconify()
            self.root.destroy()

    def print_purchase(self):
        show_receipt(self)

    def select_product(self, prod_dict):
        show_product(self, prod_dict)
        self.terminal_data.see(END)

    def set_subtotal(self, amount, operation="add"):
        if operation == "add":
            self.subtotal_value = self.subtotal_value + amount
        elif operation == "subtract":
            self.subtotal_value = self.subtotal_value - amount
        self.subtotal_value = float("{:.2f}".format(round(self.subtotal_value, 2)))
        self.subtotal_input.destroy()
        self.subtotal_input = Label(self.menu_frame, text=f"{self.subtotal_value} $", font=("Calibri", 12))
        self.subtotal_input.place(x=100, y=600)

    def set_total(self, sub_total, IVA_porcentage):
        self.total_value = sub_total + (sub_total * (IVA_porcentage / 100))
        self.total_value = float("{:.2f}".format(round(self.total_value, 2)))
        self.total_input.destroy()
        self.total_input = Label(self.menu_frame, text=f"{self.total_value} $",
                                 font=("Calibri", 14, "bold"), fg="green")
        self.total_input.place(x=170, y=660)
