from tkinter import *
from currency_converter import CurrencyConverter

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

# Currencies to convert
currencies = list(c.currencies)

currencies = list(c.currencies)
excluded_currencies = ["ROL", "CYP", "TRL", "LVL", "MTL"]

for currency in excluded_currencies:
    if currency in currencies:
        currencies.remove(currency)

# Create StringVar variables to store the input and output currency values
currency_input = StringVar(root)
currency_output = StringVar(root)

# Set the title and size of the root window
root.title("Currency Converter")
root.minsize(width=300, height=300)

running = True

# Function to convert the currency
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
        currency_output.set(round(c.convert(amount, fromm.get(), too.get()), 5))

# Function to validate the input in the currency input field
def entry_valid(input):
    """
    Validate the input in the currency input field.

    Parameters:
    input (str): The input value.

    Returns:
    bool: True if the input is valid, False otherwise.
    """
    global currency_val1, currency_val2, currency_input
    if input[-1] == "." or input[-1].isdigit():
        currency_input = input
        if currency_val1.get() != "From" and currency_val2.get() != "To":
            convert_cur(input, currency_val1, currency_val2)
            return True
        else:
            return True
    elif input == "":
        return True
    else:
        return False
    
# Function to update the currency conversion
def callback(*args):
    """
    Callback function to update the currency conversion when the selected currencies change.
    """
    global currency_input, currency_val1, currency_val2
    convert_cur(currency_input, currency_val1, currency_val2)

# Create a label widget for the title
label = Label(root, text='Currency Converter', font="Helvetica 40 bold")
label.pack()

# Create an entry widget for the currency input
amount = Entry(root, textvariable=currency_input, font="Geneva 30 bold", justify=CENTER)
amount.pack(padx=10)

# Register the entry_valid function as a validation command for the amount entry widget
reg = root.register(entry_valid)
amount.config(validate="key", validatecommand=(reg, '%P'))

# Create an option menu widget for the source currency selection
currency_from = OptionMenu(root, currency_val1, *currencies)
currency_from.config(width=38, height=2, font="Helvetica 15 bold", justify=CENTER)
currency_from.pack()

# Create an option menu widget for the target currency selection
currency_to = OptionMenu(root, currency_val2, *currencies)
currency_to.config(width=38, height=2, font="Helvetica 15 bold", justify=CENTER)
currency_to.pack()

# Bind the callback function to the changes in the source and target currency selections
currency_val1.trace('w', callback)
currency_val2.trace('w', callback)

# Create an entry widget for the currency output
output = Entry(root, textvariable=currency_output, font="Geneva 30 bold", justify=CENTER)
output.pack()

# Start the main event loop
root.mainloop()