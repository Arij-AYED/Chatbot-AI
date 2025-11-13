# AI Voice Chatbot

This is my personal voice-enabled AI chatbot, built in Python and powered by Google Gemini API.
It can listen to your voice, understand what you say, and respond naturally using speech synthesis.

I designed it to feel like a friendly assistant, specifically as a travel agency helper for university students looking to study abroad.
---
## Quick Start
### 1. Clone the repository
```bash
git clone <your-repo-url>
cd chatbot
```

### 2️. Set Up Environment Variables

Create a .env file in the project root:
```bash
cp .env.example .env
```

Then open .env and add your Gemini API key:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

Where to get your Gemini API Key:

1.Go to Google AI Studio
2.Create a new API key
3.Copy it into your .env

### 3️. Install Dependencies
```bash
pip install google-generativeai python-dotenv pyttsx3 SpeechRecognition
```

### 4️. Run the Chatbot
```bash
python main.py
```
The bot will start and say:
```bash
Bot: hello how can I help you?
```
Then you can speak to it, and it will respond both in text and voice.

### How It Works
Here’s the flow behind the scenes:

1.Listen: Uses SpeechRecognition to capture your voice from the microphone.
2.Understand: Converts your speech to text.
3.Think: Sends your text to Google Gemini with a preconfigured system instruction (acting as a travel agency assistant).
4.Speak: Reads out the AI response using pyttsx3.
5.Context: Keeps a conversation history so responses are context-aware.

### Features

+Voice input & output — talk to the bot like a real assistant
+Text feedback in the console
+Context-aware responses using Gemini 1.5 Flash
+Fast, lightweight, and easy to run
+Secure API key stored in environment variables

### Error handling for speech recognition or network issues

```bash
chatbot/
├── .env                  # Contains your Gemini API key
├── .env.example          # Example environment file
├── README.md             # Project documentation
└── main.py               # Main chatbot script

```

### Environment Variables
+ Variable	Description	Required
+ GEMINI_API_KEY	Google Gemini API key from AI Studio

### Troubleshooting

 Bot doesn’t respond / GEMINI_API_KEY not found
+Make sure .env exists in the root folder
+Double-check your API key

 Speech isn’t recognized
 +Ensure your microphone is working and accessible
 +Speak clearly; noisy environments may reduce accuracy
