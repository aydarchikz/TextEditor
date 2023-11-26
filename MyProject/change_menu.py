from change_size import *
from change_font import *
from find_change_word import *

class ChangeMenu():

    def __init__(self, main_menu, window, text_widget, font_now):
        change_btn = Menu(main_menu, tearoff=0)

        change_btn.add_command(label='Поиск', command=lambda: self.find_change(text_widget, False))
        change_btn.add_command(label='Замена', command=lambda: self.find_change(text_widget, True))

        change_btn.add_separator()

        size_change_sub = SizeMenu(change_btn, text_widget, font_now)
        font_change_sub = FontMenu(change_btn, text_widget, font_now)

        window.config(menu=change_btn)
        main_menu.add_cascade(label='Изменить', menu=change_btn)

    def find_change(self, text_widget, is_change):
        button = FindChangeWordMenu(text_widget, is_change)

class FontNow():

    current_font = 'Consolas'
    current_size = 11