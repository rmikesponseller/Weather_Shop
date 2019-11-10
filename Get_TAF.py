import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.aviationweather.gov/taf/data?ids=KSAT&format=raw&metars=on&layout=on')

soup = BeautifulSoup(r.text,'html.parser')

date_time_1 = soup.find_all('strong')
for entry in date_time_1:
	date_time = data_time_1.find('strong').text
	print(date_time)

TAF_1 = soup.find_all('code')
for entry in TAF_1:
	TAF = TAF_1.find('code').text
	print(TAF)


































