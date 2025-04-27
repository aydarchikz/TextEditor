from tkinter import Menu

class FontMenu():

    def __init__(self, change_btn, text_widget, font_now):
        def change_font(font1, text_widget):
            text_widget['font'] = (font1, font_now.current_size)
            font_now.current_font = font1

        font_change_sub = Menu(change_btn, tearoff=0)
        font_change_sub.add_command(label='Consolas', command=lambda: change_font('Consolas', text_widget))
        font_change_sub.add_command(label='Times New Roman', command=lambda: change_font('Times New Roman', text_widget))
        font_change_sub.add_command(label='Calibri', command=lambda: change_font('Calibri', text_widget))
        change_btn.add_cascade(label='Шрифт', menu=font_change_sub)