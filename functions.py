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
    if weatherStatusCode == 200:
        weatherData = weatherResponse.json()
        return weatherData
    else:
        print(F"Error {weatherStatusCode}")

#Take the forecast end point from WeatherData use it in this function
def ForeCastData (foreCastRequest):
    foreCastResponse = requests.get(F"{foreCastRequest}")
    forecastData = foreCastResponse.json()
    return forecastData

#allow user input to be 5 digit only, no alpha

def userZipCodeInput():
    while True:
        userZipCode = input("Please enter valid 5 digit local zipcode: ") 
        if userZipCode.isdigit() and len(userZipCode) == 5:
            return userZipCode
        else:
            print("Please enter a valid 5 digit zip code")