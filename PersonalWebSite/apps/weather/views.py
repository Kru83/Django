from django.shortcuts import render
from datetime import datetime

from apps.weather.weather_nearby import *
from apps.weather.weather_zipcode import *

def weatherView(request):
    weatherDataContext = {}

    if request.POST.get('form_type') == 'zip':
        userCountryCode = "US"
        zipCode = request.POST.get('zipCode')

        # Get latitude, longitude from the zip code
        latitude, longitude, zipCode, countryCode = geoLocation(zipCode, userCountryCode)
        weatherData = weather(latitude, longitude)

        city = weatherData["properties"]["relativeLocation"]["properties"]["city"]
        state = weatherData["properties"]["relativeLocation"]["properties"]["state"]

        # Get daily forecast
        daily_url = weatherData["properties"]["forecast"]
        foreCastData = foreCast(daily_url)
        dailyForecast = foreCastData["properties"]["periods"]

        # Get hourly forecast from forecastHourly URL
        hourly_url = weatherData["properties"]["forecastHourly"]
        hourly_data = foreCast(hourly_url)
        hourlyForecast = hourly_data["properties"]["periods"]

        # Format startTime and endTime for hourly forecast
        for hour in hourlyForecast:
            # Convert ISO 8601 to 12-hour format
            start_time = hour['startTime']
            end_time = hour['endTime']

            # Parse the ISO 8601 string and convert to 12-hour format with AM/PM
            hour['startTime'] = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S%z").strftime("%I:%M %p")
            hour['endTime'] = datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S%z").strftime("%I:%M %p")

        # Get the current date based on the first hourly forecast
        if hourlyForecast:
            first_hour = datetime.strptime(hourlyForecast[0]['startTime'], "%I:%M %p")
            hourly_date = first_hour.strftime("%A, %B %d, %Y")  # Format: Tuesday, April 29, 2025
        else:
            hourly_date = "N/A"

        forecast_list = []
        for period in dailyForecast:
            forecast_list.append({
                'name': period["name"],
                'temperature': period["temperature"],
                'temperatureUnit': period["temperatureUnit"],
                'shortForecast': period["shortForecast"],
                'detailedForecast': period["detailedForecast"],
                'precipitationProbability': period.get("precipitationProbability", "N/A"),
                'icon': period["icon"]
            })

        weatherDataContext = {
            'city': city,
            'state': state,
            'forecast': forecast_list,
            'hourlyForecast': hourlyForecast,
            'hourlyDate': hourly_date  # Pass the current date for hourly forecast
        }

    elif request.POST.get('form_type') == 'nearby':
        ipAddressData = ipAddress()

        latitude = ipAddressData["geoplugin_latitude"]
        longitude = ipAddressData["geoplugin_longitude"]
        weatherData = weather(latitude, longitude)

        city = weatherData["properties"]["relativeLocation"]["properties"]["city"]
        state = weatherData["properties"]["relativeLocation"]["properties"]["state"]

        # Get daily forecast
        daily_url = weatherData["properties"]["forecast"]
        foreCastData = foreCast(daily_url)
        dailyForecast = foreCastData["properties"]["periods"]

        # Get hourly forecast from forecastHourly URL
        hourly_url = weatherData["properties"]["forecastHourly"]
        hourly_data = foreCast(hourly_url)
        hourlyForecast = hourly_data["properties"]["periods"]

        # Format startTime and endTime for hourly forecast
        for hour in hourlyForecast:
            # Convert ISO 8601 to 12-hour format
            start_time = hour['startTime']
            end_time = hour['endTime']

            # Parse the ISO 8601 string and convert to 12-hour format with AM/PM
            hour['startTime'] = datetime.strptime(start_time, "%Y-%m-%dT%H:%M:%S%z").strftime("%I:%M %p")
            hour['endTime'] = datetime.strptime(end_time, "%Y-%m-%dT%H:%M:%S%z").strftime("%I:%M %p")

        # Get the current date based on the first hourly forecast
        if hourlyForecast:
            first_hour = datetime.strptime(hourlyForecast[0]['startTime'], "%I:%M %p")
            hourly_date = first_hour.strftime("%A, %B %d, %Y")  # Format: Tuesday, April 29, 2025
        else:
            hourly_date = "N/A"

        forecast_list = []
        for period in dailyForecast:
            forecast_list.append({
                'name': period["name"],
                'temperature': period["temperature"],
                'temperatureUnit': period["temperatureUnit"],
                'shortForecast': period["shortForecast"],
                'detailedForecast': period["detailedForecast"],
                'precipitationProbability': period.get("precipitationProbability", "N/A"),
                'icon': period["icon"]
            })

        weatherDataContext = {
            'city': city,
            'state': state,
            'forecast': forecast_list,
            'hourlyForecast': hourlyForecast,
            'hourlyDate': hourly_date  # Pass the current date for hourly forecast
        }

    return render(request, 'weather.html', weatherDataContext)