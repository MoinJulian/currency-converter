from tkinter import ttk

def add_info_label(root):
    # Add an information label to the main window.
    info_label = ttk.Label(root, text="Please note that this program is not using an API and therefore can't have "
                                       "up-to-date information.")
    info_label.grid(row=0, column=0, columnspan=2, pady=10)
    info_label.config(font=("Arial", 12, "bold"))