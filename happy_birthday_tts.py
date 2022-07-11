"""

Author: Zachary Stewart
Date: 07/07/2022

Description: Program takes in a user's name and age and generates a TTS response saying happy birthday.

"""

# imports pyttsx3 module
import pyttsx3

# Initializes instance of pyttsx3
tts = pyttsx3.init()

# Tells user speakers would be needed
print("Make sure you have your speakers turned on!")

# Prompts user for their name and age
name = input("Enter Your Name: ")
age = input("Enter Your Age: ")

# Song being read out
lyrics = """
Happy Birthday to You,
You are [age],
Happy Birthday Dear [name]
Happy Birthday to You.
"""

# Inserts given name into song lyrics
lyrics = lyrics.replace("[name]", name)
lyrics = lyrics.replace("[age]", age)

# Changes voice being used
voices = tts.getProperty('voices')
# Keeping voice as default (voices[0].id)
tts.setProperty('voice', voices[0].id)

# Tells program to say given string
tts.say(lyrics)
tts.runAndWait()
