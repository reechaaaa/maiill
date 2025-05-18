import smtplib
import os


def send_email():
    sender_email = input("Enter your email address: ")
    sender_password = input("Enter your email password (or App Password): ")
    recipient_email = input("Enter the recipient's email address: ")
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")


    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(sender_email, sender_password)

            

            msg = f'Subject: {subject}\n\n{body}'


            smtp.sendmail(sender_email, recipient_email, msg)
            print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Error: Could not authenticate. Please check your email and password (or App Password).")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    send_email()
