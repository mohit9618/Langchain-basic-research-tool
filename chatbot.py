import logging
logging.disable(logging.WARNING)

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage , AIMessage , SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.7-flash')

chat_history = [
    SystemMessage(content = 'You are a helpful aissistant.')

]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))
    print("AI: ",result.content[0]['text'])

print(chat_history.content[0]['text'])