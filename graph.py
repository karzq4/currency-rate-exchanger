import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from database import DataBase
import tkinter as tk
from tkinter import messagebox
import sqlite3
import os


class Graph(DataBase):
    def __init__(self):
        super().__init__()
        self.history_button = tk.Button(self.root, text="Show History", command=self.graph)
        self.history_button.pack(pady=20)

        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.DB_PATH = os.path.join(self.BASE_DIR, "currencydata.db")


    def graph(self):
        self.conn = sqlite3.connect(self.DB_PATH)
        self.cursor = self.conn.cursor()
        self.exchange_rates = self.jsonResult['result'][0]
        self.base_currency = self.exchange_rates.get("base")
        self.target_currency = self.exchange_rates["data"][0]["rate"]
        targetcode = self.target_currency.split()[-1]

        self.cursor.execute(
            """
            SELECT date, currencyBase, currencyTo
            FROM rates
            WHERE currencyBase LIKE ? AND currencyTo LIKE ?
            ORDER BY id ASC
            """,
            (f"%{self.base_currency}%", f"%{targetcode}%")
        )
        self.fetch_all = self.cursor.fetchall()
        self.conn.close()   

        if not self.fetch_all:
            messagebox.showerror(title="error", message="Could not find any historical data.")
        
        else:
            dates = []
            rates = []

            for i in self.fetch_all:
                date = i[0]
                rate = i[2]

                rate_split = float(rate.split()[0])

                dates.append(date)
                rates.append(rate_split)


            plt.figure(figsize=(8, 5))
            plt.plot(dates, rates)      
            plt.xlabel("Date and Time")
            plt.ylabel("Value")
            plt.show()
