# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:09:15 2023

@author: shiva
"""

import tkinter as tk
import datetime as dt
from PIL import Image, ImageTk



class StopWatch:
    def __init__(self, master):
        self.master = master
        self.start_time = None
        self.elapsed_time = None
        self.lap_time = None
        self.lap_count = 0
        
        
        img = Image.open("stbck2.png")
        img = img.resize((500, 500), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(img)
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.lower()  # place the background label behind all other widgets


        self.display = tk.Label(master, text="00:00:00.000", font=("Arial", 30,"italic"), fg="cyan",bg="black")
        self.display.pack(pady=10)

        self.start_button = tk.Button(master, text="Start", command=self.start,font=("Arial",15,"italic"), fg="cyan",bg="black")
        self.start_button.pack(side="left", padx=10)
        self.start_button.place(x=10,y=150)
        
        self.stop_button = tk.Button(master, text="Stop", command=self.stop, state="disabled",bg='black', fg="cyan", font=("Arial", 15,'italic'))
        self.stop_button.pack(side="left")
        self.stop_button.place(x=10,y=200)
        
        self.lap_button = tk.Button(master, text="Lap", command=self.lap, state="disabled",bg="black",fg="cyan", font=("Arial", 15,'italic'))
        self.lap_button.pack(side="left", padx=10)
        self.lap_button.place(x=10,y=250)
        
        self.reset_button = tk.Button(master, text="Reset", command=self.reset,bg='black',fg="cyan", font=("Arial", 15,'italic') )
        self.reset_button.pack(side="left")
        self.reset_button.place(x=10,y=300)
        
        self.laps_label = tk.Label(master, text="Laps:",bg='black',fg="cyan", font=("Arial", 15,'italic'))
        self.laps_label.pack(pady=5)
        self.laps_label.place(x=100,y=150)

        self.laps_display = tk.Listbox(master, height=10, bg="black",fg="cyan",relief='solid',bd=1,font=("Arial", 12,'italic'), selectbackground="cyan",selectforeground="black")
        self.laps_display.pack(side="right",padx='30',pady="10")
        self.laps_display.place(x=100,y=180)
    def start(self):
        self.start_time = dt.datetime.now()
        self.elapsed_time = dt.timedelta()
        self.lap_time = self.start_time
        self.lap_count = 0

        self.update()

        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.lap_button.config(state="normal")
        self.reset_button.config(state="normal")

    def stop(self):
        self.master.after_cancel(self.timer_id)

        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.lap_button.config(state="disabled")

    def lap(self):
        lap_elapsed = dt.datetime.now() - self.lap_time
        self.lap_time = dt.datetime.now()
        self.lap_count += 1

        lap_string = f"Lap {self.lap_count}: {str(lap_elapsed).split('.')[0]}"
        self.laps_display.insert(tk.END, lap_string)

    def reset(self):
        self.master.after_cancel(self.timer_id)

        self.display.config(text="00:00:00.000")
        self.laps_display.delete(0, tk.END)

        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.lap_button.config(state="disabled")
        self.reset_button.config(state="disabled")

    def update(self):
        self.elapsed_time = dt.datetime.now() - self.start_time
        time_string = str(self.elapsed_time).split('.')[0] + "." + str(self.elapsed_time.microseconds)[:3]
        self.display.config(text=time_string)

        self.timer_id = self.master.after(10, self.update)


# if __name__ == "__main__":
root = tk.Tk()
root.title("Stopwatch")
root.resizable(False,False)
root.geometry("450x450")
stopwatch = StopWatch(root)

root.mainloop()
