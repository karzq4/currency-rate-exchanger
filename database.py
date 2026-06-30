import sqlite3
from fetchData import FetchCurrency
import json
from tkinter import messagebox
import tkinter as tk
import os

class DataBase(FetchCurrency):
    def __init__(self):
        super().__init__()
        self.data_button = tk.Button(self.root, command=self.loadData, text="Save", width=5)
        self.data_button.pack()
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.DB_PATH = os.path.join(self.BASE_DIR, "currencydata.db")


    def loadData(self):
        self.conn = sqlite3.connect(self.DB_PATH)
        self.cursor = self.conn.cursor()
        self.exchange_rates = self.jsonResult['result'][0]
        self.base_currency = self.exchange_rates.get("base")
        self.date = self.exchange_rates.get("lastupdate")

        if str(self.amount).strip() != "1":
            self.conn.close()
            return messagebox.showerror(title="error", message="Amount must be 1")

        else:
            self.base_currency = self.exchange_rates.get("base")
            self.target_currency = self.exchange_rates["data"][0]["rate"]
            self.date = self.exchange_rates.get("lastupdate")

            if self.target_currency:
                try:
                    self.cursor.execute(
                        """
                        INSERT INTO rates (currencyBase, currencyTo, date) 
                        VALUES (?, ?, ?)
                        """,
                        (self.base_currency, self.target_currency, self.date)
                    )
                #Duplicate error gosterimi icin ai'dan yardim alindi.
                except sqlite3.IntegrityError:
                    messagebox.showwarning(
                    title="Duplicate Entry", message=f"Data for this exact timestamp ({self.date}) has already been saved.")
            self.conn.commit()
        self.conn.close()

