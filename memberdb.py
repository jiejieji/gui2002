import sqlite3

conn = sqlite3.connect('basicdb.sqlite3')
c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS member (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,

                membercode TEXT,
                fullname TEXT,
                tel TEXT,
                usertype TEXT,
                points INTEGER ) """)


def Insert_member(membercode,fullname,tel,usertype,points):
    with conn:
        command = 'INSERT INTO member VALUES (?,?,?,?,?)'
        c.execute(command,(None,membercode,fullname,tel,usertype,points))
    conn.commit()
    print('save')



def View_member():
    with conn:
        command = 'SELECT * FROM product'
        c.execute(command)
        result = c.fetchall()
    print(result)
    return result
 

def Update_member(ID,field,newvalue):
    with conn:
        command = 'UPDATE member SET {} = (?) WHERE ID=(?)'.format(field)
        c.execute(command,([newvalue,ID]))
    conn.commit()
    print('updated')


def Delete_member(ID):
    with conn:
        command = 'DELETE FROM member WHERE ID=(?)'
        c.execute(command,([ID]))
    conn.commit()
    print('delete')    


#res = View_member()
#print(res[1])


#Update_member(2,'fullname','ยอด เยี่ยม')

Delete_member(1)
View_member()        

#Insert_member('MB-1001','สมชาย ดีมาก','0984953244','vip',100)


