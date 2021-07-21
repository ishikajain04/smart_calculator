/* CALCULATE */


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
                r=oprations[word.upper()](l[0],l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'Something went wrong Please try again')
            finally:
                break
        elif word.upper not in operations.keys():
            list.delete(0,END)
            list.insert(END,'Something went wrong Please try again')
            
