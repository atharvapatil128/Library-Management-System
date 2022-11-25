from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import datetime
import tkinter

from matplotlib.table import Table


class BookManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Management System")
        self.root.geometry("1500x780+0+0")


        # =================== Variables ===================
        
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()



        labeltitle = Label(self.root, text = "Books Management System", bg="lavender", fg = "black", bd = 12, relief = GROOVE, font = ("inter", 30, "bold"), padx = 2, pady = 5)
        # To display the label, we need to pack it
        labeltitle.pack(side = TOP, fill = X)

        frame = Frame(self.root, bd = 12, relief = GROOVE, padx = 20, bg = "lavender")
        frame.place(x = 0, y = 100, width = 1500, height = 400)

        # =================== Presets ===================
        d1 = datetime.date.today()
        d2 = datetime.timedelta(days = 15)
        d3 = d1 + d2

        # =================== DataFrame Left ===================
        DataFrameLeft = LabelFrame(frame, text = "Book Information", bg="lavender", fg = "black", bd = 12, relief = GROOVE, font = ("inter", 12, "bold"))
        DataFrameLeft.place(x = 0, y = 5, width = 900, height = 350)

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
        txtDateBorrowed.insert(END,d1)
        txtDateBorrowed.grid(row = 3, column = 3)

        labelDateDue = Label(DataFrameLeft, text = "Date Due:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelDateDue.grid(row = 4, column = 2, sticky = W)
        txtDateDue = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.datedue_var, width = 29)
        txtDateDue.insert(END,d3)
        txtDateDue.grid(row = 4, column = 3)

        labelDaysOnBook = Label(DataFrameLeft, text = "Days On Book:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelDaysOnBook.grid(row = 5, column = 2, sticky = W)
        txtDaysOnBook = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.daysonbook_var, width = 29)
        txtDaysOnBook.insert(END,"0")
        txtDaysOnBook.grid(row = 5, column = 3)

        labelLateReturnFine = Label(DataFrameLeft, text = "Late Return Fine:", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelLateReturnFine.grid(row = 6, column = 2, sticky = W)
        txtLateReturnFine = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.latereturnfine_var, width = 29)
        txtLateReturnFine.insert(END,"20")
        txtLateReturnFine.grid(row = 6, column = 3)

        labelDateOverdate = Label(DataFrameLeft, text = "Date Over Due", bg = "lavender", font = ("inter", 12, "bold"), padx = 2, pady = 6)
        labelDateOverdate.grid(row = 7, column = 2, sticky = W)
        txtDateOverdate = Entry(DataFrameLeft, font = ("inter", 12, "bold"), textvariable = self.dateoverdue_var, width = 29)
        txtDateOverdate.insert(END,"-")
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


        # =================== Frame for Buttons ===================
        FrameButton = Frame(self.root, bd = 12, relief = GROOVE, padx = 20, bg = "lavender")
        FrameButton.place(x = 0, y = 500, width = 1500, height = 70)

        btnAddData = Button(FrameButton, text = "Add Book", command = self.add_data, font = ("inter", 12, "bold"), width = 23, bg = "dark slate blue", fg = "white")
        btnAddData.grid(row = 0, column = 0)

        btnAddData = Button(FrameButton, text = "Display Book", command = self.show_data,font = ("inter", 12, "bold"), width = 23, bg = "dark slate blue", fg = "white")
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


        self.library_table = ttk.Treeview(Table_frame, column = ("bookid", "booktitle", "author", "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", "finalprice"), xscrollcommand = xscroll.set, yscrollcommand = yscroll.set)

        xscroll.pack(side = BOTTOM, fill = X)
        yscroll.pack(side = RIGHT, fill = Y)

        xscroll.config(command = self.library_table.xview)
        yscroll.config(command = self.library_table.yview)


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
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("insert into books_lib values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
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

        messagebox.showinfo("Success", "Book Info has been Inserted Successfully.")

    def update(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database ="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("update books_lib set BookTitle=%s, Author=%s, DateBorrowed=%s, DateDue=%s, DaysOnBook=%s, LateReturnFine=%s, DateOverDue=%s, ActualPrice=%s where BookID=%s", (
                                                                                                            self.booktitle_var.get(),
                                                                                                            self.author_var.get(),
                                                                                                            self.dateborrowed_var.get(),
                                                                                                            self.datedue_var.get(),
                                                                                                            self.daysonbook_var.get(),
                                                                                                            self.latereturnfine_var.get(),
                                                                                                            self.dateoverdue_var.get(),
                                                                                                            self.finalprice_var.get(),
                                                                                                            self.bookid_var.get(),
                                                                                                            )) 
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success", "Book Info has been Updated Successfully.")

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="root",database ="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from books_lib")
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

        self.bookid_var.set(row[0]),
        self.booktitle_var.set(row[1]),
        self.author_var.set(row[2]),
        self.dateborrowed_var.set(row[3]),
        self.datedue_var.set(row[4]),
        self.daysonbook_var.set(row[5]),
        self.latereturnfine_var.set(row[6]),
        self.dateoverdue_var.set(row[7]),
        self.finalprice_var.set(row[8])


    def show_data(self):
        self.txtBox.insert(END, "Book ID:\t\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Author:\t\t" + self.author_var.get() + "\n")
        self.txtBox.insert(END, "Date Borrowed:\t\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "Date Due:\t\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END, "Days on Book:\t\t" + self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END, "Late Return Fine:\t\t" + self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END, "Final Price:\t\t" + self.finalprice_var.get() + "\n")

    def reset(self):
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
        iExit = tkinter.messagebox.askyesno("Book Management System", "Do you want to exit?")

        if iExit > 0:
            self.root.destroy()
            return

    def delete(self):
        if self.bookid_var.get() == "":
            messagebox.showerror("Error", "Select a Book DataField!")
        else:
            conn = mysql.connector.connect(host="localhost",username="root",password="root",database ="mydata")
            my_cursor = conn.cursor()
            query = "delete from books_lib where BookID=%s"
            value=(self.bookid_var.get(),) # fix this
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()

            messagebox.showinfo("Success", "Member Info has been Deleted.")
            



if __name__ == "__main__":
    root=Tk()
    obj = BookManagementSystem(root)
    # To make sure that the window remains open
    root.mainloop()