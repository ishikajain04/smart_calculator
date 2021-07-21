/* FRONT END */


from tkinter import *
win=Tk()
win.geometry( '500x300' )
win.title('Smart Pugger')
win.configure(bg='lightblue')
l1=Label(win,text='I am a Smart Calculator',width=20,padx=3)
l1.place(x=150,y=10)

l2=Label(win,text='My namr is Pugger',padx=3)
l2.place(x=180,y=40)

l3=Label(win,text='What can I help you',padx=3)
l3.place(x=176,y=130)

textin=StringVar()
e1=Entry(win,width=30,textvariable=textin)
e1.place(x=100,y=160)
b1=Button(win,text='Just This')
b1.place(x=210,y=200)

list=Listbox(win,width=20,height=3)
list.place(x=150,y=230)

win.mainloop()
