from tkinter import (
  Entry,
  Button,
  LEFT,
  RIGHT,
  END,
  Tk
)
import tkinter as tk

class FindChangeWordMenu():

    def __init__(self, text_widget, is_change):
        self.find_window = Tk()
        entry_find = Entry(self.find_window)
        entry_find.pack(side=LEFT)
        if is_change:
            entry_change = Entry(self.find_window)
            entry_change.pack(side=LEFT)
            btn = Button(self.find_window, text='Заменить')
            btn.pack(side=RIGHT)
            btn.config(command=lambda: self.change_word(entry_find.get(), entry_change.get(), text_widget))
        else:
            btn = Button(self.find_window, text='Найти')
            btn.pack(side=RIGHT)
            btn.config(command=lambda: self.find_word(entry_find.get(), text_widget))

    def find_word(self, entry, text_widget):
        find_result = self.find(entry, text_widget)
        if find_result[0] != -1:
            n_lines = find_result[0]
            ind = find_result[1]
            text_widget.tag_add(tk.SEL, str(n_lines) + '.' + str(ind), str(n_lines) + '.' + str(ind + len(entry)))
            text_widget.mark_set(tk.INSERT, str(n_lines) + '.' + str(ind + len(entry)))
        self.find_window.destroy()

    def find(self, entry, text_widget):
        text = text_widget.get('1.0', END)
        lines = text.splitlines()
        n_lines = 0
        for line in lines:
            n_lines += 1
            if line:
                result = line.find(entry)
                if (result != -1):
                    return [n_lines, result]
        return [-1, -1]

    def change_word(self, entry1, entry2, text_widget):
        text = text_widget.get('1.0', END)
        lines = text.splitlines()
        text_widget.delete('1.0', END)
        for line in lines:
            line = self.replace(line, entry1, entry2) + '\n'
            text_widget.insert(END, line)
        text_widget.delete('end-1c', END)
        self.find_window.destroy()

    def replace(self, line, string1, string2):
        ind = line.find(string1)
        while (ind != -1):
            line = line[:ind] + string2 + line[ind + len(string1):]
            ind = line.find(string1)
        return line