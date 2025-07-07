import tkinter as tk
from database import user_database
import sqlite3

class cancel_button(tk.Button):

    def __init__(self, frameRef: tk.Frame):
        super().__init__(frameRef, text="Cancel", font=["Century Gothic", 11], command=self.close_window)

    def close_window(self):
        self.winfo_toplevel().destroy()


class login_page_frame(tk.Frame):

    usernameEntry: tk.Entry
    password_entry: tk.Entry

    def __init__(self, window_ref: tk.Tk, oldFrame:tk.Frame = None):
        if oldFrame is not None:
            oldFrame.destroy()
        super().__init__(window_ref)
        self.setup_layout()
        self.pack(fill="both", expand=True)

    def setup_layout(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        tk.Label(self, text="Login", font=["Century Gothic", 11]).grid(row=0, column=0, columnspan=3)
        tk.Label(self, text="Username:", font=["Century Gothic", 11]).grid(row=1, column=0)
        tk.Label(self, text="Password:", font=["Century Gothic", 11]).grid(row=2, column=0)

        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=1, columnspan=2)

        self.password_entry = tk.Entry(self)
        self.password_entry.grid(row=2, column=1, columnspan=2)

        cancel_button(self).grid(row=3, column=0)
        login_button = tk.Button(self, text="Login", font=["Century Gothic", 11], command=lambda: self.SubmitButtonClick())
        login_button.grid(row=3, column=1)
        register_button = tk.Button(self, text="Register", font=["Century Gothic", 11], command=lambda: self.SubmitButtonClick(True))
        register_button.grid(row=3, column=2)

    def SubmitButtonClick(self,register=False):
        if register:
            print(".")
            register_page_frame(self.master,self)
        username: str = self.username_entry.get()
        password: str = self.password_entry.get()

        print(username)
        print(password)
        db = user_database("./user_database.db")
        user_exists = db.check_account(username, password)
        if user_exists:
            print("working")
        else:
            label = tk.Label(self, text="Incorrect Username or Password", font=["Century Gothic", 11])
            label.grid(row=3, column=1, columnspan=3)
            self.after(1000, label.destroy)
        # valid = true

class register_page_frame(tk.Frame):

    usernameEntry: tk.Entry
    password_entry: tk.Entry

    def __init__(self, window_ref: tk.Tk, oldFrame:tk.Frame = None):
        if oldFrame is not None:
            oldFrame.destroy()
        super().__init__(window_ref)
        self.setup_layout()
        self.pack(fill="both", expand=True)

    def setup_layout(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        tk.Label(self, text="Register", font=["Century Gothic", 11]).grid(row=0, column=0, columnspan=3)
        tk.Label(self, text="Username:", font=["Century Gothic", 11]).grid(row=1, column=0)
        tk.Label(self, text="Password:", font=["Century Gothic", 11]).grid(row=2, column=0)

        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=1, columnspan=2)

        self.password_entry = tk.Entry(self)
        self.password_entry.grid(row=2, column=1, columnspan=2)

        cancel_button(self).grid(row=3, column=0)
        tk.Button(self, text="Login", font=["Century Gothic", 11], command=lambda: self.SubmitButtonClick()).grid(row=3, column=1)
        tk.Button(self, text="Sign Up", font=["Century Gothic", 11], command=lambda: self.SubmitButtonClick(True)).grid(row=3, column=2)

    def SubmitButtonClick(self,register=False):
        if register:
            username: str = self.username_entry.get()
            password: str = self.password_entry.get()
            db = user_database("./user_database.db")
            db.add_user(username,password)
            login_page_frame(self.master, self)
        login_page_frame(self.master, self)


class main_page(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("400x220")
        self.configure(bg="#ff8803")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        login_page_frame(self)

        self.mainloop()

x: main_page = main_page()