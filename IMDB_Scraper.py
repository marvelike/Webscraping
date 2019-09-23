"""scraping the best 100 movies of all time and saving the result in a text file"""

import requests
from bs4 import BeautifulSoup


with open('imdb.txt', 'w', encoding='utf-8') as outfile:

    website = requests.get('https://www.imdb.com/list/ls041322734/')  # download the web content
    soup = BeautifulSoup(website.content, 'lxml')
    movies = soup.select('.lister-item-header a')  # using the select method to chose the content to be displayed
    text = [''.join(s.find_all(text=True)) for s in movies]

    for item in text:
        print(item, file=outfile)  # print  in the imdb.txt file
