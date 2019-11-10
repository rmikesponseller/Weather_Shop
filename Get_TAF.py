import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.aviationweather.gov/taf/data?ids=KDLF&format=raw&metars=on&date=&submit=Get+TAF+data')

soup = BeautifulSoup(r.text,'html.parser')

results = soup.find_all('strong')
len(results)






