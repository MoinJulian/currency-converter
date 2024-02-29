import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import cairosvg
import webbrowser
from conversion_rate import CONVERSION_RATES
from currency_utils import get_fullname
from currency_conversion import perform_currency_conversion

user_font_size = 12  # This should be updated based on user's settings
wakatime_badge = "https://wakatime.com/badge/github/MoinJulian/currency-converter.svg"
wakatime_response = requests.get(wakatime_badge)
print(wakatime_response.status_code)
img_data = wakatime_response.content

def open_github():
    webbrowser.open("https://github.com/MoinJulian")


def create_main_window():
    root = tk.Tk()
    root.title("Currency Converter")
    return root


def add_info_label(root):
    info_label = ttk.Label(root, text="Please note that this program is not using an API and therefore can't have "
                                       "up-to-date information.")
    info_label.grid(row=0, column=0, columnspan=2, pady=10)
    info_label.config(font=("Arial", user_font_size, "bold"))


def add_choice_section(root):
    choice_label = ttk.Label(root, text="Select conversion:")
    choice_label.grid(row=1, column=0, pady=5, sticky="e")

    choice_var = tk.StringVar()
    choice_combobox = ttk.Combobox(root, textvariable=choice_var,
                                   values=[get_fullname(key) for key in CONVERSION_RATES.keys()], state="readonly")
    choice_combobox.grid(row=1, column=1, pady=5)
    return choice_var, choice_combobox


def add_amount_section(root):
    amount_label = ttk.Label(root, text="Enter amount:")
    amount_label.grid(row=2, column=0, pady=5, sticky="e")

    amount_entry = ttk.Entry(root)
    amount_entry.grid(row=2, column=1, pady=5)
    return amount_entry


def add_convert_button(root, choice_var, choice_combobox, amount_entry, result_label, result_link):
    def convert():
        perform_currency_conversion(choice_var, choice_combobox, amount_entry, result_label, result_link, CONVERSION_RATES)

    convert_button = ttk.Button(root, text="Convert", command=convert)
    convert_button.grid(row=3, column=0, columnspan=2, pady=10)


def add_result_labels(root):
    result_label = ttk.Label(root, text="")
    result_label.grid(row=4, column=0, columnspan=2, pady=10)

    result_link = ttk.Label(root, text="")
    result_link.grid(row=5, column=0, columnspan=2, pady=5)

    return result_label, result_link


def add_github_button(root):
    button = ttk.Button(root, text="GitHub", command=open_github)
    button.grid(row=6, column=0, columnspan=2, pady=20)

def open_waka_time():
    webbrowser.open("https://wakatime.com/@MoinJulian")

def load_wakatime_badge(root, img_data):
    # Convert SVG data to PNG
    png_data = cairosvg.svg2png(bytestring=img_data)

    # Open the PNG image with PIL
    img = Image.open(BytesIO(png_data))
    img = ImageTk.PhotoImage(img)
    panel = tk.Button(root, image=img, text="Open Wakatime Profile", command=open_waka_time)
    panel.image = img
    panel.grid(row=7, column=0, columnspan=2, pady=10)

def main():
    root = create_main_window()
    add_info_label(root)
    load_wakatime_badge(root, img_data)
    choice_var, choice_combobox = add_choice_section(root)
    amount_entry = add_amount_section(root)
    result_label, result_link = add_result_labels(root)
    add_convert_button(root, choice_var, choice_combobox, amount_entry, result_label, result_link)
    add_github_button(root)
    root.mainloop()


if __name__ == "__main__":
    main()
