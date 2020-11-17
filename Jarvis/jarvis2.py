"""
JARVIS:
- Control Windows programs with your voice
__author__ = 'Muhammed Shokr <mohammedshokr2014@gmail.com>'
__version__ = 'v 1.0'
JARVIS repo <https://github.com/Shokr/JARVIS>
"""

# import modules

# subprocess module allows you to spawn new processes
import subprocess

# speech_recognition Library for performing speech recognition with support for Google Speech Recognition
import speech_recognition as sr

# importing the pyttsx3 library
import pyttsx3

import wikipedia  # for wikipedia search
import smtplib  # for sending mails

# initialisation
engine = pyttsx3.init()

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    engine.say("Say something")
    engine.runAndWait()
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
Query = r.recognize_google(audio, language='zh-CN')
print(Query)


# Run Application with Voice Command Function
def get_app(query):
    cmd = {
        'browser': 'C:\Program Files\Internet Explorer\iexplore.exe',
        'calculator': 'calc.exe',
        'cmd': 'cmd.exe',
        'notepad': 'Notepad.exe',
        'paint': 'mspaint.exe',
        'shell': 'powershell.exe',
        'stikynot': 'StikyNot.exe',
    }.get(query.lower())
    if cmd:
        subprocess.call([cmd])
    else:
        engine.say("Sorry Try Again")
        engine.runAndWait()


def main():
    # Call get_app(Query) Func.
    get_app(Query)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('example123@gmail.com', 'Pass@123')
    server.sendemail('receivermail@gmail.com', to, content)
    server.close()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")

    except Exception as e:

        print('say that again pls sir')
        return "None"
    return query


if __name__ == '__main__':
    main()
    while True:
        query = takeCommand().lower()
        # logic for executing programs
        if 'wikipedia' in query:
            speak("searching wikipedia.....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("according to wikipedia")
            speak(results)


        elif 'send email' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                speak("wo is receiver, sir")
                receiver = input("enter receiver email sir")
                to = receiver
                sendEmail(to, content)
                speak(content)
                speak("email is sent")
            except Exception as e:
                print(e)
                speak("Sorray i am not send this mail")
        elif 'go offlie' in query:
            speak("going offline sir")
            quit()