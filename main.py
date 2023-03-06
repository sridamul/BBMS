from tkinter import *
from tkinter import ttk, messagebox
from quote_generator import quote_of_the_day
from db_read import read, availability, database, modify_return, check_book_availability, update_profile, check_due
from news import NewsFromBBC
from inventoryManagement import *
from userManagement import *
from userwindow import *

# create window object

app = Tk()

app.title('BBMS')
an = app.winfo_screenwidth()
al = app.winfo_screenheight()

tam = '%dx%d' % (an, al)


# app.geometry()
# create a frame for the left half of the window


def close():
    app.destroy()


# --------------------------------------------------------------------------------------------------------------------
def dashboard_admin():
    dash_admin = Tk()
    dash_admin.title('BBMS - Admin Login')
    dash_admin.geometry(tam)
    tab_control = ttk.Notebook(dash_admin)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab3 = ttk.Frame(tab_control)

    tab_control.add(tab1, text='Home Page')
    tab_control.add(tab2, text='Inventory Management')
    tab_control.add(tab3, text='User Management')
    tab_control.pack(expand=1, fill="both")
    # Home articles ----------------------------------------------------------------------------------
    txtarea = Text(tab1, font=("Times New Roman", 15, "bold"), bg='#f7f7f7', fg="black")
    # txtarea.grid(column=0, row=0, pady=30, padx=30)
    txtarea.place(x=10, y=10, width=an, height=al)
    txtarea.insert(END, f"\n Today's News Highlights\n\n\n")
    articles = NewsFromBBC()
    print(articles)
    if articles != 0:
        news_count = 0
        for i in articles:
            news_count = news_count + 1
            txtarea.insert(END, f"{news_count})")
            txtarea.insert(END, f"{i}\n\n\n")

    else:
        txtarea.insert(END, "Sorry no news available")
    # ttk.Label(tab1, text=articles).grid(column=0, row=0, padx=30, pady=30)
    # Book Management function ----------------------------------------------------------------------------------

    ttk.Label(tab2, text="Book Management System", font=('Times New Roman', 32, 'bold')).pack()
    add_button = Button(tab2, text='Add Book', font=('Bookman Old Style', 20), width=40, command=add_books)
    add_button.pack(pady=20)
    update_button = Button(tab2, text='Update Book', font=('Bookman Old Style', 20), width=40, command=update_books)
    update_button.pack(pady=20)
    delete_button = Button(tab2, text='Delete Book', font=('Bookman Old Style', 20), width=40, command=delete_books)
    delete_button.pack(pady=20)
    print_frame = Frame(tab2, width=an, height=200)
    print_frame.pack(side='bottom', expand=True)
    print_button = Button(print_frame, text='Book list PDF', font=('Bookman antiqua', 20), bg="#808080",
                          command=print_books)
    print_button.place(x=1300, y=50)
    # User management function --------------------------------------------------------------------------------------
    ttk.Label(tab3, text="User Management Section", font=('Times New Roman', 32, 'bold')).pack()

    registered_users = Button(tab3, text='Registered Users', font=('Bookman Old Style', 20), width=40,
                              command=registered_users_list)
    registered_users.pack(pady=20)
    add_borrower = Button(tab3, text='Add Borrower', font=('Bookman Old Style', 20), width=40, command=borrower)
    add_borrower.pack(pady=20)
    delete_borrower = Button(tab3, text='Return Book', font=('Bookman Old Style', 20), width=40, command=return_book)
    delete_borrower.pack(pady=20)
    borrower_pdf = Button(tab3, text='Borrower list', font=('Bookman Old Style', 20), width=40, command=pdf_borrower)
    borrower_pdf.pack(pady=20)
    returner_pdf = Button(tab3, text='Returner list', font=('Bookman Old Style', 20), width=40, command=pdf_returner)
    returner_pdf.pack(pady=20)
    send_notification = Button(tab3, text='Send Notification', font=('Bookman Old Style', 20), width=40,
                               command=sends_notification)
    send_notification.pack(pady=20)
    dash_admin.mainloop()
    dash_admin.mainloop()


