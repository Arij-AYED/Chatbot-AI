# AI Voice Chatbot

This is my personal voice-enabled AI chatbot, built in Python and powered by Google Gemini API.
It can listen to your voice, understand what you say, and respond naturally using speech synthesis.

I designed it to feel like a friendly assistant, specifically as a travel agency helper for university students looking to study abroad.

 Quick Start
1. Clone the repository
git clone <your-repo-url>
cd chatbot

2️. Set Up Environment Variables

Create a .env file in the project root:

cp .env.example .env


Then open .env and add your Gemini API key:

GEMINI_API_KEY=your_gemini_api_key_here


Where to get your Gemini API Key:

Go to Google AI Studio

Create a new API key

Copy it into your .env

3️. Install Dependencies
pip install google-generativeai python-dotenv pyttsx3 SpeechRecognition

4️. Run the Chatbot
python main.py


The bot will start and say:

Bot: hello how can I help you?


Then you can speak to it, and it will respond both in text and voice.

 How It Works

Here’s the flow behind the scenes:

 Listen: Uses SpeechRecognition to capture your voice from the microphone.

Understand: Converts your speech to text.

Think: Sends your text to Google Gemini with a preconfigured system instruction (acting as a travel agency assistant).

Speak: Reads out the AI response using pyttsx3.

Context: Keeps a conversation history so responses are context-aware.

The bot is designed to respond welcomingly and helpfully, encouraging users to share their needs so it can provide personalized assistance.

Features

 Voice input & output — talk to the bot like a real assistant

 Text feedback in the console

 Context-aware responses using Gemini 1.5 Flash

Fast, lightweight, and easy to run

Secure API key stored in environment variables

Error handling for speech recognition or network issues

 Project Structure
chatbot/
├── .env                  # Your Gemini API key
├── .env.example          # Template
├── README.md
└── main.py               # Voice chatbot script

Environment Variables
Variable	Description	Required
GEMINI_API_KEY	Google Gemini API key from AI Studio	
Troubleshooting

 Bot doesn’t respond / GEMINI_API_KEY not found
✔ Make sure .env exists in the root folder
✔ Double-check your API key

 Speech isn’t recognized
✔ Ensure your microphone is working and accessible
✔ Speak clearly; noisy environments may reduce accuracy
