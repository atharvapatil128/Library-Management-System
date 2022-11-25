from msilib.schema import ListBox
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter

from matplotlib.table import Table


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
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
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()

        labeltitle = Label(self.root, text="Library Management System", bg="lavender",
                           fg="black", bd=12, relief=GROOVE, font=("inter", 30, "bold"), padx=2, pady=5)
        # To display the label, we need to pack it
        labeltitle.pack(side=TOP, fill=X)

        frame = Frame(self.root, bd=12, relief=GROOVE, padx=20, bg="lavender")
        frame.place(x=0, y=100, width=1500, height=400)

        # =================== DataFrame Left ===================
        DataFrameLeft = LabelFrame(frame, text="Member Information", bg="lavender",
                                   fg="black", bd=12, relief=GROOVE, font=("inter", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        labelMember = Label(DataFrameLeft, text="Member: ", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelMember.grid(row=0, column=0, sticky=W)

        comMember = ttk.Combobox(DataFrameLeft, font=(
            "inter", 12, "bold"),  textvariable=self.member_var, width=27, state="readonly")
        comMember["value"] = ("Authorities", "Student", "Professor")
        comMember.grid(row=0, column=1)

        labelPRN_No = Label(DataFrameLeft, text="PRN: ", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_NO = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.prn_var, width=29)
        txtPRN_NO.grid(row=1, column=1)

        labelID = Label(DataFrameLeft, text="ID No.: ", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelID.grid(row=2, column=0, sticky=W)
        txtID = Entry(DataFrameLeft, font=("inter", 12, "bold"),
                      textvariable=self.id_var, width=29)
        txtID.grid(row=2, column=1)

        labelFirstName = Label(DataFrameLeft, text="First Name: ", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.firstname_var, width=29)
        txtFirstName.grid(row=3, column=1)

        labelLastName = Label(DataFrameLeft, text="Last Name: ", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.lastname_var, width=29)
        txtLastName.grid(row=4, column=1)

        labelAddress = Label(DataFrameLeft, text="Address:", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelAddress.grid(row=5, column=0, sticky=W)
        txtAddress = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.address_var, width=29)
        txtAddress.grid(row=5, column=1)

        labelPostCode = Label(DataFrameLeft, text="Postal Code:", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelPostCode.grid(row=6, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.postcode_var, width=29)
        txtPostCode.grid(row=6, column=1)

        labelMobile = Label(DataFrameLeft, text="Mobile:", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelMobile.grid(row=7, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.mobile_var, width=29)
        txtMobile.grid(row=7, column=1)

        labelBookId = Label(DataFrameLeft, text="Book ID:", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelBookId.grid(row=0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.bookid_var, width=29)
        txtBookId.grid(row=0, column=3)

        labelBookTitle = Label(DataFrameLeft, text="Book Title:", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.booktitle_var, width=29)
        txtBookTitle.grid(row=1, column=3)

        labelAuthor = Label(DataFrameLeft, text="Author:", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.author_var, width=29)
        txtAuthor.grid(row=2, column=3)

        labelDateBorrowed = Label(DataFrameLeft, text="Date Borrowed:", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.dateborrowed_var, width=29)
        txtDateBorrowed.grid(row=3, column=3)

        labelDateDue = Label(DataFrameLeft, text="Date Due:", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.datedue_var, width=29)
        txtDateDue.grid(row=4, column=3)

        labelDaysOnBook = Label(DataFrameLeft, text="Days On Book:", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.daysonbook_var, width=29)
        txtDaysOnBook.grid(row=5, column=3)

        labelLateReturnFine = Label(DataFrameLeft, text="Late Return Fine:", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.latereturnfine_var, width=29)
        txtLateReturnFine.grid(row=6, column=3)

        labelDateOverdate = Label(DataFrameLeft, text="Date Over Due", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelDateOverdate.grid(row=7, column=2, sticky=W)
        txtDateOverdate = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.dateoverdue_var, width=29)
        txtDateOverdate.grid(row=7, column=3)

        labelActualPrice = Label(DataFrameLeft, text="Actual Price:", bg="lavender", font=(
            "inter", 12, "bold"), padx=2, pady=6)
        labelActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=(
            "inter", 12, "bold"), textvariable=self.finalprice_var, width=29)
        txtActualPrice.grid(row=8, column=3)


        FrameDetailsR = Frame(
            self.root, bd=12, relief=GROOVE, padx=10, bg="lavender")
        FrameDetailsR.place(x=935, y=122, width=550, height=345)

        # ---------------------------------------BOOKS TABLE-------------------------------------------------

        Table_frameR1 = Frame(FrameDetailsR, bd=4,
                              relief=GROOVE, bg="lavender")
        Table_frameR1.place(x=0, y=6, width=250, height=300)

        xscrollR1 = ttk.Scrollbar(Table_frameR1, orient=HORIZONTAL)
        yscrollR1 = ttk.Scrollbar(Table_frameR1, orient=VERTICAL)

        self.books_table = ttk.Treeview(Table_frameR1, column=(
            "bookID"), xscrollcommand=xscrollR1.set, yscrollcommand=yscrollR1.set)

        xscrollR1.pack(side=BOTTOM, fill=X)
        yscrollR1.pack(side=RIGHT, fill=Y)

        xscrollR1.config(command=self.books_table.xview)
        yscrollR1.config(command=self.books_table.yview)

        self.books_table.heading("bookID", text="Book ID")

        self.books_table["show"] = "headings"
        self.books_table.pack(fill=BOTH, expand=1)

        self.books_table.column("bookID", width=100)

         ##-----------------------------------------------------------------------------------------
        self.fetch_data3(table_name="books_lib")
        self.books_table.bind("<ButtonRelease-1>", self.getcursors1)

        # ---------------------------------------STUDENTS TABLE-------------------------------------------------

        Table_frameR2 = Frame(FrameDetailsR, bd=4,
                              relief=GROOVE, bg="lavender")
        Table_frameR2.place(x=258, y=6, width=250, height=300)

        xscrollR2 = ttk.Scrollbar(Table_frameR2, orient=HORIZONTAL)
        yscrollR2 = ttk.Scrollbar(Table_frameR2, orient=VERTICAL)

        self.students_table = ttk.Treeview(Table_frameR2, column=(
            "PRN_NO"), xscrollcommand=xscrollR2.set, yscrollcommand=yscrollR2.set)

        xscrollR2.pack(side=BOTTOM, fill=X)
        yscrollR2.pack(side=RIGHT, fill=Y)

        xscrollR2.config(command=self.students_table.xview)
        yscrollR2.config(command=self.students_table.yview)

        self.students_table.heading("PRN_NO", text="PRN")
        self.students_table["show"] = "headings"
        self.students_table.pack(fill=BOTH, expand=1)

        self.students_table.column("PRN_NO", width=100)

        
        ##-----------------------------------------------------------------------------------------
        self.fetch_data1(table_name="student_lib")
        self.students_table.bind("<ButtonRelease-1>", self.getcursors)

        # =================== Frame for Buttons ===================
        FrameButton = Frame(self.root, bd=12, relief=GROOVE,
                            padx=20, bg="lavender")
        FrameButton.place(x=100, y=500, width=1270, height=64)

        btnAddData = Button(FrameButton, text="Add Data", command=self.add_data, font=(
            "inter", 12, "bold"), width=23, bg="dark slate blue", fg="white")
        btnAddData.grid(row=0, column=0)

        # btnAddData = Button(FrameButton, text = "Show Data", command = self.show_data,font = ("inter", 12, "bold"), width = 23, bg = "dark slate blue", fg = "white")
        # btnAddData.grid(row = 0, column = 1)

        btnAddData = Button(FrameButton, text="Update", command=self.update, font=(
            "inter", 12, "bold"), width=23, bg="dark slate blue", fg="white")
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(FrameButton, text="Delete", command=self.delete, font=(
            "inter", 12, "bold"), width=23, bg="dark slate blue", fg="white")
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(FrameButton, text="Reset", command=self.reset, font=(
            "inter", 12, "bold"), width=23, bg="dark slate blue", fg="white")
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(FrameButton, text="Exit", command=self.iExit, font=(
            "inter", 12, "bold"), width=23, bg="dark slate blue", fg="white")
        btnAddData.grid(row=0, column=4)

        # =================== Frame for Information (MySQL) ===================
        FrameDetails = Frame(
            self.root, bd=12, relief=GROOVE, padx=20, bg="lavender")
        FrameDetails.place(x=0, y=570, width=1500, height=195)

        Table_frame = Frame(FrameDetails, bd=4, relief=GROOVE, bg="lavender")
        Table_frame.place(x=0, y=2, width=1400, height=190)

        xscroll = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.library_table = ttk.Treeview(Table_frame, column=("membertype", "prnno", "id", "firstname", "lastname", "address", "postid", "mobile", "bookid", "booktitle",
                                          "author", "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN No.")
        self.library_table.heading("id", text="ID")
        self.library_table.heading("firstname", text="First Name")
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("address", text="Address")
        self.library_table.heading("postid", text="PostCode")
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")
        self.library_table.heading("dateborrowed", text="Date of Borrowing")
        self.library_table.heading("datedue", text="Due Date")
        self.library_table.heading("days", text="DaysOnBook")
        self.library_table.heading("latereturnfine", text="LateReturnFine")
        self.library_table.heading("dateoverdue", text="DateOverDue")
        self.library_table.heading("finalprice", text="Final Price")

        self.library_table["show"] = "headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("id", width=100)
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100)
        self.library_table.column("address", width=100)
        self.library_table.column("postid", width=100)
        self.library_table.column("mobile", width=100)
        self.library_table.column("bookid", width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=100)
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100)
        self.library_table.column("finalprice", width=100)

        self.fetch_data2(table_name="library")
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def add_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get()
        ))
        conn.commit()
        self.fetch_data2(table_name="library")
        conn.close()

        messagebox.showinfo(
            "Success", "Member Info has been Inserted Successfully.")

    def update(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("update library set Member=%s, ID=%s, FirstName=%s, LastName=%s, Address=%s, Postcode=%s,mobile_var=%s, BookId=%s, Mobile=%s, Author=%s, DateBorrowed=%s, datedue=%s, daysofbook=%s, latereturnfine=%s, dateoverdue=%s, finalprice=%s where PRN_NO=%s", (
            self.member_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.latereturnfine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get(),
            self.prn_var.get()
        ))
        conn.commit()
        self.fetch_data2(table_name="library")
        self.reset()
        conn.close()

        messagebox.showinfo(
            "Success", "Member Info has been Updated Successfully.")

    # def fetch_data(self):
    #     conn = mysql.connector.connect(
    #         host="localhost", username="root", password="root", database="mydata")
    #     my_cursor = conn.cursor()
    #     my_cursor.execute("select * from library")
    #     rows = my_cursor.fetchall()

    #     if len(rows) != 0:
    #         self.library_table.delete(*self.library_table.get_children())
    #         for i in rows:
    #             self.library_table.insert("", END, values=i)
    #         conn.commit()
    #     conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address_var.set(row[5]),
        self.postcode_var.set(row[6]),
        self.mobile_var.set(row[7]),
        self.bookid_var.set(row[8]),
        self.booktitle_var.set(row[9]),
        self.author_var.set(row[10]),
        self.dateborrowed_var.set(row[11]),
        self.datedue_var.set(row[12]),
        self.daysonbook_var.set(row[13]),
        self.latereturnfine_var.set(row[14]),
        self.dateoverdue_var.set(row[15]),
        self.finalprice_var.set(row[16])


    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set("")
        #self.txtBox.delete("1.0", END)

    def iExit(self):
        iExit = tkinter.messagebox.askyesno(
            "Library Management System", "Do you want to exit?")

        if iExit > 0:
            self.root.destroy()
            return

    def delete(self):
        # if self.prn_var.get() == "" or self.id_var.get() == "":
        #   messagebox.showerror("Error", "Select a Member DataField!")
        # else:
        conn = mysql.connector.connect(
            host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn.cursor()
        query = "delete from library where PRN_NO=%s"
        value = (self.prn_var.get(),)
        my_cursor.execute(query, value)
        conn.commit()
        self.fetch_data2(table_name="library")
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "Member Info has been Deleted.")

    def fetch_data1(self,table_name):
        conn1 = mysql.connector.connect(
            host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn1.cursor()
        my_cursor.execute(f"select * from {table_name}")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.students_table.delete(*self.students_table.get_children())
            for i in rows:
                self.students_table.insert("", END, values=i)
            conn1.commit()
        conn1.close()
    
    def fetch_data2(self,table_name):
        conn1 = mysql.connector.connect(
            host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn1.cursor()
        my_cursor.execute(f"select * from {table_name}")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn1.commit()
        conn1.close()

    def fetch_data3(self,table_name):
        conn1 = mysql.connector.connect(
            host="localhost", username="root", password="root", database="mydata")
        my_cursor = conn1.cursor()
        my_cursor.execute(f"select * from {table_name}")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.books_table.delete(*self.books_table.get_children())
            for i in rows:
                self.books_table.insert("", END, values=i)
            conn1.commit()
        conn1.close()

    def getcursors(self, event=""):
        cursor_row = self.students_table.focus()
        content = self.students_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[1]),
        self.prn_var.set(row[0]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address_var.set(row[5]),
        self.postcode_var.set(row[6]),
        self.mobile_var.set(row[7])


    def getcursors1(self, event=""):
        cursor_row = self.books_table.focus()
        content = self.books_table.item(cursor_row)
        row = content['values']

        self.bookid_var.set(row[0]),
        self.booktitle_var.set(row[1]),
        self.author_var.set(row[2]),
        self.dateborrowed_var.set(row[3]),
        self.datedue_var.set(row[4]),
        self.daysonbook_var.set(row[5]),
        self.latereturnfine_var.set(row[6]),
        self.dateoverdue_var.set(row[7]),
        self.finalprice_var.set(row[8])


if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    # To make sure that the window remains open
    root.mainloop()
