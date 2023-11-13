# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 18:01:03 2023

@author: shiva
"""

import tkinter as tk
import datetime as dt
import winsound
from PIL import Image, ImageTk


class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.duration = None
        self.end_time = None
        self.time_left = None
        self.timer_id = None
        self.timer_running = False
        
        img = Image.open("cttbck.jpg")
        img = img.resize((400, 400), Image.ANTIALIAS)
        self.background_image = ImageTk.PhotoImage(img)
        self.background_label = tk.Label(self.master, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.lower()  # place the background label behind all other widgets


        self.display = tk.Label(master, text="00:00:00", font=("Arial", 30,"italic"), fg="cyan",bg="black")
        self.display.pack(padx=30,pady=30)


        self.hour_input_label = tk.Label(master, text="Hours:", font=("Arial", 15,"italic"), fg="cyan",bg="black")
        self.hour_input_label.pack(pady=5)
        self.hour_input_label.place(x=10,y=100)
        
        self.hour_input = tk.Entry(master, width=10)
        self.hour_input.pack(pady=5)
        self.hour_input.place(x=90,y=105)
        
        self.time_input_label = tk.Label(master, text="minutes:", font=("Arial", 15,"italic"), fg="cyan",bg="black")
        self.time_input_label.pack(pady=5)
        self.time_input_label.place(x=10,y=150)

        self.time_input = tk.Entry(master, width=10)
        self.time_input.pack(pady=5)
        self.time_input.place(x=110,y=155)
        
        self.second_input_label = tk.Label(master, text="Seconds:", font=("Arial", 15,"italic"), fg="cyan",bg="black")
        self.second_input_label.pack(pady=5)
        self.second_input_label.place(x=10,y=200)
        
        self.second_input = tk.Entry(master, width=10)
        self.second_input.pack(pady=5)
        self.second_input.place(x=110,y=205)


        self.set_button = tk.Button(master, text="Start", command=self.set_time,font=("Arial", 15,"italic"), fg="cyan",bg="black")
        self.set_button.pack(side="left", padx=10,pady=30)
        self.set_button.place(x=10,y=250)
        
        self.start_button = tk.Button(master, text="play", command=self.start, state="disabled",font=("Arial", 15,"italic"), fg="cyan",bg="black")
        self.start_button.pack(side="left",pady=30)
        self.start_button.place(x=80,y=250)
        
        self.stop_button = tk.Button(master, text="pause", command=self.stop, state="disabled",font=("Arial", 15,"italic"), fg="cyan",bg="black")
        self.stop_button.pack(side="left", padx=10,pady=30)
        self.stop_button.place(x=150,y=250)
        
        self.reset_button = tk.Button(master, text="reset", command=self.reset, state="disabled",font=("Arial", 15,"italic"), fg="cyan",bg="black")
        self.reset_button.pack(side="left",pady=30)
        self.reset_button.place(x=240,y=250)
    def set_time(self):
        try:
            time_in_minutes = int(self.time_input.get())
            s=int(self.second_input.get())
            h=int(self.hour_input.get())
        except ValueError:
            self.time_input.delete(0, tk.END)
            self.time_input.insert(0, "Invalid input")
            return

        self.duration = dt.timedelta(hours=h,minutes=time_in_minutes,seconds=s)
        self.end_time = dt.datetime.now() + self.duration
        self.time_left = self.duration
        self.timer_running = True
        self.update()

        self.stop_button.config(state="normal")
        self.set_button.config(state="disabled")
        self.start_button.config(state="disabled")
        self.reset_button.config(state="normal")

    def start(self):
        self.timer_running = True

        self.update()

        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

    def stop(self):
        self.timer_running = False

        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def reset(self):
        self.master.after_cancel(self.timer_id)

        self.duration = None
        self.end_time = None
        self.time_left = None
        self.timer_running = False

        self.display.config(text="00:00:00", fg="cyan")

        self.set_button.config(state="normal")
        self.start_button.config(state="disabled")
        self.stop_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        

    def update(self):
        if self.timer_running:
            self.time_left = self.end_time - dt.datetime.now()

            if self.time_left.total_seconds() <= 0:
                self.display.config(text="time up",fg="cyan")
                self.timer_running = False
                winsound.PlaySound("Alarm.wav", winsound.SND_ALIAS)
            elif self.time_left.total_seconds() <= 11:
                self.display.config(bg="yellow",fg="black")
                if self.time_left.total_seconds() <= 6:
                    self.display.config(bg="red",fg="white")
                     
            # elif self.time_left.total_seconds() <= 5:
            #     self.display.config(bg="yellow")
            else:
                self.display.config(fg="cyan")

            time_string = str(self.time_left).split('.')[0]
            self.display.config(text=time_string)

            self.timer_id = self.master.after(10, self.update)


# if __name__ == "__main__":
root = tk.Tk()
root.title("Countdown Timer")
root.geometry("400x400")
countdown = CountdownTimer(root)
root.mainloop()