# --------------------------------------------------------------------------------------------------------------------


def dashboard_user():
    dash_user = Tk()
    dash_user.title('BBMS - User Login')
    dash_user.geometry(tam)
    tab_control1 = ttk.Notebook(dash_user)
    tab1 = ttk.Frame(tab_control1)
    tab2 = ttk.Frame(tab_control1)
    tab3 = ttk.Frame(tab_control1)
    tab4 = ttk.Frame(tab_control1)

    tab_control1.add(tab1, text='Home Page')
    tab_control1.add(tab2, text='E-Books')
    tab_control1.add(tab3, text='Order Books')
    tab_control1.add(tab4, text='Manage Profile')
    tab_control1.pack(expand=1, fill="both")
    # ---------------------------------------------------------------------------------------------------------------
    # Home articles ----------------------------------------------------------------------------------
    txtarea = Text(tab1, font=("Times New Roman", 15, "bold"), bg='#f7f7f7', fg="black")
    # txtarea.grid(column=0, row=0, pady=30, padx=30)
    txtarea.place(x=10, y=10, width=an, height=al)
    txtarea.insert(END, f"\n Today's News Highlights\n\n\n")
    articles = NewsFromBBC()
    print(articles)
    if articles != 0:
        news_count = 0
        for i in articles:
            news_count = news_count + 1
            txtarea.insert(END, f"{news_count})")
            txtarea.insert(END, f"{i}\n\n\n")

    else:
        txtarea.insert(END, "Sorry no news available")
    # --------------------------------------------------------------------------------------------------------------
    # E- books
    ttk.Label(tab2, text="E-Books Section", font=('Times New Roman', 32, 'bold')).pack()
    ttk.Label(tab2, text="Available in Google Books", font=('Bookman Old Style', 14, 'italic')).pack()
    search_books = Button(tab2, text='All E books', font=('Bookman Old Style', 20), width=40, command=search_ebook)
    search_books.pack(pady=20)
    free_ebooks = Button(tab2, text='Free ebooks', font=('Bookman Old Style', 20), width=40, command=free_ebook)
    free_ebooks.pack(pady=20)

    # --------------------------------------------------------------------------------------------------------------
    # order books
    ttk.Label(tab3, text="Manage Books", font=('Times New Roman', 32, 'bold')).pack()
    check_availability = Button(tab3, text="Check Availability", font=('Bookman Old Style', 20), width=40,
                                command=check_book_availability)
    check_availability.pack(pady=20)
    modify_return_date = Button(tab3, text="Modify Return Date", font=('Bookman Old Style', 20), width=40,
                                command=modify_return)
    modify_return_date.pack(pady=20)

    ttk.Label(tab4, text="Profile Manager", font=('Times New Roman', 32, 'bold')).pack()
    manage_profile = Button(tab4, text="Change Password", font=('Bookman Old Style', 20), width=40, command=update_profile)
    manage_profile.pack(pady=20)
    check_due_amount = Button(tab4, text="Check Due Amount", font=('Bookman Old Style', 20), width=40, command=check_due)
    check_due_amount.pack(pady=20)

    dash_user.mainloop()


# --------------------------------------------------------------------------------------------------------------------


