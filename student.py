#ProjectGurukul python School Management System - Import modules
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

#ProjectGurukul- Initializing window frame
window = tk.Tk()
window.geometry("1350x700")
window.title("Student Management System by Oluwaniyi")
 
Label_Heading = tk.Label(window, text="Student Management System", font=("Times new roman", 35,"bold"),bg="blue",foreground="yellow", border=12, relief=tk.GROOVE)
Label_Heading.pack(side=tk.TOP, fill=tk.X)
 
Frame_Details =  tk.LabelFrame(window, text="Enter details", font = ("Times new roman", 22,"bold"), bd=12, relief=tk.GROOVE, bg="#e3f4f1")
Frame_Details.place(x=20, y=100, width=400, height=575)
 
Frame_Data = tk.Frame(window, bd=12, relief=tk.GROOVE, bg="#e3f4f1")
Frame_Data.place(x=440 , y=100, width=890, height=575)

# Variables
rollno = tk.StringVar()
name = tk.StringVar()
email = tk.StringVar()
gender = tk.StringVar()
class_var = tk.StringVar()
contact = tk.StringVar()
dob = tk.StringVar()
address = tk.StringVar()
search_box = tk.StringVar()
 
# Entry widget
Label_Name = tk.Label(Frame_Details, text="Name", font=("Times new roman", 17), bg="#e3f4f1")
Label_Name.grid(row=0, column=0, padx=2, pady=2)
Entry_Name = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17,textvariable=rollno)
Entry_Name.grid(row=0, column=1, padx=2, pady=2)
 
Label_RollNo = tk.Label(Frame_Details, text="Roll No", font=("Times new roman", 17), bg="#e3f4f1")
Label_RollNo.grid(row=1, column=0, padx=2, pady=2)
Entry_RollNo = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17, textvariable=name)
Entry_RollNo.grid(row=1, column=1, padx=2, pady=2)
 
Label_Email = tk.Label(Frame_Details, text="Email", font=("Times new roman", 17), bg="#e3f4f1")
Label_Email.grid(row=2, column=0, padx=2, pady=2)
Entry_Email = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17, textvariable=email)
Entry_Email.grid(row=2, column=1, padx=2, pady=2)
 
Label_Gender = tk.Label(Frame_Details, text="Gender", font=("Times new roman", 17), bg="#e3f4f1")
Label_Gender.grid(row=3, column=0, padx=2, pady=2)
Entry_Gender = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17, textvariable=gender)
Entry_Gender.grid(row=3, column=1, padx=2, pady=2)
 
Label_Class = tk.Label(Frame_Details, text="Class", font=("Times new roman", 17), bg="#e3f4f1")
Label_Class.grid(row=4, column=0, padx=2, pady=2)
Entry_Class = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17, textvariable=class_var)
Entry_Class.grid(row=4, column=1, padx=2, pady=2)
 
Label_Contact_No = tk.Label(Frame_Details, text="Contact No", font=("Times new roman", 17), bg="#e3f4f1")
Label_Contact_No.grid(row=6, column=0, padx=2, pady=2)
Entry_Contact_No = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17,textvariable=contact)
Entry_Contact_No.grid(row=6, column=1, padx=2, pady=2)
 
Label_DOB = tk.Label(Frame_Details, text="D.O.B", font=("Times new roman", 17), bg="#e3f4f1")
Label_DOB.grid(row=7, column=0, padx=2, pady=2)
Entry_DOB = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17, textvariable=dob)
Entry_DOB.grid(row=7, column=1, padx=2, pady=2)
 
Label_Address = tk.Label(Frame_Details, text="Address", font=("Times new roman", 17), bg="#e3f4f1")
Label_Address.grid(row=8, column=0, padx=2, pady=2)
Entry_Address = tk.Entry(Frame_Details,bd=7, font= ("Times new roman", 17),width=17, textvariable=address)
Entry_Address.grid(row=8, column=1, padx=2, pady=2)

def GET_DATA():
    con=pymysql.connect(host='localhost',user='root',password='',database='stud_ms')
    cur=con.cursor()
    cur.execute('SELECT * FROM data')
    rows=cur.fetchall()
           
    if len(rows)!=0:
        Student_table.delete(*Student_table.get_children())
        for row in rows:
           Student_table.insert('',tk.END,values=row)
        con.commit()
        con.close()

def ADD_DATA():
    if rollno.get()=="" or name.get()=="" or class_var.get =="":
        messagebox.showerror('Error','All Fields required')
    else:
        con=pymysql.connect(host='localhost',user='root',password='',database='stud_ms')
        cur = con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)" (rollno.get(), name.get(), gender.get(), class_var.get(), contact.get(), dob.get(), address.get()))
        con.commit()
        con.close()
        GET_DATA()
        CLEAR()
        messagebox.showinfo("Record has been saved successfully")
 
 
def UPDATE_DATA():
    con=pymysql.connect(host='localhost',user='root',password='',database='stud_ms')
    cur = con.cursor()
    cur.execute("Update dataset name=%s, gender=%s, class_var=%s, contact=%s, dob=%s, address=%s where rollno=%s",(name.get(), gender.get(), class_var.get(), contact.get(), dob.get(), address.get(),rollno.get()))
    con.commit()
    GET_DATA()
    con.close()
    CLEAR()
 
