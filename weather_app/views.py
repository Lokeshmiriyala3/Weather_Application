from django.shortcuts import render
import requests
import datetime

def index(request):
    api_key = open("D:\\Files\\django\\Weather\\current\\weather_project\\weather", "r").read()
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

    if request.method == 'POST':
        city1 = request.POST['city1']
        city2 = request.POST.get('city2', None)

        weather_data1 = fetch_weather_and_forecast(city1, api_key, current_weather_url)

        if city2:
            weather_data2= fetch_weather_and_forecast(city2, api_key, current_weather_url)
        else:
            weather_data2 = None

        context = {
            'weather_data1': weather_data1,
           
            'weather_data2': weather_data2,
            
        }

        return render(request, 'weather_app/index.html', context)
    else:
        return render(request, 'weather_app/index.html')


def fetch_weather_and_forecast(city, api_key, current_weather_url):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    lat, lon = response['coord']['lat'], response['coord']['lon']
   

    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15, 2),
        'description': response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
    }

   

    return weather_data