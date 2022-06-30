from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

top = Tk()
top.title("LOGIN PAGE")
top.geometry("400x300")
top.configure(bg="#1E90FF")


def kiran():
    user = e1.get()
    password = e2.get()
    if user == "" and password == "":

        def insert():
            id = e_id.get()
            name = e_name.get()
            phone = e_phone.get()

            if (id == '' or name == '' or phone == ''):
                MessageBox.showinfo('Insert status', 'you must enter your ID')
            else:
                con = mysql.connect(host='localhost', user='root', password='', database='my_database')
                cursor = con.cursor()
                cursor.execute("insert into student values('" + id + "','" + name + "','" + phone + "')")
                cursor.execute('commit')

                e_id.delete(0, 'end')
                e_name.delete(0, 'end')
                e_phone.delete(0, 'end')
                show()
                MessageBox.showinfo('Insret Status', 'Inserted Successfully')
                con.close()

        def delete():
            id = e_id.get()
            name = e_name.get()
            phone = e_phone.get()

            if (id == '' or name == '' or phone == ''):
                MessageBox.showinfo('ID is compulsary for deleting data')
            else:
                con = mysql.connect(host='localhost', user='root', password='', database='my_database')
                cursor = con.cursor()
                cursor.execute("delete from student where id='" + e_id.get() + "'")
                cursor.execute('commit')

                e_id.delete(0, 'end')
                e_name.delete(0, 'end')
                e_phone.delete(0, 'end')
                show()
                MessageBox.showinfo('Delete Status', 'Deleted Successfully')
                con.close()

        def update():
            id = e_id.get()
            name = e_name.get()
            phone = e_phone.get()

            if (id == '' or name == '' or phone == ''):
                MessageBox.showinfo('Update Status', 'All Field Are Required')
            else:
                con = mysql.connect(host='localhost', user='root', password='', database='my_database')
                cursor = con.cursor()
                cursor.execute("update student set name='" + name + "', phone='" + phone + "' where id='" + id + "'")
                cursor.execute('commit')

                e_id.delete(0, 'end')
                e_name.delete(0, 'end')
                e_phone.delete(0, 'end')
                show()
                MessageBox.showinfo('Insret Status', 'Inserted Successfully')
                con.close()

        def get():
            if (e_id.get() == ""):
                MessageBox.showinfo('Fetch Status', 'ID is compulsary for delete')
            else:
                con = mysql.connect(host='localhost', user='root', password='', database='my_database')
                cursor = con.cursor()
                cursor.execute("select * from student where id='" + e_id.get() + "'")
                rows = cursor.fetchall()

                for row in rows:
                    e_name.insert(0, row[1])
                    e_phone.insert(0, row[2])
                    con.close()

        def show():
            con = mysql.connect(host='localhost', user='root', password='', database='my_database')
            cursor = con.cursor()
            cursor.execute("select * from student")
            rows = cursor.fetchall()
            list.delete(0, list.size())

            for row in rows:
                insertData = str(row[0]) + '       ' + row[1]
                list.insert(list.size() + 1, insertData)
            con.close()

        root = Tk()
        root.geometry('600x300')
        root.title('Python+Tkinter+Mysql')
        root.configure(bg='#8cbed6')

        id = Label(root, text='Enter ID', font=('bold', 10))
        id.place(x=20, y=30)

        name = Label(root, text='Enter Name', font=('bold', 10))
        name.place(x=20, y=60)

        phone = Label(root, text='Enter Phone', font=('bold', 10))
        phone.place(x=20, y=90)

        e_id = Entry(root)
        e_id.place(x=150, y=30)

        e_name = Entry(root)
        e_name.place(x=150, y=60)

        e_phone = Entry(root)
        e_phone.place(x=150, y=90)

        # ============================================buttons=====================================================
        insert = Button(root, text=' Insert ', font=('italic', 10), bg='BLUE', fg='white', command=insert)
        insert.place(x=40, y=160)

        delete = Button(root, text='Delete', font=('italic', 10), bg='blue', fg='white', command=delete)
        delete.place(x=150, y=160)

        update = Button(root, text='Update', font=('italic', 10), bg='blue', fg='white', command=update)
        update.place(x=40, y=230)

        get = Button(root, text='  Get  ', font=('italic', 10), bg='blue', fg='white', command=get)
        get.place(x=150, y=230)

        l1 = Label(root, text="A SIMPLE REGESTRATION FORM :", bg='#8cbed6', fg="RED", font="Times 13 italic bold")
        l1.place(x=310, y=50)

        list = Listbox(root)
        list.place(x=350, y=110)
        show()
        root.mainloop()
    else:
        MessageBox.showinfo(user, "INVALID CREDENTIALS")


# ---------------------------------creating label-----------------------------------------------------------

l1 = Label(top, text="USER ID :", bg="black", fg="white", font="Times 10 italic bold")
l1.place(x=50, y=90)
l2 = Label(top, text="PASSWORD :", bg="black", fg="white", font="Times 10 italic bold")
l2.place(x=35, y=130)

# --------------------------------creating entry boxes------------------------------------------------------

e1 = Entry(top, bg="white", fg="black", width="34")
e1.place(x=120, y=90)
e2 = Entry(top, bg="white", fg="black", width="34")
e2.place(x=120, y=130)

# ---------------------------------creating button-----------------------------------------------------------

b1 = Button(top, text="SIGN IN", fg="white", bg="black", width="20", height="2",
            font="Times 10 italic bold", command=kiran)
b1.place(x=145, y=182)
top.mainloop()
