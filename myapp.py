from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import load_spreadsheet
import json


class IntroductionScreen(Screen):
    pass


class InputScreen(Screen):
    def call_load_spreadsheet(self, path, selection):
        json_actions = load_spreadsheet.get_actions(selection[0])
        App.get_running_app().shared_data.json = json_actions

        print(json.dumps(App.get_running_app().shared_data.json, indent=4, sort_keys=True))


class SharedData:
    def __init__(self):
        self.json = None


class CQApp(App):
    # This class-level variable is accessible from anywhere in the code by
    # using App.get_running_app().shared_data
    # If you wanted to share more than just a string, you could add more
    # attributes to the SharedData class
    shared_data = SharedData()

    def build(self):
        return Builder.load_file("cq.kv")


if __name__ == '__main__':
    CQApp().run()