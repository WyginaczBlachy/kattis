import requests
from bs4 import BeautifulSoup

class PointScrapper:
    def getPoints(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')
        difficulty_number = soup.find('span', class_='difficulty_number').get_text()
        findall = soup.find_all('span', class_='text-lg font-bold text-blue-200')
        difficulty_level = findall[2].get_text()
        return f"{difficulty_number}" + f"({difficulty_level})"

