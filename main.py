from tkinter import *
from tkinter import messagebox
import mysql.connector


#GUI Part
window = Tk()
window.geometry("600x270")
window.title("Employee CRUD App")

#Labels
empId = Label(window,text="Employee ID", font=("Serif",12))
empId.place(x=20,y=30)

empName = Label(window,text="Employee Name", font=("Serif", 12))
empName.place(x=20,y=60)

empDept = Label(window,text="Employee Dept", font=("Serif",12))
empDept.place(x=20,y=90)

#Entries
enterId = Entry(window)
enterId.place(x=170, y=30)

enterName = Entry(window)
enterName.place(x=170,y=60)

enterDept = Entry(window)
enterDept.place(x=170, y=90)

#Functions
def insertData():
    #Read the data provided by user
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()
    query = (
        "INSERT INTO empDetails (empID, empName, empDept)"
        "VALUES (%s, %s, %s)"
        )
    data = (id, name, dept)
    if(id == "" or name =="" or dept == ""):
    #if empty data provided by user #If empty data provided by user
        messagebox.showwarning("Cannot Insert", "All the fields are required!")
    else:
        #Add your own localhost, username, passwd and database
        myDB = mysql.connector.connect(host="", user="", passwd="", database="")
        myCur = myDB.cursor()
        myCur.execute(query, data)
        myDB.commit()

    #Clear out the entries from the fields filled by user
        enterId.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")

        show()
        messagebox.showinfo("Insert Status", "Data Inserted Successsfully.")
        myDB.close()
def updateData():
    #Read the data provide by user
    id = enterId.get()
    name = enterName.get()
    dept = enterDept.get()

    query = (" UPDATE empDetails SET empName= %s, empDept= %s WHERE empID= %s ")

    data = (name, dept, id)
    if(id =="" or name == "" or dept== ""):
        #if empt data provided by user
        messagebox.showwarning("Cannot Update", "All the fields are required!")
    else:
        # Add your own localhost, username, passwd and database
        myDB = mysql.connector.connect(host="", user="", passwd="", database="")
        myCur = myDB.cursor()
        myCur.execute(query, data)
        myDB.commit()

        #Clear out the entries from the fields filled by user
        enterId.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")
        show()
        messagebox.showinfo("Update status", "Data Update Successfully")
        myDB.close()
def getData():
    query = ("Select * from empDetails where empID=" + enterId.get())
    if(enterId.get() == ""): # Combined reading and checking for empty data
        messagebox.showwarning("Fetch Status", "Please provide the Emp ID to fetch the data")
    else: #Fill the entry fields from database
        # Add your own localhost, username, passwd and database
        myDB = mysql.connector.connect(host="", user="", passwd="", database="")
        myCur = myDB.cursor()
        myCur.execute(query)
        rows = myCur.fetchall()

        for row in rows:
            enterName.insert(0,row[1])
            enterDept.insert(0,row[2])

        myDB.close()

def deleteData():
    query = ("DELETE from empDetails where empID=" + enterId.get())
    if(enterId.get() == ""): #Combined reading and checking of empID data
        messagebox.showwarning("Cannot Delete", "Please provide the Emp ID to delete the data!")
    else: #Delete selected record matching the emp ID
        # Add your own localhost, username, passwd and database
        myDB = mysql.connector.connect(host="", user="", passwd="", database="")
        myCur = myDB.cursor()
        myCur.execute(query)
        myDB.commit()

        #Clear out data from all fields
        enterId.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")
        show()
        messagebox.showinfo("Delete Status", "Data Deleted Successfully.")
        myDB.close()

def show():
    query = ("Select * from empDetails")
    # Add your own localhost, username, passwd and database
    myDB = mysql.connector.connect(host="", user="", passwd="", database="")
    myCur= myDB.cursor()
    myCur.execute(query)
    rows= myCur.fetchall()
    showData.delete(0,showData.size())

    for row in rows:
        addData = str(row[0]) + ' '+ row[1] + ' '+ row[2]
        showData.insert(showData.size()+1, addData)
    myDB.close()
def resetFields():
    enterId.delete(0,"end")
    enterName.delete(0,"end")
    enterDept.delete(0,"end")

#Buttons
insertBtn = Button(window,text="Insert", font=("Sans", 12), bg="white",command=insertData)
insertBtn.place(x=20,y=160)

updateBtn = Button(window,text="Update", font=("Sans", 12), bg="white",command=updateData)
updateBtn.place(x=80,y=160)

getBtn = Button(window,text="Fetch", font=("Sans", 12), bg="white",command=getData)
getBtn.place(x=150,y=160)

deleteBtn = Button(window,text="Delete", font=("Sans", 12), bg="white",command=deleteData)
deleteBtn.place(x=210,y=160)

resetBtn = Button(window,text="Reset", font=("Sans", 12), bg="white",command=resetFields)
resetBtn.place(x=20,y=210)

#Listbox
showData = Listbox(window)
showData.place(x=330,y=30)

show() #Added call to show the data in Listbox after the box is created
window.mainloop()



