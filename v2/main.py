from tkinter import *
from currency_converter import CurrencyConverter

# Create the root window
root = Tk()
root.title("Currency Converter")

# Create StringVar variables to store the selected currencies
currencyval1 = StringVar(root)
currencyval2 = StringVar(root)
currencyval1.set("From")
currencyval2.set("To")

# Create an instance of the CurrencyConverter class
c = CurrencyConverter()

# Create StringVar variables to store the input and output currency values
currecyinput = StringVar(root)
currecyoutput = StringVar(root)

# Set the title and size of the root window
root.title("Currency Converter")
root.minsize(width=300, height=300)

running = True

def convert_cur(amount, fromm, too):
    """
    Convert the currency based on the given amount, source currency, and target currency.

    Parameters:
    amount (float): The amount of currency to convert.
    fromm (str): The source currency.
    too (str): The target currency.
    """
    if amount == None or fromm.get() == "From" or too.get() == "To":
        # TODO: Add implementation
        pass
    else:
        currecyoutput.set(round(c.convert(amount, fromm.get(), too.get()), 5))

def entry_valid(input):
    """
    Validate the input in the currency input field.

    Parameters:
    input (str): The input value.

    Returns:
    bool: True if the input is valid, False otherwise.
    """
    global currencyval1, currencyval2, currecyinput
    if input[-1] == "." or input[-1].isdigit():
        currecyinput = input
        if currencyval1.get() != "From" and currencyval2.get() != "To":
            convert_cur(input, currencyval1, currencyval2)
            return True
        else:
            return True
    elif input == "":
        return True
    else:
        return False

def callback(*args):
    """
    Callback function to update the currency conversion when the selected currencies change.
    """
    global currecyinput, currencyval1, currencyval2
    convert_cur(currecyinput, currencyval1, currencyval2)

# Create a label widget for the title
label = Label(root, text='Currency Converter', font="Helvetica 40 bold")
label.pack()

# Create an entry widget for the currency input
amount = Entry(root, textvariable=currecyinput, font="Geneva 30 bold", justify=CENTER)
amount.pack(padx=10)

# Register the entry_valid function as a validation command for the amount entry widget
reg = root.register(entry_valid)
amount.config(validate="key", validatecommand=(reg, '%P'))

# Create an option menu widget for the source currency selection
currencyfrom = OptionMenu(root, currencyval1, *["EUR", "USD", "GBP", "CAD", "JPY", "CNY", "RUB"])
currencyfrom.config(width=38, height=2, font="Helvetica 15 bold", justify=CENTER)
currencyfrom.pack()

# Create an option menu widget for the target currency selection
currencyto = OptionMenu(root, currencyval2, *["EUR", "USD", "GBP", "CAD", "JPY", "CNY", "RUB"])
currencyto.config(width=38, height=2, font="Helvetica 15 bold", justify=CENTER)
currencyto.pack()

# Bind the callback function to the changes in the source and target currency selections
currencyval1.trace('w', callback)
currencyval2.trace('w', callback)

# Create an entry widget for the currency output
output = Entry(root, textvariable=currecyoutput, font="Geneva 30 bold", justify=CENTER)
output.pack()

# Start the main event loop
root.mainloop()