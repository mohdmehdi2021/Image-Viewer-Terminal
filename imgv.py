#!/usr/bin/env python3

# Image Viewer for Terminal
# Developer: Mohd Mehdi Rannavi s/o Arshad Abbas Khan
# Date: 08 October, 2024
# Motive: View images directly from Terminal

from tkinter import *
from PIL import Image, ImageTk, ImageOps
import argparse

def display_image(file_name):
    window = Tk()
    # window.geometry("400x400")
    window.title("Image Viewer from Terminal (Developer: Mohd Mehdi Rannavi)")
    img = Image.open(file_name)
    img_tk = ImageTk.PhotoImage(img)

    label = Label(window, image=img_tk)
    label.pack()

    window.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Image Viewer for Terminal (Mohd Mehdi Rannavi)")
    parser.add_argument("-f", "--file", required=True, help="Enter current file name or file path")
    args = parser.parse_args()
    display_image(args.file)

if __name__== "__main__":
    main()