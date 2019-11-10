import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.aviationweather.gov/taf/data?ids=KSAT&format=raw&metars=on&layout=on')

soup = BeautifulSoup(r.text,'html.parser')

date_results = soup.find_all('strong')
date_time_records = []

for result in date_results:
	print(result)
	date_time = result.find('strong').text
	data_time_records.append(date_time)

TAF_results = soup.find_all('code')
TAF_records = []

for result in TAF_results:
	print(result)
	TAF = result.find('code').text
	TAF_records.append(TAF)

print(data_time_records)
print(TAF_records)


































