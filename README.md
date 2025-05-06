# Multilingual Translator Chatbot using NLP

This is a simple command-line chatbot that detects the language of the input text and translates it into a desired target language using Natural Language Processing (NLP).

## Features

- Detects language of user input automatically
- Translates to any target language (e.g., English, Hindi, French, etc.)
- Cleans text before translation for better accuracy
- Built with Python and NLP libraries
- Works in a simple interactive terminal environment

## How It Works

1. The user types any sentence.
2. The chatbot detects the language.
3. The user selects a target language (by language code like `en`, `hi`, `fr`, etc.).
4. The chatbot replies with the translated text.

## Demo

You: Bonjour
Detected Language: fr
Translate to (e.g., 'en', 'hi', 'fr'): en
🤖 Translation: Hello

## Installation

Make sure you have Python installed. Then install the required libraries:

pip install -r requirements.txt

Type your messages and translate across languages! Type exit to quit the chatbot.

## Requirements
googletrans==4.0.0-rc1

langdetect

nltk

## Author
Kavya Sri Medi


