import requests
from bs4 import BeautifulSoup
import win10toast
import time

URL = 'https://www.amazon.in/Canon-EOS-200D-II-Digital/dp/B07RJWB548/ref=lp_29783338031_1_1'

headers = {"User Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()

    price = soup.find(id="aria-hidden="true"").get_text()
    converted_price = float(price.split(",")[0])
    print(converted_price)

    if(converted_price > 700):
        send_alert()

    print(converted_price)
    print(title.strip())

def send_alert():
        toaster = win10toast.ToastNotifier().show_toast("Python", 'Cheaper', duration=5)

while True:
    check_price()
    time.sleep(5) #sleep 5 seconds before requesting the price again