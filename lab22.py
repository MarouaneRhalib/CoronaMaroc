# Web Scraping: Extracting Date from the Web
import requests
from bs4 import BeautifulSoup
import pandas as pd
url='https://covid.hespress.com'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
region = soup.find('div', attrs={'id':'region_ma06'})
items = region.findAll('tr')
CITY =[item.find('th').get_text() for item in items]
Number =[item.find('td').get_text() for item in items]
LAT = [33.5724108, 33.2603204, 33.3561752, 33.6874463, 33.4698209, 33.2335191, 32.9929001,32.6492964 , 33.6137952 ]
LNG = [-7.6570329, -7.6159936, -7.6473719, -7.4239143, -7.5947135,-8.5386841 , -7.6371687,-8.4471453 , -7.1463109]
print(CITY)
print(Number)
stat = {
    'CITY':CITY,
    'LAT':LAT,
    'LNG': LNG,
    'Number': Number
}
df = pd.DataFrame(stat)
df.to_json('corona.json')
df.to_csv('corona.csv')
print(df)