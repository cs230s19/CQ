from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

class IntroductionScreen(Screen):
    pass


class InputScreen(Screen):
    def button_function(self):
        shared_data = App.get_running_app().shared_data
        shared_data.text += self.ids.input.text + '\n'

        self.ids.input.text = ''

        introduction_screen = self.manager.get_screen('introduction')
        introduction_screen.ids.input.text = shared_data.text


class SharedData:
    def __init__(self):
        self.text = ''


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