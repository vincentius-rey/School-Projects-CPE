from tkinter import *
from tkinter import ttk
import tkinter.messagebox as MessageBox
import mysql.connector
from PIL import ImageTk, Image

def submit():
    l = lnamebox.get()
    f = fnamebox.get()
    m = monthbox.get()
    d = daybox.get()
    y = yearbox.get()

    dBase = mysql.connector.connect(
        host ="localhost",
        user ="root",
        database = "Birthday Manager"
    )
    c = dBase.cursor()

    if (l == '' or f == '' or m == '' or d == '' or y == ''):
        MessageBox.showwarning("Warning!", "All Fields are Required!")
    else:
        c.execute("INSERT INTO data VALUES ('{}', '{}', '{}', '{}', '{}')" .format(l, f, m, d, y))
        dBase.commit()
        lnamebox.delete(0, END)
        fnamebox.delete(0, END)
        monthbox.delete(0, END)
        daybox.delete(0, END)
        yearbox.delete(0, END)
        List()
        MessageBox.showinfo("Insert Status", "Inserted Successfully!")
        dBase.close()
    
def update():
    l = lnamebox.get()
    f = fnamebox.get()
    m = monthbox.get()
    d = daybox.get()
    y = yearbox.get()

    dBase = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "Birthday Manager"
    )
    c = dBase.cursor()

    if l == '':
        MessageBox.showwarning("Warning!", "All Fields are Required!")
    else:
        c.execute("UPDATE data SET Last_Name='{}', First_Name='{}', Month='{}', Day='{}', Year='{}' WHERE First_Name='{}'" .format(l, f, m, d, y, f))
        dBase.commit()
        lnamebox.delete(0, END)
        fnamebox.delete(0, END)
        monthbox.delete(0, END)
        daybox.delete(0, END)
        yearbox.delete(0, END)
        List()
        MessageBox.showinfo("Update Status", "Data has been updated successfully!")
        dBase.close()

def delete():
    f = fnamebox.get()

    dBase = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "Birthday Manager"
    )
    c = dBase.cursor()

    if f == '':
        MessageBox.showwarning("WARNING!", "Input 'First Name' first!")
    elif f != '':
        ask = MessageBox.askyesno("Delete Status", "Are you sure you want to delete this data?")
        if ask == YES:
            c.execute("DELETE FROM data WHERE First_Name = '{}'" .format(f))
            dBase.commit()
            lnamebox.delete(0, END)
            fnamebox.delete(0, END)
            monthbox.delete(0, END)
            daybox.delete(0, END)
            yearbox.delete(0, END)
            List()
            MessageBox.showinfo("Delete Status", "Data has been deleted successfully!")
            dBase.close()
        if ask == NO:
            MessageBox.showinfo("Delete Status", "Think before you click!")

def List():
    dBase = mysql.connector.connect(
        host ="localhost",
        user ="root",
        database = "Birthday Manager"
    )
    c = dBase.cursor()
    c.execute("SELECT * FROM data")
    rows = c.fetchall()
    
    for i , (Last_Name, First_Name, Month, Day, Year) in enumerate(rows, start=1):
        list.insert('', 'end', values=(Last_Name, First_Name, Month, Day, Year))

    if len(rows) !=0:
        list.delete(*list.get_children())
        for row in rows:
            list.insert('', 'end', values=row)
    if len(rows)==0:
        list.delete(*list.get_children())
    dBase.commit()
    dBase.close()

def updte(rows):
    list.delete(*list.get_children())
    for row in rows:
        list.insert('', 'end', values=row)

def get(event):
   lnamebox.delete(0, END)
   fnamebox.delete(0, END)
   monthbox.delete(0, END)
   daybox.delete(0, END)
   yearbox.delete(0, END)
   row = list.selection()[0]
   select = list.set(row)
   lnamebox.insert(0, select['Last Name'])
   fnamebox.insert(0, select['First Name'])
   monthbox.insert(0, select['Month'])
   daybox.insert(0, select['Day'])
   yearbox.insert(0, select['Year'])

def search():
    s = searchbox.get()

    dBase = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "Birthday Manager"
    )
    c = dBase.cursor()
    get = c.execute("SELECT * FROM data WHERE Last_Name='{}'" .format(s))
    
    rows = c.fetchall()
    for i, get in enumerate(rows):
        list.insert('', 'end', values=get)

    if len(rows) !=0:
        list.delete(*list.get_children())
    for row in rows:
        list.insert('', 'end', values=row)

    if len(rows)==0:
        list.delete(*list.get_children())
        for row in rows:
            list.insert('', 'end', values=row)

    if len(rows)==0:
            list.delete(*list.get_children())
    dBase.commit()

