import time
import requests
from bs4 import BeautifulSoup
import smtplib

myurl = 'https://www.amazon.in/Fossil-Analog-Off-White-Dial-Watch-FS5380/dp/B074ZHN54C/ref=sr_1_10?crid=O0U0PG8Z136K&keywords=watches+for+men&qid=1661357907&refinements=p_89%3AFossil&rnid=3837712031&s=watches&sprefix=watch%2Caps%2C256&sr=1-10'

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}

page = requests.get(myurl, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

def check_price():
    title = soup.find('span',{'id': 'productTitle'})
    print(title.text.strip())
    price = soup.find('span',{'class': 'a-price-whole'})
    print(price.get_text())
    converted_price = float(price.text.strip().replace(',',''))

    if converted_price < 8000:
        send_mail()
    else:
        print("Let's keep on Checking!")

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # Enter your Email and Password
    server.login('<xxxx@gmail.com>', '<password>')

    subject = 'Price fell down: Fossil Watch'
    body = 'Check the amazon link https://www.amazon.in/Fossil-Analog-Off-White-Dial-Watch-FS5380/dp/B074ZHN54C/ref=sr_1_10?crid=O0U0PG8Z136K&keywords=watches+for+men&qid=1661357907&refinements=p_89%3AFossil&rnid=3837712031&s=watches&sprefix=watch%2Caps%2C256&sr=1-10'

    msg = f"Subject: {subject}\n\n{body}"

    # Enter From and To Address
    server.sendmail('<xxx@gmail.com>','xxx@gmail.com', msg)
    print("Email sent")

    server.quit()

while (True):
    check_price()
    time.sleep(60*60*12)

