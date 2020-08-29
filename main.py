import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# engine = pyttsx3.init('sapi5')
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')

# engine.setProperty('voice', voices[1].id)
engine.setProperty('voice', voices[20].id)

userName = input("Cual es tu nombre? ").lower()#Si no reconoce al usuario

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def saludo():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak(f"Buenos días {userName}!")
    elif hour >= 12 and hour < 18:
        speak(f"Buenas tardes {userName}!")
    else:
        speak(f"Buenas noches {userName}!")

    speak("¿Cómo puedo ayudarte?")#Si reconoce al usuario
    # speak("Mi nombre es Sabina, dime ¿cómo puedo ayudarte?")#Si no reconoce al usuario


def comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Compilando...")
        query = r.recognize_google(audio, language='es-mx')
        print(f"{userName}: {query}\n")

    except Exception as e:
        # print(e)
        speak(f"Lo siento {userName}, no enetendi, lo puede repetir por favor...?")
        print(f"Lo siento {userName}, no enetendi, lo puede repetir por favor...?")
        return "None"
    return query

def buscarEnGoogle():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak(f"Que deseas buscar {userName}...?")
        print(f"Que deseas buscar {userName}...?")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language='es-mx')
            print("Tu dijiste : {}".format(query))
            url = 'https://google.com/search?q='
            searchUrl = url + query
            webbrowser.open(searchUrl)
        except:
            speak("Dijiste algo? No entendi, lo puede repetir? ")
            print("Dijiste algo? No entendi, lo puede repetir? ")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ruben.vim@yahoo.com', 'j3v11296')
    server.sendmail('ruben.vim@yahoo.com', to, content)
    server.close()


if __name__ == "__main__":
    saludo()
    while True:
        # if 1:
        query = comando().lower()

        # Logica para ejecutar tareas basadas en query
        if 'buscar en google' in query:
            buscarEnGoogle()

        elif 'qué hora es' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"{userName}, la hora es {strTime}")
            print(strTime)



        # ----- Bloque de tareas escluidas para futura mejoria -----
        
        # if 'wikipedia' in query:
        #     speak('Buscando en Wikipedia...')
        #     query = query.replace("Wikipedia", "")
        #     results = wikipedia.summary(query, sentences=2)
        #     speak("De acuerdo con Wikipedia")
        #     print(results)
        #     speak(results)

        # elif 'abrir youtube' in query:
        #     webbrowser.open("youtube.com")

        # elif 'abrir stackoverflow' in query:
        #     webbrowser.open("stackoverflow.com")

        # elif 'play music' in query:
        #     music_dir = 'C:\Users\eadbox\Music\Projetos de Vídeo'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        # elif 'open code' in query:
        #     codePhat = url('C:\Users\eadbox\AppData\Local\Programs\Microsoft VS Code\Code.exe')
        #     os.startfile(codePhat)

        # elif 'email para' in query:
        #     try:
        #         speak("Qué deberia decir?")
        #         content = comando()
        #         to = "ruben.vim@yahoo.com"
        #         sendEmail(to, content)
        #         speak("El email a sido enviado!")
        #     except Exception as e:
        #         print(e)
        #         speak(f"Lo siento {userName}. No puedo enviar este email")

        # ----- Fin de bloque de tareas escluidas -----

        elif 'hasta luego sabina' in query:
            speak(f"De acuerdo {userName}, nos vemos más tarde")
            break     