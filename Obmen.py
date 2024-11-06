from tkinter.ttk import Combobox

import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def exchange():
    code = combobox.get()

    if code:
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate: .3f} {code} за 1 USD")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Введите код валюты")


window = Tk()
window.title("Курс обмена валют")
window.geometry("360x180")

Label(text="Выберите код валюты").pack(padx=10, pady=10)
cur = ["RUB", "EUR", "TRY", "THB", "UAH", "CNY", "KZT", "UZS", "CHF", "CAD"]
combobox = ttk.Combobox(values=cur)
combobox.pack(padx=10, pady=10)

# entry = Entry()
# entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к USD", command=exchange).pack(padx=10, pady=10)

window.mainloop()
