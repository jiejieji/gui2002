

from tkinter import *
from tkinter import ttk


import tkinter


GUI = Tk()
GUI.title('โปรแกรมคํานวลปลา')
GUI.geometry('700x600')

bg = PhotoImage(file='car.png')

BG = Label(GUI, image=bg)
BG.pack()



L = Label(GUI,text='กรุณากรอกจํานวนไอติม',font=(None,20))
L.pack()

v_quantity = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack()


def Cal():
	try:
		quan = float(v_quantity.get())
		calc = quan * 39
		messagebox.showinfo('ราคาทั้งหมด','ราคาไอติมทั้งหมด {} บาท'.format(calc) )
		v_quantity.set('1')
	except:
		 messagebox.showinfo('กรอกผิด')
		 v_quantity.set('1')
		 E1.focus()	


B = ttk.Button(GUI, text='คํานวน',command=Cal)
B.pack(ipadx=30,ipady=20)


GUI.mainloop()