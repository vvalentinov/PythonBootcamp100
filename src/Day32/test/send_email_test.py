import smtplib

my_email = "test@gmail.com"
app_password = "app_pass_here"

# Create a connection to the SMTP Server
connection = smtplib.SMTP("smtp.gmail.com")

# Make the connection secure and encrypt the email
connection.starttls()

connection.login(user=my_email, password=app_password)

connection.sendmail(
    from_addr=my_email,
    to_addrs="to_address_here",
    msg="Subject:Learning Sending Emails With Python\n\nThis is the body of the email!")

connection.close()
