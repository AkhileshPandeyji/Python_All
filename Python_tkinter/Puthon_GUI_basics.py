# Basic flow
from tkinter import *
import time
from tkinter.ttk import Combobox


def say_hi():
    Label(window,text='Hello or Hi there!!',font=('Algerian bold',10),fg='white',bg='blue').grid(column=0,row=2)


def login():
    if password.get() == '123':
        l1.configure(text=username.get()+' successfully joined')
    else:
        l1.configure(text='Invalid Password')


def showmessage():
    messagebox.showwarning("Successful","You successfully logged in")


def event_1(event):
    Label(window,text='Right Button clicked').grid(column=4,row=9)


def event_2(event):
    Label(window, text='left Button clicked').grid(column=4, row=9)


def event_3(event):
    Label(window, text='Middle Button clicked').grid(column=4, row=9)


window = Tk()

window.title('LoginForm')

window.geometry('300x300')

# window.iconbitmap('dwnload.ico')


# time.sleep(5)
# window.destroy()

# widgets

# 1. Label
l1 = Label(window,text = 'GUI ',font = ('Arial bold',10),bg='red')
l1.grid()

# 2. Button
hello_btn = Button(window,text='Greet!',fg='red',bg='white',command=say_hi)
hello_btn.grid(column=0,row=1)

# 3. Entry
username_l = Label(window,text='User Name:',font=('Arial bold',10))
username_l.grid(column = 0,row = 3)

username = Entry(window,width=20)
username.grid(column = 1,row = 3)

password_l = Label(window,text='Password:',font=('Arial bold',10))
password_l.grid(column = 0,row = 4)

password = Entry(window,width=20)
password.grid(column = 1,row = 4)

password_t = password.get()

submit = Button(window,text='Login',command = login)
submit.grid(column = 1,row = 5)

# 4. combobox

combo = Combobox(window)
combo['values'] = ['Male','Female']
combo.current(1)
combo.grid(column = 0,rowspan=2)

# 5. checkButton

chck_state = BooleanVar()
chck_state.set(True)
chck = Checkbutton(window,text='Keep me logged in',var =chck_state)
chck.grid()

# 6. messagebox

from tkinter import messagebox

b2 = Button(window,text='Message',command=showmessage)
b2.grid()

# 7.Radiobutton

rad1 = Radiobutton(window,text="Videos",value=1)
rad2 = Radiobutton(window,text="Music",value=2)
rad3 = Radiobutton(window,text="Games",value=3)
rad4 = Radiobutton(window,text="All",value=4)

rad1.grid()
rad2.grid()
rad3.grid()
rad4.grid()

# 8. Images

icon = PhotoImage(file="dwnload.ico")
l3 = Label(window,image=icon)
l3.grid()

# 9. scrolledText

from tkinter import scrolledtext

stxt = scrolledtext.ScrolledText(window,width=40,height=20)
stxt.insert(INSERT,"""

############################################################# WELCOME ########################################

###############################################################################################################
""")
stxt.grid(column=5,row=6)

# 10. spinbox

spin = Spinbox(window,from_=100,to=200,width=20)
spin.grid(column=5,row=7)

# 11.Binding functions seen already

# 12. EventHandling

btn = Button(window,text='click to close window',bg='yellow')
btn.bind('<Button-1>',event_1)
btn.bind('<Button-3>',event_2)
btn.bind('<Button-2>',event_3)

btn.grid(column=5,row=8)

window.mainloop()


