import urllib.request
from bs4 import *
import smtplib
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
msg=[]
link="http://www.bloomberg.com/quote/AAPL:US"
page = urllib.request.urlopen(link)
soup = BeautifulSoup(page,'html.parser')
title = soup.title.text
value = soup.find('span', {'class': 'priceText__1853e8a5'}).text

msg.append("The stock price of " + "AAPL" + '= ' + str(value) + '\n')

fromaddr = 'godofwar123bhanu@gmail.com'
toaddr = ['likebhanuprakash@gmail.com']
username ='godofwar123bhanu@gmail.com'
gmail_password ='bhanua153ds'
message = """From : War
To: likebhanuprakash@gmail.com
Subject : Daily stock digest
 """



for item in msg:
    msg1 = '\n'
    msg1 = msg1 + item
    message = message + msg1

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login(username,gmail_password)
server.sendmail(fromaddr,toaddr,message)
server.close()
print('email sent successfully')
