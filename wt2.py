# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:55:36 2023

@author: shiva
"""

import requests
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime

# API key from OpenWeatherMap
API_KEY = "4d6080956bf931f3a6b47332361c4ae6"

# API endpoint
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Create a tkinter app
app = tk.Tk()
app.title("Weather App")
app.configure(background="orange")
app.geometry("350x400")
img = Image.open("wtbnk.jpeg")
img = img.resize((500, 500), Image.ANTIALIAS)
app.background_image = ImageTk.PhotoImage(img)
app.background_label = tk.Label(app.master, image=app.background_image)
app.background_label.place(x=0, y=0, relwidth=1, relheight=1)
    


# Define a function to get weather information
def get_weather_info(city):
    params = {"appid": API_KEY, "q": city, "units": "metric"}
    response = requests.get(API_URL, params=params)
    weather_data = response.json()
    
    # Get required weather information
    location = weather_data["name"]
    temp = weather_data["main"]["temp"]
    min_temp = weather_data["main"]["temp_min"]
    max_temp = weather_data["main"]["temp_max"]
    sunrise = datetime.fromtimestamp(weather_data["sys"]["sunrise"]).strftime("%H:%M:%S")
    sunset = datetime.fromtimestamp(weather_data["sys"]["sunset"]).strftime("%H:%M:%S")
    weather_desc = weather_data["weather"][0]["description"]
    
    # Display weather information in GUI
    location_label.config(text="" + location)
    temp_label.config(text="" + str(temp) + "°C")
    min_temp_label.config(text="Min: " + str(min_temp) + "°C")
    max_temp_label.config(text="Max:" + str(max_temp) + "°C")
    sunrise_label.config(text="Sunrise at: " + sunrise)
    sunset_label.config(text="Sunset at: " + sunset)
    weather_desc_label.config(text="" + weather_desc)

# Define a function to handle button click event
def on_button_click():
    city = city_entry.get()
    get_weather_info(city)

# Create GUI widgets
city_label = tk.Label(app, text="Enter City Name: ",font=('Times','14', 'italic'),bg='black',fg='white')
city_label.place(x=20,y=10)

city_entry = tk.Entry(app)
city_entry.place(x=180,y=14)

button = tk.Button(app, text="Get Weather Info", command=on_button_click,bg='black',fg='white')
button.place(x=140,y=50)

location_label = tk.Label(app, text="",font=('Times','28', 'italic'),bg='black',fg='white')
location_label.place(x=10,y=90)

temp_label = tk.Label(app, text="",font=('Times','14'),bg='black',fg='white')
temp_label.place(x=10,y=150)

min_temp_label = tk.Label(app, text="",font=('Times','14', 'italic'),bg='black',fg='white')
min_temp_label.place(x=10,y=200)

max_temp_label = tk.Label(app, text="",font=('Times','14', 'italic'),bg='black',fg='white')
max_temp_label.place(x=10,y=250)

sunrise_label = tk.Label(app, text="",font=('Times','14', 'italic'),bg='black',fg='white')
sunrise_label.place(x=10,y=300)

sunset_label = tk.Label(app, text="",font=('Times','14', 'italic'),bg='black',fg='white')
sunset_label.place(x=10,y=350)

weather_desc_label = tk.Label(app, text="",font=('Times','18'),bg='black',fg='white')
weather_desc_label.place(x=10,y=400)

#Start the GUI event loop
app.mainloop()
