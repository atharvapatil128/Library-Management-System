from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter

from matplotlib.table import Table


class StudentManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1500x780+0+0")


        # =================== Variables ===================
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()



        labeltitle = Label(self.root, text = "Student Management System", bg="lavender", fg = "black", bd = 12, relief = GROOVE, font = ("inter", 30, "bold"), padx = 2, pady = 5)
        # To display the label, we need to pack it
        labeltitle.pack(side = TOP, fill = X)

        frame = Frame(self.root, bd = 12, relief = GROOVE, padx = 20, bg = "lavender")
        frame.place(x = 0, y = 100, width = 1500, height = 400)


        # =================== DataFrame Left ===================
        DataFrameLeft = LabelFrame(frame, text = "Student Information", bg="lavender", fg = "black", bd = 12, relief = GROOVE, font = ("inter", 12, "bold"))
        DataFrameLeft.place(x = 0, y = 5, width = 900, height = 350)

        labelMember = Label(DataFrameLeft, text = "Member: ", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelMember.grid(row = 0, column = 0, sticky = W)
        
        comMember = ttk.Combobox(DataFrameLeft, font = ("inter", 12, "bold"),  textvariable = self.member_var, width = 27, state = "readonly")
        comMember["value"]=("Authorities", "Student", "Professor")
        comMember.grid(row = 0, column = 1)


        labelPRN_No = Label(DataFrameLeft, text = "PRN: ", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelPRN_No.grid(row = 1, column = 0, sticky = W)
        txtPRN_NO = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.prn_var, width = 29)
        txtPRN_NO.grid(row = 1, column = 1)

        labelID = Label(DataFrameLeft, text = "ID No.: ", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelID.grid(row = 2, column = 0, sticky = W)
        txtID = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.id_var, width = 29)
        txtID.grid(row = 2, column = 1)

        labelFirstName = Label(DataFrameLeft, text = "First Name: ", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelFirstName.grid(row = 3, column = 0, sticky = W)
        txtFirstName = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.firstname_var, width = 29)
        txtFirstName.grid(row = 3, column = 1)

        labelLastName = Label(DataFrameLeft, text = "Last Name: ", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelLastName.grid(row = 4, column = 0, sticky = W)
        txtLastName = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.lastname_var, width = 29)
        txtLastName.grid(row = 4, column = 1)

        labelAddress = Label(DataFrameLeft, text = "Address:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelAddress.grid(row = 5, column = 0, sticky = W)
        txtAddress = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.address_var, width = 29)
        txtAddress.grid(row = 5, column = 1)

        labelPostCode = Label(DataFrameLeft, text = "Postal Code:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelPostCode.grid(row = 6, column = 0, sticky = W)
        txtPostCode = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.postcode_var, width = 29)
        txtPostCode.grid(row = 6, column = 1)

        labelMobile = Label(DataFrameLeft, text = "Mobile:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelMobile.grid(row = 7, column = 0, sticky = W)
        txtMobile = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.mobile_var, width = 29)
        txtMobile.grid(row = 7, column = 1)




        # =================== DataFrame Right ===================
        
        DataFrameRight = LabelFrame(frame, text = "Student Information", bg="lavender", fg = "black", bd = 12, relief = GROOVE, font = ("inter", 12, "bold"))
        DataFrameRight.place(x = 910, y = 5, width = 520, height = 350)
        
        self.txtBox = Text(DataFrameRight, font = ("inter", 12, "bold"), width = 26, height = 15, padx = 2, pady = 6)
        self.txtBox.grid(row = 0, column = 2)


        # =================== Frame for Buttons ===================
        FrameButton = Frame(self.root, bd = 12, relief = GROOVE, padx = 20, bg = "lavender")
        FrameButton.place(x = 0, y = 500, width = 1500, height = 70)

        btnAddData = Button(FrameButton, text = "Add Data", command = self.add_data, font = ("inter", 12, "bold"), width = 23, bg = "dark slate blue", fg = "white")
        btnAddData.grid(row = 0, column = 0)

        btnAddData = Button(FrameButton, text = "Show Data", command = self.show_data,font = ("inter", 12, "bold"), width = 23, bg = "dark slate blue", fg = "white")
        btnAddData.grid(row = 0, column = 1)

        btnAddData = Button(FrameButton, text = "Update", command = self.update, font = ("inter", 12, "bold"), width = 23, bg = "dark slate blue", fg = "white")
        btnAddData.grid(row = 0, column = 2)

        btnAddData = Button(FrameButton, text = "Delete", command = self.delete, font = ("inter", 12, "bold"), width = 23, bg = "dark slate blue", fg = "white")
        btnAddData.grid(row = 0, column = 3)

        btnAddData = Button(FrameButton, text = "Reset", command = self.reset, font = ("inter", 12, "bold"), width = 23, bg = "dark slate blue", fg = "white")
        btnAddData.grid(row = 0, column = 4)

        btnAddData = Button(FrameButton, text = "Exit", command = self.iExit, font = ("inter", 12, "bold"), width = 23, bg = "dark slate blue", fg = "white")
        btnAddData.grid(row = 0, column = 5)


        # =================== Frame for Information (MySQL) ===================
        FrameDetails = Frame(self.root, bd = 12, relief = GROOVE, padx = 20, bg = "lavender")
        FrameDetails.place(x = 0, y = 570, width = 1500, height = 195)

        Table_frame = Frame(FrameDetails, bd = 4, relief = GROOVE, bg = "lavender")
        Table_frame.place(x = 0, y = 2, width = 1400, height = 190)

        xscroll = ttk.Scrollbar(Table_frame, orient = HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient = VERTICAL)


        self.library_table = ttk.Treeview(Table_frame, column = ("membertype", "prnno", "id", "firstname", "lastname", "address", "postid", "mobile"), xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)

        xscroll.pack(side = BOTTOM, fill = X)
        yscroll.pack(side = RIGHT, fill = Y)

        xscroll.config(command = self.library_table.xview)
        yscroll.config(command = self.library_table.yview)


        self.library_table.heading("membertype", text = "Member Type")
        self.library_table.heading("prnno", text = "PRN No.")
        self.library_table.heading("id", text = "ID")
        self.library_table.heading("firstname", text = "First Name")
        self.library_table.heading("lastname", text = "Last Name")
        self.library_table.heading("address", text = "Address")
        self.library_table.heading("postid", text = "PostCode")
        self.library_table.heading("mobile", text = "Mobile")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill = BOTH, expand = 1)

        self.library_table.column("membertype", width = 100)
        self.library_table.column("prnno", width = 100)
        self.library_table.column("id", width = 100)
        self.library_table.column("firstname", width = 100)
        self.library_table.column("lastname", width = 100)
        self.library_table.column("address", width = 100)
        self.library_table.column("postid", width = 100)
        self.library_table.column("mobile", width = 100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)


    def add_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into student_lib values(%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                            self.prn_var.get(),
                                                                                                            self.member_var.get(),
                                                                                                            self.id_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.lastname_var.get(),
                                                                                                            self.address_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobile_var.get()
                                                                                                            ))
        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success", "Student Info has been Inserted Successfully.")

    def update(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database ="mydata")
        my_cursor = conn.cursor()
        # my_cursor.execute("update student_lib set Member=%s, ID=%s, FirstName=%s, LastName=%s, Address=%s, Postcode=%s,Mobile=%s, PRN_NO=%s", (
        #                                                                                                     self.member_var.get(),
        #                                                                                                     self.id_var.get(),
        #                                                                                                     self.firstname_var.get(),
        #                                                                                                     self.lastname_var.get(),
        #                                                                                                     self.address_var.get(),
        #                                                                                                     self.postcode_var.get(),
        #                                                                                                     self.mobile_var.get(),
        #                                                                                                     self.prn_var.get()
        #                                                                                                     ))
        my_cursor.execute("update student_lib set Member=%s, ID=%s, FirstName=%s, LastName=%s, Address=%s, Postcode=%s,Mobile=%s where PRN_NO=%s", (
                                                                                                            self.member_var.get(),
                                                                                                            self.id_var.get(),
                                                                                                            self.firstname_var.get(),
                                                                                                            self.lastname_var.get(),
                                                                                                            self.address_var.get(),
                                                                                                            self.postcode_var.get(),
                                                                                                            self.mobile_var.get(),
                                                                                                            self.prn_var.get()
                                                                                                            ))

        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "Student Info has been Updated Successfully.")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database ="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student_lib")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values = i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[1]),
        self.prn_var.set(row[0]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address_var.set(row[5]),
        self.postcode_var.set(row[6]),
        self.mobile_var.set(row[7]),


    def show_data(self):
        self.txtBox.insert(END, "Member Type\t\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No:\t\t" + self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID:\t\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END, "Name:\t\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "Address:\t\t" + self.address_var.get() + "\n")
        self.txtBox.insert(END, "Mobile:\t\t" + self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "PostCode:\t\t" + self.postcode_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.txtBox.delete("1.0", END)


    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System", "Do you want to exit?")

        if iExit > 0:
            self.root.destroy()
            return

    def delete(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error", "Select a Member DataField!")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database ="mydata")
            my_cursor = conn.cursor()
            query = "delete from student_lib where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Student Info has been Deleted.")
            



if __name__ == "__main__":
    root=Tk()
    obj = StudentManagementSystem(root)
    # To make sure that the window remains open
    root.mainloop()