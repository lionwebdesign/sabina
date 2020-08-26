import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[20].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Buenos días!")
    elif hour >= 12 and hour < 18:
        speak("Buenas tardes!")
    else:
        speak("Buenas noches!")

    speak("Mi nombre es Sabina, dime ¿cómo puedo ayudarte?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='es-mx')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Puede repetir por favor...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ruben.vim@yahoo.com', 'j3v11296')
    server.sendmail('ruben.vim@yahoo.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'abrir youtube' in query:
            webbrowser.open("youtube.com")

        elif 'abrir google' in query:
            webbrowser.open("google.com")

        elif 'abrir stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        # elif 'play music' in query:
        #     music_dir = 'C:\Users\eadbox\Music\Projetos de Vídeo'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'me puedes dar la hora por favor' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Señor, la hora es {strTime}")

        elif 'hasta luego' in query:
            speak("De acuerdo señor, nos vemos más tarde")
            break

        # elif 'open code' in query:
        #     codePhat = url('C:\Users\eadbox\AppData\Local\Programs\Microsoft VS Code\Code.exe')
        #     os.startfile(codePhat)

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "ruben.vim@yahoo.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir. Im not able to send this email")