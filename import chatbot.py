import chatbot 
import re
def simple_chatbot(user_input):
    
    rules = {
        r"(hi|hello|hey|greetings).*": "Hello! How can I help you?",
        r"what is your name": "I am a simple chatbot.",
        r"how are you": "I'm just a computer program, but thanks for asking!",
        r"bye|goodbye": "Goodbye! Have a great day.",
        r"([a-zA-Z]+)\s*\?\s*": "I'm sorry, I don't have the answer to that question.",
        r".*": "I'm not sure how to respond to that."
    }

    
    for pattern, response in rules.items():
        if re.match(pattern, user_input.lower()):
            return response


while True:
    user_input = input("You: ")
    
    
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    
   
    bot_response = simple_chatbot(user_input)
    
    
    print("Chatbot:", bot_response)
