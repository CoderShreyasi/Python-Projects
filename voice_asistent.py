import speech_recognition as sr
import os
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

# Main voice assistant loop
while True:
    # Listen to user input
    user_input = listen()

    if user_input:
        # Perform actions based on user input
        if "shutdown" in user_input:
            speak("Shutting down the computer.")
            os.system("shutdown /s /t 1")
            break  # exit the loop after shutting down
        elif "play music" in user_input:
            speak("Playing music.")
            # You can add code here to play music using your preferred music player
        elif "stop" in user_input:
            speak("Stopping.")
            # You can add code here to stop any ongoing action
        else:
            speak("I'm sorry, I didn't understand that.")

# End of the program
