from google import genai
import os

class ResponseGenerator:
    MODEL_NAME = 'gemini-2.0-flash'

    def __init__(self):
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def generate_response(self, prompt):
        response = self.client.models.generate_content(model=self.MODEL_NAME, contents=prompt)
        return response.text
