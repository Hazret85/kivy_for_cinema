from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.gridlayout import GridLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import BooleanProperty
from kivy.core.text import LabelBase
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
import webbrowser


class MenuButton(ToggleButton):
    pass


class CustomButton(ButtonBehavior, Label):
    pass

LabelBase.register(name='Roboto',
                   fn_regular='Roboto-Bold.ttf')

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Используем MarkupLabel для поддержки форматирования
        title = Label(
            text="[color=ff3333][b]Н[/b][/color]"
                 "[color=33ff33][i]а[/i][/color]"
                 "[color=3333ff]з[/color]"
                 "[color=ff66ff]в[/color]"
                 "[color=ffff33]а[/color]"
                 "[color=66ffff]н[/color]"
                 "[color=ff9933]и[/color]"
                 "[color=cc33ff]е[/color]"
                 "[color=cc33cc] [/color]"
                 "[color=33cc33]к[/color]"
                 "[color=cc9933]и[/color]"
                 "[color=3399ff]н[/color]"
                 "[color=ff6699]о[/color]"
                 "[color=66cc66]т[/color]"
                 "[color=cc99cc]е[/color]"
                 "[color=9966ff]а[/color]"
                 "[color=cc9966]т[/color]"
                 "[color=ccff99]р[/color]"
                 "[color=ffcc00]а[/color]",
            font_size=32, font_name='Roboto', size_hint=(1, 0.2),
            halign='center', valign='middle', markup=True
        )
        title.bind(size=title.setter('text_size'))

        content = Label(text='Главная страница\nТекст под заголовком', size_hint=(1, 0.6))

        footer_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        left_footer = Label(text='Адрес кинотеатра:\n г Семей, ул Абая 63 ', size_hint=(0.5, 1), halign='left', valign='middle')
        right_footer = Label(text='Настоящее приложение сделано и разработано энтузиастами Python', size_hint=(0.5, 1),
                             halign='right', valign='middle')

        left_footer.bind(size=left_footer.setter('text_size'))
        right_footer.bind(size=right_footer.setter('text_size'))

        footer_layout.add_widget(left_footer)
        footer_layout.add_widget(right_footer)

        layout.add_widget(title)
        layout.add_widget(content)
        layout.add_widget(footer_layout)

        self.add_widget(layout)

class ClickableImage(ButtonBehavior, Image):
    def __init__(self, url, **kwargs):
        super(ClickableImage, self).__init__(**kwargs)
        self.url = url

    def on_press(self):
        webbrowser.open(self.url)

class PostersScreen(Screen):
    def __init__(self, **kwargs):
        super(PostersScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        # Заголовок
        layout.add_widget(Label(text='Афиши', font_size=32, size_hint=(1, 0.2)))

        # Контейнер для изображений
        images_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        images_layout.bind(minimum_height=images_layout.setter('height'))

        # Добавляем изображения с привязкой к URL YouTube
        images_layout.add_widget(ClickableImage(source='movie.jpg', size_hint_y=None, height=200,
                                                url='https://www.youtube.com/watch?v=trailer1'))
        images_layout.add_widget(ClickableImage(source='movies2.jpg', size_hint_y=None, height=200,
                                                url='https://www.youtube.com/watch?v=trailer2'))
        images_layout.add_widget(ClickableImage(source='movies3.jpg', size_hint_y=None, height=200,
                                                url='https://www.youtube.com/watch?v=trailer3'))
        images_layout.add_widget(ClickableImage(source='movies4.jpg', size_hint_y=None, height=200,
                                                url='https://www.youtube.com/watch?v=trailer4'))

        # Прокрутка для изображений, если их много
        scroll_view = ScrollView(size_hint=(1, 0.8))
        scroll_view.add_widget(images_layout)

        layout.add_widget(scroll_view)
        self.add_widget(layout)


class ScheduleScreen(Screen):
    def __init__(self, **kwargs):
        super(ScheduleScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Расписание', font_size=32))
        self.add_widget(layout)


class BuyTicketScreen(Screen):
    def __init__(self, **kwargs):
        super(BuyTicketScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text='Купить билет', font_size=32))
        self.add_widget(layout)


class MyScreenManager(ScreenManager):
    menu_open = BooleanProperty(False)

    def toggle_menu(self):
        self.menu_open = not self.menu_open
        if self.menu_open:
            self.transition = SlideTransition(direction='right')
            self.current = 'menu'
        else:
            self.transition = SlideTransition(direction='left')
            self.current = 'main'


class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = GridLayout(cols=1, spacing=10, padding=10)
        layout.add_widget(Button(text='Главная страница', on_press=self.go_to_main))
        layout.add_widget(Button(text='Афиши', on_press=self.go_to_posters))
        layout.add_widget(Button(text='Расписание', on_press=self.go_to_schedule))
        layout.add_widget(Button(text='Купить билет', on_press=self.go_to_buy_ticket))
        self.add_widget(layout)

    def go_to_main(self, instance):
        self.manager.current = 'main'

    def go_to_posters(self, instance):
        self.manager.current = 'posters'

    def go_to_schedule(self, instance):
        self.manager.current = 'schedule'

    def go_to_buy_ticket(self, instance):
        self.manager.current = 'buy_ticket'


class MainApp(App):
    def build(self):
        sm = MyScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(PostersScreen(name='posters'))
        sm.add_widget(ScheduleScreen(name='schedule'))
        sm.add_widget(BuyTicketScreen(name='buy_ticket'))
        sm.add_widget(MenuScreen(name='menu'))

        main_layout = BoxLayout()
        menu_button = MenuButton(text='Меню', size_hint=(0.1, 1), on_press=lambda x: sm.toggle_menu())
        main_layout.add_widget(menu_button)
        main_layout.add_widget(sm)

        return main_layout


if __name__ == '__main__':
    MainApp().run()
