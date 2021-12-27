import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as  wk
import webbrowser as wb
import os
from playsound import playsound
import random
import multiprocessing
import smtplib
import requests as re 
import json



  
machine = pyttsx3.init()
voices = machine.getProperty('voices')

machine.setProperty('voice',voices[7].id)


def speak(audio):
    machine.say(audio)
    machine.runAndWait()                                  # speak function for saying



def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak('Good Morning')
    elif hour >=12 and hour <18:
        speak('Good afternoon')
    else:
        speak('Good Evening') 
    speak('I am Clippy, how can i help you ')                           #wish function to say good morn

def takespeech():
    e = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening..')
        e.pause_threshold = 1
        audio = e.listen(source)
    try:
        print('Recognizing')
        query = e.recognize_google(audio,language='en-in')
        print(f'user said :{query}\n')
    except Exception as e:
        print('Say that again')                                        #speech to text conversation
        return 'None'
    return query
def newsread():
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=632d6bec70874cad843839749bbea144"
    res = re.get(url)
    news = json.loads(res.text)
    news = news['articles']
    speak("Today's news is ")
    for new in news:
        print(f"{new['title']},\n ")
        speak(new['title'])
    # speak('Thank you')
    return 0



if __name__ == '__main__':
    user = input()
    speak('Hi')
    speak(user)
    wish()
    # takespeech()
    while True:
        query = takespeech().lower()

        #logic for executing task
        
        if 'wikipedia' in query:
            speak('Searching wikipedia ...')
            query = query.replace('wikipedia','')
            result = wk.summary(query,sentences = 2)
            speak('According to wikipedia ..')
            print(result)
            speak(result)
        elif 'open facebook' in query:
            wb.open("https://www.facebook.com")

        elif 'open google' in query:
            wb.open("hhttps://www.google.co.in")

        elif 'open youtube' in query:
            wb.open("https://www.youtube.com")

        elif 'open stackoveflow' in query:
            wb.open("https://stackoverflow.com")

        elif 'open github' in query:
            wb.open("https://github.com")

        elif 'play music' in query:
            path = '//Users//satyabrata557//Desktop//songs'
            speak("Opening music player please wait")
            songs = os.listdir(path)
            song = random.choice(songs)
            p = multiprocessing.Process(target=playsound, args=(f'/{path}/{song}',))
            p.start()
            print('playing sound using  playsound')
            input("press ENTER to stop playback")
            p.terminate()
        elif 'time' in query:
            now = datetime.datetime.now().hour
            if 0 <= now < 12:
                current = datetime.datetime.now().strftime("[%H:%M]am of %Y-%m-%d")
                speak(current)
            else:
                current = datetime.datetime.now().strftime("[%H:%M]pm of %Y-%m-%d")
                speak(current)
            
        elif 'open safari' in query:
            path = '//Applications//Safari.app'
            speak("opening safari")
            os.system('open ' + path)

        elif 'open photos' in query:
            path = '//System//Applications//Photos.app'
            speak("opening Photos")
            os.system('open ' + path)
        
        elif 'open code' in query:
            path = "//Applications//'Visual Studio Code'.app"
            speak("opening code")
            os.system('open ' + path+ ' -n')

        elif 'open skype' in query:
            path = '//Applications//Skype.app'
            speak("opening Skype")
            os.system('open ' + path)
        
        elif 'news' in query:
            newsread()
        elif 'stop' in query:
            break
            
        
        
            



