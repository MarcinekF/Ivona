from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_file('Screens/ProfileScreen/ProfileScreenLayout.kv')
Window.size = (300, 500)

class ProfileGridLayout(Screen):

    def function(self):
        pass