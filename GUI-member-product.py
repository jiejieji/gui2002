
from tkinter import *
from tkinter import ttk, messagebox
import wikipedia
#from memberdb import *
#from productdb import *

#View_member()

#import memberdb  
#memberdb.View_member()

#import memberdb as db
#db.View_member()

import csv
from datetime import datetime
def writetocsv(data, filename='data.csv'):
    with open(filename,'a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)


GUI = Tk()
GUI.title('โปรแกรมจัดการ layout')


W = 1200
H = 600
MW = GUI.winfo_screenwidth()
MH = GUI.winfo_screenheight()
SX = (MW/2) - (W/2)
SY = (MH/2) - (H/2)
#SY = SY - 50   

print(MW,MH,SX,SY)
print('{}x{}+{:.0f}+{:.0f}'.format(W,H,SX,SY))
GUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(W,H,SX,SY))

menubar = Menu(GUI)
GUI.config(menu=menubar)



filemenu = Menu(menubar)
menubar.add_cascade(label='File',menu=filemenu)



def ExportDatabase():
    print('Export Database to CSV')
filemenu.add_command(label='Export',command=ExportDatabase)
filemenu.add_command(label='ปิดโปรแกรม',command=lambda: GUI.destroy())


membermenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Member',menu=membermenu)


import webbrowser


helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='help',menu=helpmenu)
contact_url = 'https://uncle-engineer.com'
helpmenu.add_command(label='Contact US',command=lambda: webbrowser.open(contact_url))


def About():
    ABGUI = Toplevel()
    W = 300
    H = 200
    MW = GUI.winfo_screenwidth()
    MH = GUI.winfo_screenheight()
    SX = (MW/2) - (W/2)
    SY = (MH/2) - (H/2)
    SY = SY - 50   


    GUI.geometry('{}x{}+{:.0f}+{:.0f}'.format(W,H,SX,SY))
    L = Label(ABGUI,text='โปรแกรมร้านกาแฟ',fg='green',font=('Angsana New',30)).pack()
    L = Label(ABGUI,text='chun.com',font=('Angsana New',30)).pack()
    ABGUI.mainloop()

helpmenu.add_command(label='About',command=About)


Tab =ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
T4 = FrameT3 = Frame(Tab)

icon_tab1 = PhotoImage(file='tab1.png')
icon_tab2 = PhotoImage(file='tab2.png')
icon_tab3 = PhotoImage(file='tab3.png')
icon_tab4 = PhotoImage(file='tab4.png')

Tab.add(T1, text='กุ้ง',image=icon_tab1,compound='left')
Tab.add(T2, text='wiki',image=icon_tab2,compound='left')
Tab.add(T3, text='CAFE',image=icon_tab3,compound='left')
Tab.add(T4, text='Member',image=icon_tab4,compound='left')


############ TAB 1 - กุ้ง#############


L1 = Label(GUI,text='กรอกจํานวนกุ้ง (กิโลกรัม)',font=('Angsana New',25))
L1.pack()

v_kilo = StringVar() 


E1 = ttk.Entry(T1, textvariable= v_kilo, width=10,justify='right',font=('impact',30))
E1.pack(pady=20)

E1.focus()

def Calc(event=None):
    print('กําลังคํานวณ...กรุณารอสักคู่')
    kilo = float(v_kilo.get())
    print(kilo * 10)
    calc_result = kilo * 299
    date = datetime.now()
    year = date.year + 543
    stamp = date.strftime('%Y-%m-%d %H:%M:%S'.format(year))
    data = [stamp, 'กุ้ง', '{:,.2f}'.format(calc_result)]
    writetocsv(data)
    messagebox.showinfo('รวมทั้งหมด','ลูกค้าต้องจ่ายตังทังหมด: {:,.2f} บาท'.format(calc_result))
    
B1 = ttk.Button(T1,text='คํานวนราคา',command=Calc)
B1.pack(ipadx=40,ipady=30)

E1.bind('<Return>',Calc)

FONT1 = ('Angsana New',25)

L2 = Label(T2,text='ค้นหาข้อมูล wikipedia',font=('Angsana New',25))
L2.pack()

v_search = StringVar()

E2 = ttk.Entry(T2, textvariable=v_search, font=FONT1)
E2.pack(pady=10)

wikipedia.set_lang('th')

v_link = StringVar() 

