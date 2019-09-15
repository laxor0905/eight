from tkinter import *
from tkinter import messagebox
from tkinter import ttk

students = []


def addStu():
    global students
    global std

    std = Student(e1.get(), e2.get(), e3.get(), e4.get())

    students.append(std)
    messagebox.showinfo("Added", "Student Added")
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

    for a in students:
        tv.insert('', 'end', values=(a.getName(), a.getGrade(), a.getSection()))

    students.clear()


def delStu():
    selected = tv.selection()
    tv.delete(selected)
    messagebox.showinfo('Delete', 'Student Removed')
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def updateStu():
    selected_item = tv.selection()[0]
    tv.item(selected_item,  values=(e1.get(), e2.get(), e3.get()))
    messagebox.showinfo('Update', 'Student Updated')
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def showContent():
    print(tv.selection())

    for er in tv.selection():
        a1, a2, a3, a4 = tv.item(er, 'values')
        e1.insert(END, a1)
        e2.insert(END, a2)
        e3.insert(END, a3)
        e4.insert(END, a4)


class Student:
    def __init__(self, fName, lName, grade, section):
        self.fName = fName
        self.lName = lName
        self.grade = grade
        self.section = section

    def getName(self):
        return self.fName + " " + self.lName

    def getGrade(self):
        return self.grade

    def getSection(self):
        return self.section

    def getFirstname(self):
        return self.fName

    def getLastname(self):
        return self.lName


frame = Tk()
frame.title('Student Registration')


tv = ttk.Treeview(frame)
tv.grid(row=4, columnspan=5)

tv["columns"] = ("name", "grade", "section")
tv.column("#0", width=0, stretch=NO)
tv.column("name")
tv.column("grade")
tv.column("section")

tv.heading("#1",text="Student name", anchor=W)
tv.heading("#2", text="Grade", anchor=W)
tv.heading("#3", text="Section", anchor=W)


l1 = Label(frame, text='First Name').grid(row=0, column=0, padx=10, pady=15)
l2 = Label(frame, text='Last Name').grid(row=1, column=0, padx=10, pady=15)
l3 = Label(frame, text='Grade Level').grid(row=2, column=0, padx=10, pady=15)
l4 = Label(frame, text='Section').grid(row=3, column=0, padx=10, pady=15)

e1 = Entry(frame)
e1.grid(row=0, column=1, padx=10, pady=15)
e2 = Entry(frame)
e2.grid(row=1, column=1, padx=10, pady=15)
e3 = Entry(frame)
e3.grid(row=2, column=1, padx=10, pady=15)
e4 = Entry(frame)
e4.grid(row=3, column=1, padx=10, pady=15)

b1 = Button(frame, text='Add', width='10', command=addStu).grid(row=0, column=2, padx=10, pady=15)
b2 = Button(frame, text='Delete', width='10', command=delStu).grid(row=1, column=2, padx=10, pady=15)
b3 = Button(frame, text='Update', width='10', command=updateStu).grid(row=2, column=2, padx=10, pady=15)
b4 = Button(frame, text='Exit', width='10', command=frame.destroy).grid(row=3, column=2, padx=10, pady=15)


frame.mainloop()
