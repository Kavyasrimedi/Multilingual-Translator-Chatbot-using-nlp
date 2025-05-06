# Installing required libraries
# You can run these commands separately in your environment
# !pip install googletrans==4.0.0-rc1
# !pip install langdetect
# !pip install nltk

# Importing libraries and download nltk data
from googletrans import Translator
from langdetect import detect
import nltk
import re

nltk.download('punkt')

# Clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # remove special chars
    return text

# Detect language
def detect_language(text):
    try:
        return detect(text)
    except:
        return "Could not detect"

# Translate
def translate_text(text, dest_lang):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"Error: {e}"

print("Multilingual Translator Chatbot")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    cleaned = clean_text(user_input)
    src_lang = detect_language(cleaned)
    print(f"Detected Language: {src_lang}")

    dest_lang = input("Translate to (e.g., 'en', 'hi', 'fr'): ")

    translation = translate_text(cleaned, dest_lang)
    print(f"🤖 Translation: {translation}\n")
