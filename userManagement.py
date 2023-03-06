# list of registered users - pdf - full format
# list of users who availed book - name, ISBN, borrowDate and returnDate
# list of users with fine amount - name and fee pending
# send notification about the due submit and late fee - sends notification
from db_read import database
from fpdf import FPDF
from tkinter import *
from tkinter import messagebox
from twilio.rest import Client


def registered_users_list():
    try:
        user = database.child("Users").get().val()
        pdf = FPDF()
        for i in user:
            pdf.add_page()
            for j in user[i]:
                txt = j + "->" + user[i][j]
                pdf.set_font("Arial", size=15)
                pdf.cell(200, 10, txt=txt, ln=1, align='L')
        pdf.output("Users.pdf")
        messagebox.showinfo('Success', "PDF saved Successfully")
    except:
        messagebox.showerror('Error', "No Users.")


def borrower():
    def borrower_add():
        if name.get() == "" or isbn.get() == "" or title.get() == "" or date.get() == "" or due_date.get() == "":
            messagebox.showerror('Error', "All fields are required", parent=borrower_window)
        else:
            if (database.child("Users").child(name.get()).get().val() and database.child("Books").child(isbn.get()).get().val()) is not None:
                try:
                    quantity = int(database.child("Books").child(isbn.get()).child("Quantity").get().val())
                    if quantity > 0:
                        database.child("Books").child(isbn.get()).update({
                            "Quantity": str(quantity - 1)
                        })
                        data = {
                            "Username": name.get(),
                            "ISBN": isbn.get(),
                            "Title": title.get(),
                            "Date": date.get(),
                            "Due Date": due_date.get()
                        }
                        database.child("BorrowerList").child(name.get()).child(isbn.get()).set(data)
                        messagebox.showinfo('Success', "Data Updated Successfully", parent=borrower_window)
                        borrower_window.destroy()
                    else:
                        messagebox.showerror('Error', "Book currently unavailable.", parent=borrower_window)
                except:
                    messagebox.showerror('Error', "Try again later", parent=borrower_window)
                    borrower_window.destroy()
            else:
                messagebox.showerror('Error', "Invalid ISBN or User.", parent=borrower_window)
                borrower_window.destroy()

    borrower_window = Tk()
    borrower_window.title('Add Borrower')
    borrower_window.geometry('500x600')
    heading = Label(borrower_window, text="Add Borrower", font=('Times New Roman', 20, 'bold'))
    heading.place(x=80, y=60)
    name = Label(borrower_window, text="Username :", font='Verdana 10 bold')
    name.place(x=80, y=160)
    isbn = Label(borrower_window, text="ISBN :", font='Verdana 10 bold')
    isbn.place(x=80, y=190)
    title = Label(borrower_window, text="Title :", font='Verdana 10 bold')
    title.place(x=80, y=220)
    date = Label(borrower_window, text="Date Borrowed:", font='Verdana 10 bold')
    date.place(x=80, y=250)
    due_date = Label(borrower_window, text="Due Date :", font='Verdana 10 bold')
    due_date.place(x=80, y=280)

    name = StringVar()
    isbn = StringVar()
    title = StringVar()
    date = StringVar()
    due_date = StringVar()

    name = Entry(borrower_window, width=40, textvariable=name)
    name.place(x=200, y=163)
    isbn = Entry(borrower_window, width=40, textvariable=isbn)
    isbn.place(x=200, y=193)
    title = Entry(borrower_window, width=40, textvariable=title)
    title.place(x=200, y=223)
    date = Entry(borrower_window, width=40, textvariable=date)
    date.place(x=200, y=253)
    due_date = Entry(borrower_window, width=40, textvariable=due_date)
    due_date.place(x=200, y=283)

    btn_signup = Button(borrower_window, text=" Update", font=('Bookman antiqua', 12, 'bold'), command=borrower_add,
                        bg='#2176F2',
                        fg='white')
    btn_signup.place(x=200, y=313)
    borrower_window.bind('<Return>', lambda event: borrower_add())
    borrower_window.mainloop()


