import speech_recognition as sr
import pyttsx3

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    """Speak out the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to microphone and return recognized text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that. Please repeat.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

def main():
    speak("Hello! I am your virtual assistant. How can I help you?")
    while True:
        command = listen()

        if 'hello' in command:
            speak("Hello! How are you?")
        elif 'your name' in command:
            speak("I am your Python virtual assistant.")
        elif 'how are you' in command:
            speak("I am doing great! Thank you for asking.")
        elif 'exit' in command or 'stop' in command or 'bye' in command:
            speak("Goodbye! Have a nice day.")
            break
        elif command != "":
            speak("I am sorry, I don't know how to respond to that.")

if __name__ == "__main__":
    main()
