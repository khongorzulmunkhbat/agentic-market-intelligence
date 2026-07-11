import os
from google import genai
from google.genai import types
from pydantic import BaseModel

class LLMClient:
    def __init__(self):
        # Assumes GEMINI_API_KEY is in environment or .env
        self.client = genai.Client()
        self.model_name = "gemini-3.5-flash"

    def generate_structured(self, prompt: str, response_schema: type[BaseModel]) -> BaseModel:
        """
        Generates a structured response based on a Pydantic schema.
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=response_schema,
                temperature=0.2
            )
        )
        return response_schema.model_validate_json(response.text)

    def generate_text(self, prompt: str, temperature: float = 0.5) -> str:
        """
        Generates standard text response.
        """
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=temperature
            )
        )
        return response.text
