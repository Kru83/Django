import pgeocode
import requests

# User provides zip code, and we return the original zip code, along with latitude and longitude from pgeocode.  The data it self is in panda df. 
# to see full data frame use print(geoLocationData)

def GeoLocation(userZipCode):
    nomi = pgeocode.Nominatim("us")
    geoLocationData = (nomi.query_postal_code(userZipCode))
    latitude = geoLocationData["latitude"]
    longitude = geoLocationData["longitude"]
    userZipCode = userZipCode

    return latitude, longitude, userZipCode

# We are taking the lati and Longi response from above and getting weather data.

def WeatherData (latitude, longitude):
    weatherRequest = "https://api.weather.gov/points/"
    weatherResponse = requests.get(F"{weatherRequest}{latitude},{longitude}")
    weatherStatusCode = (weatherResponse.status_code)
    weatherData = weatherResponse.json()
    return weatherData

#Take the forecast end point from WeatherData use it in this function
def ForeCastData (foreCastRequest):
    foreCastResponse = requests.get(F"{foreCastRequest}")
    forecastData = foreCastResponse.json()
    return forecastData