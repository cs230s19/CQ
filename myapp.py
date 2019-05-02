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
        self.json = [{"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "10", "Strategy": "None", "Action": "None", "Repeat?": "No", "Action and Category": "Sign up for the CQ Mobile App!"}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "2", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Start a list of 3 ways you can gain more enjoyment from your intercultural interactions."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "2", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Start a list of 3 ways you can connext your existing interests with an intercultural interest. "}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "2", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Brainstorm new insights you can by increased exposure to different cultures."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "2", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Think of one way your intercultural experience can benefit someone else."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "5", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Create a way to share your access to an intercultural network with someone else."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "3", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Share with a friend the benefits you think they could gain from learning about cultural differences."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "3", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Research a new cultural group and the impact of friending them. "}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "1", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Invite someone from a different cultural background than you to share a meal."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "2", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Have a meal with someone who has a very different background than you. "}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "3", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Compare notes with someone on cultural similarities and differences."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "2", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Recall a time when you felt out of your element, but ended up succeeding. Write down what led to your success and compare it to interacting effectively with someone from a different culture."}, {"Knowledge": "3", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Read a country profile on the BBC News website before traveling to that country."}, {"Knowledge": "3", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Read a country profile on the BBC News website before meeting with someone from that country."}, {"Knowledge": "2", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Refer to a travel  guidebook to learn more about a country."}, {"Knowledge": "2", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Read an article about a current event in a foreign country."}, {"Knowledge": "3", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Talk with someone from a different country about a current event happening in their country."}, {"Knowledge": "2", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Pick a value and read about different culture's attitudes surrounding that value."}, {"Knowledge": "3", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Speak to someone from a different culture about a particular value and compare and contrast value or belief systems."}, {"Knowledge": "2", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "When you use an idiom, stop and think about how you could say the same thing without using an idiom that people from other cultures might not understand."}, {"Knowledge": "2", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Identify an ethnocentric bias toward a particular culture in a remark someone makes or in something you read or watch."}, {"Knowledge": "3", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "None", "Action and Category": "Point out (in a nonjudgmental way) an ethnocentric bias toward a particular cultureto the person making the remark."}, {"Knowledge": "1", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Study a foreign language independently. 1 pt each day you study."}, {"Knowledge": "10", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Take a foreign language class. 10 points each week you study."}, {"Knowledge": "500", "Maximum?": "2", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Study a foreign language while studying in a culture that speaks that language. 500 pts each semester"}, {"Knowledge": "20", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "No", "Action and Category": "Read Expand Your Borders (Livermore, 2013)  (available from the library) to get an overview of the 10 largest cultural clusters globally. "}, {"Knowledge": "10", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Spend a month seeing how much you can learn about a different country or region."}, {"Knowledge": "3", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Learn basic vocabularly for a new language. Focus on words and expressions that would help you build rapport with individual who use that language."}, {"Knowledge": "2", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Practice basic vocabulary for a new language with someone who uses that language."}, {"Knowledge": "3", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "Yes", "Action and Category": "Discuss similarities and differences in several idioms  with someone who speaks a different language. Explore what that reveals about cultural differences."}, {"Knowledge": "20", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "No", "Action and Category": "Read Leading with Cultural Intelligence (Livermore, 1015) to gain specific insighs for how leadership varies between different cultures (national, regional, organizational, etc.)"}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "5", "Action": "None", "Repeat?": "Yes", "Action and Category": "Develop an if-then strategy to anticipate multiple ways to address a reoccuring intercultural dilemma. "}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "2", "Action": "None", "Repeat?": "Yes", "Action and Category": "Find a cultural coach to help you make sense of culturally unfamiliar place. 2 pt per meeting"}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "1", "Action": "None", "Repeat?": "Yes", "Action and Category": "Read up on how to behave in a new cultural situation."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "1", "Action": "None", "Repeat?": "Yes", "Action and Category": "Take an implicit bias test at Projectimplicit.org and reflect on the experience.  1 pt per test"}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "2", "Action": "None", "Repeat?": "Yes", "Action and Category": "Speak with someone about what you learned from an implicit bias test result. "}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "3", "Action": "None", "Repeat?": "Yes", "Action and Category": "Ask someone from a particular culture to explain something that occurred during a crosscultural encounter andmake a plan to handle the situation better the next time."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "3", "Action": "None", "Repeat?": "Yes", "Action and Category": "Immerse yourself in a different cultural environment by visiting an ethnic grocery store and purchasing ingredients to make an ethnic meal."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "3", "Action": "None", "Repeat?": "Yes", "Action and Category": "Pay attention to the nonverbal communication during a meeting with diverse participants. Write down what you observed and seek out answers for actions and reactions."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "3", "Action": "None", "Repeat?": "Yes", "Action and Category": "Ask someone for feedback about the way you handle a crosscultural interaction. Elicit their help for planning a different strategy for future interactions."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "2", "Action": "None", "Repeat?": "Yes", "Action and Category": "Think about a behavior you've observed in an individual from a different culture. Research to see whether this behavior is somewhat typical among individuals from this culture or unrelated to their cultural background."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "3", "Repeat?": "Yes", "Action and Category": "If appropriate, sow down when speaking to someone to a non native language speaker."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "3", "Repeat?": "Yes", "Action and Category": "Modify how close or far apart you stand hwen interacting with people from a different culture."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "3", "Repeat?": "Yes", "Action and Category": "Modify the way you disagree with others to fit into the cultural setting."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "1", "Repeat?": "Yes", "Action and Category": "Greet someone from a different culture  in the culturally appropriate manner for their country."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "3", "Repeat?": "Yes", "Action and Category": "Use nonverbal behavior appropriate to a different culture when interacting with individuals from that country."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "3", "Repeat?": "Yes", "Action and Category": "Practice voicing your opinion on an important topic in an indirect way and a direct way. Practice wieht someone whose preference for direct/indirect communication is opposite yours."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "3", "Repeat?": "Yes", "Action and Category": "Get a group of individuals together, and practice nonverbal behaviors that are uncomfortable for members of the group."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "2", "Repeat?": "Yes", "Action and Category": "Eat at an ethnic restaurant and order something you've never tried."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "2", "Repeat?": "Yes", "Action and Category": "Watch a film that takes place in a different country (or different time period) and discuss cultural differences or similaries you see."}, {"Knowledge": "None", "Maximum?": "None", "Times Completed": 0, "Drive": "None", "Strategy": "None", "Action": "None", "Repeat?": "None", "Action and Category": "Their own activity (in each category)"}]


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
        actions = json.loads(App.get_running_app().shared_data.json)

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
        actions = json.loads(App.get_running_app().shared_data.json)


        for index in range(len(actions)):
            btn_label =  "{}:{}".format(index + 1, actions[index]["Action and Category"])
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
        App.get_running_app().shared_data.json = json_actions

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
                if action['Times Completed'] > 1:
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

