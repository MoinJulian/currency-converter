import tkinter as tk
from tkinter import ttk

def add_result_labels(root):
    # Add the result labels to the main window.
    result_label = ttk.Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    result_link = ttk.Label(root, text="")
    result_link.grid(row=5, column=0, columnspan=2, pady=5)

    return result_label, result_link