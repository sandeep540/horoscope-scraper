# Import libraries
import requests
from bs4 import BeautifulSoup


# Set the URL you want to webscrape from
url = 'https://www.eastrolog.com/daily-horoscope/aries.php'

# Connect to the URL
response = requests.get(url)

print(response.status_code)

# Parsing the HTML
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.title)
s = soup.find('div', class_='contentLining')
# 
if(s):
    print("Found")
    content = s.find_all('p')
    print(content.text)
