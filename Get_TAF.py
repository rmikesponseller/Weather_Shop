import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.aviationweather.gov/taf/data?ids=KSAT&format=raw&metars=on&layout=on')

soup = BeautifulSoup(r.text,'html.parser')

date_results = soup.find_all('strong')
date_time_records = []

for result in date_results:
	date_time = result.find('strong').text
	print(date_time)
	date_time_records.append(date_time)

TAF_results = soup.find_all('code')
TAF_records = []

for result in TAF_results:
	TAF = result.find('code').text
	TAF_records.append(TAF)

print(date_time_records)
print(TAF_records)

































