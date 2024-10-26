from tkinter import * # Import tkinter for GUI & * for all functions at once
# # Whay Tkinter? It is a standard GUI library for Python. It is lightweight and easy to use.It provides a powerful object-oriented interface to the Tk GUI toolkit.It is the standard Python interface to the Tk GUI toolkit, and is Python's de facto standard GUI.
from tkinter import ttk # Import ttk for combobox, which used to create a drop-down list.
from googletrans import Translator, LANGUAGES # pip install googletrans==4.0.0-rc1 (ony works on Install Python 3.10 from)
# #you can use google cdn, the url is https://cdn.jsdelivr.net/gh/ssut/py-googletrans@4.0.0-rc1/googletrans/gtoken.py. How to use this url in this code with an ex


def change(text="Type ... ",src="English", dest="Hindi"):
    text1=text # Create a variable text1 to store the text
    translator01 = Translator() # Create a Translator01 object
    translated_text = translator01.translate(text, src1=src, dest1=dest) # create a variable translated_text to store the translated text
    return text1.text # Return the translated text

# # Create a function to translate the text
def data():
    s = comb_source.get() # Get the source language from the combobox
    d = comb_destination.get() # Get the destination language from the combobox
    masg = Source_text.get(1.0, END) # Get the text from the textbox
    textget = change(text= masg, src=s, dest=d) # Call the change function to translate the text
    Output_text.delete(1.0, END) # Delete the previous text from the textbox
    Output_text.insert(END, textget) # Insert the translated text into the textbox





# Create a object root for Tk class
root = Tk() # Create a root window, which is a main application window in Tkinter.
root.title("Translator")
root.geometry("500x750")
root.configure(bg='black')

# Create a label
label_text = Label(root, text="Translator", font=("Helvetica", 40,"bold"), bg='black', fg='white')
label_text.place(x=100, y=40, height=50, width=300)

Frame1 = Frame(root, bg='black').pack(side=BOTTOM) # Create a frame for the textbox

label_text = Label(root, text="Enter Text", font=("Helvetica", 20,"bold"), bg='black', fg='gray')
label_text.place(x=10, y=120, height=20, width=150)

# Create a textbox
Source_text = Text(Frame1, font=("Helvetica", 20,"bold"), wrap=WORD, bg='gray', fg='white', bd=6) # bd is border width
Source_text.place(x=10, y=150, height=100, width=480)

# Create a combobox
list_of_language = list(LANGUAGES.values())




comb_source = ttk.Combobox(Frame1, values=list_of_language, font=("Helvetica", 20,"bold"), state="readonly")
comb_source.place(x=10, y=260, height=40, width=155)
comb_source.set("English") # Set the default value of combobox

label_text = Label(root, text="To", font=("Helvetica", 20,"bold"), bg='black', fg='gray')
label_text.place(x=170, y=260, height=40, width=45)

comb_destination = ttk.Combobox(Frame1, values=list_of_language, font=("Helvetica", 20,"bold"), state="readonly")
comb_destination.place(x=220, y=260, height=40, width=155)
comb_destination.set("English") # Set the default value of combobox

Button_change = Button(Frame1, text="Change",relief=RAISED, font=("Helvetica", 18,"bold"), bg='black', fg='white', bd=6, command=data)
Button_change.place(x=380, y=260, height=45, width=110)




# Create a heading label for the output
label_text = Label(root, text="Output", font=("Helvetica", 20,"bold"), bg='black', fg='gray')
label_text.place(x=10, y=380, height=30, width=120)

# Create a textbox for the output
Output_text = Text(Frame1, font=("Helvetica", 20,"bold"), wrap=WORD, bg='gray', fg='white', bd=6) # bd is border width
Output_text.place(x=10, y=420, height=120, width=480)


root.mainloop() # Start the event loop of the Tkinter by calling the mainloop method of the root object.