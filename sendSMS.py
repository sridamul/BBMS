# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from tkinter import messagebox

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "ACed4fd4cfe8ff5ff41c72977ac2366eb4"
auth_token = "a7dac4f9f6a0f0f74b2ed4f874d92cb8"
client = Client(account_sid, auth_token)


def sendSMS(msg, phone):
    message = client.messages.create(
        body=msg,
        from_="+15673131780",
        to="+91" + str(phone)
    )
    messagebox.showinfo('Success', "Message Sent Successfully")
