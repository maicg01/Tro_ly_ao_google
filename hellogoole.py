
#phan 1: nghe

you = "hello"
rb_brain = ""
if you == "":
    rb_brain = "I can't hear you,..."
    
elif you == "hello":
    rb_brain = "Hello everyone"

elif you == "today":
    rb_brain == "thu 6"

else: 
    rb_brain = "I'm fine, thank you"
print(rb_brain)

# phan 2: hieu
import speech_recognition 

rb_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm listening...")
    audio = rb_ear.listen(mic)
try:
    you = rb_ear.recognize_google(audio)
except:
    you = ""

print(you)


# phan 3: noi

import pyttsx3
rb_mouth = pyttsx3.init()
rb_mouth.say(rb_brain)
rb_mouth.runAndWait()

