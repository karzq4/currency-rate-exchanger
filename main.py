import tkinter as tk
from tkinter import ttk


class Window():
    def __init__(self):
        self.root = tk.Tk()
        self.title = self.root.title("Currency Rates")
        self.root.geometry("500x400")
        self.root.resizable(width=False,height=False)
        self.label()
        self.Currencies()
        self.Input()





    def label(self):
        self.label = tk.Label(self.root, text="Currency Rate Calculator", font=('Times New Roman', 20, "bold"))
        self.label.pack(pady = 20)

    def Input(self, event= None):
        self.inputframe = tk.Frame(self.root)
        self.inputframe.pack()
        self.inputtext = tk.Label(self.inputframe, text="Enter amount: ")
        self.inputtext.pack(side="left")
        self.input = tk.Entry(self.inputframe, validate="key", validatecommand=(self.root.register(self.CharLim), '%P'))
        self.input.pack(side="right")


    def Currencies(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.currency1 = []
        self.selected1 = ttk.Combobox(self.frame, width=20, state='readonly')
        self.selected1['values'] = self.currency1
        self.selected1.pack(side='left', pady=25, padx=30)
        arrow = tk.Label(self.frame, text="→", font=('Times New Roman', 25, "bold"))
        arrow.pack(side='left', padx=30)
        self.currency2 = []
        self.selected2 = ttk.Combobox(self.frame, width=20, state='readonly')
        self.selected2.pack(side='left', pady=25, padx=30)



    def CharLim(self, P):
        if P == "":
            return True
        

        is_valid_char = all(char.isdigit() and P[0] != "0" for char in P)
        
        return is_valid_char




