import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get(
#     "https://forecast.weather.gov/MapClick.php?lat=41.8843&lon=-87.6324#.XkqTMDIzbIU"
    "https://forecast.weather.gov/MapClick.php?lat=34.09979000000004&lon=-118.32721499999997#.XktzeDIzbIV"
    )
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id='seven-day-forecast-body')
# print(week.find_all('li'))
items = week.find_all(class_='tombstone-container')
# print (item)
# print (items[1].find(class_='period-name').get_text())
# print (items[1].find(class_='short-desc').get_text())
# print (items[1].find(class_='temp').get_text())

period_name = [item.find (class_='period-name').get_text() for item in items]
short_description = [item.find (class_='short-desc').get_text() for item in items]
temprature = [item.find (class_='temp').get_text() for item in items]
# 
# print(period_name)
# print(short_description)
# print(temprature)

weather_data= pd.DataFrame(
    {
        'period' : period_name,
        'drscription': short_description,
        'temp' : temprature,
    })

print(weather_data)
weather_data.to_csv('result.csv')