def clear():
    searchbox.delete(0, END)
    List()

def sort(S):
    S = Sort.get()

    dBase = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database = "Birthday Manager"
    )
    c = dBase.cursor()

    if Sort.get() == "By Name":
        c.execute("SELECT * FROM data ORDER BY Last_Name, First_Name")
        rows = c.fetchall()
        updte(rows)
        dBase.commit()

    if Sort.get() == "By Month":
        c.execute("SELECT * FROM data ORDER BY STR_TO_DATE(CONCAT(Month, '01', '0001'), '%M %d %Y')")
        rows = c.fetchall()
        updte(rows)
        dBase.commit()
        
    if Sort.get() == "By Day":
        c.execute("SELECT * FROM data ORDER BY Day")
        rows = c.fetchall()
        updte(rows)
        dBase.commit()
        
    if Sort.get() == "By Year":
        c.execute("SELECT * FROM data ORDER BY Year")
        rows = c.fetchall()
        updte(rows)
        dBase.commit()
    dBase.close()
        
# Window ====================================================================================================
root = Tk()
root.title("Birthday Manager")
root.geometry('626x417')
root.resizable(0, 0)

#Background Photo
bg_img = ImageTk.PhotoImage(Image.open("C:/Users/Roel/Downloads/Compressed/1.png"))
bg = Label(root, image=bg_img)
bg.place(x=0,y=0)

# Heading ===================================================================================================
heading = Label(root, text="Birthday Manager", font=('jokerman', 20, 'bold'), padx=10, pady=10, relief='raised')
heading.place(x=180, y=10)

# Labels ====================================================================================================
name = Label(root, text="NAME:").place(x=60, y=80)
lname = Label(root, text="Last Name").place(x=190, y=100)
fname = Label(root, text="First Name").place(x=380, y=100)
bday = Label(root, text="BIRTHDAY:").place(x=60, y=140)
month = Label(root, text="Month").place(x=173, y=160)
day = Label(root, text="Day").place(x=303, y=160)
year = Label(root, text="Year").place(x=423, y=160)
srch = Label(root, text='SEARCH:').place(x=20, y=210)

# Entry Box =================================================================================================
lnamebox = Entry(root, width=29, justify='center')
fnamebox = Entry(root, width=29, justify='center')
monthbox = Entry(root, width=19, justify='center')
daybox = Entry(root, width=19, justify='center')
yearbox = Entry(root, width=19, justify='center')
searchbox = Entry(root, width=40)

lnamebox.place(x=133, y=80)
fnamebox.place(x=316, y=80)
monthbox.place(x=133, y=140)
daybox.place(x=256, y=140)
yearbox.place(x=379, y=140)
searchbox.place(x=80, y=211)

# Buttons=====================================================================================================
Insert = Button(root, text='Insert', padx= 15,pady=5,command=lambda: submit()).place(x=540, y=80)
Update = Button(root, text='Update', padx= 10.5,pady= 5,command=lambda: update()).place(x=540, y=120)
Delete = Button(root, text='Delete', padx= 13,pady= 5,command=lambda: delete()).place(x=540, y=160)
Search = Button(root, text='Search', padx= 15,pady= 5, command=lambda: search()).place(x=340, y=205)
Clear = Button(root, text='Clear', padx= 15,pady=5, command=lambda: clear()).place(x=420, y=205)

Sort = StringVar()
Sort.set("Sort")
options = ("By Name", "By Month", "By Day", "By Year")
SortMenu = OptionMenu(root, Sort, *options, command=sort)
SortMenu.pack(padx=1, pady=5)
SortMenu.place(x=495, y=207)

# Table Frame =================================================================================================
frame = LabelFrame(root, text='Birthday List')
frame.place(x=7, y=245)

# Table for List ==============================================================================================
column = ('Last Name', 'First Name', 'Month', 'Day', 'Year')
list = ttk.Treeview(frame, columns=column, show='headings', height=6)
list.column('# 1', anchor=CENTER, width=150)
list.column('# 2', anchor=CENTER, width=160)
list.column('# 3', anchor=CENTER, width=100)
list.column('# 4', anchor=CENTER, width=80)
list.column('# 5', anchor=CENTER, width=100)
list.pack(side=LEFT)
style = ttk.Style()
style.theme_use('clam')
list.bind('<Double-Button 1>', get)

for clm in column:
    list.heading(clm, text=clm)

# Vertical Scrollbar ==========================================================================================
scrllbar = ttk.Scrollbar(frame, orient='vertical', command=list.yview)
scrllbar.pack(side=RIGHT, fill='y')

list.configure(yscrollcommand=scrllbar.set)

List()

root.mainloop()
