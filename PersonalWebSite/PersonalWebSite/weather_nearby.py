import  requests

def ipAddress():
    ipAddressData = None
    ipAddressRequest = "http://www.geoplugin.net/json.gp"
    ipAddressResponse = requests.get(ipAddressRequest)
    ipAddressStatus = ipAddressResponse.status_code

    if ipAddressStatus == 200:
        ipAddressData = ipAddressResponse.json()
    else:
        print(F"Error {ipAddressStatus}")
    return ipAddressData
'''
latitude = ipAddressData["geoplugin_latitude"]
longitude = ipAddressData["geoplugin_longitude"]

#calling the weatherData functions to store all weather data into dic from the API.
weatherData = WeatherData(latitude, longitude,)

#extract City and State from weatherData functions
city = weatherData["properties"]["relativeLocation"]["properties"]["city"]
state = weatherData["properties"]["relativeLocation"]["properties"]["state"]

# This section uses the forecastRequest end point from free weather API to get actual forecast
foreCastRequest = weatherData["properties"]["forecast"]

foreCastData = ForeCastData(foreCastRequest)


# temp and temp unit are captured from index values of 0, it's defined as This Afternoon, you can go index, 1, 2, and other for tonight and next day on and on
temperature = foreCastData["properties"]["periods"][0]["temperature"]
temperatureUnit = foreCastData["properties"]["periods"][0]["temperatureUnit"]
detailedForecast = foreCastData["properties"]["periods"][0]["detailedForecast"]
foreCastTime = foreCastData["properties"]["periods"][0]["name"]
'''