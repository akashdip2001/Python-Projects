import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install SpeechRecognition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
# import os
# import smtplib
import pyjokes # pip install pyjokes
# import requests
# import json
# import time
# import subprocess
# import wolframalpha # pip install wolframalpha
# import psutil # pip install psutil
# import pyautogui # pip install pyautogui
# import random
# import operator

def sptext(): # create a variable, Function to convert text to speech
	recognizer = sr.Recognizer() # recognizer class to recognize the speech
	with sr.Microphone() as source: # use microphone as source
		print("Listening...")
		recognizer.adjust_for_ambient_noise(source) # adjust for ambient noise
		audio = recognizer.listen(source) # audio variable to store the audio
		try: # exception handling
			print("Recognizing...")
			text = recognizer.recognize_google(audio) # text variable to store the recognized text & use google recognizer
			print(f"User said: {text}") # f-string to print the recognized text, f use for formatting
		except Exception as e: # or use, except sr.UnknownValueError:, the difference is that it will catch any exception
			print("Sorry, I did not get that") 
			return "None" # return None if exception occurs
		return text # return the recognized text
		# except sr.UnknownValueError: # except block to handle the exception
		# 	print("Sorry, I did not get that")
		# 	return "None" # return None if exception occurs
		# except sr.RequestError: # except block to handle the exception
		# 	print("Sorry, my speech service is down")
		# 	return "None" # return None if exception occurs
sptext() # call the function