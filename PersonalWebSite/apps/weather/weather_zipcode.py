import requests
import pgeocode

def geoLocation(userZipCode, UserCountryCode):
    nomi = pgeocode.Nominatim(UserCountryCode)
    geoLocationData = (nomi.query_postal_code(userZipCode))
    latitude = geoLocationData["latitude"]
    longitude = geoLocationData["longitude"]
    zipCode = geoLocationData["postal_code"]
    countryCode = geoLocationData["country_code"]
    return latitude, longitude, zipCode, countryCode

# We are taking the lati and Longi response from above and getting weather data.
def weather(latitude, longitude):
    base_url = "https://api.weather.gov/points"
    headers = {
        "User-Agent": "www.kru.dev/1.0 (kru1983@gmail.com)",
        "From": "kru1983@gmail.com"
    }

    try:
        response = requests.get(f"{base_url}/{latitude},{longitude}", headers=headers)
        response.raise_for_status()  # Raises exception for non-2xx responses
        weatherData = response.json()
        return weatherData
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

#Take the forecast end point from WeatherData use it in this function
def foreCast(forecast_url):
    headers = {
        "User-Agent": "www.kru.dev/1.0 (kru1983@gmail.com)",
        "From": "kru1983@gmail.com"
    }

    try:
        response = requests.get(forecast_url, headers=headers)
        response.raise_for_status()  # Raises an exception for HTTP errors
        forecastData = response.json()
        return forecastData
    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return None


import requests


def get_hourly_forecast(latitude, longitude):
    # Define the endpoint for hourly forecast based on latitude and longitude
    hourly_forecast_url = f"https://api.weather.gov/gridpoints/TOP/{latitude},{longitude}/forecast/hourly"

    headers = {
        "User-Agent": "www.kru.dev/1.0 (kru1983@gmail.com)",
        "From": "kru1983@gmail.com"
    }

    try:
        # Make the request to the Weather API
        response = requests.get(hourly_forecast_url, headers=headers)
        response.raise_for_status()  # Check for successful response

        # Return the entire JSON response as hourlyForecast
        hourlyForecast = response.json()

        return hourlyForecast  # Return the full JSON data for hourly forecast

    except requests.exceptions.RequestException as e:
        # Handle exceptions (e.g., network issues, invalid response)
        print(f"Error fetching hourly forecast: {e}")
        return None


#allow user input to be 5 digit only, no alpha

def userZipCodeInput():
    while True:
        userZipCode = input("Please enter valid 5 digit local zipcode: ")
        if userZipCode.isdigit() and len(userZipCode) == 5:
            return userZipCode
        else:
            print("Please enter a valid 5 digit zip code")