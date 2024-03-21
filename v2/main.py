from tkinter import *
from currency_converter import CurrencyConverter

from v2.callback import callback
from v2.entry_valid import entry_valid

# Create the root window
root = Tk()
root.title("Currency Converter")

# Create StringVar variables to store the selected currencies
currency_val1 = StringVar(root)
currency_val2 = StringVar(root)
currency_val1.set("From")
currency_val2.set("To")

# Create an instance of the CurrencyConverter class
c = CurrencyConverter()

# Create StringVar variables to store the input and output currency values
currecy_input = StringVar(root)
currecy_output = StringVar(root)

# Set the title and size of the root window
root.title("Currency Converter")
root.minsize(width=300, height=300)

running = True

# Create a label widget for the title
label = Label(root, text='Currency Converter', font="Helvetica 40 bold")
label.pack()

# Create an entry widget for the currency input
amount = Entry(root, textvariable=currecy_input, font="Geneva 30 bold", justify=CENTER)
amount.pack(padx=10)

# Register the entry_valid function as a validation command for the amount entry widget
reg = root.register(entry_valid)
amount.config(validate="key", validatecommand=(reg, '%P'))

# Create an option menu widget for the source currency selection
currency_from = OptionMenu(root, currency_val1, *["EUR", "USD", "GBP", "CAD", "JPY", "CNY", "RUB"])
currency_from.config(width=38, height=2, font="Helvetica 15 bold", justify=CENTER)
currency_from.pack()

# Create an option menu widget for the target currency selection
currency_to = OptionMenu(root, currency_val2, *["EUR", "USD", "GBP", "CAD", "JPY", "CNY", "RUB"])
currency_to.config(width=38, height=2, font="Helvetica 15 bold", justify=CENTER)
currency_to.pack()

# Bind the callback function to the changes in the source and target currency selections
currency_val1.trace('w', callback)
currency_val2.trace('w', callback)

# Create an entry widget for the currency output
output = Entry(root, textvariable=currecy_output, font="Geneva 30 bold", justify=CENTER)
output.pack()

# Start the main event loop
root.mainloop()