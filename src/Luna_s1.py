import requests
import speech_recognition as sr
import pyttsx3
import openai
import os
from dotenv import load_dotenv
from sympy import false,true

load_dotenv()

r = sr.Recognizer()
engine = pyttsx3.init()
ollama = openai.OpenAI(base_url="http://localhost:11434/v1", api_key=os.getenv("OLLAMA_API_KEY"))
result = ""
check = false
NASA_HIT = ["nasa","nasa facts","space facts","astronomy facts","space","astronomy"]

def say(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()

while true:
    with sr.Microphone(device_index=1) as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)

        print("Audio captured!")
        print("Thinking....")

        try :
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            if text.lower()=="what is your name" or text.lower()=="who are you":
                result = "I am luna your personal assistant, how can I help you today?"
                check = true

            elif text.lower() in NASA_HIT:
                for attempt in range(3):
                    response = requests.get(
                        "https://api.nasa.gov/planetary/apod",
                        params = {"api_key": os.getenv("NASA_API_KEY"), "count" : 1}
                    )
                    if response.status_code == 200: ## getting random space / astronomy fact and image from apod
                        data = response.json()[0]
                        image_url = data.get("hdurl") or data.get("url")
                        image_get = requests.get(image_url).content
                        with open("apod_image.jpg", "wb") as f:
                            f.write(image_get)
                        os.startfile("apod_image.jpg")
                        say(data.get("explanation"))
                        print("Title:", data.get("title"))
                        print("Image_URL:", data.get("url"))
                        print("Explanation:", data.get("explanation"))                       
                        print("Image saved as apod_image.jpg")
                        check = true
                        break

            elif text.lower() == "exit":
                say("Exiting, Have a nice day ahead")
                print("Exiting...")
                break
            
        except sr.UnknownValueError:
            unknown = "Sorry, I did not understand that."
            print(unknown)
            say(unknown)
            check = true
        except sr.RequestError as e:
            error = f"Error fetching results from Google Speech Recognition service; {e}"
            print(error)
            say(error)
            check = true

    if check == false: ## generating ai responses
        response = ollama.chat.completions.create(
        model = "llama3.2:latest",
        messages = [
            {"role": "system", "content": "You are a helpful assistant that responds to user queries."},
            {"role": "user", "content": text}
        ]
    )
        result = response.choices[0].message.content
    print(f"Response: {result}")
    say(result)
    check = false