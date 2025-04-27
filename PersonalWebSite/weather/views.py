from django.shortcuts import render
from weather.weather_nearby import *
from weather.weather_zipcode import *

# Create your views here.

def weather(request):
    weatherDataContext = {}
    if request.POST.get('form_type') == 'zip':
        userCountryCode = "US"
        zipCode = request.POST.get('zipCode')

        latitude, longitude, zipCode, countryCode = GeoLocation(zipCode, userCountryCode)

        weatherData = WeatherData(latitude, longitude)

        city = weatherData["properties"]["relativeLocation"]["properties"]["city"]
        state = weatherData["properties"]["relativeLocation"]["properties"]["state"]

        foreCastRequest = weatherData["properties"]["forecast"]

        foreCastData = ForeCastData(foreCastRequest)

        temperature = foreCastData["properties"]["periods"][0]["temperature"]
        temperatureUnit = foreCastData["properties"]["periods"][0]["temperatureUnit"]
        detailedForecast = foreCastData["properties"]["periods"][0]["detailedForecast"]
        foreCastTime = foreCastData["properties"]["periods"][0]["name"]

        weatherDataContext = {
            'city': city,
            'state': state,
            'temperature': temperature,
            'temperatureUnit': temperatureUnit,
            'detailedForecast': detailedForecast,
            'foreCastTime': foreCastTime
        }
    elif request.POST.get('form_type') == 'nearby':
        ipAddressData = ipAddress()

        latitude = ipAddressData["geoplugin_latitude"]
        longitude = ipAddressData["geoplugin_longitude"]

        weatherData = WeatherData(latitude, longitude)

        city = weatherData["properties"]["relativeLocation"]["properties"]["city"]
        state = weatherData["properties"]["relativeLocation"]["properties"]["state"]

        foreCastRequest = weatherData["properties"]["forecast"]

        foreCastData = ForeCastData(foreCastRequest)

        temperature = foreCastData["properties"]["periods"][0]["temperature"]
        temperatureUnit = foreCastData["properties"]["periods"][0]["temperatureUnit"]
        detailedForecast = foreCastData["properties"]["periods"][0]["detailedForecast"]
        foreCastTime = foreCastData["properties"]["periods"][0]["name"]

        weatherDataContext = {
            'city': city,
            'state': state,
            'temperature': temperature,
            'temperatureUnit': temperatureUnit,
            'detailedForecast': detailedForecast,
            'foreCastTime': foreCastTime
        }

    return render(request, 'Weather/weather.html', weatherDataContext)