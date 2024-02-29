from wakatime import open_waka_time
import cairosvg
from PIL import Image, ImageTk
import tkinter as tk
from io import BytesIO

def load_wakatime_badge(root, img_data):
    # Load and display the WakaTime badge in the main window.
    # Convert SVG data to PNG
    png_data = cairosvg.svg2png(bytestring=img_data)

    # Open the PNG image with PIL
    img = Image.open(BytesIO(png_data))
    img = ImageTk.PhotoImage(img)
    panel = tk.Button(root, image=img, text="Open Wakatime Profile", command=open_waka_time)
    panel.image = img
    panel.grid(row=7, column=0, columnspan=2, pady=10)