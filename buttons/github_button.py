from tkinter import ttk
from utils.open_github import open_github


def add_github_button(root):
    # Add the GitHub button to the main window.
    button = ttk.Button(root, text="GitHub", command=open_github)
    button.grid(row=6, column=0, columnspan=2, pady=20)