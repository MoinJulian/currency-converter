from tkinter import *
from currency_converter import CurrencyConverter
import tkinter.messagebox as messagebox

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
excluded_currencies = ["ROL", "CYP", "TRL", "LVL", "MTL", "HRK"]

for currency in excluded_currencies:
    if currency in currencies:
        currencies.remove(currency)

currencies.sort()

currencies_names = {
    "AUD": "Australian Dollar (AUD)",
    "BGN": "Bulgarian Lev (BGN)",
    "BRL": "Brazilian Real (BRL)",
    "CAD": "Canadian Dollar (CAD)",
    "CHF": "Swiss Franc (CHF)",
    "CNY": "Chinese Yuan (CNY)",
    "CZK": "Czech Koruna (CZK)",
    "DKK": "Danish Krone (DKK)",
    "EEK": "Estonian Kroon (EEK)",
    "EUR": "Euro (EUR)",
    "GBP": "British Pound (GBP)",
    "HKD": "Hong Kong Dollar (HKD)",
    "HUF": "Hungarian Forint (HUF)",
    "IDR": "Indonesian Rupiah (IDR)",
    "ILS": "Israeli New Shekel (ILS)",
    "INR": "Indian Rupee (INR)",
    "ISK": "Icelandic Krona (ISK)",
    "JPY": "Japanese Yen (JPY)",
    "KRW": "South Korean Won (KRW)",
    "LTL": "Lithuanian Litas (LTL)",
    "MXM": "Mexican Peso (MXM)",
    "MYR": "Malaysian Ringgit (MYR)",
    "NOK": "Norwegian Krone (NOK)",
    "NZD": "New Zealand Dollar (NZD)",
    "PHP": "Philippine Peso (PHP)",
    "PLN": "Polish Zloty (PLN)",
    "RON": "Romanian Leu (RON)",
    "RUB": "Russian Ruble (RUB)",
    "SEK": "Swedish Krona (SEK)",
    "SGD": "Singapore Dollar (SGD)",
    "SIT": "Slovenian Tolar (SIT)",
    "SKK": "Slovak Koruna (SKK)",
    "THB": "Thai Baht (THB)",
    "TRY": "Turkish Lira (TRY)",
    "USD": "US Dollar (USD)",
    "ZAR": "South African Rand (ZAR)"
}

# Create StringVar variables to store the input and output currency values
currency_input = StringVar(root)
currency_output = StringVar(root)

# Output number of decimal places
decimal_places = 2

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
    if amount.get() == '' or fromm.get() == "From" or too.get() == "To":
        return
    else:
        try:
            amount_value = amount.get()
            converted_value = c.convert(amount_value, fromm.get(), too.get())
            currency_output.set(round(converted_value, decimal_places))
            return currency_output.get()
        except Exception as e:
            messagebox.showerror("Error", str(e))

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
        currency_input.set(input)
        if currency_val1.get() != "From" and currency_val2.get() != "To":
            convert_cur(input, currency_val1, currency_val2)
        else:
            return True
    elif input == "":
        return True
    else:
        return False

# Initialize an empty list for the history of conversions
conversion_history = []

# Function to update the currency conversion
def callback(*args):
    """
    Callback function to update the currency conversion when the selected currencies change.
    """
    global currency_input, currency_val1, currency_val2
    currency_output.set(convert_cur(currency_input, currency_val1, currency_val2))

    print(f"Converted value: {currency_output.get()}")

    input_amount = currency_input.get()
    input_currency = currency_val1.get()
    output_amount = currency_output.get()
    output_currency = currency_val2.get()

    # Append the conversion details to the history
    if output_amount != 'None' and output_currency != 'To':
        conversion_history.append({
            'input_currency': input_currency,
            'input_amount': input_amount,
            'output_currency': output_currency,
            'output_amount': output_amount
        })

    print(conversion_history)

# Create a label widget for the title
FONT_STYLE = "Helvetica 15 bold"

label = Label(root, text='Currency Converter', font=FONT_STYLE)
label.pack()

# Create a frame for the listbox and its label
listbox_frame = Frame(root)
listbox_frame.pack(side=RIGHT)

# Create a label widget for the listbox heading
listbox_label = Label(listbox_frame, text='Names for Currencies with abbreviations', font=FONT_STYLE)
listbox_label.pack(padx=10)

# Create a scrollbar for the listbox
scrollbar = Scrollbar(listbox_frame)
scrollbar.pack(side=RIGHT, fill=Y, padx=10)

# Create a listbox widget to display the currencies
listbox = Listbox(listbox_frame, yscrollcommand=scrollbar.set)
for currency in currencies_names.values():
    listbox.insert(END, currency)
listbox.pack(fill=BOTH)

# Configure the scrollbar to scroll the listbox
scrollbar.config(command=listbox.yview)

# Create a input for the decimal places
decimal_places_label = Label(root, text='Decimal Places (max. 6)', font=FONT_STYLE)
decimal_places_label.pack()

