import speech_recognition as sr  # module used to convert spoken words to text
import pyttsx3  # module used to convert text to speech
import datetime
import webbrowser  # opens any website
import wikipedia
import os  # module helps to open a file in a directory
from AppOpener import run
import pywhatkit  # module used to send whatsapp message and play a youtube video
import pytube  # module used for downloading videos


def speak(audio):
    engine = pyttsx3.init()  # text-to-speech converter
    engine.setProperty('rate', 180)  # 2nd parameter sets speed
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)  # now function returns the time
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir, Duke at your service.")
    elif hour > 12 and hour < 16:
        speak("Good Afternoon Sir, Duke at your service.")
    else:
        speak("Good Evening Sir, Duke at your service.")


def talk():
    # recognizer will recognize your voice and will understand whatever you say
    listener = sr.Recognizer()
    print("Listening...")
    with sr.Microphone() as source:  # default microphone used as audio source to speak which will be converted to audiodata
        # even if we take a gap before speaking it will not stop taking in input
        # number of seconds the system will take to recognise the voice after user has completed their sentence
        listener.pause_threshold = 1
        audio = listener.listen(source)

    try:
        command = listener.recognize_google(
            audio, language='en-in')  # google assisstant API is used
        speak("Is this what my humble master wanted to say:")
        print(f"Is this what my humble master wanted to say:{command}\n")

    except Exception as e:
        speak("Please forgive me, but could the master repeat...")
        return "None"
    return command


if __name__ == "__main__":
    wishMe()
    while True:
        # agr command lowercase mein hai to vaisi hi rahegi, agr uppercase
        command = talk().lower()
        # mein hai to lowercase mein convert ho jayegi
        if 'wikipedia' in command:
            speak("Searching Wikipedia for my master....")
            print("Searching Wikipedia for my master....")
            command = command.replace("wikipedia", "")
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in command:
            speak("Opening Youtube for my master....")
            webbrowser.open("youtube.com")

        elif 'open google' in command:
            speak("Opening Google for my master....")
            webbrowser.open("google.com")

        elif 'open unsplash' in command:
            speak("Opening Unsplash for my master....")
            webbrowser.open("unsplash.com")

        elif 'open university website' in command:
            speak("Opening CUIMS for my master....")
            webbrowser.open("uims.cuchd.in")

        elif 'open code' in command:
            codePath = "D:\\VS Code\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open spotify' in command:
            run("Spotify")
            speak("Opening Spotify")

        elif 'play' in command:
            video = command.replace("play", "")
            print(f"Playing{video}")
            speak(f"Playing{video}")
            pywhatkit.playonyt(video)

        elif 'date and time' in command:
            strTime = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            print(f"Master the date & time is-{strTime}")
            speak(f"Master the date & time is {strTime}")

        elif 'download video' in command:
            link = input("Enter Youtube URL: ")
            yt = pytube.YouTube(link)
            stream = yt.streams.get_highest_resolution()
            stream.download()

        elif 'how are you' in command:
            print("I'm delighted as my master recalled me. I would like to ask the same from my master. Master, how are you?")
            speak("I'm delighted as my master recalled me. I would like to ask the same from my master. Master, how are you?")

        elif 'fine' in command:
            print(
                "Don't be so humble to this petty servant,my master. Well, do remember me when needed.")
            speak(
                "Don't be so humble to this petty servant,my master. Well, do remember me when needed.")

        elif 'quit' in command:
            speak("Goodbye Master, Duke signing off!")
            exit()
