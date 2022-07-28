from ast import Try
import ctypes
from time import strftime
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import wikipedia
import smtplib



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")

    elif hour>=12 and hour<=18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")    

    speak("I am millie b sir,please tell me how may i help you")

def takeCommand():
    #it takes microphone input from the user and returns string output 
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
    

    except Exception as e:
        #print(e)
        print("say that again please...")
        return "None"
    return query
     
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('rigvedtupsakhare@gmail.com','hathway1234')
    server.sendmail('rigvedtupsakhare@gmail.com',to,content)
    server.close()


if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

          # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.rplace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
               webbrowser.open("youtube.com")

        elif 'open google' in query:
               webbrowser.open("google.com")       

        elif 'open stackoverflow' in query:
               webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "C:\\Users\\Admin\\Downloads\\One Direction -Take me Home (Deluxe Yearbook Edition) (2012) [M4A-320KBPS] [JRR] [truHD]"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir,the time is {strTime}")

        elif 'open code' in query:
                   codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                   os.startfile(codePath)

        elif  'send a email' in query:
           try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
                
           except Exception as e:
                print(e)
                speak("I am not able to send this email")        

        elif 'open www.' in query:
            webbrowser.open(query + ".com")

        elif 'exit' in query:
            speak("see you later")
            exit()                

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif "who i am" in query:
            speak("If you talk then definitely your human.")    
         
         
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation() 