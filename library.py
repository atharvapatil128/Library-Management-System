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



        labeltitle = Label(self.root, text = "Library Management System", bg="lavender", fg = "black", bd = 12, relief = GROOVE, font = ("inter", 30, "bold"), padx = 2, pady = 5)
        # To display the label, we need to pack it
        labeltitle.pack(side = TOP, fill = X)

        frame = Frame(self.root, bd = 12, relief = GROOVE, padx = 20, bg = "lavender")
        frame.place(x = 0, y = 100, width = 1500, height = 400)


        # =================== DataFrame Left ===================
        DataFrameLeft = LabelFrame(frame, text = "Member Information", bg="lavender", fg = "black", bd = 12, relief = GROOVE, font = ("inter", 12, "bold"))
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

        labelBookId = Label(DataFrameLeft, text = "Book ID:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelBookId.grid(row = 0, column = 2, sticky = W)
        txtBookId = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.bookid_var, width = 29)
        txtBookId.grid(row = 0, column = 3)

        labelBookTitle = Label(DataFrameLeft, text = "Book Title:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelBookTitle.grid(row = 1, column = 2, sticky = W)
        txtBookTitle = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.booktitle_var, width = 29)
        txtBookTitle.grid(row = 1, column = 3)

        labelAuthor = Label(DataFrameLeft, text = "Author:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelAuthor.grid(row = 2, column = 2, sticky = W)
        txtAuthor = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.author_var, width = 29)
        txtAuthor.grid(row = 2, column = 3)

        labelDateBorrowed = Label(DataFrameLeft, text = "Date Borrowed:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelDateBorrowed.grid(row = 3, column = 2, sticky = W)
        txtDateBorrowed = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.dateborrowed_var, width = 29)
        txtDateBorrowed.grid(row = 3, column = 3)

        labelDateDue = Label(DataFrameLeft, text = "Date Due:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelDateDue.grid(row = 4, column = 2, sticky = W)
        txtDateDue = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.datedue_var, width = 29)
        txtDateDue.grid(row = 4, column = 3)

        labelDaysOnBook = Label(DataFrameLeft, text = "Days On Book:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelDaysOnBook.grid(row = 5, column = 2, sticky = W)
        txtDaysOnBook = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.daysonbook_var, width = 29)
        txtDaysOnBook.grid(row = 5, column = 3)

        labelLateReturnFine = Label(DataFrameLeft, text = "Late Return Fine:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelLateReturnFine.grid(row = 6, column = 2, sticky = W)
        txtLateReturnFine = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.latereturnfine_var, width = 29)
        txtLateReturnFine.grid(row = 6, column = 3)

        labelDateOverdate = Label(DataFrameLeft, text = "Date Over Due", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelDateOverdate.grid(row = 7, column = 2, sticky = W)
        txtDateOverdate = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.dateoverdue_var, width = 29)
        txtDateOverdate.grid(row = 7, column = 3)

        labelActualPrice = Label(DataFrameLeft, text = "Actual Price:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelActualPrice.grid(row = 8, column = 2, sticky = W)
        txtActualPrice = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.finalprice_var, width = 29)
        txtActualPrice.grid(row = 8, column = 3)



        # =================== DataFrame Right ===================
        DataFrameRight = LabelFrame(frame, text = "Book Information", bg="lavender", fg = "black", bd = 12, relief = GROOVE, font = ("inter", 12, "bold"))
        DataFrameRight.place(x = 910, y = 5, width = 520, height = 350)

        self.txtBox = Text(DataFrameRight, font = ("inter", 12, "bold"), width = 26, height = 15, padx = 2, pady = 6)
        self.txtBox.grid(row = 0, column = 2)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row = 0, column = 1, sticky = "ns")

        listBooks = ['The Hunger Games', 'Harry Potter and the Order of the Phoenix', 'Pride and Prejudice', 'To Kill a Mockingbird', 'The Book Thief', 'Twilight', 'Animal Farm', 'The Chronicles of Narnia', 'The Fault in Our Stars', 'Gone with the Wind', 'The Giving Tree', 'Wuthering Heights', 'The Picture of Dorian Gray', 'Jane Eyre']


        def SelectBook(event=""):
            value = str(listBox.get(listBox.curselection()))
            x = value
            if (x=='The Hunger Games'):
                self.bookid_var.set("BKID1")
                self.booktitle_var.set("TheHungerGames")
                self.author_var.set("Suzanne Collins")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 20")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 60")

            elif (x=='Harry Potter and the Order of the Phoenix'):
                self.bookid_var.set("BKID2")
                self.booktitle_var.set("Harry Potter Order of the Phoenix")
                self.author_var.set("JK Rowling")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 20")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 55")

            elif (x=='Pride and Prejudice'):
                self.bookid_var.set("BKID3")
                self.booktitle_var.set("Pride and Prejudice")
                self.author_var.set("Jane Austen")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 15")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 40")
            
            elif (x=='To Kill a Mockingbird'):
                self.bookid_var.set("BKID4")
                self.booktitle_var.set("To Kill a Mockingbird")
                self.author_var.set("Jane Austen")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 15")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 45")

            elif (x=='The Book Thief'):
                self.bookid_var.set("BKID5")
                self.booktitle_var.set("The Book Thief")
                self.author_var.set("Markus Zusak")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 15")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 40")

            
            elif (x=='Twilight'):
                self.bookid_var.set("BKID6")
                self.booktitle_var.set("Twilight")
                self.author_var.set("Stephenie Meyer")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 20")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 45")

            elif (x=='Animal Farm'):
                self.bookid_var.set("BKID7")
                self.booktitle_var.set("Animal Farm")
                self.author_var.set("George Orwell")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 20")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 50")

            elif (x=='The Chronicles of Narnia'):
                self.bookid_var.set("BKID8")
                self.booktitle_var.set("The Chronicles of Narnia")
                self.author_var.set("C. S. Lewis")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 20")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 45")

            elif (x=='The Fault in Our Stars'):
                self.bookid_var.set("BKID9")
                self.booktitle_var.set("The Fault in Our Stars")
                self.author_var.set("John Green")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 20")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 55")

            elif (x=='Gone with the Wind'):
                self.bookid_var.set("BKID10")
                self.booktitle_var.set("Gone with the Wind")
                self.author_var.set("Margaret Mitchell")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 10")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 30")

            elif (x=='The Giving Tree'):
                self.bookid_var.set("BKID11")
                self.booktitle_var.set("The Giving Tree")
                self.author_var.set("Shel Silverstein")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 12")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 40")

            elif (x=='Wuthering Heights'):
                self.bookid_var.set("BKID12")
                self.booktitle_var.set("Wuthering Heights")
                self.author_var.set("Emily Brontë")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 12")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 30")

            elif (x=='The Picture of Dorian Gray'):
                self.bookid_var.set("BKID13")
                self.booktitle_var.set("The Picture of Dorian Gray")
                self.author_var.set("Oscar Wilde")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 10")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 40")

            elif (x=='Jane Eyre'):
                self.bookid_var.set("BKID14")
                self.booktitle_var.set("Jane Eyre")
                self.author_var.set("Charlotte Brontë")
                
                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1 + d2

                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs. 6")
                self.dateoverdue_var.set("NA")
                self.finalprice_var.set("Rs. 20")
            

            




        listBox = Listbox(DataFrameRight, font = ("inter", 12, "bold"), width = 24, height = 15)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row = 0, column = 0, padx = 4)
        listScrollbar.config(command = listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)


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


        self.library_table = ttk.Treeview(Table_frame, column = ("membertype", "prnno", "id", "firstname", "lastname", "address", "postid", "mobile", "bookid", "booktitle", "author", "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"), xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)

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
        self.library_table.heading("bookid", text = "Book ID")
        self.library_table.heading("booktitle", text = "Book Title")
        self.library_table.heading("author", text = "Author")
        self.library_table.heading("dateborrowed", text = "Date of Borrowing")
        self.library_table.heading("datedue", text = "Due Date")
        self.library_table.heading("days", text = "DaysOnBook")
        self.library_table.heading("latereturnfine", text = "LateReturnFine")
        self.library_table.heading("dateoverdue", text = "DateOverDue")
        self.library_table.heading("finalprice", text = "Final Price")

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
        self.library_table.column("bookid", width = 100)
        self.library_table.column("booktitle", width = 100)
        self.library_table.column("author", width = 100)
        self.library_table.column("dateborrowed", width = 100)
        self.library_table.column("datedue", width = 100)
        self.library_table.column("days", width = 100)
        self.library_table.column("latereturnfine", width = 100)
        self.library_table.column("dateoverdue", width = 100)
        self.library_table.column("finalprice", width = 100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)


    def add_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root@2002",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into libraryms values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
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
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success", "Member Info has been Inserted Successfully.")

    def update(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root@2002",database ="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("update libraryms set Member=%s, ID=%s, FirstName=%s, LastName=%s, Address=%s, PostId=%s,Mobile=%s, BookId=%s, BookTitle=%s, Author=%s, DateBorrowed=%s, DateDue=%s, DaysofBook=%s, LateReturnFine=%s, DateOverDue=%s, FinalPrice=%s, PRN_NO=%s", (
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
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "Member Info has been Updated Successfully.")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root@2002",database ="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from libraryms")
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


    def show_data(self):
        self.txtBox.insert(END, "Member Type\t\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No:\t\t" + self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID:\t\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END, "Name:\t\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "Address:\t\t" + self.address_var.get() + "\n")
        self.txtBox.insert(END, "Mobile:\t\t" + self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "PostCode:\t\t" + self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Author:\t\t" + self.author_var.get() + "\n")

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
            conn = mysql.connector.connect(host="localhost",username="root",password="root@2002",database ="mydata")
            my_cursor = conn.cursor()
            query = "delete from libraryms where PRN_NO=%s"
            value=(self.prn_var.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Member Info has been Deleted.")
            



if __name__ == "__main__":
    root=Tk()
    obj = LibraryManagementSystem(root)
    # To make sure that the window remains open
    root.mainloop()