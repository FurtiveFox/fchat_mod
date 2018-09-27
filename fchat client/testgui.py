import tkinter as tk
from tkinter import ttk
from tksupport import LabelInput as LI


class loginwindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Login")
        # self.geometry("300x200")
        self.resizable(width=False, height=False)
        loginframe = login_frame(self)
        loginframe.grid(padx=50, pady=50)


class login_frame(tk.Frame):
    """login frame"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.inputs = {}
        inputframe = tk.LabelFrame(self, text="Account Information")
        self.inputs['Username'] = LI(inputframe, "Username: ", input_class=ttk.Entry, input_var=tk.StringVar())
        self.inputs['Username'].grid(row=0, column=0, padx=15, pady=10)

        self.inputs['Password'] = LI(inputframe, "Password: ", input_class=ttk.Entry, input_var=tk.StringVar(), input_args={'show': '*'})
        self.inputs['Password'].grid(row=1, column=0, padx=15)
        inputframe.grid(columnspan=2)

        self.saveloginbox = ttk.Checkbutton(self, text="Save Info")
        self.saveloginbox.grid(row=2, column=0)

        self.loginbutton = ttk.Button(self, text="Login", command=self.on_login)
        self.loginbutton.grid(row=2, column=1, pady=25)

    def on_login(self):
        quit()


if __name__ == '__main__':
    main = loginwindow()
    main.mainloop()
