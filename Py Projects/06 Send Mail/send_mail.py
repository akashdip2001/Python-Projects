## Without ssh
import smtplib as s # pip install secure-smtplib

ob =s.SMTP("smtp.gmail.com",587) # ob is the object of SMTP class for
ob.ehlo() # Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email.
ob.starttls() # It is used to secure the connection between the client and the server using SSL/TLS.
##ob.login("sender_email","password") # If you have 2FA enabled, you need to generate an app password and use that as the password here.
ob.login("mail.me.akashdip2001@gmail.com","passward") # login to the email server
subject = "Sending email using Python"
body = "This is a test email sent using Python"
message = "Subject:{}\n\n{}".format(subject,body) # use subject directly like message = f"Subject: {subject}\n\n{body}", f-string use for formatting.
##but here we use dit format method. so that also user can add their own subject using input function.
listofaddress = ["receiver_email@gmail.com","akashdipmahapatra2001@gmail.com"] # list of email address to send the email.

ob.sendmail("sender_email",listofaddress,message) # sendmail(sender_email,receiver_email,message)
print("Email has been sent to",listofaddress)
ob.quit() # quit the connection.