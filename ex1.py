import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement

CHROME_DRIVER = "/home/ilya/PycharmProjects/devops-hw-6/chromedriver"
FIREFOX_DRIVER = "/usr/bin/geckodriver"

urls: dict = {
    "walla": "http://www.walla.co.il",
    "ynet": "http://ynet.co.il",
    "google_translate": "https://translate.google.com/"
}

locators = {
    "walla_title": (By.CSS_SELECTOR, '[title="וואלה! NEWS"]'),
    "google_translate_source": (By.CSS_SELECTOR, "textarea[aria-label='Source text']"),
}


def chrome_driver() -> WebDriver:
    print("Using Chrome...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    os.chmod(CHROME_DRIVER, 0o755)
    chrome_driver: WebDriver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROME_DRIVER)
    return chrome_driver


def firefox_driver() -> WebDriver:
    print("Using Firefox...")
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    os.chmod(CHROME_DRIVER, 0o755)
    firefox_driver: WebDriver = webdriver.Firefox(options=firefox_options, executable_path=FIREFOX_DRIVER)

    return firefox_driver


def task_1():
    chrome: WebDriver = chrome_driver()
    chrome.get(urls['walla'])
    print('Page title: ', chrome.title)
    chrome.quit()

    firefox: WebDriver = firefox_driver()
    firefox.get(urls['ynet'])
    print('Page title: ', firefox.title)
    firefox.quit()


def task_2():
    chrome: WebDriver = chrome_driver()
    chrome.get(urls['walla'])

    try:
        title = "וואלה! NEWS"
        page_title = chrome.find_element(*locators['walla_title'])
        assert title == page_title.get_attribute('title')
    except (AssertionError, NoSuchElementException) as e:
        raise e
    finally:
        chrome.quit()


def task_3():
    chrome: WebDriver = chrome_driver()
    chrome.get(urls['walla'])
    print('Page title: ', chrome.title)
    chrome_page_title = chrome.find_element(*locators['walla_title']).get_attribute('title')
    chrome.quit()

    firefox: WebDriver = firefox_driver()
    firefox.get(urls['ynet'])
    print('Page title: ', firefox.title)
    firefox_page_title = chrome.find_element(*locators['walla_title']).get_attribute('title')
    firefox.quit()

    assert firefox_page_title == chrome_page_title


def task_4():
    chrome: WebDriver = chrome_driver()
    chrome.get(urls['google_translate'])
    print('Page title: ', chrome.title)

    source_text_element: WebElement = chrome.find_element(locators["google_translate_source"])
    source_text_element.send_keys("תפוח")
    chrome.quit()


task_1()
task_2()
task_3()
task_4()
