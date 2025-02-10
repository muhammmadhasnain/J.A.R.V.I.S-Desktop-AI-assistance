Jarvis AI - Voice Assistant

Overview

Jarvis AI is a voice-controlled virtual assistant built using Python. It can recognize speech, respond using text-to-speech, perform web searches, open files, and generate AI-based responses using Google Gemini API.

Features

Speech Recognition: Uses the speech_recognition library to understand user commands.

Text-to-Speech (TTS): Uses SAPI.SpVoice to convert AI responses into speech.

Web Browsing: Opens websites like Google, Wikipedia, and ChatGPT on command.

File Management: Opens specific files and folders on request.

AI-Powered Responses: Uses Google Gemini API to generate intelligent responses.

Continuous Listening: Runs in a loop to constantly listen for new commands.

Installation

Prerequisites

Ensure you have the following installed:

Python 3.x

Required Python libraries:

pip install speechrecognition pywin32 google-generativeai

A valid Google Gemini API key (stored in config.py as apikey).

Usage

Run the script:

python jarvis.py

Speak commands like:

"Open Google"

"Open music"

"Using artificial intelligence, tell me about space"

"Jarvis quit" (to exit)

File Structure

Jarvis-AI/
│── jarvis.py            # Main script
│── config.py            # API key storage
│── openai/              # Folder for AI-generated responses
│── README.md            # Project documentation

Future Improvements

Add support for more commands (weather updates, reminders, etc.)

Improve speech recognition accuracy

Implement a GUI interface
