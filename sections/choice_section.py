from tkinter import ttk
import tkinter as tk
from currency.conversion_rate import CONVERSION_RATES

from currency.currency_utils import get_fullname

def add_choice_section(root):
    # Add the currency conversion choice section to the main window.
    choice_label = ttk.Label(root, text="Select conversion:")
    choice_label.grid(row=1, column=0, pady=5, sticky="e")

    choice_var = tk.StringVar()
    choice_combobox = ttk.Combobox(root, textvariable=choice_var,
                                   values=[get_fullname(key) for key in CONVERSION_RATES.keys()], state="readonly")
    choice_combobox.grid(row=1, column=1, pady=5)
    return choice_var, choice_combobox