import tkinter
from tkinter import StringVar,END,messagebox,BOTH
import tkinter.font as font
from PIL import ImageTk,Image


def close():
    qp = messagebox.askyesno("Exit?", "Are You Sure You Want To Exit?", parent=root)
    if qp == 1:
        r.destroy()

r = tkinter.Tk()
r.withdraw()
root = tkinter.Toplevel()
root.title('FLAMES Calculator')
root.protocol("WM_DELETE_WINDOW", close)
w = 400
h = 330
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(0,0)

root_colour = '#a9d6e5'
input_colour = '#ff6b6b'
output_colour = '#ffe66d'
myfont = font.Font(family='Helevetica')

root.config(bg=root_colour)

def submit_name():
    if name1.get() and name2.get()!='':
        global name_label, st
        name1l = list(name1.get().lower())
        name2l = list(name2.get().lower())
        l1 = []
        for i in name2l:
            if i in name1l:
                l1.append(i)
                name1l.remove(i)
        for i in l1:
            name2l.remove(i)
        count = len(name1l) + len(name2l)
        l2 = 'FLAMES'
        if count != 0:
            while len(l2) > 1:
                if count > len(l2):
                    t = (count % len(l2)) - 1
                else:
                    t = count - 1
                l = l2.split(l2[t])
                s = l[1] + l[0]
                l2 = s
            if l2 == 'S':
                st = 'The Relationship Between \n' + str(name1.get()).upper() + '\n and \n' + str(name2.get()).upper() + '\n will end in ' + "SIBLINGS"
            elif l2 == 'E':
                st = 'The Relationship Between \n' + str(name1.get()).upper() + '\n and \n' + str(name2.get()).upper() + '\n will end in ' + "ENEMY"
            elif l2 == 'M':
                st = 'The Relationship Between \n' + str(name1.get()).upper() + '\n and \n' + str(name2.get()).upper() + '\n will end in ' + "MARRIAGE"
            elif l2 == 'A':
                st = 'The Relationship Between \n' + str(name1.get()).upper() + '\n and \n' + str(name2.get()).upper() + '\n will end in ' + "AFFECTION"
            elif l2 == 'L':
                st = 'The Relationship Between \n' + str(name1.get()).upper() + '\n and \n' + str(name2.get()).upper() + '\n will end in ' + "LOVE"
            elif l2 == 'F':
                st = 'The Relationship Between \n' + str(name1.get()).upper() + '\n and \n' + str(name2.get()).upper() + '\n will end in ' + "FRIENDS"
        else:
            st = 'FLAMES NOT POSSIBLE!'
        name_label.config(text=st)
        name1.delete(0,END)
        name2.delete(0,END)

input_frame = tkinter.LabelFrame(root, bg=input_colour)
output_frame = tkinter.Frame(root,bg=output_colour)
input_frame.pack(pady=10)
output_frame.pack(padx=10,pady=(0,10),fill=BOTH,expand=True)

x = tkinter.Label(input_frame,text='First Name:',bg=input_colour,font=myfont)
var_name = StringVar()
max_len = 20
def on_write(*args):
    s = var_name.get()
    if len(s) > max_len:
        var_name.set(s[:max_len])
var_name.trace_variable("w", on_write)
name1 = tkinter.Entry(input_frame,width=20,font=myfont,textvariable=var_name)
var_name1 = StringVar()
max_len1 = 20
def on_write1(*args):
    s1 = var_name1.get()
    if len(s1) > max_len1:
        var_name1.set(s1[:max_len1])
var_name1.trace_variable("w", on_write1)
name2 = tkinter.Entry(input_frame,width=20,font=myfont,textvariable=var_name1)
y = tkinter.Label(input_frame,text='Second Name:',bg=input_colour,font=myfont)
submit_button = tkinter.Button(input_frame,text='Submit',command=submit_name,font=myfont,bg=root_colour)
x.grid(row=0,column=0)
name1.grid(row=0,column=1,padx=(0,10),pady=10)
y.grid(row=1,column=0)
name2.grid(row=1,column=1,padx=(0,10),pady=10)
submit_button.grid(row=2,column=0,columnspan=2,padx=10,pady=10,ipadx=20)
name_label = tkinter.Label(output_frame, text='',font=myfont,bg=output_colour)
name_label.pack()

r.mainloop()
