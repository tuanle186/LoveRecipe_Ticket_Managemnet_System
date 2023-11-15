import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def currency_format(input_money):
    input_money = str(input_money)
    reversed_money = input_money[::-1]
    output_money = ''
    for i in range(0, len(input_money)):
        if i % 3 == 0 and i != 0:
            output_money = output_money + ',' + reversed_money[i]
        else:
            output_money = output_money + reversed_money[i]
    return output_money[::-1] + ' VND'


def send_email(email, name, phone, pin, lanyard, tote, combo):      
    with open('C:/Programming/merchSystem/email_template.html', 'r', encoding='utf-8') as file:
        html_str = file.read()

    html_str = html_str.replace('helvetica', 'sans serif')
    html_str = html_str.replace('guest_name', name)
    html_str = html_str.replace('guest_phone', phone)
    html_str = html_str.replace('guest_pin', str(pin))
    html_str = html_str.replace('guest_lanyard', str(lanyard))
    html_str = html_str.replace('guest_tote', str(tote))
    html_str = html_str.replace('guest_combo', str(combo))
    html_str = html_str.replace('guest_total', currency_format(str(pin*15000 + lanyard*45000 + tote*60000 + combo*110000)))

    # sender = "lequoctuan.qt@email.com"
    sender = "thebigbasscrew24413@gmail.com"
    recipent = email

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "LOVE RECIPE - XÁC NHẬN ĐẶT MERCHANDISE THÀNH CÔNG"
    msg['From'] = sender
    msg['To'] = recipent

    msg.attach(MIMEText(html_str, 'html'))
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("thebigbasscrew24413@gmail.com", "veitpreedsssxuza")
    s.sendmail(sender, recipent, msg.as_string())
    s.quit()


email = input("\nEmail: ")
name = input("\nHọ và tên: ")
phone = input("\nSố điện thoại: ")
pin = int(input("\nSố lượng Pin: "))
lanyard = int(input("\nSố lượng Lanyard: "))
tote = int(input("\nSố lượng Túi Tote: "))
combo = int(input("\nSố lượng Combo: "))
print("\nXác nhận thông tin và tiến hành gửi email?")
op = input("Lựa chọn (y/n): ")
if op.capitalize() == 'Y':
    send_email(email, name, phone, pin, lanyard, tote, combo)
    print("\nĐã gửi email xác nhận thanh toán thành công! ✅")