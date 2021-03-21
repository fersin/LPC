import requests
from bs4 import BeautifulSoup

p = requests.get('https://spotifycharts.com/regional')
sup = BeautifulSoup(p.content, 'html.parser')
k= sup.find('td', class_='chart-table-track')
s=k.find('span') #artist
t=k.find('strong')
print("the top song of the day is ",t.text,s.text)
