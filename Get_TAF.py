import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.aviationweather.gov/taf/data?ids=KSAT&format=raw&metars=on&layout=on')

soup = BeautifulSoup(r.text,'html.parser')

date_time_1 = soup.find_all('strong')
date_time = soup.find('strong').text
print(date_time_1)

TAF_1 = soup.find_all('code')
TAF = soup.find('code').text
print(TAF_1)





















