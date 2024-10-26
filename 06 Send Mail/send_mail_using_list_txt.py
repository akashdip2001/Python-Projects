# With ssh
import smtplib as s  # Import SMTP for sending email
import ssl  # For securing the connection

# SMTP server configuration
SMTP_SERVER = "smtp.gmail.com"
PORT = 587

# Sender credentials (remove password here for security)
sender_email = "mail.me.akashdip2001@gmail.com"
password = "passward"  # Replace with actual app password or use environment variable

# Email content
subject = "Sending email using Python"
body = "This is a test email sent using Python by Akashdip Mahapatra"
message = f"Subject: {subject}\n\n{body}"

# Load list of email addresses from file
with open(r"C:\Users\akash\Desktop\Py Projects\06 Send Mail\list.txt") as f:
    list_of_addresses = f.read().splitlines()  # Read each line as an email address

# Initialize and secure the connection
with s.SMTP(SMTP_SERVER, PORT) as ob:
    ob.ehlo()  # Identify client to server
    ob.starttls(context=ssl.create_default_context())  # Secure the connection
    ob.login(sender_email, password)  # Login to the email server

    # Send the email to each address in the list
    for recipient in list_of_addresses:
        ob.sendmail(sender_email, recipient, message)  # Send email
        print(f"Email has been sent to {recipient}")  # Confirmation message

# Close the connection automatically with the `with` block
print("All emails have been sent successfully!")  # Final confirmation message
