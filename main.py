import tkinter as tk
import requests
from amount_section import add_amount_section
from choice_section import add_choice_section
from convert_button import add_convert_button
from github_button import add_github_button
from info_label import add_info_label
from load_wakatime import load_wakatime_badge
from result_labels import add_result_labels

wakatime_badge = "https://wakatime.com/badge/github/MoinJulian/currency-converter.svg"
wakatime_response = requests.get(wakatime_badge)
print(wakatime_response.status_code)
img_data = wakatime_response.content

def create_main_window():
    # Create the main window for the currency converter application.
    root = tk.Tk()
    root.title("Currency Converter")
    return root

def main():
    # Main function to create and run the currency converter application.
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
