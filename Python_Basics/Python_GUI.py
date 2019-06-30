from tkinter import *
from tkinter import Tk


def clicked(btn):
    print(btn+' clicked!!')

root = Tk()

root.title('Hello World')

root.geometry('300x300')




btn1 = Button(text='Btn1',command=clicked('Btn1'))
btn2 = Button(text='Btn2',command=clicked('Btn2'))
btn3 = Button(text='Btn3',command=clicked('Btn3'))
btn4 = Button(text='Btn4',command=clicked('Btn4'))

btn1.place(x=100,y=100)
btn2.place(x=100,y=200)
btn3.place(x=200,y=100)
btn4.place(x=200,y=200)

root.mainloop()