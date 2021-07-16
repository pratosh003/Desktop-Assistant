import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def wishme():
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good Morning sir.")
  elif hour>=12 and hour<18:
    speak("Good afternoon sir.")
  else:
    speak("good evening!")

  speak("I am Jarvis. How may I help you sir?")

def takecommand():
  r = sr.Recognizer()
  r.energy_threshold = 4000
  with sr.Microphone() as source:
    print("listening...")  
    r.pause_threshold = 1
    audio = r.listen(source)

    try:
      print("recognizing...")
      query = r.recognize_google(audio, language='en-in')
      print(f"user said: {query}\n")

    except Exception as e:
      print("say that again please...")
      return "nome"
    return query



if __name__ == "__main__":
    wishme()
    while True:
    
        query = takecommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.Chrome.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        

 
