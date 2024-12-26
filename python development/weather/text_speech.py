import pyttsx3

engine = pyttsx3.init()

text = "Hello ! sir , I'm sakshi gupta"
engine.say(text)
engine.runAndWait()