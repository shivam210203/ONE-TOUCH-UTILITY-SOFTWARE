# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:56:30 2023

@author: shiva
"""

import datetime
import tkinter as tk

from PIL import Image, ImageTk

# Dictionary to map timezone name to UTC offset in seconds
timezones = {
    "New York": -5*3600,
    "London": 0,
    "Paris": 1*3600,
    "Tokyo": 9*3600,
    "Sydney": 11*3600,
    "India": 5.5*3600
}

# Function to get the current time and date for a specific timezone
def get_local_time(zone):
    # Get current UTC time
    current_utc_time = datetime.datetime.utcnow()
    # Add the UTC offset for the specified timezone to get the local time
    current_local_time = current_utc_time + datetime.timedelta(seconds=timezones[zone])
    # Return the formatted local time and date
    return current_local_time.strftime('%H:%M:%S'), zone, f"UTC{timezones[zone]/3600:+.1f}"

# Function to update the clock display every second
def update_clock():
    # Get local time information for the selected location
    local_time, timezone, utc_offset = get_local_time(location.get())
    # Update the clock display with the local time, timezone, and UTC offset information for the selected location
    clock.config(text=local_time)
    timezone_label.config(text=timezone)
    utc_offset_label.config(text=utc_offset)
    # Schedule the update_clock function to run again after 1 second
    root.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

root.configure(background="orange")
root.geometry("500x400")
img = Image.open("bck.jpg")
img = img.resize((600, 600), Image.ANTIALIAS)
root.background_image = ImageTk.PhotoImage(img)
root.background_label = tk.Label(root.master, image=root.background_image)
root.background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the location selection dropdown menu
location = tk.StringVar(root)
location.set("New York")
location_menu = tk.OptionMenu(root, location, "New York", "London", "Paris", "Tokyo", "Sydney", "India")
location_menu.config(font=('Arial', 14))
location_menu.pack(pady=10)

# Create the clock display labels
clock = tk.Label(root, font=('Arial', 94,'italic'), bg='white', fg='black')
clock.pack(pady=20)
timezone_label = tk.Label(root, font=('times', 18), fg='black')
#timezone_label.pack()
utc_offset_label = tk.Label(root, font=('times', 18,'italic'), fg='black')
utc_offset_label.pack()

# Start the clock update loop
update_clock()
root.resizable(False,False)
# Run the main window event loop
root.mainloop()
