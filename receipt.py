from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

from functions import center_window


def show_receipt(prev_class):
    global window
    try:
        if window.root.state() == "normal": window.root.focus()
    except:
        prev_class.terminal_data.insert(END, "Printing Receipt..")
        prev_class.terminal_data.see(END)
        window = Receipt(prev_class)
        center_window(window.root, 500, 700)
        prev_class.root.withdraw()

class Receipt:
    def __init__(self, previous_class):
        self.root = Toplevel(bg="white")
        self.root.title("Receipt - Carniceria Margarita")
        self.root.iconbitmap("./images/favicon.ico")
        self.root.resizable(False, False)
        self.root.focus()

        self.main_class = previous_class

        self.receipt = self.main_class.list_items.get(0, END)

        # Images
        self.logo_32 = ImageTk.PhotoImage(Image.open("./images/logo_75.png"))

        # Title
        Label(self.root, image=self.logo_32, bg="white").place(x=20, y=20)
        self.title = Label(self.root, text="Carniceria Margarita", font=("Sans-serif", 28), bg="white")
        self.title.place(x=125, y=35)

        self.data_frame = Frame(self.root, bg="white", relief=RIDGE, bd=3, height=100, width=200)
        self.data_frame.place(x=10, y=125)

        # Scrollbar
        scrollbar_products = Scrollbar(self.data_frame)
        scrollbar_products.pack(side=RIGHT, fill=Y)

        # List Products Selected
        self.listbox_products = Listbox(self.data_frame, yscrollcommand=scrollbar_products.set, width=50, height=25,
                                        selectbackground="white", selectforeground="black", activestyle=NONE,
                                        font=("Sans-serif", 12))
        for index in range(0, len(self.receipt), 4):
            data = f"{self.receipt[index]}          {self.receipt[index + 1]}          {self.receipt[index + 2]}"
            self.listbox_products.insert(END, f"{data}")
        self.listbox_products.pack(side=LEFT, fill=BOTH)
        # Inserting Scrollbar with Listbox
        scrollbar_products.config(command=self.listbox_products.yview)

        # Buttons
        Button(self.root, text="Cancel", width=15, height=2, command=self.cancel) \
            .place(x=125, y=625)

        Button(self.root, text="Imprimir",
               width=15, height=2, bg="#bbbcbd", activebackground="#8c9196", command=self.print_bill) \
            .place(x=275, y=625)

    def cancel(self):
        self.main_class.terminal_data.insert(END, "Bill Canceled")
        self.main_class.terminal_data.see(END)
        self.main_class.root.deiconify()
        self.root.destroy()

    def print_bill(self):
        with open("./records/receipts.txt", "a") as file:
            file.write("===== RECIBO ====\n")
            for index in range(0, len(self.receipt), 4):
                file.write(f"{self.receipt[index]} || {self.receipt[index + 1]} || {self.receipt[index + 2]}\n")
            file.write("\n")
        self.main_class.list_items.delete(0, END)
        messagebox.showinfo("Bill Printed", "Se guardado la factua en records/receipts.txt")
        self.main_class.terminal_data.insert(END, "Bill Printed: Data Saved on the file records/receipts.txt")
        self.main_class.terminal_data.see(END)
        self.main_class.root.deiconify()
        self.root.destroy()