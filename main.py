import functions
welcome = "Welcome to the Python Weather application"

userZipCode = input("Please enter valid 5 digit local zipcode: ")

latitude, longitude, userZipCode = functions.GeoLocation(userZipCode)

#calling the weatherData fuctions to store all weather data into dic from the API.
weatherData = functions.WeatherData(latitude, longitude)

#extract City and State from weatherData Fucntion
city = weatherData["properties"]["relativeLocation"]["properties"]["city"]
state = weatherData["properties"]["relativeLocation"]["properties"]["state"]

# This section uses the forecastRequest end point from free weather API to get actual forecast
foreCastRequest = weatherData["properties"]["forecast"]

foreCastData = functions.ForeCastData(foreCastRequest)

# temp and tempunit are captured from index values of 0, it's defined as This Afternoon, you can go index, 1, 2, and other for tonight and next day on and on
temperature = foreCastData["properties"]["periods"][0]["temperature"]
temperatureUnit = foreCastData["properties"]["periods"][0]["temperatureUnit"]
detailedForecast = foreCastData["properties"]["periods"][0]["detailedForecast"]

# print all the info from above
print (f"{welcome}")
print (f"{city},{state}")
print (f"{userZipCode}")
print (f"{temperature} {temperatureUnit}")
print (f"{detailedForecast}")