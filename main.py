from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class FeedbackApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)
        label = Label(text="Student Feedback System", font_size=20)
        layout.add_widget(label)

        self.feedback_input = TextInput(hint_text="Enter your feedback here")
        layout.add_widget(self.feedback_input)

        submit_button = Button(text="Submit Feedback")
        submit_button.bind(on_press=self.submit_feedback)
        layout.add_widget(submit_button)

        return layout

    def submit_feedback(self, instance):
        feedback_text = self.feedback_input.text
        # Here, you should implement code to store the feedback data, e.g., in a database.

if __name__ == '__main__':
    FeedbackApp().run()
