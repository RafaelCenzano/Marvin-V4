from marvin.helpers import physics
import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label

Config.set('graphics', 'resizable', 1)

kivy.require('1.11.1')

class MarvinApp(App):
   
    def build(self):
        return Label(text='Child')