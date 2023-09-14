from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


def scrape(url):
    service = webdriver.chrome.service.Service(
        executable_path='C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe')
    options = webdriver.ChromeOptions()

    # Включаем headless-режим с помощью add_argument
    options.add_argument('--headless')

    # Генерируем случайный User-Agent с помощью библиотеки fake-useragent
    user_agent = UserAgent().random
    options.add_argument(f"user-agent={user_agent}")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    # Подождем немного, чтобы страница успела загрузиться
    time.sleep(3)

    # Получаем содержимое страницы с помощью BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Завершаем работу браузера
    driver.quit()

    return soup


def find_publication_count(soup):
    publications_element = soup.find('td', class_='midtext', string='Число публикаций в РИНЦ')

    if publications_element:
        publication_count = publications_element.find_next('a').text
        return publication_count
    else:
        return None

def find_Hirsh(soup):
    publications_element = soup.find('td', class_='midtext', string='Индекс Хирша по всем публикациям на elibrary.ru')

    if publications_element:
        publication_hirsh = publications_element.find_next('a').text
        return publication_hirsh
    else:
        return None

def find_author_name(soup):
    items = soup.find_all('div')
    div_num = 0
    for n, i in enumerate(items, start=0):
        tags = i.find_all('span', class_='aster')
        for j in tags:
            if j.text == '*':
                div_num = n
    return items[div_num].find('b').text


def main():
    url = 'https://elibrary.ru/author_profile.asp?authorid=1092485'  # Замените на URL, который вы хотите парсить
    soup = scrape(url)
    print('Автор: ' + find_author_name(soup))
    print('Число публикаций в РИНЦ:'+ find_publication_count(soup))
    print('Индекс Хирша по всем публикациям на elibrary.ru:' +find_Hirsh(soup))


if __name__ == '__main__':
    main()


