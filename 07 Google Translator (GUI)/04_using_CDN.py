from tkinter import *  # Import tkinter for GUI
from tkinter import ttk  # Import ttk for combobox
import requests  # Import requests to use the CDN version of googletrans
#from googletrans import LANGUAGES  # Import LANGUAGES to get supported languages

# Function to translate text using the CDN version of googletrans
def change(text="Type ... ", src="English", dest="Hindi"):
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        'client': 'gtx',
        'sl': src,
        'tl': dest,
        'dt': 't',
        'q': text,
    }
    response = requests.get(url, params=params)
    translated_text = response.json()[0][0][0]
    return translated_text

# Function to retrieve data and display the translated text
def data():
    s = comb_source.get()  # Get the source language
    d = comb_destination.get()  # Get the destination language
    masg = Source_text.get(1.0, END)  # Get the text to translate
    textget = change(text=masg, src=s, dest=d)  # Translate the text
    Output_text.delete(1.0, END)  # Clear previous text in output box
    Output_text.insert(END, textget)  # Display translated text

# Main application window
root = Tk()
root.title("Translator")
root.geometry("500x750")
root.configure(bg='black')

# Title label
Label(root, text="Translator", font=("Helvetica", 40, "bold"), bg='black', fg='white').place(x=100, y=40, height=50, width=300)

# Frame for input text
Frame1 = Frame(root, bg='black').pack(side=BOTTOM)
Label(root, text="Enter Text", font=("Helvetica", 20, "bold"), bg='black', fg='gray').place(x=10, y=120, height=20, width=150)

# Textbox for input text
Source_text = Text(Frame1, font=("Helvetica", 20, "bold"), wrap=WORD, bg='gray', fg='white', bd=6)
Source_text.place(x=10, y=150, height=100, width=480)



## Language selection comboboxes
languages = ["en", "hi", "es", "fr", "de"]  # Add language codes here as needed
## or use --> from googletrans import LANGUAGES  # Import LANGUAGES to get supported languages
#languages = [name.capitalize() for name in LANGUAGES.values()]  # Capitalize for better display


comb_source = ttk.Combobox(Frame1, values=languages, font=("Helvetica", 20, "bold"), state="readonly")
comb_source.place(x=15, y=260, height=40, width=80)
comb_source.set("en")  # Default source language

Label(root, text="To", font=("Helvetica", 20, "bold"), bg='black', fg='gray').place(x=100, y=260, height=40, width=45)

comb_destination = ttk.Combobox(Frame1, values=languages, font=("Helvetica", 20, "bold"), state="readonly")
comb_destination.place(x=160, y=260, height=40, width=80)
comb_destination.set("hi")  # Default destination language

# Translate button
Button(Frame1, text="Translate", relief=RAISED, font=("Helvetica", 18, "bold"), bg='black', fg='white', bd=6, command=data).place(x=350, y=260, height=45, width=130)



# Output label and textbox
Label(root, text="Output", font=("Helvetica", 20, "bold"), bg='black', fg='gray').place(x=10, y=380, height=30, width=120)
Output_text = Text(Frame1, font=("Helvetica", 20, "bold"), wrap=WORD, bg='gray', fg='white', bd=6)
Output_text.place(x=10, y=420, height=120, width=480)

root.mainloop()
