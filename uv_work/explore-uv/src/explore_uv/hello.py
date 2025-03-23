from litellm import completion
from dotenv import load_dotenv
load_dotenv()
import os 

api_key = os.getenv('GOOGLE_API_KEY')

def greet():
    response = completion(
        api_key = api_key,
        model = 'gemini/gemini-2.0-flash-exp',
        messages = [{'role':'user', 'content':'what is mudaraba and musharaka?'}]
    )
    print(response['choices'][0]['message']['content'])
