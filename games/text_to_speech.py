import pyttsx3

def speak_text(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties before adding anything to speak
    # Set the rate (speed)
    rate = engine.getProperty('rate')   # Getting current speaking rate
    engine.setProperty('rate', rate-50) # Setting new speaking rate (lower is slower)
    
    # Set the volume
    volume = engine.getProperty('volume')  # Getting current volume level (min=0, max=1)
    engine.setProperty('volume', volume+0.25)  # Setting new volume level

    # Set the voice (male or female)
    voices = engine.getProperty('voices')       # Getting details of current voice
    engine.setProperty('voice', voices[0].id)   # Changing index changes voices: 0 for male, 1 for female
    
    # Pass the text to the engine
    engine.say(text)
    
    # Process and speak the text
    engine.runAndWait()

if __name__ == "__main__":
    text = input("Enter the text you want to speak: ")
    speak_text(text)