def return_book():
    def return_add():
        if name.get() == "" or isbn.get() == "" or title.get() == "" or date.get() == "":
            messagebox.showerror('Error', "All fields are required", parent=return_window)
        else:
            if (database.child("BorrowerList").child(name.get()).child(isbn.get()).get().val()) is not None:
                try:
                    quantity = int(database.child("Books").child(isbn.get()).child("Quantity").get().val())
                    database.child("Books").child(isbn.get()).update({
                        "Quantity": str(quantity + 1)
                    })
                    due_amount = (database.child("DueList").child(name.get()).get().val())
                    amount = int(due_amount['Due Amount'])
                    database.child("DueList").child(name.get()).update({
                        "Due Amount": str(amount + int(late_fees.get()))
                    })
                    data = {
                        "Username": name.get(),
                        "ISBN": isbn.get(),
                        "Title": title.get(),
                        "Date": date.get(),
                        "Due amount": late_fees.get()
                    }
                    database.child("BorrowerList").child(name.get()).child(isbn.get()).remove()
                    database.child("ReturnerList").child(name.get()).child(isbn.get()).set(data)
                    messagebox.showinfo('Success', "Data Updated Successfully", parent=return_window)
                    return_window.destroy()
                except:
                    messagebox.showerror('Error', "Try again later", parent=return_window)
                    return_window.destroy()
            else:
                messagebox.showerror('Error', "User haven't borrowed yet.", parent=return_window)
                return_window.destroy()

    return_window = Tk()
    return_window.title('Return Window')
    return_window.geometry('500x600')
    heading = Label(return_window, text="Add Returner", font=('Times New Roman', 20, 'bold'))
    heading.place(x=80, y=60)
    name = Label(return_window, text="Username :", font='Verdana 10 bold')
    name.place(x=80, y=160)
    isbn = Label(return_window, text="ISBN :", font='Verdana 10 bold')
    isbn.place(x=80, y=190)
    title = Label(return_window, text="Title :", font='Verdana 10 bold')
    title.place(x=80, y=220)
    date = Label(return_window, text="Return Date:", font='Verdana 10 bold')
    date.place(x=80, y=250)
    late_fees = Label(return_window, text="Due amount :", font='Verdana 10 bold')
    late_fees.place(x=80, y=280)

    name = StringVar()
    isbn = StringVar()
    title = StringVar()
    date = StringVar()
    late_fees = IntVar(return_window, value=0)

    name = Entry(return_window, width=40, textvariable=name)
    name.place(x=200, y=163)
    isbn = Entry(return_window, width=40, textvariable=isbn)
    isbn.place(x=200, y=193)
    title = Entry(return_window, width=40, textvariable=title)
    title.place(x=200, y=223)
    date = Entry(return_window, width=40, textvariable=date)
    date.place(x=200, y=253)
    late_fees = Entry(return_window, width=40, textvariable=late_fees)
    late_fees.place(x=200, y=283)

    btn_signup = Button(return_window, text=" Update", font=('Bookman antiqua', 12, 'bold'), command=return_add,
                        bg='#2176F2',
                        fg='white')
    btn_signup.place(x=200, y=313)
    return_window.bind('<Return>', lambda event: return_add())
    return_window.mainloop()


def pdf_borrower():
    try:
        user = database.child("BorrowerList").get().val()
        print(user)
        pdf = FPDF()
        for i in user:
            contact = database.child("Users").child(i).child("PhoneNumber").get().val()
            isbn = database.child("BorrowerList").child(i).get().val()
            pdf.add_page()
            pdf.set_font("Arial", size=15)
            pdf.cell(200, 10, txt=f"Phone Number -> {contact}", ln=1, align='L')
            for j in isbn:
                for k in isbn[j]:
                    pdf.set_font("Arial", size=15)
                    pdf.cell(200, 10, txt=f"{k} -> {isbn[j][k]}", ln=1, align='L')
        pdf.output("BorrowedUsers.pdf")
        messagebox.showinfo('Success', "PDF saved Successfully")
    except:
        messagebox.showerror('Error', "No Borrowers.")


def pdf_returner():
    try:
        user = database.child("ReturnerList").get().val()
        print(user)
        pdf = FPDF()
        for i in user:
            contact = database.child("Users").child(i).child("PhoneNumber").get().val()
            isbn = database.child("ReturnerList").child(i).get().val()
            pdf.add_page()
            pdf.set_font("Arial", size=15)
            pdf.cell(200, 10, txt=f"Phone Number -> {contact}", ln=1, align='L')
            for j in isbn:
                for k in isbn[j]:
                    pdf.set_font("Arial", size=15)
                    pdf.cell(200, 10, txt=f"{k} -> {isbn[j][k]}", ln=1, align='L')

        pdf.output("ReturnedUsers.pdf")
        messagebox.showinfo('Success', "PDF saved Successfully")
    except:
        messagebox.showerror('Error', "No Returners.")


def sends_notification():
    account_sid = "ACed4fd4cfe8ff5ff41c72977ac2366eb4"
    auth_token = "a7dac4f9f6a0f0f74b2ed4f874d92cb8"
    client = Client(account_sid, auth_token)

    def sendSMS(msg, phone):
        message = client.messages.create(
            body=msg,
            from_="+15673131780",
            to="+91" + str(phone)
        )
        print(message.sid)
        messagebox.showinfo('Success', "Message Sent Successfully")

    def send_data():
        if name.get() == "" or message.get() == "":
            messagebox.showerror('Error', "All fields are required")
        else:
            try:
                contact = database.child("Users").child(name.get()).child("PhoneNumber").get().val()
                if contact is not None:
                    msg = message.get()
                    sendSMS(msg, contact)
                else:
                    messagebox.showerror('Error', "No username matches the Database.", parent=send_window)
            except:
                messagebox.showerror('Error', "Cannot send the message right now.", parent=send_window)
            finally:
                send_window.destroy()
    send_window = Tk()
    send_window.title('Send Notifications')
    send_window.geometry('500x600')
    heading = Label(send_window, text="Notification Center", font=('Times New Roman', 20, 'bold'))
    heading.place(x=80, y=60)
    name = Label(send_window, text="Username :", font='Verdana 10 bold')
    name.place(x=80, y=160)
    message = Label(send_window, text="message :", font='Verdana 10 bold')
    message.place(x=80, y=190)

    name = StringVar()
    message = StringVar()
    name = Entry(send_window, width=40, textvariable=name)
    name.place(x=200, y=163)
    message = Entry(send_window, width=40, textvariable=message)
    message.place(x=200, y=193)

    btn_signup = Button(send_window, text=" Send", font=('Bookman antiqua', 12, 'bold'), command=send_data,
                        bg='#2176F2',
                        fg='white')
    btn_signup.place(x=200, y=313)
    send_window.bind('<Return>', lambda event: send_data())
    send_window.mainloop()
