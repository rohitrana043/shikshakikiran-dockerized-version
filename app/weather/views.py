from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):

    url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&appid=05198d72bc37e38dca43536db6932600'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    Cities = City.objects.all()

    weather_data = []
    if(Cities):
        for city in Cities:

            r = requests.get(url.format(city)).json()

            city_weather = {
                'city' : city.name,
                'temperature' : r['list'][2]['main']['temp'],
                'description' : r['list'][2]['weather'][0]['description'],
                'icon' : r['list'][2]['weather'][0]['icon'],
                'pressure': r['list'][2]['main']['pressure'],
                'date': r['list'][2]['dt_txt'],
                'wind': r['list'][2]['wind']['speed'],
                'humidity': r['list'][2]['main']['humidity'],
                'cloud': r['list'][2]['clouds']['all'],
                'max': r['list'][2]['main']['temp_max'],

                'city1' : city.name,
                'temperature1' : r['list'][6]['main']['temp'],
                'description1' : r['list'][6]['weather'][0]['description'],
                'icon1' : r['list'][6]['weather'][0]['icon'],
                'pressure1': r['list'][6]['main']['pressure'],
                'date1': r['list'][6]['dt_txt'],
                'wind1': r['list'][6]['wind']['speed'],
                'humidity1': r['list'][6]['main']['humidity'],
                'cloud1': r['list'][6]['clouds']['all'],
                'max1': r['list'][6]['main']['temp_max'],

                'city12' : city.name,
                'temperature12' : r['list'][13]['main']['temp'],
                'description12' : r['list'][13]['weather'][0]['description'],
                'icon12' : r['list'][13]['weather'][0]['icon'],
                'pressure12': r['list'][13]['main']['pressure'],
                'date12': r['list'][13]['dt_txt'],
                'wind12': r['list'][13]['wind']['speed'],
                'humidity12': r['list'][13]['main']['humidity'],
                'cloud12': r['list'][13]['clouds']['all'],
                'max12': r['list'][13]['main']['temp_max'],

                'city18' : city.name,
                'temperature18' : r['list'][21]['main']['temp'],
                'description18' : r['list'][21]['weather'][0]['description'],
                'icon18' : r['list'][21]['weather'][0]['icon'],
                'pressure18': r['list'][21]['main']['pressure'],
                'date18': r['list'][21]['dt_txt'],
                'wind18': r['list'][21]['wind']['speed'],
                'humidity18': r['list'][21]['main']['humidity'],
                'cloud18': r['list'][21]['clouds']['all'],
                'max18': r['list'][21]['main']['temp_max'],

                'city24' : city.name,
                'temperature24' : r['list'][30]['main']['temp'],
                'description24' : r['list'][30]['weather'][0]['description'],
                'icon24' : r['list'][30]['weather'][0]['icon'],
                'pressure24': r['list'][30]['main']['pressure'],
                'date24': r['list'][30]['dt_txt'],
                'wind24': r['list'][30]['wind']['speed'],
                'humidity24': r['list'][30]['main']['humidity'],
                'cloud24': r['list'][30]['clouds']['all'],
                'max24': r['list'][30]['main']['temp_max'],

                

                'city36' : city.name,
                'temperature36' : r['list'][36]['main']['temp'],
                'description36' : r['list'][36]['weather'][0]['description'],
                'icon36' : r['list'][36]['weather'][0]['icon'],
                'pressure36': r['list'][36]['main']['pressure'],
                'date36': r['list'][36]['dt_txt'],
                'wind36': r['list'][36]['wind']['speed'],
                'humidity36': r['list'][36]['main']['humidity'],
                'cloud36': r['list'][36]['clouds']['all'],
                'max36': r['list'][36]['main']['temp_max'],

            }

            weather_data.append(city_weather)

    context={
    'weather_data': weather_data, 
    'form': form,
    'city_weather': city_weather
    }
    return render(request, 'weather/weather.html', context)