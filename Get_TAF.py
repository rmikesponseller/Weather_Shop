import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.aviationweather.gov/taf/data?ids=KDLF&format=raw&metars=on&date=&submit=Get+TAF+data')

print(r.text[0:500])
soup = BeautifulSoup(r.text,'html.parser')

results = soup.find_all('span', attrs={'class':'short-desc'})
len(results)
print(results[0:3])