# Create a StringVar for the label text
decimal_places_text = StringVar()
decimal_places_text.set(f"Current Decimal Places: {decimal_places}")

# Function to update the decimal places
def update_decimal_places():
    """
    Update the decimal places based on the input in the decimal places entry widget.
    """
    global decimal_places
    if decimal_places_entry.get() == "":
        decimal_places = 2
        print(f"Decimal places: {decimal_places}")
        decimal_places_text.set(f"Current Decimal Places: {decimal_places}")
        return
    
    if int(decimal_places_entry.get()) > 6:
        decimal_places = 6
        print(f"Decimal places: {decimal_places}")
        decimal_places_text.set(f"Current Decimal Places: {decimal_places}")
        return

    decimal_places = int(decimal_places_entry.get())
    print(f"Decimal places: {decimal_places}")
    decimal_places_text.set(f"Current Decimal Places: {decimal_places}")

    callback()

# Create a button widget to update the decimal places
update_button = Button(root, text="Update Decimal Places", command=update_decimal_places, font=FONT_STYLE)
update_button.pack()

# Create an entry widget for the decimal places
decimal_places_entry = Entry(root, textvariable=decimal_places, font="Geneva 15 bold", justify=CENTER)
decimal_places_entry.pack()

# Create a label widget for the current decimal places
current_decimal_places_label = Label(root, textvariable=decimal_places_text, font=FONT_STYLE)
current_decimal_places_label.pack()

# Create an entry widget for the currency input
amount = Entry(root, textvariable=currency_input, font="Geneva 30 bold", justify=CENTER)
amount.pack(padx=10, pady=15)

# Register the entry_valid function as a validation command for the amount entry widget
reg = root.register(entry_valid)
amount.config(validate="key", validatecommand=(reg, '%P'))

# Create an option menu widget for the source currency selection
currency_from = OptionMenu(root, currency_val1, *currencies)
currency_from.config(width=38, height=2, font=FONT_STYLE, justify=CENTER)
currency_from.pack()

# Create an option menu widget for the target currency selection
currency_to = OptionMenu(root, currency_val2, *currencies)
currency_to.config(width=38, height=2, font=FONT_STYLE, justify=CENTER)
currency_to.pack()

# Bind the callback function to the changes in the source and target currency selections
currency_val1.trace('w', callback)
currency_val2.trace('w', callback)

# Create an entry widget for the currency output
output = Entry(root, textvariable=currency_output, font="Geneva 30 bold", justify=CENTER)
output.pack()


# Create a button widget to open a new window with the conversion history
def open_history():
    """
    Open a new window with the conversion history.
    """

    # Function to clear the conversion history
    def clear_history():
        """
        Clear the conversion history.
        """
        global conversion_history
        conversion_history = []
        history_listbox.delete(0, END)

    history_window = Toplevel(root)
    history_window.title("Conversion History")
    history_window.geometry("500x500")

    # Create a label widget for the title of the history window
    history_label = Label(history_window, text='Conversion History', font="Helvetica 20 bold")
    history_label.pack()

    # Add clear history button
    clear_history_button = Button(history_window, text="Clear History", command=clear_history, font=FONT_STYLE)
    clear_history_button.pack(pady=10)

    # Create a frame for the history listbox and its label
    history_frame = Frame(history_window)
    history_frame.pack(side=RIGHT, fill=BOTH, expand=True)

    # Create a label widget for the history listbox heading
    history_listbox_label = Label(history_frame, text='Conversion History', font=FONT_STYLE)
    history_listbox_label.pack()

    # Create a scrollbar for the history listbox
    history_scrollbar = Scrollbar(history_frame)
    history_scrollbar.pack(side=RIGHT, fill=Y)

    # Create a listbox widget to display the conversion history
    history_listbox = Listbox(history_frame, yscrollcommand=history_scrollbar.set)
    for conversion in conversion_history:
        history_listbox.insert(END, f"{conversion['input_currency']} {conversion['input_amount']} = {conversion['output_currency']} {conversion['output_amount']}")
    history_listbox.pack(fill=BOTH)

    # Configure the scrollbar to scroll the history listbox
    history_scrollbar.config(command=history_listbox.yview)

# Create a button widget to open the conversion history window
history_button = Button(root, text="Conversion History", command=open_history, font=FONT_STYLE)
history_button.pack(pady=10)

import webbrowser

# GitHub repository link
github_link = "https://github.com/MoinJulian/currency-converter"

def open_github():
    """
    Open the GitHub repository link in the default web browser.
    """
    webbrowser.open(github_link)

# Create a label widget for the GitHub repository link
github_button = Button(root, text="GitHub repository",command=open_github, font=FONT_STYLE)
github_button.pack(pady=10)

# Function to close the application
def on_closing():
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

# Create a button widget to close the application
close_button = Button(root, text="Close", command=on_closing, font=FONT_STYLE)
close_button.pack(pady=10)

# Start the main event loop
root.mainloop()