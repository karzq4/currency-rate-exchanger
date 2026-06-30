import tkinter as tk
import http.client
from main import Window
import json
from tkinter import messagebox


class FetchCurrency(Window):
    def __init__(self):
        super().__init__()
        self.button = tk.Button(self.root, command=self.fetch, text="get", width=5)
        self.button.pack(pady=20)

        self.updateCurrencies()
        
    def fetch(self, event=None):
        self.selectedbase = self.selected1.get()  
        self.selectedto = self.selected2.get()
        self.amount = self.input.get()
        conn = http.client.HTTPSConnection("api.collectapi.com")
        headers = {
            'content-type' : "application/json",
            'authorization' : "apikey 4MBDHpG1Muzb8dBE6ZyJqQ:4KNZZcTQl1CeiCUMf0GVGY"
        }
        conn.request("GET", f"/economy/exchange?int={self.amount}&to={self.selectedto}&base={self.selectedbase}", headers=headers)

        res = conn.getresponse()
        data = res.read()
        self.dataDecoded = data.decode("utf-8")
        self.jsonResult = json.loads(self.dataDecoded)

        if self.jsonResult.get('success') == False or self.selectedbase == "" or self.selectedto == "":
            return messagebox.showerror(title='error', message='error')
        else:
            self.result = json.loads(self.dataDecoded)['result'][0]['data'][0]['rate']
            self.resultBase = json.loads(self.dataDecoded)['result'][0]['base']
            self.time = json.loads(self.dataDecoded)['result'][0]['lastupdate']
            if self.amount == "":
                #print(self.dataDecoded)
                return messagebox.showinfo(title="Exchange Rate", message=f"Last updated {self.time} \n 1 {self.selectedbase} is equal to {self.result}")
            else:
                return messagebox.showinfo(title="Exchange Rate", message=f"{self.amount} {self.selectedbase} is equal to {(self.result)}")



        




    def updateCurrencies(self, event=None):
        # base currency
        self.currency1 = [
    "USD", "EUR", "TRY", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "SEK", 
    "NZD", "KRW", "SGD", "NOK", "MXN", "INR", "RUB", "ZAR", "HKD", "BRL", 
    "AED", "SAR", "KWD", "QAR", "BHD", "PLN", "THB", "DKK", "HUF", "ILS", 
    "PHP", "MYR"
]         
        self.selected1['values'] = self.currency1
        # currency you want to exchange to

        self.currency2 = [
    "USD", "EUR", "TRY", "GBP", "JPY", "CAD", "AUD", "CHF", "CNY", "SEK", 
    "NZD", "KRW", "SGD", "NOK", "MXN", "INR", "RUB", "ZAR", "HKD", "BRL", 
    "AED", "SAR", "KWD", "QAR", "BHD", "PLN", "THB", "DKK", "HUF", "ILS", 
    "PHP", "MYR"
]
        self.selected2['values'] = self.currency2






