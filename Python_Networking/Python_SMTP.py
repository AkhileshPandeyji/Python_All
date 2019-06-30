import smtplib
from email.mime.text import MIMEText

body = """How are you my Friends I Love You So much.
Can we meet tomorrow if you consider that i am your friend.
And always remember 'A Friend who helps Friend in need is a Friend indeed '
"""
from_addr = "pandeyakhilesh5372@gmail.com"
to_addr = "pandeyakhilesh7677@gmail.com"
subject = "Ek Shaam Dosto Ke Naam"

msg = MIMEText(body)
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject

server = smtplib.SMTP("smtp.gmail.com", 587)

try:
    server.starttls()
    passwd = str(input("Enter your Gmail password:"))
    server.login(from_addr, passwd)
    server.send_message(msg)

except smtplib.SMTPAuthenticationError as e:
    print(str(e))

server.quit()

