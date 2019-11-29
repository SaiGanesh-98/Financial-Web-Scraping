import urllib.request
from bs4 import *
import smtplib
import csv
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
msg=[]

with open("C:/Users/bakkolla/Desktop/StockSymbols.csv") as csvfile:
    symbollist = csv.DictReader(csvfile)
    for row in symbollist:
        url = "http://www.bloomberg.com" + "/quote/" +row['SYMBOL'] +":US"
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page,'html.parser')
        value = soup.find('span', {'class': 'priceText__1853e8a5'}).text
        msg.append("The stock price of " + row['SYMBOL'] + '= ' +str(value) + '\n')

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
