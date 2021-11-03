from bs4 import BeautifulSoup
import urllib.request as req
from time import time

start = time()
# HTML
url = "http://finance.naver.com/marketindex/"
res = req.urlopen(url)

# HTML analysis
soup = BeautifulSoup(res, "html.parser")

# get data
price = soup.select_one("div.head_info > span.value").string
# print("usd/krw = ",price)
print("time : ",time() - start)