#! -*- coding:utf-8 -*-

import tkinter
import tkinter.messagebox

def tkinker_test():
    flag = True

    def change_label_text():
        nonlocal flag
        flag = not flag

        color, msg = ('red', "hello world")\
            if flag else ('blue', 'goodbye world')
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('tips', "wanna quit?"):
            top.quit()


    top = tkinter.Tk()
    top.geometry('240x160')
    top.title('test')
    label = tkinter.Label(top, text="hi", font='Arial-32', fg='black')
    label.pack(expand=1)
    panel = tkinter.Frame(top)
    b1 = tkinter.Button(panel, text='modify', command=change_label_text)
    b1.pack(side='left')
    b2 = tkinter.Button(panel, text='quit', command=confirm_to_quit)
    b2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()


if __name__ == "__main__":
    tkinker_test()