from kivymd.app import MDApp # pip install kivymd
from kivymd.uix.label import MDLabel

class MainApp(MDApp): # MainApp class & inharitance from MDApp
    def build(self): # build function with budefault object "self"
        return MDLabel(text="Hello, World!", halign="center") # MDLabel widget
    
if __name__ == "__main__": # main function to saparate the code from class
    MainApp().run() # calling MainApp class and run function

## If you convert this code to apk for Mac or Linux then you need to install buildozer
## pip install buildozer
## buildozer init

## For Windows, you can use PyInstaller
## pip install pyinstaller
## pyinstaller --onefile main.py

## or use Google Colab to convert this code to apk, its create a Linux virtual environment in Windows