import speech_recognition as sr
import pyttsx3
import requests
import datetime

engine = pyttsx3.init()
print("Assistant: Hello! I'm your personal assistant. How can I help you today?")
engine.say("Hello! I'm your personal assistant. How can I help you today?")
engine.runAndWait()

while True:
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
         recognizer.adjust_for_ambient_noise(source, duration=2)
         print("Please speak something...")
         try: 
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio, language="en-US").lower()
            print("You: ",text)
         except sr.UnknownValueError:
             print("Assistant: Sorry, I did not understand that")
             engine.say("Sorry, I did not understand that")

         if "weather" in text:
              city = "kolkata"
              api_key = "31895d271571d8b36da9d91f08d14d86"
              url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
              response = requests.get(url)
              if response.status_code == 200:
                   data = response.json()
                   weather = data["weather"][0]["description"]
                   temp = data["main"]["temp"]
                   print(f"Assistant: The weaher in {city} is {weather} with a temperature of {temp}°C")
                   engine.say(f"The weaher in {city} is {weather} with a temperature of {temp}°C")

              else:
                  engine.say("Sorry, I couldn't fetch the weather")
                  print("Sorry, I couldn't fetch the weather")
              engine.runAndWait()

         elif "news" in text:
             api_key_news = "c83dc0a09cf6440d914b14f4eb9a2528"
             url_news = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key_news}"
             response = requests.get(url_news)
             if response.status_code == 200:
                 articles = response.json().get("articles", [])
                 headlines = [article['title'] for article in articles[:5]]
                 print("Assistant: Here are the top 5 news headlines: ")
                 for i, headline in enumerate(headlines, 1):
                     print(f"{i}. {headline}")
                 engine.say("Here are the top 5 news headlines: " + ", " .join(headlines))
                 engine.runAndWait()

         elif "time" in text:
             time = datetime.datetime.now().strftime("%I:%M %p")
             print(f"Assistant: The current time is {time}.")
             engine.say(f"The current time is {time}.")
             engine.runAndWait()

         elif "exit" or "quit" in text:
              break
         
         else:
             print("Assistant: I'm not sure how to help with that.")
             engine.say("Assistant: I'm not sure how to help with that.")
             engine.runAndWait()
