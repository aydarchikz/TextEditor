from tkinter import *

from file_menu import *
from change_menu import *
class CreateMenu():
    #Создание меню

    def __init__(self, window, text_widget, font_now):
        main_menu = Menu(window)

        file_btn = FileMenu(main_menu, window, text_widget)
        change_btn = ChangeMenu(main_menu, window, text_widget, font_now)

        window.config(menu=main_menu)