from marvin.helpers import physics
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class MarvinApp(App):
 
    def build(self):
 
        return Label(text="Hello Kivy!")