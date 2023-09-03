from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock


class ShoppingListApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.display = None
        self.input = None
        self.shopping_list_layout = None
        self.shopping_list = []

    def build(self):
        self.title = 'Shopping List'
        root = BoxLayout(orientation='vertical', padding=10)

        # Input and buttons
        input_layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=0.2)
        self.input = TextInput(hint_text='Enter an item', multiline=False)
        self.input.focus = True

        button_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=0.1)
        add_button = Button(text='Add Item')
        clear_button = Button(text='Clear List')

        add_button.bind(on_press=self.add_item)
        self.input.bind(on_text_validate=self.add_item)  # Capture Enter key press
        clear_button.bind(on_press=self.clear_list)

        input_layout.add_widget(self.input)
        button_layout.add_widget(add_button)
        button_layout.add_widget(clear_button)
        root.add_widget(input_layout)
        root.add_widget(button_layout)

        # Display and Shopping List area
        display_layout = GridLayout(cols=1, spacing=5, padding=10, size_hint_y=1)
        self.display = Label(text='Your shopping list is empty.', size_hint_y=None, height=30)

        self.shopping_list_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.shopping_list_layout.bind(minimum_height=self.shopping_list_layout.setter('height'))

        scroll_view = ScrollView()
        scroll_view.add_widget(self.shopping_list_layout)

        display_layout.add_widget(self.display)
        display_layout.add_widget(scroll_view)

        root.add_widget(display_layout)

        return root

    def add_item(self, instance):
        item = self.input.text.strip()
        if item:
            self.shopping_list.append(item)
            self.input.text = ''
            self.update_display()

        # Schedule a focus change after a short delay
        Clock.schedule_once(self.change_focus, 0.2)

    def change_focus(self, dt):
        self.input.focus = True

    def clear_list(self, instance):
        self.shopping_list = []
        self.update_display()

    def update_display(self):
        self.shopping_list_layout.clear_widgets()
        if self.shopping_list:
            for item in self.shopping_list:
                self.shopping_list_layout.add_widget(Label(text=item, size_hint_y=None, height=30))
            self.display.text = ''
        else:
            self.display.text = 'Your shopping list is empty.'


if __name__ == '__main__':
    from kivy.core.window import Window

    Window.size = (400, 600)  # Set the initial window size
    ShoppingListApp().run()
