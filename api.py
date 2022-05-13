
import json
import os
import urllib.request
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Callable
import requests
from tkinter import *

from app import get_input




root =Tk()
root.geometry("800x800") #size of the window by default
root.resizable(1000,1000) #to make the window resizable
root.title("Weather App")#title of our window


city_value = StringVar()

def read_cred(name: str):
    
    with open('parameters.json') as f:
        par = json.loads(f)
        return par[name]
    

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
endpoint = BASE_URL + "?q={city_name}&appid={api_key}&units=metric"
API = "7d6b470e0feba322cf886d3ca22a7478"


city_value = StringVar()
    


def requests_adapter(url: str) -> dict:
    
    
    """An adapter that encapsulates requests.get"""
   
   
    resp = requests.get(url)
    return resp.json()
###############################################################################################
def urllib_adapter(url: str) -> dict:    
    """An adapter that encapsulates urllib.urlopen"""
        
    with urllib.request.urlopen(url) as response:
        resp = response.read()
    return json.loads(resp)
city_value = StringVar()


def get_weather():
    """Given a city name passed as query parameter. Display a weather summary."""
    global city_name
    city_name = get_input()
    weather_info = retrieve_weather_with_adapter(city_name, adapter=requests_adapter)
    
    tfield.delete("1.0", "end")   #to clear the text field for every new output

    #as per API documentation, if the cod is 200, it means that weather data was successfully fetched
    city_name = get_input()

    if weather_info['cod'] == 200:
    
    #-----------Storing the fetched values of weather of a city

        temp = int(weather_info['main']['temp'] )                                    
        feels_like_temp = int(weather_info['main']['feels_like'])
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] 
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        #assigning Values to our weather varaible, to display as output
            
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nWind Speed: {wind_speed} m\s 1\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather in '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
    
    tfield.insert(INSERT, weather)

###############################################################################################

def retrieve_weather_with_adapter(city: str, adapter: Callable[[str], dict] = requests_adapter):
    
    
    """Retrieve weather implementation that uses an adapter."""
    
    
    data = find_weather_with_adapter_for(city, adapter=adapter)

    return data
############################################################################################


def time_format_for_location(utc_with_tz):
        local_time = datetime.utcfromtimestamp(utc_with_tz)
        return local_time.time()


def find_weather_with_adapter_for(city: str, adapter: Callable[[str], dict]) -> dict:
    
    
    """Find the weather using an adapter."""
    
    
    url = endpoint.format(city_name=city, api_key=API)
    return adapter(url)

###############################################################################################

def find_weather_for():
       
    """Queries the weather API and returns the weather data for a particular city."""
    tfield.delete("1.0", "end")
    city = get_input()
    url = endpoint.format(city_name=city, api_key=read_cred('api_key'))
    resp = requests.get(url)
    return resp.json()



###############################################################################################


###############################################################################################

def retrieve_weather(city: str):
    
    
    """Finds the weather for a city and returns a WeatherInfo instance."""
    
    
    data = find_weather_for(city)
    return (data)

###############################################################################################


def format_date(timestamp: int) -> str:
   
   
    """Formats a timestamp into date time."""
    
    
    dt = datetime.fromtimestamp(timestamp)
    return dt.strftime("%m/%d/%Y, %H:%M:%S")




city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10) #to generate label heading
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()

Button(root, command = get_weather, text = "Check Weather status", font="Arial 10", bg='lightblue',
       fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=50, height=50)
tfield.pack()
 
root.mainloop()