def login_page():
    close()

    def close_login_page():
        login_root.destroy()

    def login():
        if username.get() == "" or password.get() == "":
            messagebox.showerror("Error", "Please fill all the credentials", parent=login_root)
        else:
            username_value = username.get()
            password_value = password.get()
            if username_value == "Admin" and password_value == "Admin":
                messagebox.showinfo("Success", "Successfully Logged in", parent=login_root)
                close_login_page()
                dashboard_admin()
                exit()
            pwd = read(username_value)
            if pwd != "None":
                if password_value == pwd:
                    messagebox.showinfo("Success", "Successfully Logged in", parent=login_root)
                    close_login_page()
                    dashboard_user()
                    exit()
                else:
                    messagebox.showerror("Error", "Wrong Credentials", parent=login_root)

    login_root = Tk()
    login_root.title('Login Page')
    login_root.geometry('600x650')
    login_label = Label(login_root, text='Login', font=('Helvatica', 32, 'bold'))
    login_label.pack(pady=20)
    text_label = Label(login_root, text='Welcome back! Login with your credentials', font=('Book antiqua', 12),
                       fg='#AEAEAE')
    text_label.pack(pady=10)
    username_label = Label(login_root, text='Username', font=('Times New Roman', 18), fg='#525252')
    username_label.pack(pady=20)
    username = StringVar()
    user_entry = Entry(login_root, width=40, textvariable=username, font=('Times New Roman', 16))
    user_entry.focus()
    user_entry.pack()
    password_label = Label(login_root, text='Password', font=('Times New Roman', 18), fg='#525252')
    password_label.pack(pady=30)
    password = StringVar()
    password_entry = Entry(login_root, width=40, textvariable=password, font=('Times New Roman', 16), show="*")
    password_entry.pack()
    login_button = Button(login_root, width=17, text='Login', font=('Bookman Old Style', 24), bg='#2176F3', fg='white',
                          command=login)
    login_button.pack(pady=30)
    login_root.bind('<Return>', lambda event: login())
    login_root.mainloop()


# ---------------------------------------------------------------------------------------------------------------------


def sign_up_page():
    close()

    def close_signup_page():
        winsignup.destroy()

    def sign_up():
        if first_name.get() == "" or last_name.get() == "" or age.get() == "" or contact.get() == "" or year_of_study.get() == "" or department.get() == "" or add.get() == "" or user_name.get() == "" or password.get() == "" or very_pass.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=winsignup)
        elif password.get() != very_pass.get():
            messagebox.showerror("Error", "Password & Confirm Password Should Be Same", parent=winsignup)
        else:
            username_entered = user_name.get()
            username_db = availability(username_entered)
            if username_db is not None:
                messagebox.showerror("Error", "Username already taken", parent=winsignup)
            else:
                data = {
                    "FirstName": first_name.get(),
                    "LastName": last_name.get(),
                    "Age": age.get(),
                    "Address": add.get(),
                    "Department": department.get(),
                    "YearOfStudy": year_of_study.get(),
                    "PhoneNumber": contact.get(),
                    "Gender": var.get(),
                    "Username": user_name.get(),
                    "Password": password.get(),
                }
                database.child("Users").child(user_name.get()).set(data)
                messagebox.showinfo("Success", "Successfully registered.Please restart the application",
                                    parent=winsignup)
                data1 = {
                    "Due Amount": "0"
                }
                database.child("DueList").child(user_name.get()).set(data1)
                close_signup_page()

    winsignup = Tk()
    winsignup.title("SignUp Page")
    winsignup.maxsize(width=500, height=600)
    winsignup.minsize(width=500, height=600)

    # heading label
    heading = Label(winsignup, text="Signup", font='Verdana 20 bold')
    heading.place(x=80, y=60)

    # form data label
    first_name = Label(winsignup, text="First Name :", font='Verdana 10 bold')
    first_name.place(x=80, y=130)

    last_name = Label(winsignup, text="Last Name :", font='Verdana 10 bold')
    last_name.place(x=80, y=160)

    age = Label(winsignup, text="Age :", font='Verdana 10 bold')
    age.place(x=80, y=190)

    gender = Label(winsignup, text="Gender :", font='Verdana 10 bold')
    gender.place(x=80, y=220)

    department = Label(winsignup, text="Department:", font='Verdana 10 bold')
    department.place(x=80, y=260)

    year_of_study = Label(winsignup, text="Year :", font='Verdana 10 bold')
    year_of_study.place(x=80, y=290)

    add = Label(winsignup, text="Address :", font='Verdana 10 bold')
    add.place(x=80, y=320)

    contact = Label(winsignup, text="Contact :", font='Verdana 10 bold')
    contact.place(x=80, y=350)

    user_name = Label(winsignup, text="User Name :", font='Verdana 10 bold')
    user_name.place(x=80, y=380)

    password = Label(winsignup, text="Password :", font='Verdana 10 bold')
    password.place(x=80, y=410)

    very_pass = Label(winsignup, text="Re Password:", font='Verdana 10 bold')
    very_pass.place(x=80, y=440)

    # Entry Box ------------------------------------------------------------------

    first_name = StringVar()
    last_name = StringVar()
    age = IntVar(winsignup, value=0)
    var = StringVar()
    department = StringVar()
    add = StringVar()
    year_of_study = StringVar()
    contact = StringVar()
    user_name = StringVar()
    password = StringVar()
    very_pass = StringVar()

    first_name = Entry(winsignup, width=40, textvariable=first_name)
    first_name.place(x=200, y=133)

    last_name = Entry(winsignup, width=40, textvariable=last_name)
    last_name.place(x=200, y=163)

    age = Entry(winsignup, width=40, textvariable=age)
    age.place(x=200, y=193)

    radio_button_male = ttk.Radiobutton(winsignup, text='Male', value="Male", variable=var)
    radio_button_male.place(x=200, y=220)
    radio_button_female = ttk.Radiobutton(winsignup, text='Female', value="Female", variable=var)
    radio_button_female.place(x=200, y=238)

    department = Entry(winsignup, width=40, textvariable=department)
    department.place(x=200, y=263)

    year_of_study = Entry(winsignup, width=40, textvariable=year_of_study)
    year_of_study.place(x=200, y=293)

    add = Entry(winsignup, width=40, textvariable=add)
    add.place(x=200, y=323)

    contact = Entry(winsignup, width=40, textvariable=contact)
    contact.place(x=200, y=353)

    user_name = Entry(winsignup, width=40, textvariable=user_name)
    user_name.place(x=200, y=383)

    password = Entry(winsignup, width=40, textvariable=password)
    password.place(x=200, y=413)

    very_pass = Entry(winsignup, width=40, show="*", textvariable=very_pass)
    very_pass.place(x=200, y=443)

    # button login and clear

    btn_signup = Button(winsignup, text="Signup", font=('Bookman antiqua', 12, 'bold'), command=sign_up, bg='#2176F2',
                        fg='white')
    btn_signup.place(x=200, y=473)
    winsignup.bind('<Return>', lambda event: sign_up())
    winsignup.mainloop()


