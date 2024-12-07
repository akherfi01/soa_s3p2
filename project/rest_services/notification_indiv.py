import smtplib

# # email = input("SENDER EMAIL:")
# email_ = "clinique.ask@gmail.com"
# receiver_email = input ("L'email du patient:")

# subject = input("sujet: ")
# message = input("message: ")

# text = f"Subject: {subject}\n\n{message}"

# server = smtplib.SMTP("smtp.gmail.com", 587)
# server.starttls()
# server.login(email_, "cxvg qnvz zwgq aydc")

# server.sendmail(email_, receiver_email, text)
# print("Email has been sent to " + receiver_email)


def send_email_to_patient():
    # email = input("SENDER EMAIL:")
    email_ = "clinique.ask@gmail.com"
    receiver_email = input("L'email du patient: ")

    subject = input("Sujet: ")
    message = input("Message: ")

    text = f"Subject: {subject}\n\n{message}"

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_, "cxvg qnvz zwgq aydc")  
        server.sendmail(email_, receiver_email, text)
        print(f"Email has been sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()
        input("\nPress Enter to return to the main menu...")

