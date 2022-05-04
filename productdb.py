import sqlite3

conn = sqlite3.connect('productdb.sqlite3') #สร้างไฟล์ฐานข้อมูล
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS product (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                productid TEXT,
                title TEXT,
                price REAL,
                image TEXT ) """)

def Insert_product(productid,title,price,image):
    with conn:
        command = 'INSERT INTO product VALUES (?,?,?,?,?)'
        c.execute(command,(None,productid,title,price,image))
    conn.commit()
    print('saved')

def View_product():
    with conn:
        command = 'SELECT * FROM product'
        c.execute(command)
        result = c.fetchall()
    print(result)
    return result

def View_product_single(productid):
    with conn:
        command = 'SELECT * FROM product WHERE productid=(?)'
        c.execute(command,([productid]))
        result = c.fetchall()
    print(result)
    return result    
if __name__ == '__main_':
    Insert_product('CF-1001','ลาเต้',35, r'C:\Image\latte.png')
    View_product()