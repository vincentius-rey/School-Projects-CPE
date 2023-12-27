from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import mysql.connector
import tkinter.messagebox as MessageBox
    
def Add():
    id = idbox.get()
    fn = fbox.get()
    ln = lbox.get()
    mn = mbox.get()

    if (id=="" or fn=="" or ln=="" or mn==""):
        MessageBox.showwarning("Insert Status", "All Fields are Required")
    else:
        dataBase = mysql.connector.connect(
            host ="localhost",
            user ="root",
            passwd ="",
            database = "pnc student information system"
            )
        c = dataBase.cursor()
        c.execute("INSERT INTO information VALUES ('{}', '{}', '{}', '{}')" .format(id, fn, ln, mn))
        dataBase.commit()
        idbox.delete(0, END)
        fbox.delete(0, END)
        lbox.delete(0, END)
        mbox.delete(0, END)
        MessageBox.showinfo("Insert Status", "Student's Information Added Successfully!")
        List()
        dataBase.close()
    
def Update():
    id = idbox.get()
    fn = fbox.get()
    ln = lbox.get()
    mn = mbox.get()

    if (id=="" or fn=="" or ln=="" or mn==""):
        MessageBox.showwarning("Update Status", "All Fields are Required")
    else:
        dataBase = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="",
        database = "pnc student information system"
        )
        c = dataBase.cursor()
        c.execute("UPDATE `information` SET `Student_ID`='{}',`First_Name`='{}',`Last_Name`='{}',`Mobile`='{}' WHERE `Student_ID`='{}'" .format(id, fn, ln, mn, id))
        dataBase.commit()
        idbox.delete(0, END)
        fbox.delete(0, END)
        lbox.delete(0, END)
        mbox.delete(0, END)
        list.update()
        List()
        MessageBox.showinfo("Update Status", "Student's Information Updated Successfully!")
        dataBase.close()

def Delete():
    id = idbox.get()

    if(id == ""):
        MessageBox.showwarning("Delete Status", "Student ID is necessary")
    else:
        dataBase = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="",
        database = "pnc student information system"
        )
        c = dataBase.cursor()
        c.execute("DELETE FROM `information` WHERE `Student_ID` = '{}'" .format(id))
        dataBase.commit()
        idbox.delete(0, END)
        fbox.delete(0, END)
        lbox.delete(0, END)
        mbox.delete(0, END)
        List()
        
        MessageBox.showinfo("Delete Status", "Student's Information Deleted Successfully!")
        dataBase.close()
        
def List():
    dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database = "pnc student information system"
    )
    c = dataBase.cursor()
    c.execute("SELECT * FROM information")
    rows = c.fetchall()
    
    for i , (Student_ID, First_Name, Last_Name, Mobile) in enumerate(rows, start=1):
        list.insert('', 'end', values=(Student_ID, First_Name, Last_Name, Mobile))

    if len(rows) !=0:
        list.delete(*list.get_children())
        for row in rows:
            list.insert('', 'end', values=row)
    if len(rows)==0:
        list.delete(*list.get_children())

    dataBase.commit()
    dataBase.close()

def Bulk_Open():
    bbox.delete(0, END)
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/roelv/Downloads", 
                                                title="Select a File", 
                                                filetypes=[("Text Documents", "*.txt")]
                                                )
    bbox.insert(0, root.filename)

def Bulk_Add():
    b = bbox.get()
    dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database = "pnc student information system"
    )
    c = dataBase.cursor()
    sql = "INSERT INTO information (Student_ID, First_Name, Last_Name, Mobile) VALUES (%s, %s, %s, %s)"

    read = open(b, 'r')
    list1 = []
    list2 = []
    for lines in read.readlines():
        l1 = lines.lstrip().split(",")
        list1.append(l1)
    for a in list1:
        l1=[]
        for b in a:
            l2 = b.strip().replace("\n","")
            l1.append(l2)
        list2.append(l1)
    read.close()

    c.executemany(sql, list2)
    dataBase.commit()
    List()
    MessageBox.showinfo("Insert Status", "Student's Information Added Successfully!")
    dataBase.close()

def Export_Open():
    ebox.delete(0, END)
    root.filename = filedialog.askopenfilename(initialdir="C:/Users/roelv/Downloads", 
                                                title="Select a File", 
                                                filetypes=[("Text Documents", "*.txt")]
                                                )
    ebox.insert(0, root.filename)

def Export():
    e = ebox.get()
    dataBase = mysql.connector.connect(
    host ="localhost",
    user ="root",
    passwd ="",
    database = "pnc student information system"
    )
    c = dataBase.cursor()
    c.execute("SELECT * FROM information")
    file = open(e, 'w')
    data = c.fetchall()
    for x in data:
        file.write(str(x[0]) + ':' + x[2] + "\n")
    file.close()
    MessageBox.showinfo("Export Status", "Student's Information Exported Successfully!")
    dataBase.close()

def Get(event):
    idbox.delete(0, END)
    fbox.delete(0, END)
    lbox.delete(0, END)
    mbox.delete(0, END)
    row = list.selection()[0]
    select = list.set(row)
    idbox.insert(0, select['Student ID'])
    fbox.insert(0, select['First Name'])
    lbox.insert(0, select['Last Name'])
    mbox.insert(0, select['Mobile'])
        

root = Tk()
root.title("Student Information System")
root.geometry("815x435")

id = Label(root, text='Student ID').place(x=10, y=10)
fname = Label(root, text='First Name').place(x=10, y=40)
lname = Label(root, text='Last Name').place(x=10, y=70)
mobile = Label(root, text='Mobile').place(x=10, y=100)
bulk = Label(root, text='Add Bulk Student').place(x=350, y=10)
export = Label(root, text='Export').place(x=350, y=40)

idbox = Entry(root)
idbox.place(x=150, y=10)
fbox = Entry(root)
fbox.place(x=150, y=40)
lbox = Entry(root)
lbox.place(x=150, y=70)
mbox = Entry(root)
mbox.place(x=150, y=100)
bbox = Entry(root)
bbox.place(x=500, y=10)
ebox = Entry(root)
ebox.place(x=500, y=40)

bAdd = Button(root, text='Add', padx=30, pady=15, command=Add).place(x=30, y=130)
bUpdate = Button(root, text='Update', padx=30, pady=15, command=Update).place(x=130, y=130)
bDelete = Button(root, text='Delete', padx=30, pady=15, command=Delete).place(x=250, y=130)
bBulkOpen = Button(root, text='Open', padx=5, command=Bulk_Open).place(x=630, y=10)
bExportOpen = Button(root, text='Open', padx=5, command=Export_Open).place(x=630, y=40)
bBulkAdd = Button(root, text='Add', padx=7, command=Bulk_Add).place(x=700, y=10)
bExport = Button(root, text='Export', command=Export).place(x=700, y=40)

column = ('Student ID', 'First Name', 'Last Name', 'Mobile')
list = ttk.Treeview(root, columns=column, show='headings')
list.place(x=6, y=200)

for clm in column:
    list.heading(clm, text=clm)

List()
list.bind('<Double-Button-1>', Get)


root.mainloop()