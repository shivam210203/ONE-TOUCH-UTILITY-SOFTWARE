# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 23:21:51 2023

@author: shiva
"""

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.resizable(False,False)

        # create the display widget
        self.display = tk.Entry(master, width=40,font=('Arial', 16))
        self.display.grid(row=0, column=1, columnspan=5, padx=20, pady=10)

        # create the style for the buttons
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 16), padding=5, width=5)

        # create the number buttons
        self.create_button(7, 2, 1)
        self.create_button(8, 2, 2)
        self.create_button(9, 2, 3)
        self.create_button(4, 3, 1)
        self.create_button(5, 3, 2)
        self.create_button(6, 3, 3)
        self.create_button(1, 4, 1)
        self.create_button(2, 4, 2)
        self.create_button(3, 4, 3)
        self.create_button(0, 5, 1)

        # create the operator buttons
        self.create_button("+", 2, 4)
        self.create_button("-", 3, 4)
        self.create_button("*", 2, 5)
        self.create_button("/", 3, 5)
        self.create_button("%", 4, 5)

        # create the clear and equals buttons
        self.create_button("C", 1, 5)
        self.create_button("=", 5, 5)

        # create the trigo function buttons
        self.create_button("sin", 1, 1)
        self.create_button("cos", 1, 2)
        self.create_button("tan", 1, 3)
        self.create_button("pi", 1, 4)
        
        self.create_button("log", 5, 2)
        self.create_button("ln", 5,3)
#        self.create_button("exp", 2, 6)
        self.create_button("^", 4, 4)
        self.create_button("!", 5, 4)


    def create_button(self, text, row, column, rowspan=1, columnspan=1):
        button = ttk.Button(self.master, text=text, style='TButton', command=lambda: self.button_click(text))
        button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "sin":
            try:
                result = math.sin(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "cos":
            try:
                result = math.cos(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "tan":
            try:
                result = math.tan(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "log": 
            try: 
                result = math.log10(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")

        elif text == "ln":
            try:
                result = math.log(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif text == "^":
            self.display.insert(tk.END, "**")
        elif text == "exp":
            try:
                result = math.exp(float(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")        

        elif text == "!":
            try:
                n = int(self.display.get())
                result = math.factorial(n)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
                self.display.insert(tk.END, text)
        
        
rootcal = tk.Tk()
rootcal.geometry("550x400")
img = Image.open("bck.jpg")
img = img.resize((550, 400), Image.ANTIALIAS)
rootcal.background_image = ImageTk.PhotoImage(img)
rootcal.background_label = tk.Label(rootcal.master, image=rootcal.background_image)
rootcal.background_label.place(x=0, y=0, relwidth=1, relheight=1)
style = ttk.Style()
style.configure('TLabel', font=('Arial', 20))
style.configure('TEntry', font=('Arial', 20))

calculator = Calculator(rootcal)
rootcal.mainloop()

