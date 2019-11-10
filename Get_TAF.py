import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.aviationweather.gov/taf/data?ids=KDLF&format=raw&metars=on&date=&submit=Get+TAF+data')

soup = BeautifulSoup(r.text,'html.parser')

date_time = soup.find('strong').text
print(date_time)

TAF = soup.find('code').text
print(TAF)












