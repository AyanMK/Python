import pyttsx3                      #pip install pyttsx3
import datetime
import speech_recognition as sr     #pip install speechRecognition
import wikipedia                    #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<6:  #night time
        print("Good day!")
        speak("Good day!")
    
    elif hour>=6 and hour<12:  
        print("Good Morning!")
        speak("Good Morning!")

    elif hour==12:
        print("Good Noon!")
        speak("Good Noon!")

    elif hour>12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("I am Ron Sir. how may I help you?\n")
    speak("I am Ron Sir. how may I help you?")

def tackCommand():
    #IT take microphone input from user and returns string & voice output

    r = sr.Recognizer()
    with sr.Microphone() as source:
          print("Listening...")
          r.pause_threshold = 0.6
          r.energy_threshold = 500
          audio = r.listen(source)

    try:
        print("Recognize...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kakonayan123@gmail.com', 'Password')
    server.sendmail('kakonayan123@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = tackCommand().lower()
        #Logick for executing tasks based on query
        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 1)
            print("According to Wikipedia")
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'what is your name' in query:
            print("I am ron. an AI... I work as voice assistant")
            speak("I am ron. an AI... I work as voice assistant")
            
        elif 'who are you' in query:
            print("I am ron. an AI... I work as voice assistant")
            speak("I am ron. an AI... I work as voice assistant")
            
        elif 'stop listening' in query:
            print("I am out.")
            speak("I am out.")
            exit()

        elif '000' in query:
            print("I am out.")
            speak("I am out.")
            exit()
        
        elif 'what you can do for me' in query:
            print("I can play music \nOpen MS Word \nOpen your favorite website \nAnd you can also upgrade me by your require")
            speak("I can play music \nOpen MS Word \nOpen your favorite website \nAnd you can also upgrade me by your require")
            
        elif 'open spotify' in query:
            codePath = "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify"
            os.startfile(codePath)
            
        elif 'open ms word' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word"
            os.startfile(codePath)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            
        elif 'search youtube' in query:
            query = query.replace("search youtube","")
            #print(f"User: {query}\n")
            webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")
            
        elif 'newspaper' in query:
            webbrowser.open("www.prothomalo.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\User\\Desktop\\RPSU\\Artificial Intelligence Lab\\project\\play music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\User\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'mail to ayan' in query:
            try:
                print("What should I say?")
                speak("What should I say?")
                content = tackCommand()
                to = "ayankakon123@gmail.com"
                sendEmail(to, content)
                print("Email has been sent!")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry! Email does not send.")
                
        
        