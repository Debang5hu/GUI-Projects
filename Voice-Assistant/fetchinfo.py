#!/usr/bin/python3

# _*_ coding: utf-8 _*_


import requests
import wikipedia # type: ignore


WeatherAPI = 'b145926e1363addf8db5a988dad9ef4a'
NewsAPI = '4dbc17e007ab436fb66416009dfb59a8'


# fetch weather info from openweathermap api 
def weather(city='kolkata') -> str :
    data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WeatherAPI}&units=metric')
    
    if data.status_code == 200:
        #weather = data.json()['weather'][0]['main']
        temparature = data.json()['main']['temp']
        feel = data.json()['main']['feels_like']
        humidity = data.json()['main']['humidity']

        return f'Today\'s temparature is {temparature} degree celsius but feels like {round(feel)} degree celsius , with a humidity of {round(humidity)}'
    
    elif data.json()['cod'] == 404:
        return f'no city found'
    else:
        return f'say it again'



# fetch information from wikipedia
def info(text) -> str:
    try:
        info = wikipedia.summary(text,sentences=1)
        print(info)    
        return info
    except:
        return 'tell me more precisely'



# fetch top headlines from newsapi
def headlines() -> list :    
    query_params = {"source": "bbc-news","sortBy": "top","apiKey": NewsAPI}   # to fix

    try:
        response = requests.get('https://newsapi.org/v1/articles', params=query_params)
        response.raise_for_status()  # Raises a HTTPError for bad responses
        data = response.json()
        
        articles = data.get("articles", [])[:5]  # Get only the first 5 articles

        headline = [article["title"] for article in articles if "title" in article]

        return headline

    except requests.RequestException as e:
        return ['cannot fetch and news']

#print(weather())