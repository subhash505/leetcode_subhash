import requests
from bs4 import BeautifulSoup



URL="https://www.amazon.in/Nikon-20-9MP-Camera-18-140mm-3-5-5-6G/dp/B06Y5RTN1T/ref=lp_29783338031_1_2?smid=A14CZOWI0VEHLG&th=1"

header={"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'}


page=requests.get(URL,headers=header)

soup= BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price[0:5])
print(converted_price)
#print(title.strip())
#print()