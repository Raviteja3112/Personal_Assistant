import requests
import Speak as s
import requests
import os

api_key=os.environ['weather_api_key']

def home_weather():
    weather,cel=weather_requests('Mangalagiri') 
    weather=weather.lower()
    if(weather=='clear'):
        s.speak("Outside is very clear")
    elif(weather=='rain'):
        s.speak("It is better to wear rain coat")
    elif(weather=='cloud'):
        s.speak("It may rain sir")
    else:
        cel=int(cel)
        if(cel>=30):
            s.speak("Its too hot outside don't go, and more over its corona")
        else:
            s.speak(f"Weather is ok with {cel} degrees, but it's corona time, better not go outside")
        


def weather_requests(city):
    address='http://api.openweathermap.org/data/2.5/weather?appid='+api_key+'&q='
    url=address+city
    get=requests.get(url).json()
    if(get['cod']=='404'):
        s.speak(f"Invalid city of {city} please tel again")
    else:
        name=get['name']
        lon=get['coord']['lon']
        lat=get['coord']['lat']
        weather=get['weather'] [0] ['main']#tells detail weather of description
        temp=get['main']['temp']
        cel=int(temp-273.15)
        press=get['main']['pressure']
        hum=get['main']['humidity']
        wind=get['wind']['speed']
            
        s.speak('sir, city ' + name)
        s.speak('longitude of city is ' +str(lon) )
        s.speak('latitude of city is ' +str(lat))
        s.speak('weather is ' +weather)
        s.speak('temparature of  city is ' + str(cel)+'celcius')
        s.speak('pressure of city is ' + str(press) +'hpa')
        s.speak('humidity is '+str(hum)+'%')
        s.speak('wind speed is '+str(wind))

    return weather,cel

if __name__=="__main__":
    s.speak("Now its time to your location weather")
    home_weather()