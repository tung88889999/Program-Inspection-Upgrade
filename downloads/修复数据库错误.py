import os
import requests
import sqlite3
import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException
from textblob import TextBlob
import openai
import fasttext

import sqlite3

import os
import sqlite3
import datetime
from googletrans import Translator

# Initialize database connection and cursor
conn = sqlite3.connect('translations.db')
cursor = conn.cursor()

# Drop existing tables to reset the database schema
cursor.execute('DROP TABLE IF EXISTS author_names;')
cursor.execute('DROP TABLE IF EXISTS translations;')

# Create author_names table with pen_name as a unique key
cursor.execute('''
CREATE TABLE author_names (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pen_name TEXT UNIQUE,
    pen_name_translation TEXT
);
''')

# Create translations table including the language column
cursor.execute('''
CREATE TABLE translations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    original_text TEXT,
    language TEXT,
    source TEXT,
    text TEXT,
    model_and_example_translation TEXT
);
''')

# Commit changes and close the connection to ensure the schema is updated
conn.commit()
conn.close()

# Reopen connection to insert data and perform operations
conn = sqlite3.connect('translations.db')
cursor = conn.cursor()

# Inserting author names with unique constraint handling
try:
    cursor.execute('''
    INSERT INTO author_names (pen_name, pen_name_translation)
    VALUES ('江南樵夫', 'JiangNan-QiaoFu'),
           ('南柯舟', 'NanKeZhou')
    ''')
    conn.commit()
except sqlite3.IntegrityError:
    print("Duplicate entry found. Skipping insert.")

# Initialize translator
translator = Translator()

# Define function to translate and store results
def translate_and_store(text, language_code):
    translated_text = translator.translate(text, dest=language_code).text
    try:
        cursor.execute('''
        INSERT INTO translations (original_text, language, source, text, model_and_example_translation)
        VALUES (?, ?, 'Google Translate', ?, ?)
        ''', (text, language_code, translated_text, translated_text))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting data into translations: {e}")
        conn.rollback()

# Sample text to translate
text_to_translate = "中国网络作家江南樵夫认为：给我一把气枪，我也可以为国争光！"

# Translate text to multiple languages
languages = ['en', 'de', 'fr', 'es', 'ja']
for lang in languages:
    translate_and_store(text_to_translate, lang)

# Close database connection
conn.close()
