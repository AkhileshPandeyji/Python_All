from tkinter import *



root = Tk()

root.geometry('900x700')

root.title('Canvas')

c = Canvas(root,width=900,height=700,bg='blue',cursor='hand2')

# line
id = c.create_line(20,20,100,100,400,400,width=4,fill='red')

# circle

id = c.create_oval(100,100,300,300,width=4,fill='green',outline='white',activefill='yellow')


# ellipse

id = c.create_oval(200,100,300,300,width=4,fill='cyan',outline='white',activefill='red')


# square

id = c.create_rectangle(530,300,630,400,width=2,fill='salmon1',outline='black',activefill='white')

# rectangle

id = c.create_rectangle(500,100,650,300,width=4,fill='cyan',outline='white',activefill='red')


# text

fnt = ('MS Sans Serif',-40,'bold underline italic')
id = c.create_text(200,400,text='My First Canvas',font=fnt,fill='white')

# polygon

id = c.create_polygon(200,400,300,200,600,100,width=3,fill='darkred',outline='white',activefill='pink')


# images

file1 = PhotoImage(file="dwnload.ico")
id = c.create_image(300,460,anchor=NW,image=file1)

# arcs

id = c.create_arc(560,460,660,560,start=0,extent=310,style='pieslice',width=4,fill='orange',outline='yellow',activefill='red')


c.pack()

root.mainloop()
