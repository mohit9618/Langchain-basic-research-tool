import logging
logging.disable(logging.WARNING)

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.7-flash')

chat_history = []

while True:
    user_input = input('You: ')
    chat_history.append(("human", user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(("ai", result.content))
    print("AI: ",result.content[0]['text'])

print(chat_history)