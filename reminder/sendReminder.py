import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(email):      
    with open('C:/Programming/reminder/email_template.html', 'r', encoding='utf-8') as file:
        html_str = file.read()

    html_str = html_str.replace('helvetica', 'sans serif')

    sender = "thebigbasscrew24413@gmail.com"
    recipent = email

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "LOVE RECIPE - XIN CHÂN THÀNH CẢM ƠN"
    msg['From'] = sender
    msg['To'] = recipent

    msg.attach(MIMEText(html_str, 'html'))
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("thebigbasscrew24413@gmail.com", "veitpreedsssxuza")
    s.sendmail(sender, recipent, msg.as_string())
    s.quit()

email_arr = []
for i in range(0, 91):
    email_arr.append(input("Email: "))


for email in email_arr:
    send_email(email)
    