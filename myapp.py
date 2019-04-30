from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import load_spreadsheet
import json


class DashboardScreen(Screen):
    """
    Contains an overview of what the user achieved
    """
    actions = json.loads(App.get_running_app().shared_data.json)

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

                if action['Drive']:
                    max_drive += int(action['Drive'])
                    current_drive += int(action['Drive'])
                if action['Knowledge']:
                    max_knowledge += int(action['Knowledge'])
                    current_knowledge += int(action['Knowledge'])
                if action['Strategy']:
                    max_strategy += int(action['Strategy'])
                    current_strategy += int(action['Strategy'])
                if action['Action']:
                    max_strategy += int(action['Action'])
                    current_strategy += int(action['Action'])

        else:
            actions_available += 1
            if action['Times Completed'] != 1:
                actions_completed += 1
                actions_performed += action['Times Completed']

                if action['Drive']:
                    max_drive += action['Times Completed'] * int(action['Drive'])
                    current_drive += action['Times Completed'] * int(action['Drive'])
                if action['Knowledge']:
                    max_knowledge += action['Times Completed'] * int(action['Knowledge'])
                    current_knowledge += action['Times Completed'] * int(action['Knowledge'])
                if action['Strategy']:
                    max_strategy += action['Times Completed'] * int(action['Strategy'])
                    current_strategy += action['Times Completed'] * int(action['Strategy'])
                if action['Action']:
                    max_strategy += action['Times Completed'] * (action['Action'])
                    current_strategy += action['Times Completed'] * int(action['Action'])

        result = "This screen allows you to keep track of your progress.\n\n"

        result += "Out of the available {} actions".format(actions_available)
        result += ", you have performed {} actions".format(actions_performed)
        result += " and completed {} actions.\n".format(actions_completed)
        result += "You have gathered {} out of {} drive points.\n".format(current_drive, max_drive)
        result += "You have gathered {} out of {} knowledge points.\n".format(current_knowledge, max_knowledge)
        result += "You have gathered {} out of {} strategy points.\n".format(current_strategy, max_strategy)
        result += "You have gathered {} out of {} action points.\n".format(current_action, max_action)


class ActionListScreen(Screen):
    """
    Contains a scrolling list of buttons
    """
    actions = json.loads(App.get_running_app().shared_data.json)

    for action in actions:
        raise NotImplementedError


class ActionScreen(Screen):
    """
    Contains the information available about a specific action
    """
    raise NotImplementedError


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