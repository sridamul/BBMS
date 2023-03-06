# e-book - search books, list of free e-books, list of all e-books
# orderbooks - check availability, prebook, returnbook, orderbook
# manage profile - change settings, pay due fees and manage the profiles
from tkinter import *
from tkinter import messagebox
from ebook import *
from fpdf import FPDF


def search_ebook():
    def search_results():
        if name.get() == "" or title.get() == "" or key_term == "":
            messagebox.showerror('Error', "All fields are mandatory.", parent=search_window)
        else:
            try:
                author = name.get()
                Title = title.get()
                keyword = key_term.get()
                ebooks = sends_result(keyword, author, Title)
                print(ebooks)
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial', size=32)
                pdf.cell(200, 10, txt="All suggested E-Books", ln=1, align='L')
                count = 1
                for i in ebooks['items']:
                    pdf.add_page()
                    pdf.set_font("Arial", size=15)
                    pdf.cell(200, 10, txt=f"Book Number: {count}", ln=1, align='L')
                    count = count + 1
                    for j in i['volumeInfo']:
                        try:
                            txt = j + "->" + i['volumeInfo'][j]
                        except:
                            break
                        pdf.set_font("Arial", size=15)
                        pdf.cell(200, 10, txt=txt, ln=1, align='L')

                pdf.output("E-Books.pdf")
                messagebox.showinfo('Success', "PDF saved successfully", parent=search_window)
                search_window.destroy()
            except:
                messagebox.showerror('Error', "Please try again.", parent=search_window)
                search_window.destroy()
    search_window = Tk()
    search_window.title('Search E-Books')
    search_window.geometry('500x600')
    heading = Label(search_window, text="Search E-Books", font=('Times New Roman', 20, 'bold'))
    heading.place(x=80, y=60)
    name = Label(search_window, text="Author :", font='Verdana 10 bold')
    name.place(x=80, y=160)
    key_term = Label(search_window, text="Key terms:", font='Verdana 10 bold')
    key_term.place(x=80, y=220)
    title = Label(search_window, text="Title :", font='Verdana 10 bold')
    title.place(x=80, y=190)

    name = StringVar(search_window, value='Stephen Hawking')
    # isbn = StringVar(search_window, value='9781409092360')
    title = StringVar(search_window, value='A Brief History of Time')
    key_term = StringVar(search_window, value='Black Holes')

    name = Entry(search_window, width=40, textvariable=name)
    name.place(x=200, y=163)
    # isbn = Entry(search_window, width=40, textvariable=isbn)
    # isbn.place(x=200, y=193)
    title = Entry(search_window, width=40, textvariable=title)
    title.place(x=200, y=193)
    key_term = Entry(search_window, width=40, textvariable=key_term)
    key_term.place(x=200, y=223)

    btn_signup = Button(search_window, text=" Search ", font=('Bookman antiqua', 12, 'bold'), command=search_results,
                        bg='#2176F2',
                        fg='white')
    btn_signup.place(x=200, y=293)
    search_window.bind('<Return>', lambda event: search_results())
    search_window.mainloop()


def free_ebook():
    def free_results():
        if name.get() == "" or key_term.get() == "":
            messagebox.showerror('Error', "All fields are Mandatory.", parent=free_window)
        else:
            try:
                author = name.get()
                keyword = key_term.get()
                free_ebooks = sends_free_result(keyword, author)
                print(free_ebooks)
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font('Arial', size=32)
                pdf.cell(200, 10, txt="Free E-Books", ln=1, align='L')
                count = 1
                for i in free_ebooks['items']:
                    pdf.add_page()
                    pdf.set_font("Arial", size=15)
                    pdf.cell(200, 10, txt=f"Book Number: {count}", ln=1, align='L')
                    count = count + 1
                    for j in i['volumeInfo']:
                        try:
                            txt = j + "->" + i['volumeInfo'][j]
                        except:
                            break
                        pdf.set_font("Arial", size=15)
                        pdf.cell(200, 10, txt=txt, ln=1, align='C')

                pdf.output("Free E-Books.pdf")
                messagebox.showinfo('Success', "PDF saved successfully", parent=free_window)
                free_window.destroy()
            except:
                messagebox.showerror('Error', "Please Try again later.", parent=free_window)
                free_window.destroy()

    free_window = Tk()
    free_window.title('Free E-Books')
    free_window.geometry('500x600')
    heading = Label(free_window, text="Free E-Books", font=('Times New Roman', 20, 'bold'))
    heading.place(x=80, y=60)
    name = Label(free_window, text="Author :", font='Verdana 10 bold')
    name.place(x=80, y=160)
    key_term = Label(free_window, text="Genre :", font='Verdana 10 bold')
    key_term.place(x=80, y=190)

    name = StringVar(free_window, value='Steve')
    key_term = StringVar(free_window, value='life')

    name = Entry(free_window, width=40, textvariable=name)
    name.place(x=200, y=163)
    key_term = Entry(free_window, width=40, textvariable=key_term)
    key_term.place(x=200, y=193)

    btn_signup = Button(free_window, text=" Search ", font=('Bookman antiqua', 12, 'bold'), command=free_results,
                        bg='#2176F2',
                        fg='white')
    btn_signup.place(x=200, y=293)
    free_window.bind('<Return>', lambda event: free_results())
    free_window.mainloop()

