from kivy.config import Config
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty
from kivy.storage.jsonstore import JsonStore
import load_spreadsheet
import json


class SharedData:
    """
    A class designed to hold data that needs to be access by multiple app
    screens.
    """
    def __init__(self):
        """
        Initialize the SharedData class by creating an attribute called json.
        """
        self.json = None
        self.jstore = JsonStore('.CQ.json')


class DashboardScreen(Screen):
    """
    Contains an overview of what the user achieved
    """
    recap_text = StringProperty('')


class ActionListScreen(Screen):
    action = StringProperty('')
    """
    Contains a scrolling list of buttons
    """
    def btn_callback(self, instance):
        actions = App.get_running_app().shared_data.json

        index = int(instance.text.split(':')[0]) - 1
        action = actions[index]

        result = '{}:\n\n'.format(action["Action and Category"])
        if action["Repeat?"] != "No":
            result += "This action is repeatable\n"
        if action['Times Completed']:
            result += "this action has been completed {} times.\n".format(action['Times Completed'])
        if action['Drive']:
            result += "this action will result in {} Drive point(s).\n".format(action['Drive'])
        if action['Knowledge']:
            result += "this action will result in {} Knowledge point(s).\n".format(action['Knowledge'])
        if action['Strategy']:
            result += "this action will result in {} Strategy point(s).\n".format(action['Strategy'])
        if action['Action']:
            result += "this action will result in {} Action point(s).\n".format(action['Action'])

        self.action = result
        self.manager.current = 'ActionScreen'

    def start(self):
        actions = App.get_running_app().shared_data.json


        for index in range(len(actions)):
            btn_label = "{}:{}".format(index + 1, actions[index]["Action and Category"])
            if len(btn_label) > 43:
                btn_label = btn_label[:41]
                btn_label += "..."

            btn = Button(text=btn_label, size_hint_y=None,
                         height=40, on_release= self.btn_callback)
            self.ids.content.add_widget(btn)

        self.ids.content.size_hint_y = 20


class ActionScreen(Screen):
    """
    Contains the information available about a specific action
    """
    action_text = StringProperty('')


class FileSelectorPopup(FloatLayout):
    """
    A class that creates a popup screen containing a FileChooser.
    """
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class IntroductionScreen(Screen):
    """
    A welcome screen for a new user. Gives an introductory message and prompts
    the user to upload a spreadsheet from their instructor.
    """
    loadfile = ObjectProperty(None)
    recap = StringProperty('')

    def dismiss_popup(self):
        """
        Close popup.
        :return: None
        """
        self._popup.dismiss()

    def show_load(self):
        """
        Create popup window that displays FileChooser widget, allowing a user
        to select and load a spreadsheet.
        :return: None
        """
        content = FileSelectorPopup(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, selection):
        """
        Get the json representation of an excel file when given that file's
        path. Exit popup window and transition to the next screen.
        :param selection: An array containing one element: the path of an excel
         file
        :return: None
        """
        json_actions = load_spreadsheet.get_actions(selection[0])
        App.get_running_app().shared_data.json = json.loads(json_actions)

        print(type(App.get_running_app().shared_data.json))

        self.dismiss_popup()

    def dashboard_transition(self):
        actions = App.get_running_app().shared_data.json

        max_drive = 0
        max_knowledge = 0
        max_strategy = 0
        max_action = 0

        current_drive = 0
        current_knowledge = 0
        current_strategy = 0
        current_action = 0

        actions_available = 0
        actions_completed = 0
        actions_performed = 0

        for action in actions:
            if action['Repeat?'] == 'No':
                actions_available += 1
                if action['Times Completed'] == 1:
                    actions_completed += 1
                    actions_performed += 1

                    if action['Drive'] != 'None':
                        max_drive += int(action['Drive'])
                        current_drive += int(action['Drive'])
                    if action['Knowledge'] != 'None':
                        max_knowledge += int(action['Knowledge'])
                        current_knowledge += int(action['Knowledge'])
                    if action['Strategy'] != 'None':
                        max_strategy += int(action['Strategy'])
                        current_strategy += int(action['Strategy'])
                    if action['Action'] != 'None':
                        max_action += int(action['Action'])
                        current_action += int(action['Action'])
                else:
                    if action['Drive'] != 'None':
                        max_drive += int(action['Drive'])
                    if action['Knowledge'] != 'None':
                        max_knowledge += int(action['Knowledge'])
                    if action['Strategy'] != 'None':
                        max_strategy += int(action['Strategy'])
                    if action['Action'] != 'None':
                        max_action += int(action['Action'])

            else:
                actions_available += 1
                if action['Times Completed'] > 1:
                    actions_completed += 1
                    actions_performed += action['Times Completed']

                    if action['Drive'] != 'None':
                        max_drive += action['Times Completed'] * int(action['Drive'])
                        current_drive += action['Times Completed'] * int(action['Drive'])
                    if action['Knowledge'] != 'None':
                        max_knowledge += action['Times Completed'] * int(action['Knowledge'])
                        current_knowledge += action['Times Completed'] * int(action['Knowledge'])
                    if action['Strategy'] != 'None':
                        max_strategy += action['Times Completed'] * int(action['Strategy'])
                        current_strategy += action['Times Completed'] * int(action['Strategy'])
                    if action['Action'] != 'None':
                        max_action += action['Times Completed'] * int(action['Action'])
                        current_action += action['Times Completed'] * int(action['Action'])
                else:
                    if action['Drive'] != 'None':
                        max_drive += int(action['Drive'])
                    if action['Knowledge'] != 'None':
                        max_knowledge += int(action['Knowledge'])
                    if action['Strategy'] != 'None':
                        max_strategy += int(action['Strategy'])
                    if action['Action'] != 'None':
                        max_action += int(action['Action'])

            result = "This screen allows you to keep track of your progress.\n\n"

            result += "Out of the available {} actions".format(actions_available)
            result += ", you have performed {} actions".format(actions_performed)
            result += " and completed {} actions.\n".format(actions_completed)
            result += "You have gathered {} out of {} drive points.\n".format(current_drive, max_drive)
            result += "You have gathered {} out of {} knowledge points.\n".format(current_knowledge, max_knowledge)
            result += "You have gathered {} out of {} strategy points.\n".format(current_strategy, max_strategy)
            result += "You have gathered {} out of {} action points.\n".format(current_action, max_action)
            print(result)

        self.recap = result
        self.manager.current = 'DashboardScreen'

    def actionlist_transition(self):
        self.manager.current = 'ActionListScreen'

class CQApp(App):
    """
    The overall app class.
    """
    # attribute for sharing data across screens
    shared_data = SharedData()


if __name__ == '__main__':
    Config.set('graphics', 'resizable', 0)
    Window.size = (350, 650)
    CQApp().run()

