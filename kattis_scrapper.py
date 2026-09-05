import requests
from bs4 import BeautifulSoup


class PointScrapper:
    def getPoints(self, url):
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            r = requests.get(url, headers=headers, timeout=10)
            r.raise_for_status()

            soup = BeautifulSoup(r.content, 'html.parser')  # better than html5lib

            # Try the old way first
            difficulty_span = soup.find('span', class_='difficulty_number')
            if difficulty_span:
                difficulty_number = difficulty_span.get_text().strip()
                return difficulty_number

            # Alternative: look for common patterns
            # Kattis often shows difficulty like "1.5 Easy" or just a number
            difficulty_elements = soup.find_all(['span', 'div'], class_=lambda x: x and 'difficulty' in x.lower())

            for elem in difficulty_elements:
                text = elem.get_text().strip()
                if text and any(c.isdigit() for c in text):
                    return text

            # Last resort: search for text that looks like a difficulty score
            for span in soup.find_all('span'):
                text = span.get_text().strip()
                if text and text.replace('.', '', 1).isdigit() and 1.0 <= float(text) <= 10.0:
                    return text

            print(f"Could not find difficulty for: {url}")
            return "N/A"

        except Exception as e:
            print(f"Error scraping {url}: {e}")
            return "N/A"