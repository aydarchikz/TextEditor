from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from create_menu import *
class CreateTextEditor():
    #Создание текстового редактора

    def __init__(self):
        #Создание окна и настройка текствого виджета
        window = Tk()
        window.title('Текстовый редактор')
        window.geometry('1000x500')
        window.overrideredirect(False)
        window.bind("<Control-KeyPress>", self.keypress)

        f_text = Frame(window)
        f_text.pack(fill=BOTH, expand=1)

        self.text_widget = Text(f_text,
                         bg='gray15',
                         fg='white',
                         padx=10,
                         pady=10,
                         wrap=WORD,
                         insertbackground='white',
                         spacing3=10,
                         width=10,
                         font='Consolas 11'
                         )
        self.text_widget.pack(fill=BOTH, expand=1, side=LEFT)

        #Создание полосы прокрутки
        scroll = Scrollbar(f_text, command=self.text_widget.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.text_widget.config(yscrollcommand=scroll.set)

        #Создание меню
        font_now = FontNow()
        menu = CreateMenu(window, self.text_widget, font_now)

        #Предупреждение при выходе
        def on_close():
            answer = messagebox.askokcancel('Выход', 'Действительно хотите закрыть окно?')
            if answer:
                window.destroy()

        window.protocol('WM_DELETE_WINDOW', on_close)
        window.mainloop()

    #Настройка горячих клавиш
    def keypress(self, event):
        if event.keycode == 86:
            event.widget.event_generate('<<Paste>>')
        elif event.keycode == 67:
            event.widget.event_generate('<<Copy>>')
        elif event.keycode == 88:
            event.widget.event_generate('<<Cut>>')
        elif event.keycode == 65:
            event.widget.event_generate('<<SelectAll>>')
        elif event.keycode == 79:
            event.widget.event_generate(self.open_file(self.text_widget))
        elif event.keycode == 83:
            event.widget.event_generate(self.save_file(self.text_widget))

    #Функции открытия и сохранения файла для горячих клавиш
    def open_file(self, text_widget):
        file = filedialog.askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        if file:
            text_widget.delete('1.0', END)
            text_widget.insert('1.0', open(file, encoding='utf-8').read())

    def save_file(self, text_widget):
        file = filedialog.asksaveasfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
        f = open(file, 'w', encoding='utf-8')
        text = text_widget.get('1.0', END)
        f.write(text)
        f.close()