def Search():
    try:
        Search = v_search.get()
        #text = wikipedia.summary(Search)
        text = wikipedia.page(Search)
        print(text)
        v_result.set(text.content[:1000])
        print('LINK:',text.url)
        v_link.set(text.url)
    except:
        v_result.set('ไม่มีข้้อมูลที่ โปรดค้นหาไหม')    

B2 = ttk.Button(T2,text='Search',image=icon_tab2,compound='left',command=Search)
B2.pack()

import webbrowser

def readmore():
    webbrowser.open(v_link.get()) 

B3 = ttk.Button(T2,text='อ่านต่อ',command=readmore)
B3.place(x=1000,y=50)

v_result = StringVar()
v_result.set('----------Result--------')
result = Label(T2,textvariable=v_result,wraplength=550, font=(None,15))
result.pack()

Bfont = ttk.Style()
Bfont.configure('TButton',font=('Angsana New',20))



CF1 = Frame(T3)
CF1.place(x=50,y=100)



allmenu = {}

product = {'latte':{'name':'ลาเต้','price':30},
           'cappuccino':{'name':'คาปูชิโน','price':35},
           'espresso':{'name':'เอสเปรสโซ','price':40},
           'greentea':{'name':'ชาเขียว','price':20},
           'icetea':{'name':'ชาเย็น','price':20},
           'hottea':{'name':'ชาร้อน','price':20},}

def UpdateTable():
    table.delete(*table.get_children())
    for i,m in enumerate(allmenu.values(),start=1):
        table.insert('','end',value=[i,m[0],m[1],m[2],m[3] ] )

    
def AddMenu(name='latte'):
    #name = 'latte'
    if name not in allmenu:
        allmenu[name] = [product[name]['name'],product[name]['price'],1,product[name]['price']]
        print(allmenu)

    else:    
        quan = allmenu[name][2] + 1
        total = quan * product[name]['price']
        allmenu[name] = [product[name]['name'],product[name]['price'], quan ,total]
    print(allmenu)
    count = sum([ m[3] for m in allmenu.values()])
    v_total.set('{:,.2f}'.format(count))
    UpdateTable()


def Menu1():
    AddMenu('latte')
    UpdateTable()

def Menu2():
    AddMenu('cappuccino')
    UpdateTable()

def Menu3():
    AddMenu('espresso')        
    UpdateTable()



B = ttk.Button(CF1,text='ลาเต้',image=icon_tab3,compound='top',command=lambda m='latte': AddMenu(m))
B.grid(row=0,column=0,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='คาปูชิโน',image=icon_tab3,compound='top',command=lambda m='cappuccino': AddMenu(m))
B.grid(row=0,column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='เอสเปรสโซ',image=icon_tab3,compound='top',command=lambda m='espresso': AddMenu(m))
B.grid(row=0,column=2,ipadx=20,ipady=10)

#ROW1

B = ttk.Button(CF1,text='ชาเขียว',image=icon_tab3,compound='top',command=lambda m='greentea': AddMenu(m))
B.grid(row=1,column=0,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='ชาเย็น',image=icon_tab3,compound='top',command=lambda m='icetea': AddMenu(m))
B.grid(row=1,column=1,ipadx=20,ipady=10)
B = ttk.Button(CF1,text='ชาร้อน',image=icon_tab3,compound='top',command=lambda m='hottea': AddMenu(m))
B.grid(row=1,column=2,ipadx=20,ipady=10)



CF2 = Frame(T3)
CF2.place(x=600,y=100)

header = ['No.','Order', 'Quantity','price','total']
hwidth = [50,200,100,100,100]



table = ttk.Treeview(CF2,columns=header, show='headings',height=15)
table.pack()



for hd,hw in zip(header,hwidth):
    table.column(hd,width=hw)
    table.heading(hd,text=hd)

L = Label(T3,text='total:', font=(None,15)).place(x=400,y=450)

v_total = StringVar()
v_total.set('0.0')

LT = Label(T3,textvariable=v_total, font=(None,15))
LT.place(x=500,y=450)

def Reset():
    global allmenu
    allmenu = {}
    table.delete(*table.get_children())
    v_total.set('0.0')
    trstamp = datetime.now().strftime('%y%m%d%H%M%S')
    v_transaction.set(trstamp)


B = ttk.Button(T3,text='Clear',command=Reset).place(x=600,y=550)


