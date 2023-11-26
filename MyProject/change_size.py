from tkinter import Menu

class SizeMenu():

    def __init__(self, change_btn, text_widget, font_now):
        def change_size(size):
            text_widget['font'] = (font_now.current_font, size)
            font_now.current_size = size

        size_change_sub = Menu(change_btn, tearoff=0)
        size_change_sub.add_command(label='8', command=lambda: change_size(8))
        size_change_sub.add_command(label='9', command=lambda: change_size(9))
        size_change_sub.add_command(label='10', command=lambda: change_size(10))
        size_change_sub.add_command(label='11', command=lambda: change_size(11))
        size_change_sub.add_command(label='12', command=lambda: change_size(12))
        size_change_sub.add_command(label='14', command=lambda: change_size(14))
        size_change_sub.add_command(label='16', command=lambda: change_size(16))
        size_change_sub.add_command(label='18', command=lambda: change_size(18))
        size_change_sub.add_command(label='20', command=lambda: change_size(20))
        size_change_sub.add_command(label='22', command=lambda: change_size(22))
        size_change_sub.add_command(label='24', command=lambda: change_size(24))
        change_btn.add_cascade(label='Размер текста', menu=size_change_sub)