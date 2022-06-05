import smtplib

import requests
from bs4 import BeautifulSoup

BUY_PRICE = 8
YOUR_EMAIL = "uppratagarhi@gmail.com"
YOUR_PASS = "Imlooser12@"

PRODUCT_URL = "https://www.amazon.com/MGQILING-Compatible-Electroplated-Shockproof-Protective/dp/B09XMFRZ2T/ref" \
              "=sr_1_3?crid=RRYVFKSLPMBR&keywords=iphone+13+pro+max&qid=1654400812&sprefix=%2Caps%2C251&sr=8-3"

header = {
    "Accept-Language": "en-US,en;q=0.9,hi-IN;q=0.8,hi;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 "
                  "Safari/537.36 ",
}

response = requests.get(url=f"{PRODUCT_URL}", headers=header)
data = response.text

soup = BeautifulSoup(data, "lxml")
# print(soup.prettify())

price = soup.find(name="span", class_="a-offscreen")
price_currency = price.text.replace("$", "")
price_float = float(price_currency)
print(price_float)

if BUY_PRICE <= price_float:
    message = f"Now {price_float} is th price"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASS)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs="vs92717@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{PRODUCT_URL}"
        )