v_transaction = StringVar()
trstamp = datetime.now().strftime('%y%m%d%H%M%S')
v_transaction.set(trstamp)

LTR = Label(T3,textvariable=v_transaction,font=(None,10)).place(x=950,y=70)


FB = Frame(T3)
FB.place(x=890,y=500)


def AddTransaction():
    stamp = datetime.now().strftime('%Y-%m%d %H:%M:%S')
    transaction = v_transaction.get()
    print(transaction, stamp, allmenu)
    for m in allmenu.values():
        m.insert(0,transaction)
        m.insert(1,transaction)
        writetocsv(m,'transaction.csv')
    Reset()    


B = ttk.Button(FB,text='บันทึก',command=AddTransaction)
B.pack(ipadx=30,ipady=20)


def HistoryWindow(event):
    HIS = Toplevel()
    HIS.geometry('500x500')


    L = Label(HIS,text='ประวัตรการไช้งาน:', font=(None,15)).pack()


    header = ['TS-ID','Time' 'title', 'Order','Quantity','price','total']
    hwidth = [50,200,100,100,100]



    table_history = ttk.Treeview(HIS,columns=header, show='headings',height=15)
    table_history.pack()



    for hd,hw in zip(header,hwidth):
        table_history.column(hd,width=hw)
        table_history.heading(hd,text=hd)


    with open('transaction.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        for row in fr:

            table_history.insert('',0,value=row)


    HIS.mainloop()

T3.bind('<F1>',HistoryWindow)




def ET(GUI,text,strvar,font=('Angsana New',15)):
    T = Label(GUI,text=text,font=(None,15)).pack()
    E = ttk.Entry(GUI,textvariable=strvar,font=font)  
    return E   



def ET2(GUI,text,strvar,font=('Angsana New',15)):
    T = Label(GUI,text=text,font=(None,15))
    E = ttk.Entry(GUI,textvariable=strvar,font=font)  
    return (E,T)    



def ET3(GUI,text,font=('Angsana New',15)):
    v_strvar = StringVar()
    T = Label(GUI,text=text,font=(None,15)).pack()
    E = ttk.Entry(GUI,textvariable=v_strvar,font=font)  
    return (E,T,v_strvar) 


#v_fullname = StringVar()
#E41 = ET(T4,'ชื่อ-สกุล',v_fullname)
#E41.place(x=300,y=150)

#v_tel = StringVar()
#E42,L = ET2(T4,'เบอโทร', v_tel)
#L.place(x=70,y=50)
#E42.place(x=50,y=80)

F41 = Frame(T4)
F41.place(x=50,y=50)

v_membercode = StringVar()
v_membercode.set('M-1001')
v_databasecode = IntVar()



v_membercode = StringVar()
v_membercode.set('M-1001')

L = Label(T4,text='รหัสสมาชิก:',font=(None,15)).place(x=50,y=20)
LCode = Label(T4,textvariable=v_membercode,font=(None,13)).place(x=150,y=20)


E41,L,v_fullname = ET3(F41,'ชื่อ-สกุล')
E41.pack()


E42,L,v_tel = ET3(F41,'เบอโทร')
E42.pack()


E43,L,v_usertype = ET3(F41,'ประเภทสมาชิก')
E43.pack()
v_usertype.set('general')

E44,L,v_point = ET3(F41,'คะแนนสะสม')
E44.pack()
v_point.set('0')


#E43.bind('<Return>', lambda x=None: print(v_usertype.get()))

def SaveMember():
    code = v_membercode.get() 
    fullname = v_fullname.get()
    tel = v_tel.get()
    usertype = v_usertype.get()
    point = v_point.get()
    print(fullname, tel, usertype, point)
    #writetocsv([code, fullname, tel, usertype, point],'Member.csv')
    Insert_member(code, fullname, tel, usertype, point)
    #table_member.insert('',0,value=[code, fullname, tel, usertype, point]) 
    UpdateTable_Member()
    


BSave = ttk.Button(F41,text='บันทึก',command=SaveMember)
BSave.pack()


def EditMember():
    code = v_databasecode.get()
    print(allmember)
    allmember[code][2] = v_fullname.get()
    allmember[code][3] = v_tel.get()
    allmember[code][4] = v_usertype.get()
    allmember[code][5] = v_point.get()
    #UpdateCSV(list(allmember.values()),'member.csv')
    Update_member(code,'fullname', v_fullname.get())
    Update_member(code,'tel', v_tel.get())
    Update_member(code,'usertype', v_usertype.get())
    Update_member(code,'points', v_point.get())
    UpdateTable_Member()


    BEdit.state(['disabled'])
    BSave.state(['!disabled'])
    v_fullname.set('')
    v_tel.set('')
    v_usertype.set('general')
    v_point.set('0')

BEdit = ttk.Button(F41,text='แก้ไข',command=EditMember)       
BEdit.pack()

def NewMember():
    UpdateTable_Member() 
    BEdit.state(['disabled'])
    BSave.state(['!disabled'])
    v_fullname.set('')
    v_tel.set('')
    v_usertype.set('general')
    v_point.set('0')


BNew = ttk.Button(F41,text='New',command=NewMember)
BNew.pack()

F42 = Frame(T4)
F42.place(x=600,y=100)

header = ['ID', 'Code', 'ชื่อ-สกุล', 'เบอโทร','ประเภทสมาชิก','คะแนนสะสม']
hwidth = [50, 50,200,100,100,100]



table_member = ttk.Treeview(F42,columns=header, show='headings',height=15)
table_member.pack()




for hd,hw in zip(header,hwidth):
    table_member.column(hd,width=hw)
    table_member.heading(hd,text=hd)


def UpdateCSV(data, filename='data.csv'):
    with open(filename,'w',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerows(data)
    

def DeleteMember(event=None):
    choice = messagebox.askyesno('ลบรายการซะถ้าไม่อยากโดนแฮก')
    if choice == True:
        select = table_member.selection()
        print(select)
        if len(select) != 0:
            data = table_member.item(select)['values']
            print(data)
            del allmember[data[0]]
            Delete_member(data[0])
            UpdateCSV(allmember.values(),'member.csv')
            UpdateTable_Member()
    else:
        messagebox.showwarning('ไม่ได้เลือกรายการ','กรุณาเลือกรายการ')    



table_member.bind('<Delete>',DeleteMember)




def UpdateMemberinfo(event=None):

    select = table_member.selection()
    if len(select) != 0:
        code = table_member.item(select)['values'][0]
        v_databasecode.set(code)
        print(allmember[code])
        memberinfo = allmember[code]


        v_membercode.set(memberinfo[1])
        v_fullname.set(memberinfo[2])
        v_tel.set(memberinfo[3])
        v_usertype.set(memberinfo[4])
        v_point.set(memberinfo[5])

        BEdit.state(['!disabled'])
        BSave.state(['disabled'])
    else:
        messagebox.showwarning('ไม่ได้เลือกรายการ','กรุณาเลือกก่อนลบรายการ') 

table_member.bind('<Double-1>',UpdateMemberinfo)




last_member = ''
allmember = {}



def UpdateTable_Member():
    global last_member
    
    fr = View_member()
    table_member.delete(*table_member.get_children())
    for row in fr:
        table_member.insert('',0,value=row)
        code = row[0]
        allmember[code] = list(row)    



    '''
    print('Last ROW:',row)
    last_member = row[0]
    # M-1001
    # ['M',1001+1     next_member = int(last_member.split('-')[1]) + 1
    v_membercode.set('M-{}'.format(next_member))
    print(allmember)
    '''


member_rcmenu = Menu(GUI,tearoff=0)
table_member.bind('<Button-3>',lambda event: member_rcmenu.post( event.x_root , event.y_root) )
member_rcmenu.add_command(label='Delete',command=DeleteMember)
member_rcmenu.add_command(label='Update',command=UpdateMemberinfo)



def SearchName():
    select = table_member.selection()
    name = table_member.item(select)['values'][1]
    print(name)
    url = 'https://www.google.com/search?q={}'.format(name)
    webbrowser.open(url)

member_rcmenu.add_command(label='Search Name',command=SearchName)


def SearchBBC():
    select = table_member.selection()
    name = table_member.item(select)['values'][1]
    print(name)
    url = 'https://www.bbc.co.uk/search?q={}'.format(name)
    webbrowser.open(url)

member_rcmenu.add_command(label='Search Name',command=SearchBBC)




BEdit.state(['disabled'])
try:
    UpdateTable_Member()
except:
    print('กรุณาข้อมูลนะ1ตัว')

#import os


#file = os.listdir()
#print(file)


GUI.mainloop()




