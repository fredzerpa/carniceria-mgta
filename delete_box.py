from tkinter import *
from tkinter import messagebox
from functions import center_window


def show_delete_box(prev_class):
    global window
    try:
        if window.root.state() == "normal": window.root.focus()
    except:
        window = DeleteBox(prev_class)
        prev_class.terminal_data.insert(END, f"{prev_class.name.upper()} ~ Opening Deleting Product Box")
        center_window(window.root, 300, 500)


class DeleteBox:
    def __init__(self, previous_class):
        self.root = Toplevel(bg="white")
        self.root.title("Delete Product")
        self.root.iconbitmap("./images/favicon.ico")
        self.root.resizable(False, False)
        self.root.focus()

        # Main Window Class
        self.main_class = previous_class

        # Title
        self.title = Label(self.root, text=f"Borrar Producto", font=("Sans-serif", 18), bg="white")
        self.title.place(x=65, y=15)

        self.list_purchase = self.main_class.list_items.get(0, END)
        self.list_purchase_names = self.list_purchase[::4]
        self.data_frame = Frame(self.root, bg="white", relief=RIDGE, bd=3)
        self.data_frame.place(x=15, y=50)

        # Scrollbar
        scrollbar_products = Scrollbar(self.data_frame)
        scrollbar_products.pack(side=RIGHT, fill=Y)

        # List Products Selected
        self.listbox_products = Listbox(self.data_frame, yscrollcommand=scrollbar_products.set, width=26, height=15,
                                        cursor="hand2", selectbackground="#ccc", selectforeground="black",
                                        font=("Sans-serif", 12))
        for product in self.list_purchase_names:
            self.listbox_products.insert(END, f"{self.list_purchase_names.index(product) + 1}. {product}")
        self.listbox_products.pack(side=LEFT, fill=BOTH)
        self.listbox_products.bind("<Double-Button-1>", self.deleting_product_on_list)

        # Inserting Scrollbar with Listbox
        scrollbar_products.config(command=self.listbox_products.yview)



    # Validate the Entry is INT
    def validate_int(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def close(self):
        self.main_class.terminal_data.insert(END, f"{self.main_class.name.upper()} ~ Closing Deleting Product Box")
        self.root.destroy()

    def deleting_product_on_list(self, event):
        response = messagebox.askyesno("Confirm Action", f"Desea eleminar {self.list_purchase_names[self.listbox_products.curselection()[0]]}")
        if response:
            self.main_class.terminal_data.insert(END, f"{self.main_class.name.upper()} ~ Deleted Product")
            self.root.destroy()

    def select_product_listbox(self, index):
        self.listbox_products.activate(index)