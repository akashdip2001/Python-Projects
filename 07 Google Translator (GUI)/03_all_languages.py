from tkinter import *  # Import tkinter for GUI
from tkinter import ttk  # Import ttk for combobox
import requests  # Import requests to use the CDN version of googletrans

# Dictionary of languages with codes and display names
languages = {
    'af': 'Afrikaans', 'sq': 'Albanian', 'am': 'Amharic', 'ar': 'Arabic', 'hy': 'Armenian', 'az': 'Azerbaijani',
    'eu': 'Basque', 'be': 'Belarusian', 'bn': 'Bengali', 'bs': 'Bosnian', 'bg': 'Bulgarian', 'ca': 'Catalan',
    'ceb': 'Cebuano', 'ny': 'Chichewa', 'zh-cn': 'Chinese (Simplified)', 'zh-tw': 'Chinese (Traditional)',
    'co': 'Corsican', 'hr': 'Croatian', 'cs': 'Czech', 'da': 'Danish', 'nl': 'Dutch', 'en': 'English',
    'eo': 'Esperanto', 'et': 'Estonian', 'tl': 'Filipino', 'fi': 'Finnish', 'fr': 'French', 'fy': 'Frisian',
    'gl': 'Galician', 'ka': 'Georgian', 'de': 'German', 'el': 'Greek', 'gu': 'Gujarati', 'ht': 'Haitian Creole',
    'ha': 'Hausa', 'haw': 'Hawaiian', 'iw': 'Hebrew', 'hi': 'Hindi', 'hmn': 'Hmong', 'hu': 'Hungarian', 'is': 'Icelandic',
    'ig': 'Igbo', 'id': 'Indonesian', 'ga': 'Irish', 'it': 'Italian', 'ja': 'Japanese', 'jw': 'Javanese',
    'kn': 'Kannada', 'kk': 'Kazakh', 'km': 'Khmer', 'ko': 'Korean', 'ku': 'Kurdish (Kurmanji)', 'ky': 'Kyrgyz',
    'lo': 'Lao', 'la': 'Latin', 'lv': 'Latvian', 'lt': 'Lithuanian', 'lb': 'Luxembourgish', 'mk': 'Macedonian',
    'mg': 'Malagasy', 'ms': 'Malay', 'ml': 'Malayalam', 'mt': 'Maltese', 'mi': 'Maori', 'mr': 'Marathi', 'mn': 'Mongolian',
    'my': 'Myanmar (Burmese)', 'ne': 'Nepali', 'no': 'Norwegian', 'or': 'Odia', 'ps': 'Pashto', 'fa': 'Persian',
    'pl': 'Polish', 'pt': 'Portuguese', 'pa': 'Punjabi', 'ro': 'Romanian', 'ru': 'Russian', 'sm': 'Samoan',
    'gd': 'Scots Gaelic', 'sr': 'Serbian', 'st': 'Sesotho', 'sn': 'Shona', 'sd': 'Sindhi', 'si': 'Sinhala',
    'sk': 'Slovak', 'sl': 'Slovenian', 'so': 'Somali', 'es': 'Spanish', 'su': 'Sundanese', 'sw': 'Swahili',
    'sv': 'Swedish', 'tg': 'Tajik', 'ta': 'Tamil', 'te': 'Telugu', 'th': 'Thai', 'tr': 'Turkish', 'uk': 'Ukrainian',
    'ur': 'Urdu', 'ug': 'Uyghur', 'uz': 'Uzbek', 'vi': 'Vietnamese', 'cy': 'Welsh', 'xh': 'Xhosa', 'yi': 'Yiddish',
    'yo': 'Yoruba', 'zu': 'Zulu'
}

# Function to translate text using the CDN version of googletrans
def change(text="Type ...", src="English", dest="Hindi"):
    src_code = next(key for key, value in languages.items() if value == src)
    dest_code = next(key for key, value in languages.items() if value == dest)
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        'client': 'gtx',
        'sl': src_code,
        'tl': dest_code,
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



# Language selection comboboxes using language names
comb_source = ttk.Combobox(Frame1, values=list(languages.values()), font=("Helvetica", 20, "bold"), state="readonly")
comb_source.place(x=10, y=260, height=40, width=135)
comb_source.set("English")  # Default source language

Label(root, text="To", font=("Helvetica", 20, "bold"), bg='black', fg='gray').place(x=150, y=260, height=40, width=45)

comb_destination = ttk.Combobox(Frame1, values=list(languages.values()), font=("Helvetica", 20, "bold"), state="readonly")
comb_destination.place(x=200, y=260, height=40, width=155)
comb_destination.set("Hindi")  # Default destination language

# Translate button
Button(Frame1, text="Translate", relief=RAISED, font=("Helvetica", 18, "bold"), bg='black', fg='white', bd=6, command=data).place(x=365, y=260, height=45, width=130)



# Output label and textbox
Label(root, text="Output", font=("Helvetica", 20, "bold"), bg='black', fg='gray').place(x=10, y=380, height=30, width=120)
Output_text = Text(Frame1, font=("Helvetica", 20, "bold"), wrap=WORD, bg='gray', fg='white', bd=6)
Output_text.place(x=10, y=420, height=120, width=480)

root.mainloop()