def CLEAR():
    rollno.set("")
    name.set("")
    gender.set("")
    class_var.set("")
    contact.set("")
    dob.set("")
    address.set("")
 
def DELETE():
    con=pymysql.connect(host='localhost',user='root',password='',database='stud_ms')
    cur=con.cursor()
    cur.execute('delete from data where rollno=%s ',rollno.get())
    con.commit()
    con.close()
    GET_DATA()
    CLEAR()
    messagebox.showinfo('Success','Record has been deleted')

def FOCUS(e):
    cursor=Student_table.focus()
    content=Student_table.item(cursor)
    row=content['values']
    rollno.set(row[0])
    name.set(row[1])
    gender.set(row[2])
    class_var.set(row[3])
    contact.set(row[4])
    dob.set(row[5])
    address.set(row[6])

#buttons
Frame_Btn = tk.Frame(Frame_Details, bg="#e3f4f1", bd=7, relief=tk.GROOVE)
Frame_Btn.place(x=15, y=390, width=348, height=120)
 
Add_Button = tk.Button(Frame_Btn, bg="#e3f4f1", text="Add", bd=7, font=("Times new roman", 15), width=13, command=ADD_DATA)
Add_Button.grid(row=0, column=0, padx=2, pady=2)
 
Delete_Button = tk.Button(Frame_Btn, bg="#e3f4f1", text="Delete", bd=7, font=("Times new roman", 15), width=13, command=DELETE)
Delete_Button.grid(row=0, column=1, padx=2, pady=2)
 
Update_Button = tk.Button(Frame_Btn, bg="#e3f4f1", text="Update", bd=7, font=("Times new roman", 15), width=13, command=UPDATE_DATA)
Update_Button.grid(row=1, column=0, padx=2, pady=2)
 
Clear_Button = tk.Button(Frame_Btn, bg="#e3f4f1", text="Clear", bd=7, font=("Times new roman", 15), width=13, command=CLEAR)
Clear_Button.grid(row=1, column=1, padx=2, pady=2)

# Search Frame
 
Frame_Search = tk.Frame(Frame_Data, bg="#e3f4f1" , bd=10, relief=tk.GROOVE)
Frame_Search.pack(side=tk.TOP, fill=tk.X)
 
Label_Search = tk.Label(Frame_Search, text="Search", bg="#e3f4f1", font=("Times new roman", 16))
Label_Search.grid(row=0, column=0, padx=12, pady=2)
 
Search_Box = ttk.Combobox(Frame_Search, font=("Times new roman", 16), state="readonly", textvariable=search_box)
Search_Box['values'] = ("Name", "Roll No", "Email", "Class", "Contact No", "D.O.B" )
Search_Box.grid(row=0, column=1, padx=12, pady=2)
 
Search_Button = tk.Button(Frame_Search, bg="#e3f4f1", text="Search", bd=7, font=("Times new roman", 15), width=14)
Search_Button.grid(row=0, column=2, padx=12, pady=2)
 
Show_Button = tk.Button(Frame_Search, bg="#e3f4f1", text="Show", bd=7, font=("Times new roman", 15), width=14)
Show_Button.grid(row=0, column=3, padx=12, pady=2)

# Database Frame
Frame_Database = tk.Frame(Frame_Data, bg="#e3f4f1", bd=11, relief=tk.GROOVE)
Frame_Database.pack(fill=tk.BOTH, expand=True)
 
Scroll_X = tk.Scrollbar(Frame_Database, orient=tk.HORIZONTAL)
Scroll_Y = tk.Scrollbar(Frame_Database, orient=tk.VERTICAL)
 
Student_table = ttk.Treeview(Frame_Database, columns=("Name", "Roll No", "Gender", "Class","Contact No","D.O.B", "Address"), yscrollcommand= Scroll_Y.set,xscrollcommand= Scroll_X.set)
 
Scroll_X.config(command=Student_table.xview)
Scroll_X.pack(side=tk.BOTTOM, fill=tk.X)
Scroll_Y.config(command=Student_table.yview)
Scroll_Y.pack(side=tk.RIGHT, fill=tk.Y)
 
Student_table.heading("Roll No", text="Roll No")
Student_table.heading("Name", text="Name")
Student_table.heading("Gender", text="Gender")
Student_table.heading("Class", text="Class")
Student_table.heading("Contact No", text="Contact No")
Student_table.heading("D.O.B", text="D.O.B")
Student_table.heading("Address", text="Address")
 
Student_table['show']='headings'
Student_table.column("Roll No",width= 100)
Student_table.column("Name",width= 100)
Student_table.column("Gender",width= 100)
Student_table.column("Class",width= 100)
Student_table.column("Contact No",width= 100)
Student_table.column("D.O.B",width= 100)
Student_table.column("Address",width= 150)
 
Student_table.pack(fill=tk.BOTH, expand=True)

window.mainloop()
