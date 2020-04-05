from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from register_user import show_register
from main import show_main
from functions import center_window


class LoginSystem:
    def __init__(self, win):
        self.root = win
        self.root.title("Login Form - Carniceria Margarita")
        self.root.iconbitmap("./images/favicon.ico")
        self.root.resizable(False, False)

        # Images
        self.logo = ImageTk.PhotoImage(Image.open("./images/logo.png"))
        self.user_logo = ImageTk.PhotoImage(Image.open("./images/user.png"))
        self.password_logo = ImageTk.PhotoImage(Image.open("./images/lock-icon.png"))

        # Login Logo
        Label(self.root, image=self.logo).grid(row=0, column=0, columnspan=2)

        # Login Frame
        login_frame = Frame(self.root, height=400, width=200)
        login_frame.grid(row=0, column=2, sticky=N + S)

        # Username Widgets
        Label(login_frame, image=self.user_logo).place(x=50, y=110)
        Label(login_frame, text="Usuario", font=("Sans-serif", 12)).place(x=75, y=110)
        self.username = Entry(login_frame, width=30)
        self.username.place(x=7, y=140)

        # Password Widgets
        Label(login_frame, image=self.password_logo).place(x=60, y=170)
        Label(login_frame, text="Clave", font=("Sans-serif", 12)).place(x=80, y=171)
        self.password = Entry(login_frame, width=30, show="*")
        self.password.place(x=7, y=200)

        # Register Button
        Button(login_frame, text="Register", width=10, command=show_register
               ).place(x=10, y=235)
        # Log In Button
        Button(login_frame, text="Log In", width=10, bg="#bbbcbd", activebackground="#8c9196",
               command=self.login
               ).place(x=105, y=235)

        # Forgot Username
        Label(login_frame, text="¿Olvidó la contraseña?").place(x=7, y=265)
        Button(login_frame, text="Click aqui", bd=0, fg="Blue", activeforeground="Purple", command=self.forgot_user)\
            .place(x=130, y=265)

    def login(self):
        user_exists = False
        with open("./records/accounts.txt") as file:
            for account in file:
                data_list = account.split("||")
                username = data_list[0].strip()
                password = data_list[1].strip()
                job = data_list[2].strip()

                if self.username.get() == username and self.password.get() == password:
                    user_exists = True
                    break
        if user_exists:
            self.password.delete(0, END)
            self.root.withdraw()
            show_main(username, job, self.root)
        else:
            res = messagebox.showerror("Wrong User/Password", "Usuario y/o Clave Erronea.")
            if res: self.root.focus()

    def forgot_user(self):
        messagebox.showinfo("User Forgot", "Busque en el path ./records/accounts.txt")


root = Tk()
login_window = LoginSystem(root)
center_window(login_window.root, 824, 404)

root.mainloop()
