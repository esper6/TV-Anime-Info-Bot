import smtplib
from email.message import EmailMessage

def send_email(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "rollins49@gmail.com"
    msg['from'] = "TV Anime Bot <rollins49@gmail.com>"
    password = "qhfl ffcx ptty blaa"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()