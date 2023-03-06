# add books - title, author, ISBN, quantity, publisher, language, price, edition and source
# delete books
# update books - updating quantity
# list books - lists title, author, ISBN, quantity and source
from db_read import database, availability_books
from tkinter import *
from fpdf import FPDF
from tkinter import messagebox


def add_books():
    def add_data():
        if title.get() == "" or author.get() == "" or isbn.get() == "" or quantity.get() == "" or publisher.get() == "" or edition.get() == "" or language.get() == "" or price.get() == "" or source.get() == "":
            messagebox.showerror("Error", "Please fill all the fields", parent=add_window)
        else:
            data = {
                "Title": title.get(),
                "Author": author.get(),
                "ISBN": isbn.get(),
                "Quantity": quantity.get(),
                "Publisher": publisher.get(),
                "Edition": edition.get(),
                "Language": language.get(),
                "Price": price.get(),
                "Source": source.get()
            }
            database.child("Books").child(isbn.get()).set(data)
            messagebox.showinfo('Success', "Book Successfully Entered.", parent=add_window)
            add_window.destroy()

    add_window = Tk()
    add_window.title('Add Books')
    add_window.geometry('500x600')
    # heading label
    heading = Label(add_window, text="Add Book", font=('Times New Roman', 20, 'bold'))
    heading.place(x=80, y=60)

    # form data label
    title = Label(add_window, text="Book Title :", font='Verdana 10 bold')
    title.place(x=80, y=130)

    author = Label(add_window, text="Author Name :", font='Verdana 10 bold')
    author.place(x=80, y=160)

    isbn = Label(add_window, text="ISBN :", font='Verdana 10 bold')
    isbn.place(x=80, y=190)

    publisher = Label(add_window, text="Publisher :", font='Verdana 10 bold')
    publisher.place(x=80, y=220)

    edition = Label(add_window, text="Edition :", font='Verdana 10 bold')
    edition.place(x=80, y=250)

    language = Label(add_window, text="Language :", font='Verdana 10 bold')
    language.place(x=80, y=280)

    price = Label(add_window, text="Price :", font='Verdana 10 bold')
    price.place(x=80, y=310)

    source = Label(add_window, text="Source :", font='Verdana 10 bold')
    source.place(x=80, y=340)

    quantity = Label(add_window, text="Quantity :", font='Verdana 10 bold')
    quantity.place(x=80, y=370)

    # Entry Box ------------------------------------------------------------------

    title = StringVar()
    author = StringVar()
    isbn = StringVar()
    quantity = StringVar()
    publisher = StringVar()
    edition = StringVar()
    price = StringVar()
    language = StringVar()
    source = StringVar()

    title = Entry(add_window, width=40, textvariable=title)
    title.place(x=200, y=133)

    author = Entry(add_window, width=40, textvariable=author)
    author.place(x=200, y=163)

    isbn = Entry(add_window, width=40, textvariable=isbn)
    isbn.place(x=200, y=193)

    publisher = Entry(add_window, width=40, textvariable=publisher)
    publisher.place(x=200, y=223)

    edition = Entry(add_window, width=40, textvariable=edition)
    edition.place(x=200, y=253)

    language = Entry(add_window, width=40, textvariable=language)
    language.place(x=200, y=283)

    price = Entry(add_window, width=40, textvariable=price)
    price.place(x=200, y=313)

    source = Entry(add_window, width=40, textvariable=source)
    source.place(x=200, y=343)

    quantity = Entry(add_window, width=40, textvariable=quantity)
    quantity.place(x=200, y=373)

    # button login and clear

    btn_signup = Button(add_window, text=" + Add", font=('Bookman antiqua', 12, 'bold'), command=add_data, bg='#2176F2',
                        fg='white')
    btn_signup.place(x=200, y=413)
    add_window.bind('<Return>', lambda event: add_data())
    add_window.mainloop()


