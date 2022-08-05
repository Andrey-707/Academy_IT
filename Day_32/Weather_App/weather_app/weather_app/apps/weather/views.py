import requests as rq

from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import City
from .forms import CityForm
from .config import appid
from rich import print


"""
OpenWeather

Call current weather data

read there: https://openweathermap.org/current

How to make an API call:
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
"""

# Create your views here.

# def index(request):
#     """
#     Two simple queries.
#     """
#     # return HttpResponse('<h1>Hello world!</h1>')
#     return render(request, 'weather/index.html') # first need to create file index.html


# def index(request):
#     """
#     Simple query using lib requests.
#     """
#     my_city = 'Moscow' # input('my_city: ')
#     url = f'https://api.openweathermap.org/data/2.5/weather?q={my_city}&units=metric&appid={appid}'

#     result = rq.get(url).text
#     print(result)
#     print(type(result))

#     # HARD CODE =(
#     txt_1 = 'In {} temperature is {} '.format(
#         my_city,
#         result[result.find('"temp"') + 7:result.find('"temp"') + 12]
#     )

#     result = rq.get(url).json()
#     print(result)
#     print(type(result))

#     # some better =)
#     txt_2 = 'In {} temperature is {} '.format(result['name'], result['main']['temp'])

#     return HttpResponse(f'<h1>{txt_1}<sup>0</sup>C<br>{txt_2}<sup>0</sup>C</h1>')


def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = rq.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': res['main']['temp'],
            'icon': res['weather'][0]['icon']
        }

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)


def info(request):
    return render(request, 'weather/info.html')
