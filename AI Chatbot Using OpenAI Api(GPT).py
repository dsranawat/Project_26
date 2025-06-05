'''
  - Before running the code generate a Api Key form  "https://platform.openai.com/account/api-keys"
  - Copy the generated key and Save it into  .env file with no filename just .env
  - in .env file - save it in the manner OPENAI_API_KEY= paste_key_here 
'''
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages =[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"
    
def run_chatbot():
    print("Bot (GPT): Hello! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        reply = ask_openai(user_input)
        print("Bot:", reply)

if __name__ == "__main__":
    run_chatbot()