from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

import json

from pynput.keyboard import Listener

with open("config.json") as f:
    data = json.load(f)

fold = data["cols_nb"]
keys = data["keys"]
colors = {"orange": [255/255, 165/255, 0, 1], "white": [1, 1, 1, 1], "black": [0, 0, 0, 1], "blue": [0, 110/255, 255/255, 1], "red": [240/255, 0, 0, 1], "clear_grey": [230/255, 230/255, 230/255, 1], "grey": [169/255, 169/252, 169/255, 1]}

class ShowInput(App):

    def __init__(self):
        App.__init__(self)
        Window.clearcolor = colors["grey"]
        self.current_pressed = []
        self.listener = Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        
        self.listener.start()

    def build_keys(self):
        self.keys_dict = {}
        for item in keys.keys():
            self.keys_dict[item] = Button(text=item.upper(), color=colors["black"], background_normal='', background_down='', background_color=colors["white"])
            
            self.layout.add_widget(self.keys_dict[item])



    def on_press(self, key):
        key = str(key).replace("'", "").lower()

        if key in keys.keys():
            if key not in self.current_pressed:
                self.current_pressed += [str(key)]
                self.keys_dict[key].background_color = keys[key]

    def on_release(self, key):
        key = str(key).replace("'", "").lower()

        if key in keys.keys():
            if key in self.current_pressed:
                self.current_pressed.remove(key)
                self.keys_dict[key].background_color = colors["white"]

    def build(self):
        self.layout = GridLayout(cols=min(len(keys.keys()), fold), spacing=[Window.height//100, Window.height//100], padding=[Window.height//100, Window.height//100])
        self.build_keys()

        return self.layout

if __name__ == '__main__':
    ShowInput().run()