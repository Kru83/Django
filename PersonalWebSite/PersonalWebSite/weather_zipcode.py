import requests
import pgeocode

def GeoLocation(userZipCode, UserCountryCode):
    nomi = pgeocode.Nominatim(UserCountryCode)
    geoLocationData = (nomi.query_postal_code(userZipCode))
    latitude = geoLocationData["latitude"]
    longitude = geoLocationData["longitude"]
    zipCode = geoLocationData["postal_code"]
    countryCode = geoLocationData["country_code"]
    return latitude, longitude, zipCode, countryCode

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