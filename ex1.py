import os

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options

CHROME_DRIVER = "/home/ilya/PycharmProjects/devops-hw-6/chromedriver"
FIREFOX_DRIVER = "/usr/bin/geckodriver"

urls: dict = {
    "walla": "http://www.walla.co.il",
    "ynet": "http://ynet.co.il"
}


def chrome_driver() -> WebDriver:
    print("Using Chrome...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    os.chmod(CHROME_DRIVER, 0o755)
    chrome_driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROME_DRIVER)
    return chrome_driver


def firefox_driver() -> WebDriver:
    print("Using Firefox...")
    firefox_options = Options()
    firefox_options.add_argument("--headless")
    os.chmod(CHROME_DRIVER, 0o755)
    firefox_options = webdriver.Firefox(options=firefox_options, executable_path=FIREFOX_DRIVER)

    return firefox_options


def task_1_3():
    chrome: WebDriver = chrome_driver()
    chrome.get(urls['walla'])
    print('Page title: ', chrome.title)
    chrome.quit()

    firefox:  WebDriver = firefox_driver()
    firefox.get(urls['ynet'])
    print('Page title: ', firefox.title)
    firefox.quit()


task_1_3()
