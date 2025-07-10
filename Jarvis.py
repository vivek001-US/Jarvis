import pyttsx3
import speech_recognition as sr
import datetime
import smtplib
import webbrowser
import os

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    
    # Get available microphones
    mic_list = sr.Microphone.list_microphone_names()
    
    # Choose built-in Mac mic (you can print to confirm if needed)
    mac_mic_index = 0  # Usually 0 is MacBook Air Mic

    try:
        with sr.Microphone(device_index=mac_mic_index) as source:
            print(f"[🎤] Using: {mic_list[mac_mic_index]}")
            speak("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        print("🧠 Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"🗣️ You said: {query}")
        return query.lower()

    except Exception as e:
        print("⚠️ Error recognizing speech:", e)
        speak("Sorry, I didn't catch that. Please say again.")
        return "none"

def send_email(to, content):
    your_email = "palvivek0882@gmail.com"
    your_password = "iblr yqmz cdcy ifkk"  # App password

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(your_email, your_password)
        server.sendmail(your_email, to, content)
        server.quit()
        speak("Email has been sent successfully.")
    except Exception as e:
        speak("Failed to send the email.")
        print("⚠️", e)

def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am JARVIS. How can I help you today?")

if __name__ == "__main__":
    wish_user()
    while True:
        query = take_command()

        if query == "none":
            continue

        elif 'exit' in query or 'stop' in query or 'shutdown' in query:
            speak("Shutting down. Goodbye!")
            break

        elif 'open youtube' in query:
            speak("Opening YouTube.")
            webbrowser.open("https://youtube.com")

        elif 'open google' in query:
            speak("Opening Google.")
            webbrowser.open("https://google.com")

        elif 'open vs code' in query or 'open visual studio code' in query:
            speak("Opening Visual Studio Code.")
            os.system("open -a 'Visual Studio Code'")  # macOS

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = take_command()
                if content == "none":
                    speak("Email content was not clear.")
                    continue
                to = "vpal22962@gmail.com"  # Receiver
                send_email(to, content)
            except Exception as e:
                speak("Sorry, I couldn't send the email.")
                print("⚠️", e)

        else:
            speak("I can only help with voice commands, email, and launching apps right now.")
