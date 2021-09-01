from PIL import Image,ImageDraw,ImageFont
import pandas as pd
import qrcode
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

path="./certificate.csv"
dataframe=pd.read_csv(path)
font_name=ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf',100,encoding="unic")
font_event=ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf',50,encoding="unic")

directory="./all_certificates"
email_sender = os.environ.get('MEDET_USER')
password = os.environ.get('MEDET_PASWORD')

for index,item in dataframe.iterrows():
    img=Image.open('cer.jpg')
    draw=ImageDraw.Draw(img)
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=2
    )
    qr.add_data(f"This Certificate is Presented to {item['name']} for participating in Tech Summit, Petrichor'22")
    qr.make()
    qr_img = qr.make_image(fill_color="black", back_color="white")
    draw.text(xy=(790,662),text=f"{item['name']}",fill=(255,255,255),font=font_name)
    draw.text(xy=(973,815),text=f"{item['event']}",fill=(255,255,255),font=font_event)
    offset=413,636
    img.paste(qr_img,offset)
    img.save('all_certificates/{}.jpg'.format(item['email']))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email_sender,password)


for filename in os.listdir(directory):
    for index,item in dataframe.iterrows():
        if f"{item['email']}.jpg"==filename:
            email=item['email']
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] =email
    msg['Subject'] = "Petrichor Certificate"

    body = "Hi this email is sent to test the code for automatically generating and sending petrichor certificates"

    msg.attach(MIMEText(body, 'plain'))
    file=f"{os.path.join(directory, filename)}"
    attachment = open(file, "rb")
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(p)
    

    text = msg.as_string()
    server.send_message(msg)
    

server.quit()