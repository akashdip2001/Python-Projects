from tkinter import *
from tkinter import ttk


root = Tk() 
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

# Adjust the corner radius of the Text widget
# Note: Tkinter Text widget does not support corner radius directly.
# You can use a Canvas widget to create a rounded rectangle and place the Text widget on top of it.

canvas = Canvas(root, bg='black', highlightthickness=0)
canvas.place(x=10, y=150, height=100, width=480)

# Create a rounded rectangle on the canvas
radius = 20  # Adjust the radius as needed
x0, y0, x1, y1 = 0, 0, 480, 100
canvas.create_arc((x0, y0, x0 + radius, y0 + radius), start=90, extent=90, fill='gray', outline='gray')
canvas.create_arc((x1 - radius, y0, x1, y0 + radius), start=0, extent=90, fill='gray', outline='gray')
canvas.create_arc((x0, y1 - radius, x0 + radius, y1), start=180, extent=90, fill='gray', outline='gray')
canvas.create_arc((x1 - radius, y1 - radius, x1, y1), start=270, extent=90, fill='gray', outline='gray')
canvas.create_rectangle((x0 + radius / 2, y0, x1 - radius / 2, y1), fill='gray', outline='gray')
canvas.create_rectangle((x0, y0 + radius / 2, x1, y1 - radius / 2), fill='gray', outline='gray')

# Place the Text widget on top of the canvas
Source_text.place(x=10, y=150, height=100, width=480)

# Create a combobox
list_of_language = ["English","Bengali","Hindi","Spanish","French","German","Italian","Japanese","Korean","Dutch","Polish","Portuguese","Russian","Chinese"]

comb_source = ttk.Combobox(Frame1, values=list_of_language, font=("Helvetica", 20,"bold"), state="readonly")
comb_source.place(x=10, y=260, height=40, width=155)
comb_source.set("English") # Set the default value of combobox

label_text = Label(root, text="To", font=("Helvetica", 20,"bold"), bg='black', fg='gray')
label_text.place(x=170, y=260, height=40, width=45)

comb_destination = ttk.Combobox(Frame1, values=list_of_language, font=("Helvetica", 20,"bold"), state="readonly")
comb_destination.place(x=220, y=260, height=40, width=155)
comb_destination.set("English") # Set the default value of combobox

Button_change = Button(Frame1, text="Change",relief=RAISED, font=("Helvetica", 18,"bold"), bg='black', fg='white', bd=6)
Button_change.place(x=380, y=260, height=45, width=110)




# Create a heading label for the output
label_text = Label(root, text="Output", font=("Helvetica", 20,"bold"), bg='black', fg='gray')
label_text.place(x=10, y=380, height=30, width=120)

# Create a textbox for the output
Output_text = Text(Frame1, font=("Helvetica", 20,"bold"), wrap=WORD, bg='gray', fg='white', bd=6) # bd is border width
Output_text.place(x=10, y=420, height=120, width=480)


root.mainloop() # Start the event loop of the Tkinter by calling the mainloop method of the root object.