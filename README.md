Jarvis AI - Voice Assistant

Overview

Jarvis AI is a voice-controlled assistant that can perform various tasks such as opening websites, playing music, and interacting with Google's Gemini AI for intelligent responses.

Features

Voice Recognition: Listens to user commands using speech_recognition.

Speech Synthesis: Responds via voice using win32com.client.

AI Responses: Uses Google Gemini AI to generate responses.

Web Browsing: Opens popular websites like Google, Wikipedia, and ChatGPT.

File and Music Management: Opens specific files or music based on voice commands.

Requirements

To run this project, you need to install the following dependencies:

pip install SpeechRecognition pywin32 google-generativeai

Additionally, you need an API key for Google Gemini AI, which should be stored in config.py as:

apikey = "YOUR_GOOGLE_API_KEY"

How to Use

Run the script:

python script.py

Jarvis AI will greet you and start listening for commands.

You can use commands like:

"Open Google"

"Open Wikipedia"

"Open file"

"Using artificial intelligence [your query]"

"Jarvis quit" (to exit the program)

If a command is not recognized, it will default to chatting with the AI.

File Handling

AI-generated responses are saved in the openai/ directory.

The filename is based on the user's prompt.

Exiting the Program

Say "Jarvis quit" to stop the assistant.

Future Enhancements

Add more website shortcuts.

Improve error handling in speech recognition.

Implement additional AI models for enhanced responses.

Author

This project is developed as a basic implementation of a personal AI assistant using Python.
