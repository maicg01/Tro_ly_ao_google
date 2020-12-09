import speech_recognition 
import pyttsx3
from datetime import date
from datetime import datetime

rb_ear = speech_recognition.Recognizer()
rb_mouth = pyttsx3.init()
rb_brain = ""

print("Robot: Hello, It's good to talk to you too. Come on, tell me your name...")
rb_mouth.say("Hello, It's good to talk to you too. Come on, tell me your name...")
rb_mouth.runAndWait()
print("Enter your name: ")
name = input()
print("Robot: Hello " + name)
rb_mouth.say("Hello" + name)
rb_mouth.runAndWait()



while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening...")
        audio = rb_ear.listen(mic)

    print("Robot: ...")

    try:
        you = rb_ear.recognize_google(audio)
    except:
        you = ""

    print("You: " + you)

    if you in "":
        rb_brain = "I can't hear you,..."
        rb_mouth.say(rb_brain)
        rb_mouth.runAndWait()
        break

    elif "allo Allo" in you or "allo allo" in you:
        rb_brain = "allo Allo"
        
    elif "hello" in you:
        rb_brain = "Hello Mai"

    elif "how are you" in you:
        rb_brain = "I'm good"

    elif "today" in you:
        today = date.today()
        rb_brain = today.strftime("%B %d, %Y")

    elif "time" in you:
        now = datetime.now()
        rb_brain = now.strftime("%H hours %M minutes %S seconds")

    elif "where" in you:
        rb_brain = "anywhere"
    
    elif "bye" in you:
        rb_brain = "Bye bye name"
        print("Robot: " + rb_brain)
        rb_mouth.say(rb_brain)
        rb_mouth.runAndWait()
        break
        
    else: 
        rb_brain = "I'm fine, thank you"

    print("Robot: " + rb_brain)
    rb_mouth.say(rb_brain)
    rb_mouth.runAndWait()