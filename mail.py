import smtplib

myConnection = smtplib.SMTP("smtp.gmail.com",'587')
myConnection.starttls()

myConnection.login("ravismu59@gmail.com","9934746915")
message = "hello ravi"

myConnection.sendmail("ravismu59@gmail.com","rjha4743@gmail.com",message)
print("sent mail sucessfully")
myConnection.close()
