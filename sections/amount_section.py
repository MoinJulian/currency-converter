import tkinter as tk
from tkinter import ttk

def add_amount_section(root):
    # Add the amount entry section to the main window.
    amount_label = ttk.Label(root, text="Enter amount:")
    amount_label.grid(row=2, column=0, pady=5, sticky="e")

    amount_entry = ttk.Entry(root)
    amount_entry.grid(row=2, column=1, pady=5)
    return amount_entry