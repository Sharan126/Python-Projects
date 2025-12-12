# Rule based AI Chatbot

import datetime
import time

name = input("Enter your name: ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning!", name)
if 11 <= presentHour <= 17: 
    print("Good Afternoon!", name)
if 17 <= presentHour <= 20:
    print("Good Evening!", name)
else:
    print("Good Night!", name)           

print("Welcome to your buddy chatbot!") 
print("You can ask me a basic question. Type 'exit' to end the conversation.")

# Chatbot memory (dictionary of responses)

responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! 😊",
    "good morning": "Good morning! Hope you have a wonderful day!",
    "good night": "Good night! Sleep well 😴",
    "how are you?": "I'm just a bunch of code, but thanks for asking!",
    "what is your name?": "I'm your friendly chatbot buddy!",
    "who made you?": "I was created by my developer — and now I'm here to chat with you!",
    "how old are you?": "I'm timeless… I live inside your code!",
    "what can you do?": "I can chat with you and answer basic questions.",
    "what is python?": "Python is a popular programming language known for its simplicity.",
    "help": "Sure! Ask me anything. I'm here to help!",
    "tell me a joke": "Why did the computer go to the doctor? Because it had a virus!",
    "i am bored": "Let’s fix that! Want to hear a joke or fun fact?",
    "tell me a fun fact": "Did you know? Honey never spoils. Archaeologists found 3000-year-old honey still edible!",
    "bye": "Bye! Take care 😊",
    "exit": "Goodbye! Have a great day!"
}

# Function to get bot response

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I'm sorry, I don't understand that question."

# Chat loop

while True:
    userInput = input("Please ask your question: ")  # FIXED: input() was missing
    reply = getResponseOfBot(userInput)
    print("Bot Response:", reply)

    if userInput.lower() == "exit":   # FIXED: proper exit condition
        break