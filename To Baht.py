from tkinter import *
from tkinter import ttk
from tkinter import messagebox

choice2 = []
count = 0
def display_selected(self):
    global count
    count = count+1
    if count == 1 :
        choice2.append(var1.get())
        print(choice2)      
    else:
        choice2.pop(0)
        choice2.append(var1.get())
        print(choice2)

def result2(event = None):
    try:
        if choice2[-1] == choices[0]:
            datafrom2 = datafrom1.get()
            baht = datafrom2 * 33.58
            messagebox.showinfo('ค่าเงินไทย',f'ได้ทั้งหมด {baht} บาท')
            data1.focus()
        elif choice2[-1] == choices[1]:
            datafrom2 = datafrom1.get()
            baht = datafrom2 * 0.27
            messagebox.showinfo('ค่าเงินไทย',f'ได้ทั้งหมด {baht} บาท')
            data1.focus()
        elif choice2[-1] == choices[2]:
            datafrom2 = datafrom1.get()
            baht = datafrom2 * 36.53
            messagebox.showinfo('ค่าเงินไทย',f'ได้ทั้งหมด {baht} บาท')
            data1.focus()
        elif choice2[-1] == choices[3]:
            datafrom2 = datafrom1.get()
            baht = datafrom2 * 43.72
            messagebox.showinfo('ค่าเงินไทย',f'ได้ทั้งหมด {baht} บาท')
            data1.focus()
    except:
        messagebox.showwarning('Error 000 ','โปรดเลือกสกุลเงินเพื่อแปลงค่า หรือ ใส่เพียงตัวเลขเท่านั้น')

Gui = Tk()
Gui.geometry('250x150')
Gui.title('แปลงสกุลเงินเป็นไทย')


choices = ['USD','YEN','EURO','POUND']
var1 = StringVar()
var1.set('None')

bg = PhotoImage(file='Picture1.png')

label0 = ttk.Label(Gui,image=bg)
label0.pack()

label1 = ttk.Label(Gui,text='Change to Baht',font=(None,18))
label1.pack()

datafrom1 = IntVar()
data1 = ttk.Entry(Gui , textvariable=datafrom1)
data1.pack(ipadx=5,ipady=5,side='left')

realcurrency = StringVar()
selectcurrency = OptionMenu(Gui,var1,*choices,command=display_selected)
selectcurrency.pack(side='left')

Gui.bind('<Return>', result2)
Gui.mainloop()