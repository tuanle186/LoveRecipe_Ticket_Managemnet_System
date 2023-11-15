import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from modules import transaction


def send_email(email, name, phone, std, prm):      
    with open('C:/Programming/ticketingSystem/modules/email_template.html', 'r', encoding='utf-8') as file:
        html_str = file.read()

    html_str = html_str.replace('helvetica', 'sans serif')
    html_str = html_str.replace('guest_name', name)
    html_str = html_str.replace('guest_phone', phone)
    html_str = html_str.replace('guest_std', str(std))
    html_str = html_str.replace('guest_prm', str(prm))
    html_str = html_str.replace('guest_total', transaction.currency_format(str(std*130000 + prm*150000)))

    # sender = "lequoctuan.qt@email.com"
    sender = "thebigbasscrew24413@gmail.com"
    recipent = email

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "LOVE RECIPE - XÁC NHẬN ĐẶT VÉ THÀNH CÔNG"
    msg['From'] = sender
    msg['To'] = recipent

    msg.attach(MIMEText(html_str, 'html'))
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("thebigbasscrew24413@gmail.com", "veitpreedsssxuza")
    s.sendmail(sender, recipent, msg.as_string())
    s.quit()