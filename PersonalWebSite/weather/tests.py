from django.test import TestCase
import requests
# Create your tests here.

key = "Fu5mqpximlSEDp6LZOcCcVktlalCMe5wcHbAef6T"
url = "https://api.congress.gov/v3/member?api_key="

keyURL = url + key

dataRequest = requests.get(keyURL)

data = dataRequest.json()

print(data)
print(keyURL)