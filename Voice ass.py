import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib 


# Initialize the TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    """Converts text to speech"""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Greets the user based on the time of day"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning BOSS!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon BOSS")
    else:
        speak("Good Evening BOSS!")
    speak("I am Jimmy. Please tell me how can I help you")

def takeCommand():
    """Listens to the user's voice command and returns it as a string"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 4000
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except Exception as e:
            print(f"Error while accessing the microphone: {e}")
            return "None"

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except sr.WaitTimeoutError:
        print("Listening timed out while waiting for phrase to start")
        return "None"
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "None"
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vivek.aiml.aec@gmail.com', 'Strings@132')
    server.sendmail('vivek.aiml.aec@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if query == "none":
            continue
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Sorry, I couldn't find any results on Wikipedia.")
                print(f"Error: {e}")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'open irctc' in query:
            webbrowser.open("https://www.irctc.co.in/nget/train-search")       
        
        elif 'grocery mart' in query:
            webbrowser.open("grocerymart.in")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\shriv\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        elif 'email to vivek' in query:
            try:
                speak("Tell me what I'll say?")
                content = takeCommand()
                to = "vivek.aiml.aec@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent succesfully!")
            except Exception as e:
                print(e) 
                speak("Sorry to say but i am not able to send the email")
                   

