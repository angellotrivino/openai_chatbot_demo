import openai
import requests
import os

# Get the API keys from the environment variables
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
TELEGRAM_API_KEY = os.environ.get("TELEGRAM_API_KEY")

# Set the API keys
openai.api_key = OPENAI_API_KEY
TOKEN = TELEGRAM_API_KEY

# Define the functions
def get_updates(offset):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()["result"]

# Send messages to the chat
def send_messages(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, params=params)
    return response

# Get the response from OpenAI
def get_openai_response(prompt):
    response = openai.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
        {"role": "system", "content" :"Eres un asistente que da información de Anuncios Publicitarios."},
        {"role": "user", "content" : str(prompt)}
        ],
        max_tokens = 150,
        top_p=1,
        temperature = 0.2,
        stop = " END"
    )
    return response.choices[0].message.content.strip()
