import requests
from bs4 import BeautifulSoup

urls = ['https://www.cbn.gov.ng/rates/ExchRateByCurrency.asp']
lists = ['td']
file = 'exchange'

with open(str(file)+'.txt', 'w', encoding='utf-8') as exchange:
    for url in urls:
        website = requests.get(url)
        soup = BeautifulSoup(website.content, 'lxml')
        tags = soup.find_all(lists)
        text = [''.join(s.find_all(text=True)) for s in tags]

        for item in text:
            print(item, file=exchange)

