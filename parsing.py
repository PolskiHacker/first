import time
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service('C:/Program Files/chrome_driver/chromedriver-win64/chromedriver.exe')
browser = webdriver.Chrome(service=s)
# browser.get("https://www.kinopoisk.ru/lists/movies/top250/?utm_referrer=www.kinopoisk.ru")
# time.sleep(5)
# html_text = browser.page_source
# soup = BeautifulSoup(html_text, 'lxml')
# div = soup.find('div', class_= 'base-movie-main-info_mainInfo__ZL_u3').find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
# span = soup.find('a', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').get('hfa')
# span_2=soup.find('span', class_='desktop-list-main-info_secondaryText__M_aus').text
# finding = soup.find_all('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj')
# print(span)
# print(span_2),lp,
# print(finding[0].text)
a = "https://www.kinopoisk.ru/lists/movies/top250/?utm_referrer=www.kinopoisk.ru&page="
data = []
browser.get(a + '1')
time.sleep(4)
htext = browser.page_source
soup = BeautifulSoup(htext, 'lxml')
data.append(soup.find_all('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj'))
for i in range(2, 6):
    browser.get(a + str(i))
    htext = browser.page_source
    soup = BeautifulSoup(htext, 'lxml')
    data.append(soup.find_all('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj'))
print(data[0][1].text)


