#!/usr/bin/python3

# _*_ coding:utf-8 _*_


# 3rd project
# weather app [python Internship Project (OASIS INFOBYTE)]
# @debang5hu


import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk
from os import getenv
from requests import get
import datetime
import pytz
from timezonefinder import TimezoneFinder    #type: ignore



# <--- global val --->
COLOR = 'grey'    # #3b3630

# firefox
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0'}

WeatherAPI = getenv('WeatherAPI') # to avoid hardcoding credentials

UNIT = 'celsius'  # default
temparature = 0


# to get time of all timezone
def dateandtime(lat,lon):
    tz = TimezoneFinder()
    location = tz.timezone_at(lng=lon,lat=lat)
    loctime = pytz.timezone(location)
    
    date = datetime.date.today().strftime("%d/%m/%Y")   # all country use same calendar except North Korea
    time = datetime.datetime.now(loctime).strftime('%I:%M %p')

    date_output.config(text=f"{date}")
    time_output.config(text=f"{time}")


# to set the weather icon
def seticon(file):
    icon = Image.open(f'{file}')
    resizeicon = icon.resize((190,190))
    finalicon = ImageTk.PhotoImage(resizeicon)
    position = tkinter.Label(image=finalicon)
    position.place(x=20,y=100)
    position.image = finalicon  


# to pass the icon according to the weather report
def placeicon(weather):
    if weather == "Rain":
        seticon('images/rainy.png')
    elif weather == 'Snow' :
        seticon('images/snowy.png')
    elif weather == "Clouds":
        seticon('images/cloudy.png')
    elif weather == 'Fog':
        seticon('images/foggy.png')
    elif weather == 'Storm':
        seticon('images/stormy.png')
    elif weather == 'Haze':
        seticon('images/haze.png')
    else:
        seticon('images/sunny.jpg')

# updating weather info
def UpdateScreen(humidity,pressure,description,visibility,feel,weather,temparature):

    temp_out.config(text=f'{temparature}℃')
    feel_out.config(text=f'Feels like {feel}° | {weather} ')


    humidity_output.config(text=f'{humidity}%')
    pressure_output.config(text=f'{pressure} mBar')
    description_output.config(text=f'{description}')
    visibility_output.config(text=f'{visibility} km')


# http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WeatherAPI}&units=metric

# fetch weather info from openweathermap api 
def weather(city) -> str :
    global temparature
    # for beautifying
    location_output.config(text=city.capitalize())

    data = get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WeatherAPI}&units=metric',headers=header)   # requests.get()
    
    if data.status_code == 200:
        weather = data.json()['weather'][0]['main']
        temparature = data.json()['main']['temp']
        feel = data.json()['main']['feels_like']
        
        # bottom info
        humidity = data.json()['main']['humidity'] # %
        pressure = data.json()['main']['pressure']  # mBar
        description = data.json()['weather'][0]['description'] 
        visibility = int(data.json()['visibility'])/1000  # km

        # for calculating time
        lon = data.json()['coord']['lon']
        lat = data.json()['coord']['lat']

        # updating screen
        dateandtime(lat,lon)
        UpdateScreen(humidity,pressure,description,visibility,feel,weather,temparature)
        placeicon(str(weather))

    
    elif data.json()['cod'] == '404':
        clear()
        messagebox.showerror("Error", "No Country/City Found!")
    else:
        clear()
        messagebox.showerror("Error", "Check the Internet Connection!")


# converts (C -> F) or (F -> C) [using formula]
def UnitConversion(temparature):
    global UNIT
    global fahrenheit

    if UNIT == 'celsius':
        UNIT = 'fahrenheit' # changing the unit
        fahrenheit = (int(temparature) *9/5)+32
        temp_out.config(text=f'{fahrenheit} F')

    else:
        UNIT = 'celsius'  # changing the unit
        celsius = (fahrenheit - 32) * 5/9
        temp_out.config(text=f'{celsius} ℃')



# to clear the screen
def clear():
    city.delete(0,tkinter.END)
    location_output.config(text='')
    date_output.config(text='')
    time_output.config(text='')
    humidity_output.config(text='')
    pressure_output.config(text='')
    description_output.config(text='')
    visibility_output.config(text='')
    seticon('images/default.png')
    temp_out.config(text='')
    feel_out.config(text='')


# main()
if __name__ == '__main__':
    
    screen = tkinter.Tk()
    screen.title('Weather App')
    screen.geometry("500x500")
    screen.resizable(0,0)  # can't resize
    screen.configure(background=COLOR)


    # <--- widgets --->

    # label
    city = tkinter.Entry(screen)
    city.place(x=10,y=10)

    #search button
    searchicon = Image.open(r"images/search.png")
    resize_searchicon = searchicon.resize((20,15))
    final_searchicon = ImageTk.PhotoImage(resize_searchicon)
    search_button = tkinter.Button(image=final_searchicon,command=lambda: weather(city.get()))   # passing args
    search_button.place(x=160,y=10)


    # default img
    seticon('images/default.png') # 20,100


    # temparature
    temp_out = tkinter.Label(screen,text='',background=COLOR,font=('monospace', 20))
    temp_out.place(x=250,y=200)

    # feels like
    feel_out = tkinter.Label(screen,text='',background=COLOR,font=('monospace', 12))
    feel_out.place(x=250,y=250)

    # < --- Outputs --->

    tkinter.Label(screen,text='Location: ',background=COLOR,font=('monospace', 12)).place(x=320,y=10)
    tkinter.Label(screen,text='Date: ',background=COLOR,font=('monospace', 12)).place(x=350,y=30)
    tkinter.Label(screen,text='Time: ',background=COLOR,font=('monospace', 12)).place(x=350,y=50)


    location_output = tkinter.Label(screen,text='',background=COLOR,font=('monospace', 12))
    location_output.place(x=400,y=10)

    date_output = tkinter.Label(screen,text='',background=COLOR,font=('monospace', 12))
    date_output.place(x=400,y=30)

    time_output = tkinter.Label(screen,text='',background=COLOR,font=('monospace', 12))
    time_output.place(x=400,y=50)


    # bottom output
    tkinter.Label(screen,text='Humidity',background=COLOR,font=('monospace', 12)).place(x=10,y=350)
    humidity_output = tkinter.Label(screen,text='',background=COLOR,font=('monospace', 12))
    humidity_output.place(x=10,y=380)

    tkinter.Label(screen,text='Pressure',background=COLOR,font=('monospace', 12)).place(x=100,y=350)
    pressure_output = tkinter.Label(screen,text='',background=COLOR,font=('monospace', 12))
    pressure_output.place(x=100,y=380)

    tkinter.Label(screen,text='Description',background=COLOR,font=('monospace', 12)).place(x=190,y=350)
    description_output = tkinter.Label(screen,text='',background=COLOR,font=('monospace', 12))
    description_output.place(x=190,y=380)

    tkinter.Label(screen,text='Visibility',background=COLOR,font=('monospace', 12)).place(x=310,y=350)
    visibility_output = tkinter.Label(screen,text='',background=COLOR,font=('monospace', 12))
    visibility_output.place(x=330,y=380)




    # < --- Buttons ---> 

    # clear button
    clearbutton = tkinter.Button(screen,text='Clear',activeforeground='red',activebackground='black',bd=3,font='monospace',command=clear).place(x=300,y=465)
    # convert unit
    convert_unit = tkinter.Button(screen,text='Change-Unit',activeforeground='red',activebackground='black',bd=3,font='monospace',command=lambda: UnitConversion(temparature)).place(x=375,y=465) 


    # to keep on runnig the screen
    screen.mainloop()