/* SMART CALCULATOR */


from tkinter import *

def add (a,b):
    return a+b
def sub (a,b):
    return a-b
def mul (a,b):
    return a*b
def div (a,b):
    return a/b
def mod(a,b):
    return a%b
def lcm (a,b):
    L=a if a>b else b
    while L<=a+b:
        if L%a==0 and L%b==0:
         return L
    L+=1
def hcf (a,b):
    H=a if a>b else b
    while H>=1:
        if H%a==0 and b%H==0:
         return H
    H-=1


def extract_from_text(text):
    l=[]
    for t in text.split(' '):
        try :
            l.append(float(t))
        except ValueError:
            pass
    return l

def calculate():
    text=textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_from_text(text)
                r=operations[word.upper()](l[0] , l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'something went wrong please try again')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0,END)
            list.insert(END,'Something went wrong Please try again')




operations = {'ADD': add ,'ADDITION':add,'PLUS':add,'SUM':add,
'SUB':sub ,'SUBTRACTION':sub ,'MINUS':sub,'DIFFERENCE':sub,'LCM':lcm,
'HCF':hcf,'MUL':mul,'MULTIPLICATION':mul,'PRODUCT':mul,'MULTIPLY':mul,
'DIVIDE':div,'DIV':div,'DIVISION':div,'/':div,'MOD':mod,'MODULUS':mod,'REMAINDAR':mod}

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
b1=Button(win,text='Just This',command=calculate)
b1.place(x=210,y=200)

list=Listbox(win,width=20,height=3)
list.place(x=150,y=230)

win.mainloop()