def delete_books():
    def delete_data():
        if isbn.get() == "":
            messagebox.showerror('Error', "Please Enter the ISBN", parent=delete_window)
        else:
            isbn_entered = isbn.get()
            isbn_db = availability_books(isbn_entered)
            if isbn_db is None:
                messagebox.showerror('Error', "No book with such ISBN in the Inventory.", parent=delete_window)
            else:
                database.child("Books").child(isbn.get()).remove()
                messagebox.showinfo('Success', "Book deleted Successfully", parent=delete_window)
                delete_window.destroy()

    delete_window = Tk()
    delete_window.title('Delete Book')
    delete_window.geometry('500x600')
    heading = Label(delete_window, text="Delete Book", font=('Times New Roman', 20, 'bold'))
    heading.place(x=80, y=60)

    # form data label
    isbn = Label(delete_window, text="Enter ISBN :", font='Verdana 10 bold')
    isbn.place(x=80, y=130)

    isbn = StringVar()

    isbn = Entry(delete_window, width=40, textvariable=isbn)
    isbn.place(x=200, y=133)

    btn_signup = Button(delete_window, text=" - Delete", font=('Bookman antiqua', 12, 'bold'), command=delete_data,
                        bg='#2176F2',
                        fg='white')
    btn_signup.place(x=200, y=213)
    delete_window.bind('<Return>', lambda event: delete_data())
    delete_window.mainloop()


def update_books():
    def update_data():
        if isbn.get() == "" or edition.get() == "" or quantity.get() == "":
            messagebox.showerror('Error', "Please fill all fields.", parent=update_window)
        else:
            isbn_entered = isbn.get()
            isbn_db = availability_books(isbn_entered)
            if isbn_db is None:
                messagebox.showerror('Error', "No book with such ISBN in the Inventory.", parent=update_window)
            else:
                database.child("Books").child(isbn_entered).update({
                    "Quantity": quantity.get(),
                    "Edition": edition.get()
                })
                messagebox.showinfo('Success', "Book updated Successfully", parent=update_window)
                update_window.destroy()

    update_window = Tk()
    update_window.title('Update Books')
    update_window.geometry('500x600')
    heading = Label(update_window, text="Update Book", font=('Times New Roman', 20, 'bold'))
    heading.place(x=80, y=60)
    comment = Label(update_window, text="Please Enter the updated values else enter older values", font='Verdana 10')
    comment.place(x=80, y=130)
    isbn = Label(update_window, text="ISBN :", font='Verdana 10 bold')
    isbn.place(x=80, y=160)
    quantity = Label(update_window, text="Quantity :", font='Verdana 10 bold')
    quantity.place(x=80, y=190)
    edition = Label(update_window, text="Edition :", font='Verdana 10 bold')
    edition.place(x=80, y=220)
    isbn = StringVar()
    quantity = StringVar()
    edition = StringVar()

    isbn = Entry(update_window, width=40, textvariable=isbn)
    isbn.place(x=200, y=163)
    quantity = Entry(update_window, width=40, textvariable=quantity)
    quantity.place(x=200, y=193)
    edition = Entry(update_window, width=40, textvariable=edition)
    edition.place(x=200, y=223)

    btn_signup = Button(update_window, text=" Update", font=('Bookman antiqua', 12, 'bold'), command=update_data,
                        bg='#2176F2',
                        fg='white')
    btn_signup.place(x=200, y=273)
    update_window.bind('<Return>', lambda event: update_data())
    update_window.mainloop()


def print_books():
    pdf = FPDF()
    dict_books = database.child("Books").get().val()
    for i in dict_books:
        pdf.add_page()
        for j in dict_books[i]:
            txt = j + "->" + dict_books[i][j]
            pdf.set_font("Arial", size=15)
            pdf.cell(200, 10, txt=txt, ln=1, align='L')

    pdf.output("Books.pdf")
    messagebox.showinfo('Success', "PDF Saved Successfully.")