# ---------------------------------------------------------------------------------------------------------------------


left_frame = Frame(app, width=(an / 2), height=al)
left_frame.pack(side="left", fill="both", expand=True)

# create an image object
image = PhotoImage(file=r"E:\BBMS\photos\firstPage.png")

# create a label to display the image
image_label = ttk.Label(left_frame, image=image)
image_label.pack(padx=70, fill='both', expand=True)

# create a label for some text
# text_label = Label(left_frame, text="This is some text", font=("Arial", 12))
# text_label.pack(padx=10, pady=10)

# create a frame for the right half of the window
right_frame = Frame(app, width=(an / 2), height=al)
right_frame.pack(side='right', fill="both", expand=True)
right_top_frame = Frame(right_frame)
right_top_frame.pack(side='top', pady=100, fill='both', expand=True)
# Start Program
label1 = Label(right_top_frame, text="Hey There!", font=('Bookman Old Style', 36, 'bold'))
label1.pack(pady=20)
label2 = Label(right_top_frame, text="Quote of the Day", font=('Times New Roman', 18), cursor='pencil')
label2.pack(pady=20)
label3 = Label(right_top_frame, text=quote_of_the_day(), font=('Book Antique', 12, 'italic'), wraplength=600,
               justify="center", cursor='pencil', width=100)
label3.pack(pady=25)
button1 = Button(right_top_frame, text='Login', font=('Arial', 18), bg='#2196F3', cursor='hand2', width=30,
                 command=login_page)
button2 = Button(right_top_frame, text='Sign Up', font=('Arial', 18), bg='#2196F3', cursor='hand2', width=30,
                 command=sign_up_page)
button1.pack(side='top', padx=10, pady=20, anchor='center')
button2.pack(side='top', padx=10, pady=20, anchor='center')

app.mainloop()
