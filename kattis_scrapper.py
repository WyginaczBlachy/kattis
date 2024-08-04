import requests
from bs4 import BeautifulSoup

class PointScrapper:
    def getPoints(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        return str(soup.find('span', class_='difficulty_number').get_text())