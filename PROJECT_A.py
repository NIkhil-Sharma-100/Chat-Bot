# Ai - Chat Bot

import random

responses =  {
    "hi":["Hello","Hey There","Hi! How are you"],
    "bye":["Goood Bye","Okay Bye","Great! See oyu later"],
    "how are you":["Doing Great! Thanks","I am fine. You?"]
}


while True:
    user_input = input("You : ").lower()
    if user_input in responses:
        print("Bot : ",random.choice(responses[user_input]))

    elif user_input == "exit":
        print("Bot : Turning off bot ")
        break
    else:
        print("Bot : Sorry I don't know that yet ")
