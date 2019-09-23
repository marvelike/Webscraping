"""
Scraping python events from https://www.python.org/events/python-events/
"""

# import libraries.
import requests
from bs4 import BeautifulSoup


def python_events(url):
    filename = 'Python_events.csv'
    f = open(filename, 'w', encoding='utf-8')
    headers = 'Name, Date, Location \n'  # creating the csv file headers
    f.write(headers)
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'lxml')
    events = soup.find('ul', {'class': 'list-recent-events menu'}).findAll('li')
    for event in events:  # looping through all the events present
        event_name = event.find('h3', {'class': 'event-title'}).find('a').text
        event_date = event.find('time').text
        event_location = event.find('span', {'class', 'event-location'}).text
        f.write(event_name + "," + event_date + "," + event_location.replace(",","|") + "\n")
    print('Done writing to CSV file')
    f.close()  # closing the file.


python_events('https://www.python.org/events/python-events/')
