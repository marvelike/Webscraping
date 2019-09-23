"""
Scraping best Hotel deals in Lagos, Nigeria from AdvisorTrip and
saving the data in a .csv file
"""

import requests
from bs4 import BeautifulSoup
from time import sleep
url = 'https://www.tripadvisor.com/SmartDeals-g1231487-Lagos_State-Hotel-Deals.html'
request = requests.get(url)
sleep(2)


soup = BeautifulSoup(request.text, 'html.parser')
title = soup.find(class_='listing_title').get_text()
container = soup.find_all(class_='comblock no_cpu active hacComplete linkStrategyBlackPriceHover linkStrategyUnderlinePrices offsiteArrowPartner offsiteControlOrder')
price = container[0].find(class_='price autoResize').get_text()
vendor = container[0].find(class_='vendor').get_text()
Cancellation = container[0].find(class_='message').get_text()
print(price, title)
print(container)

