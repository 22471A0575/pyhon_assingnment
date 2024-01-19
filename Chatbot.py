import nltk
from nltk.chat.util import Chat, reflections
patterns=[
    (r'hello|hi|hey',['Hi there!','Hello!','Hey!']),
    (r'how are you',["I'm just a computer program, but I'm doing well. Thanks!"]),
    (r'bye|goodbye',['Goodbye! Have a great day.', 'See you later!'])]
chatbot=Chat(patterns,reflections)
print("Bot: Hi! Type 'bye' to exit.")
while True:
    user_input=input("You: ")
    if user_input.lower()=='bye':
        print("Bot: Goodbye!")
        break
    response=chatbot.respond(user_input)
    print("Bot:",response)
