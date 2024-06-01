import tkinter as tk
from tkinter import ttk

# Conversion rates
conversion_rates = {
    'USD to EUR': 0.85,
    'USD to GBP': 0.72,
    'EUR to GBP': 0.85 / 0.72
}

def usd_to_eur(amount):
    return amount * 0.85

def usd_to_gbp(amount):
    return amount * 0.72

def eur_to_gbp(amount):
    return amount / (0.85 / 0.72)

def convert():
    amount = float(amount_entry.get())
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()

    if from_currency == to_currency:
        converted_amount_label.config(text=str(amount))
    else:
        if from_currency == 'USD':
            converted_amount = usd_to_eur(amount) if to_currency == 'EUR' else usd_to_gbp(amount)
        elif from_currency == 'EUR':
            converted_amount = usd_to_gbp(amount) if to_currency == 'GBP' else usd_to_eur(amount)
        else:  # from_currency == 'GBP'
            converted_amount = eur_to_gbp(amount) if to_currency == 'EUR' else usd_to_gbp(amount)

        converted_amount_label.config(text=str(round(converted_amount, 2)))




# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Amount label and entry
amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0, padx=5, pady=5)

amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

# From currency label and combobox
from_currency_label = tk.Label(root, text="From Currency:")
from_currency_label.grid(row=1, column=0, padx=5, pady=5)

from_currency_combobox = ttk.Combobox(root, values=list(conversion_rates.keys()))
from_currency_combobox.grid(row=1, column=1, padx=5, pady=5)
from_currency_combobox.set('USD to EUR')

# To currency label and combobox
to_currency_label = tk.Label(root, text="To Currency:")
to_currency_label.grid(row=2, column=0, padx=5, pady=5)

to_currency_combobox = ttk.Combobox(root, values=list(conversion_rates.keys()))
to_currency_combobox.grid(row=2, column=1, padx=5, pady=5)
to_currency_combobox.set('USD to GBP')

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Converted amount label
converted_amount_label = tk.Label(root, text="")
converted_amount_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Start the tkinter event loop
root.mainloop()
