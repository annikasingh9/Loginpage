from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
Builder.load_file("LoginPage.kv")



class LoginPageApp(App):
    def build(self):
        return LoginManager()

class LoginManager(ScreenManager):
    pass

class Question1Screen(Screen):
    def answer_question(self, bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "error"

class Question2Screen(Screen):
    def answer_question(self,bool):
        if bool:
            self.mananger.current = "correct"
        else:
            self.manager.current = "error"
class CorrectScreen(Screen):
    def forward(self):
        self.manager.current = "question 2"

class ErrorScreen(Screen):
    pass

if __name__ == "__main__":
    LoginPageApp().run()