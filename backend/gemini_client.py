from google import genai
import os
from dotenv import load_dotenv
from config import FILE_NAME

BASE_DIR = load_dotenv(FILE_NAME)
GEMINI_API_KEY = os.getenv("API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "API_KEY не найден в .env"
    )
client = genai.Client(api_key=GEMINI_API_KEY)

def get_answer_from_gemini(prompt: str):
    try:
        interaction = client.interactions.create(
            model="gemini-3.6-flash",
            input=prompt
        )
        return interaction.output_text
    except Exception as e:
        print(e)

        return (
            "Произошла ошибка при обращении к Gemini."
        )

