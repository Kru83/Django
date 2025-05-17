import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

def gramllm(genre, note):
    genai.configure(api_key= os.getenv("GEMINI_AI_KEY"))
    model = genai.GenerativeModel('gemini-2.0-flash')

    userInput = (F"You as a person specialized in {genre} literature. "
                 F"here is the note: '{note}'. "
                 "Transform this note into how it would be written in that genre. "
                 "Please respond back with just the transformed phrase."
                 "Do not include any options, explanations, bullet points, or analysis."
                 "Just return the rewritten passage as a single paragraph — nothing else.")
    response = model.generate_content(userInput)
    return response.text