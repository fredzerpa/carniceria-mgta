from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from functions import center_window


def show_delete_box(prev_class):
    global window
    try:
        if window.root.state() == "normal": window.root.focus()
    except:
        prev_class.terminal_data.insert(END, f"{prev_class.name.upper()} ~ Opening Deleting Product Box")
        if prev_class.list_items.size() > 0:
            prev_class.terminal_data.see(END)
            response = simpledialog.askstring("ADMIN Permission", "Por favor introduzca una clave ADMIN para continuar.",
                                              show="*")
            if response is not None:
                is_admin = False
                with open("./records/accounts.txt") as file:
                    for account in file:
                        data_list = account.split("||")
                        username = data_list[0].strip()
                        password = data_list[1].strip()
                        job = data_list[2].strip()
                        if response == password:
                            is_admin = True
                            break
                if is_admin:
                    window = DeleteBox(prev_class)
                    prev_class.terminal_data.insert(END, f"[{username.upper()} Permission Granted]")
                    prev_class.terminal_data.see(END)
                    center_window(window.root, 300, 500)
                else:
                    messagebox.showerror("Error no access", "Lo siento pero la clave no coincide con la de un ADMIN")
                    prev_class.terminal_data.insert(END, "[Access Denied]: Password is not from ADMIN")
                    prev_class.terminal_data.see(END)
            else:
                prev_class.terminal_data.insert(END, "[Access Denied]: No password received")
                prev_class.terminal_data.see(END)
        else:
            prev_class.terminal_data.insert(END, "[Access Denied]: No product selected")
            prev_class.terminal_data.see(END)


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
        self.listbox_products = Listbox(self.data_frame, yscrollcommand=scrollbar_products.set, width=27, height=18,
                                        cursor="hand2", selectbackground="#ccc", selectforeground="black",
                                        font=("Sans-serif", 12))
        for index in range(len(self.list_purchase_names)):
            self.listbox_products.insert(END, f"{index + 1}. {self.list_purchase_names[index]}")
        self.listbox_products.pack(side=LEFT, fill=BOTH)
        self.listbox_products.bind("<Double-Button-1>", self.deleting_product_on_list)

        # Inserting Scrollbar with Listbox
        scrollbar_products.config(command=self.listbox_products.yview)

        # Instructions
        Label(self.root, text="Instrucciones:", font=("Sans-serif", 12), bg="white")\
            .place(x=15, y=410)
        Label(self.root, text="1. Hacer doble click sobre el nombre.",
              font=("Sans-serif", 10), bg="white", wraplength=250)\
            .place(x=15, y=435)
        Label(self.root, text="2. Cerrar esta ventana al finalizar.", font=("Sans-serif", 10), bg="white")\
            .place(x=15, y=455)

    # Validate the Entry is INT
    def validate_int(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False

    def close(self):
        self.main_class.terminal_data.insert(END, f"{self.main_class.name.upper()} ~ Closing Deleting Product Box")
        self.main_class.terminal_data.see(END)
        self.root.destroy()

    def deleting_product_on_list(self, event):
        selected_product_index = self.listbox_products.curselection()[0]
        item_line_on_bill = (selected_product_index * 4) + 1
        response = messagebox.askyesno("Confirm Action", f"Desea eleminar "
                                                         f"{self.list_purchase_names[selected_product_index]}?")
        if response:
            item_subtotal = float(self.main_class.list_items.get((item_line_on_bill - 1) + 2).replace(" $", ""))
            self.main_class.set_subtotal(item_subtotal, "subtract")

            self.main_class.set_total(self.main_class.subtotal_value, 12)
            self.main_class.list_items.delete(item_line_on_bill - 1, (item_line_on_bill - 1) + 3)
            self.close()

            self.main_class.terminal_data.insert(END, f"{self.main_class.name.upper()} ~ Deleted "
                                                      f"{self.list_purchase_names[selected_product_index]} => "
                                                      f"- {item_subtotal}$, "
                                                      f"on line {item_line_on_bill}")
            self.main_class.terminal_data.see(END)

