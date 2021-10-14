from time import sleep
import speech_recognition as sr


recognizer = sr.Recognizer()

while  True:
    try:
        with sr.Microphone() as mic:            
            recognizer.adjust_for_ambient_noise(mic, duration =0.2)
            
            audio = recognizer.listen(mic)
            text=recognizer.recognize_google(audio)
            text=text.lower()
            print(f"Recognized:{text}")
    except sr.UnknonValueError():
        recognizer = sr.Recognizer()

        continue



# the program will print hello world
#  every 1 second foever
"""
while True:
    print("Hello, crule World")
    sleep(1)
"""

print("the fro like the boiling water")