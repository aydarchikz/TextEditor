from tkinter import *
from tkinter import filedialog

class FileMenu():
    #Раздел меню "файл"

    def __init__(self, main_menu, window, text_widget):
        file_btn = Menu(main_menu, tearoff=0)

        file_btn.add_command(label='Открыть (Ctrl+O)', command=lambda: self.open_file(text_widget))
        file_btn.add_command(label='Сохранить (Ctrl+S)', command=lambda: self.save_file(text_widget))

        window.config(menu=file_btn)
        main_menu.add_cascade(label='Файл', menu=file_btn)

    def open_file(self, text_widget):
        file = filedialog.askopenfilename(title='Выбор файла',
                                          filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        if file:
            text_widget.delete('1.0', END)
            text_widget.insert('1.0', open(file, encoding='utf-8').read())

    def save_file(self, text_widget):
        file = filedialog.asksaveasfilename(title='Выбор файла',
                                            filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        f = open(file, 'w', encoding='utf-8')
        text = text_widget.get('1.0', END)
        f.write(text)
        f.close()