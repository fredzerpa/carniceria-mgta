from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image
from functions import center_window


def show_product(prev_class, prod_dict):
    global window
    try:
        if window.root.state() == "normal": window.root.focus()
    except:
        prev_class.terminal_data.insert(END, f"{prev_class.name.upper()} ~ Selected {prod_dict['name']}")
        window = Product(prev_class, prod_dict)
        center_window(window.root, 400, 300)


class Product:
    def __init__(self, previous_class, product_dictionary):
        self.root = Toplevel(bg="white")
        self.root.title("Product Box - Carniceria Margarita")
        self.root.iconbitmap("./images/favicon.ico")
        self.root.resizable(False, False)
        self.root.focus()

        self.main_class = previous_class
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
        Button(self.root, text="Cancel", width=15, height=2, command=self.cancel_product_box) \
            .place(x=75, y=225)

        Button(self.root, text="Aceptar", width=15, height=2, bg="#bbbcbd", activebackground="#8c9196",
               command=lambda: self.set_product_price(self.product["price"], self.quantity.get())) \
            .place(x=225, y=225)

    # Cancel Box
    def cancel_product_box(self):
        self.main_class.terminal_data.insert(END, f"{self.main_class.name.upper()} ~ "
                                                  f"Cancelled {self.product['name']}")
        self.main_class.terminal_data.see(END)
        self.root.destroy()

    # Still on Stock
    def is_still_on_stock(self, quantity_req):
        if self.product["stock"] > quantity_req:
            return True
        else:
            return False

    # Set Price
    def set_product_price(self, product_price, product_quantity):
        try:
            if self.is_still_on_stock(0):  # Still on stock
                product_kg = float(product_quantity) / 1000

                if self.is_still_on_stock(product_kg):  # Quantity required doesn't exceed the stock
                    for key in self.main_class.products:
                        if self.main_class.products[key] == self.product:
                            self.main_class.products[key]['stock'] = float(
                                self.main_class.products[key]['stock'] - product_kg
                            )
                            self.main_class.products[key]['stock'] = float(
                                "{:.2f}".format(round(self.main_class.products[key]['stock'], 2)))

                    product_subprice = product_price * product_kg
                    product_subprice = float("{:.2f}".format(round(product_subprice, 2)))
                    self.main_class.list_items.insert(END, f"{self.product['name']}")
                    self.main_class.list_items.insert(END, f"{product_price}$ x {product_kg} Kg")
                    self.main_class.list_items.insert(END, f"{product_subprice} $")
                    self.main_class.list_items.insert(END, "")
                    self.main_class.set_subtotal(product_subprice)
                    self.main_class.set_total(self.main_class.subtotal_value, 12)
                    self.main_class.terminal_data.insert(END, f"{self.main_class.name.upper()} ~ "
                                                              f"Selected {self.product['name']} => "
                                                              f"{product_price}$ x {product_kg}Kg = "
                                                              f"{product_subprice}$, on line "
                                                              f"{self.main_class.list_items.size() - 3}")
                    self.root.destroy()
                else:
                    messagebox.showwarning("Not enough in stock", f"No hay suficiente {self.product['name']} en el "
                                                                  f"inventario. \nQueda {self.product['stock']} Kg.")
                    self.root.focus()
                    self.main_class.terminal_data.insert(END, f"{self.main_class.name.upper()} ~ "
                                                              f"{self.product['name']} not enough in stock. "
                                                              f"Input {product_kg}Kg - "
                                                              f"Left {self.product['stock']} Kg.")
            else:  # Out of Stock
                messagebox.showwarning("Not in stock", f"{self.product['name']} Agotado.")
                self.main_class.terminal_data.insert(END, f"{self.main_class.name.upper()} ~ "
                                                          f"{self.product['name']} out of stock")
                self.root.destroy()
        except ValueError:
            self.main_class.terminal_data.insert(END, f"{self.main_class.name.upper()} ~ "
                                                      f"{self.product['name']}: No input")
            self.root.destroy()
        self.main_class.terminal_data.see(END)

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
