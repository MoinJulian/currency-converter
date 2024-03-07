from conversion_rate import CONVERSION_RATES
from currency_conversion import perform_currency_conversion
from tkinter import ttk

def add_convert_button(root, choice_var, choice_combobox, amount_entry, result_label, result_link):
    # Add the convert button to the main window.
    def convert():
        perform_currency_conversion(choice_var, choice_combobox, amount_entry, result_label, result_link, CONVERSION_RATES)

    convert_button = ttk.Button(root, text="Convert", command=convert)
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)