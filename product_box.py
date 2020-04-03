from tkinter import *
from PIL import ImageTk, Image
from functions import center_window


def show_product(prev_win, prod_dict):
    global window
    try:
        if window.root.state() == "normal": window.root.focus()
    except:
        window = Product(prev_win, prod_dict)
        center_window(window.root, 400, 300)


class Product:
    def __init__(self, previous_window, product_dictionary):
        self.root = Toplevel(bg="white")
        self.root.title("Product Box - Carniceria Margarita")
        self.root.iconbitmap("./images/favicon.ico")
        self.root.resizable(False, False)
        self.root.focus()

        self.main_window = previous_window
        # Selected Product
        self.product = product_dictionary

        # Title
        Label(self.root, image=self.product["image"], bg="white").place(x=0, y=10)
        self.title = Label(self.root, text=f"{self.product['name']}", wraplength=200,
                           font=("Sans-serif", 24), bg="white")
        self.title.place(x=150, y=40)

        # Quantity
        Label(self.root, text="Cantidad:", font=("Sans-serif", 16), bg="white").place(x=60, y=160)

        vcmd = (self.root.register(self.validate_float),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.quantity = Entry(self.root, validate='key', validatecommand=vcmd, bd=3, relief=GROOVE)
        self.quantity.place(x=170, y=165)
        Label(self.root, text="Gramos", font=("Sans-serif", 14), bg="white").place(x=300, y=160)

        # Continue/Cancel Button
        Button(self.root, text="Cancel", width=15, height=2, command=self.root.destroy) \
            .place(x=75, y=225)

        Button(self.root, text="Aceptar", width=15, height=2, bg="#bbbcbd", activebackground="#8c9196",
               command=lambda: self.set_product_price(self.product["price"], int(self.quantity.get()))) \
            .place(x=225, y=225)

    # Set Price
    def set_product_price(self, product_price, product_quantity):
        product_subprice = product_price * (product_quantity / 1000)
        product_subprice = float("{:.2f}".format(round(product_subprice, 2)))
        self.main_window.list_items.insert(END, f"{self.product['name']}")
        self.main_window.list_items.insert(END, f"{product_price}$ x {product_quantity} gramos.")
        self.main_window.list_items.insert(END,  f"{product_subprice} $")
        self.main_window.set_subtotal(product_subprice)

    # Validate the Entry is INT
    def validate_float(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        # action=1 -> insert
        if action == '1':
            if text in '0123456789.-+':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True
