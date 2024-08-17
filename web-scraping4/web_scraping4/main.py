import requests
from bs4 import BeautifulSoup

headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36" }

Url= "https://www.vatanbilgisayar.com/"
sayfa=requests.get(Url,headers=headers)
icerik=BeautifulSoup(sayfa.content,"html.parser")

urunAdi=icerik.find_all("div",{"class":"product-list__product-name"})


for i in urunAdi:
   i=i.text
   print(i)