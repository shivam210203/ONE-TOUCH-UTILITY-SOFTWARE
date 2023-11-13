# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 21:03:22 2023

@author: shiva
"""
import tkinter as tk
from tkinter import ttk

def run_calculator():
    import calc

def run_to_do():
     import td
    
def run_stopwatch():
     import stw
     
def run_countdown():
     import ctt2

root = tk.Tk()
root.title("main")
root.configure(background="orange")
root.geometry("450x300")


add_button = ttk.Button(root, text="calci", command=run_calculator)
add_button = tk.Button(root, text="calci", command=run_calculator)
add_button.pack(padx=10, pady=10)
add_button.place(x=350, y=50)

add1_button = ttk.Button(root, text="calci", command=run_to_do)
add1_button = tk.Button(root, text="calci", command=run_to_do)
add1_button.pack(padx=10, pady=10)
add1_button.place(x=150, y=50)

add2_button = ttk.Button(root, text="calci", command=run_stopwatch)
add2_button = tk.Button(root, text="calci", command=run_stopwatch)
add2_button.pack(padx=10, pady=10)
add2_button.place(x=250, y=50)

add3_button = ttk.Button(root, text="calci", command=run_countdown)
add3_button = tk.Button(root, text="calci", command=run_countdown)
add3_button.pack(padx=10, pady=10)
add3_button.place(x=250, y=100)


root.resizable(False,False)
# Start the main loop
root.mainloop()


    
# def run_calci():
#     import calc
    
# def run_calci():
#     import calc
    
# def run_calci():
#     import calc

# def run_calci():
#     import calc
    
# def run_calci():
#     import calc
    
# def run_calci():
#     import calc
    
# def run_calci():
#     import calc
    


# ch = int(input("enter a number:"))


# if ch==1:
#     run_calci()