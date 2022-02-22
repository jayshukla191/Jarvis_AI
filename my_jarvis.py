import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
time.clock = time.time

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def make_a_chatbot():
    os.listdir("C:\\Users\\Aishwary\\Desktop\\Python\\chatterbot-corpus-master\\chatterbot-corpus-master\\chatterbot_corpus\\data")
    kgp = ChatBot('Jarvis')
    trainer = ListTrainer(kgp)

    for f in os.listdir('C:\\Users\\Aishwary\\Desktop\\Python\\chatterbot-corpus-master\\chatterbot-corpus-master\\chatterbot_corpus\\data\\english'):
        data = open('C:\\Users\\Aishwary\\Desktop\\Python\\chatterbot-corpus-master\\chatterbot-corpus-master\\chatterbot_corpus\\data\\english\\' + f).readlines()
        trainer.train(data)

    return kgp

talk("I am Jarvis. What can i do for you?")

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
              command = command.replace('jarvis', '')
              return command
            else:
              return ''
    except:
        print("error occurred")

def talk_to_me():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            return command
    except:
        print("error occurred")

def run_jarvis():
    command = take_command()
    if 'play' in command:
        video = command.replace('play', '')
        talk('playing' + video)
        pywhatkit.playonyt(video)
        return False
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        talk('Current time is' + time)
        return False
    elif 'search' in command:
        command = command.replace('search', '')
        talk('Searching' + command)
        pywhatkit.search(command)
        return False
    elif 'tell me about' in command:
        command = command.replace('tell me about', '')
        info = wikipedia.summary(command, 1)
        print(info)
        talk(info)
        return False
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        return False
    elif 'message' in command:
        command = command.replace('message', '')
        if 'to my personal group' in command:
            text = command.replace('to my personal group', '')
            text = text.strip()
            pywhatkit.sendwhatmsg_to_group("HtSv1S05KUOChpyGIG2c9d", text, datetime.datetime.now().hour, datetime.datetime.now().minute+1)
        return False
    elif 'hello' in command:
        kgp = make_a_chatbot()
        print("who are you?")
        reply = kgp.get_response("who are you?")
        print(reply)
        talk(reply)
        while True:
            command = talk_to_me()
            command = command.strip()
            print(command)
            if 'bye' in command:
                 return True
            reply = kgp.get_response(command)
            print(reply)
            talk(reply)
        return False
    elif 'write' in command:
        command = command.replace('write', '')
        text = command.strip()
        pywhatkit.text_to_handwriting(text, "C:\\Users\\Aishwary\\Desktop\\output.png", (0, 0, 138))
        return False
    elif 'bye' in command:
        return True
    else:
        talk("pardon me, please repeat")
        return False

while True:
    if(run_jarvis()): 
        break
