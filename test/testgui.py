import tkinter as tk
from tkinter import ttk
from tksupport import LabelInput as LI


class loginwindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Login")
        self.resizable(width=True, height=True)
        loginframe = login_frame(self)
        loginframe.grid()


class login_frame(tk.Frame):
    """login frame"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.inputs = {}
        inputframe = tk.LabelFrame(self, text="Account Information")
        self.inputs['Username'] = LI(inputframe, "Username: ", input_var=tk.StringVar())
        self.inputs['Username'].grid(row=0, column=0)

        self.inputs['Password'] = LI(inputframe, "Password: ", input_var=tk.StringVar(), input_args={'show': '*'})
        self.inputs['Password'].grid(row=1, column=0)
        inputframe.grid()


if __name__ == '__main__':
    main = loginwindow()
    main.mainloop()
