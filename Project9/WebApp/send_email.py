email.mime.text import MIMEText
import smtplib

def send_email(email, height, avg_h):
    from_email = 'testudemystudent@gmail.com'
    from_password = 'password'
    to_email = email
    subject = 'Height Data'

    message = "%s %s" % (height, avg_h)

    msg = MIMEtext(message, 'html')

    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
