import speech_recognition as sr
import pyttsx3
from datetime import datetime

# Initialize speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Greeting to be played at the start
def greet():
    engine.say("Hello! I am your virtual assistant. How can I assist you today?")
    engine.runAndWait()

# Function to listen to user's voice command
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language="en-in")
        print("User command:", command)
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return ''
    except sr.RequestError as e:
        print(f"Error connecting to Google Speech Recognition service; {e}")
        return ''

    return command.lower()

# Function to respond to the user
def respond(text):
    engine.say(text)
    engine.runAndWait()

# Initial greeting when the program starts
greet()

# Main loop for continuous interaction
while True:
    # Listen for user's command
    command = listen()
    
    # Check for different commands and respond accordingly
    if "hello" in command:
        respond("Hello! How can I assist you today?")
        
    elif "time" in command:
        # Function to get and respond with the current time
        now = datetime.now()
        current_time = now.strftime("%I:%M %p")
        response = f"The current time is {current_time}. Anything else I can help you with?"
        print(response)
        respond(response)

    elif "date" in command:
        # Function to get and respond with the current date
        rnow = datetime.now()
        current_date = rnow.strftime("%d %b %Y")
        reply = f"Today's Date is {current_date}. How can I assist you further?"
        print(reply)
        respond(reply)

    elif "goodbye" in command:
        # Farewell message and exit the loop
        respond("Goodbye! If you need assistance later, feel free to ask.")
        break
    else:
        # Handle unrecognized commands
        respond("Sorry, I couldn't understand your command. Can you please try again or ask something else?")
