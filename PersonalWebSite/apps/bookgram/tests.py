from django.test import TestCase
import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

# Create your tests here.
genai.configure(api_key= os.getenv("GEMINI_AI_KEY"))
genre = "mystery"
note = "Hey, What time do we need to take Niam to school for his soccer? "

model = genai.GenerativeModel('gemini-2.0-flash')

userInput = (F"You as a person specialized in {genre} literature."
             F"{note}"
             "Take this note and transform this into how would it be written in that genre of book."
             "Please respond back with just transformed phase, nothing else ")
response = model.generate_content(userInput)
print(response.text)