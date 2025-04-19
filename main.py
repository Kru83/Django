import requests
import pgeocode
import pandas as pd
welcome = "Welcome to the Python Weather application"

# Get Long and Lati using zipCode
# pgeocode is used for this module.
# result of look based on zip code panda df.
# to see full data frame use print(geoLocationData)

zipcode = 32259
nomi = pgeocode.Nominatim("us")
geoLocationData = (nomi.query_postal_code(zipcode))

latitude = geoLocationData["latitude"]
longitude = geoLocationData["longitude"]

#This section below uses free weather API to get foreCastRequest API based on logi and lati
weatherRequest = "https://api.weather.gov/points/"
weatherResponse = requests.get(F"{weatherRequest}{latitude},{longitude}")

weatherStatusCode = (weatherResponse.status_code)
weatherData = weatherResponse.json()

# City, and state is defined from weather API
city = weatherData["properties"]["relativeLocation"]["properties"]["city"]
state = weatherData["properties"]["relativeLocation"]["properties"]["state"]

# This section uses the forecastRequest end point from free weather API to get actual forecast
foreCastRequest = weatherData["properties"]["forecast"]
foreCastResponse = requests.get(F"{foreCastRequest}")
foreCastData = foreCastResponse.json()

# temp and tempunit are captured from index values of 0, it's defined as This Afternoon, you can go index, 1, 2, and other for tonight and next day on and on
temperature = foreCastData["properties"]["periods"][0]["temperature"]
temperatureUnit = foreCastData["properties"]["periods"][0]["temperatureUnit"]
detailedForecast = foreCastData["properties"]["periods"][0]["detailedForecast"]

# print all the info from above
print (f"{welcome}")
print (f"{city},{state}")
print (f"{zipcode}")
print (f"{temperature} {temperatureUnit}")
print (f"{detailedForecast}")


####Let's create a weather app to display weather data
##1 Start with Static Data
##2 fetch the data from weather API using hard coded longititude and lotitude
##3 find a way to convert zip codes into latitiude and longitude
###4 format display
#### Convert this into html site and 

#API to use http://www.geoplugin.net/json.gp
#API to use https://www.weather.gov/documentation/services-web-api