from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time

def get_source_html(driver, url=None):
    try:
        driver.get(url=url)
        # Добавьте задержку, если это необходимо
        time.sleep(3)
        with open("source-page.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)

def main():
    service = Service(executable_path='C:/Users/user/Downloads/chromedriver_win32/chromedriver.exe')
    options = Options()

    # Включаем headless-режим с использованием add_argument
    options.add_argument('--headless')

    # Используем библиотеку fake-useragent для получения случайного User-Agent
    user_agent = UserAgent().random
    options.add_argument(f"user-agent={user_agent}")

    driver = webdriver.Chrome(service=service, options=options)
    get_source_html(driver, "https://elibrary.ru/author_profile.asp?authorid=830035")
    driver.quit()

if __name__ == "__main__":
    main()
