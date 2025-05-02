import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import pyttsx3
engine=pyttsx3.init()


import speech_recognition as sr
recognizer=sr.Recognizer()
def listen():
  with sr.Microphone() as source:
    print("Listening...")
    audio=recognizer.listen(source)
  try:
    return recognizer.recognize_google(audio)
  except sr.UnknownValueError:
    return "sorry, I could not understand."
  except sr.RequestError:
    return "sorry , I'm having trouble with the speech service."


def speak(text):
  engine.say(text)
  engine.runAndWait()

print("Loaded API key:", os.getenv("GEMINI_API_KEY"))

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-8b",
  generation_config=generation_config,
  system_instruction="The user greeted me with \\\"hi\\\". As a travel agency for university students seeking study abroad opportunities, I need to respond in a welcoming and helpful manner.  I should acknowledge the greeting and immediately offer my services.  I need to clearly state my role and what I can do for the user. I should also encourage them to share their needs and preferences so I can start assisting them.  This initial response sets the tone for a helpful and personalized interaction.\n",
)
history=[]
print("Bot: hello how can I help you?")
while True:
  user_input=listen()
  print("You: ",user_input)
  chat_session = model.start_chat(
    history=history

  )

  response = chat_session.send_message(user_input)

  model_response=response.text
  print("model: ",model_response)
  speak(model_response)
  print()
  history.append({"role":"user","parts":{user_input}})
  history.append({"role":"model","parts":{model_response}})

