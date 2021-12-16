import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement

CHROME_DRIVER: str = "/home/ilya/PycharmProjects/devops-hw-6/chromedriver"
FIREFOX_DRIVER: str = "/usr/bin/geckodriver"
TIME_TO_WAIT: int = 20

urls: dict = {
    "walla": "http://www.walla.co.il",
    "ynet": "http://ynet.co.il",
    "google_translate": "https://translate.google.com/",
    "youtube": "https://www.youtube.com/",
    "facebook": "https://www.facebook.com/",
    "github": "https://github.com/"
}

locators = {
    "walla_title": (By.CSS_SELECTOR, '[title="וואלה! NEWS"]'),
    "google_translate_source": (By.CSS_SELECTOR, "textarea[aria-label='Source text']"),
    "google_translate_source_2": (By.CLASS_NAME, "er8xn"),
    "google_translate_source_3": (By.CSS_SELECTOR, "textarea.er8xn"),
    "youtube_searchbar": (By.CSS_SELECTOR, "input[id='search']"),
    "youtube_searchbar_btn": (By.ID, 'search-icon-legacy'),
    "facebook_login": (By.ID, 'email'),
    "facebook_password": (By.ID, 'pass'),
    "facebook_login_btn": (By.NAME, 'login')
}


def chrome_driver() -> WebDriver:
    print("Using Chrome...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("no-sandbox")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--headless")
    os.chmod(CHROME_DRIVER, 0o755)
    chrome_driver: WebDriver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROME_DRIVER)
    chrome_driver.implicitly_wait(TIME_TO_WAIT)
    return chrome_driver


def firefox_driver() -> WebDriver:
    print("Using Firefox...")
    firefox_options = Options()
    firefox_options.add_argument("--disable-extensions")
    firefox_options.add_argument("--headless")
    os.chmod(CHROME_DRIVER, 0o755)
    firefox_driver: WebDriver = webdriver.Firefox(options=firefox_options, executable_path=FIREFOX_DRIVER)
    firefox_driver.implicitly_wait(TIME_TO_WAIT)
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
    firefox.get(urls['walla'])
    print('Page title: ', firefox.title)
    firefox_page_title = firefox.find_element(*locators['walla_title']).get_attribute('title')
    firefox.quit()

    assert firefox_page_title == chrome_page_title


def task_4():
    chrome: WebDriver = chrome_driver()
    chrome.get(urls['google_translate'])
    print('Page title: ', chrome.title)

    source_text_element: WebElement = chrome.find_element(*locators["google_translate_source"])
    source_text_element.send_keys("תפוח")
    chrome.quit()


def task_5():
    chrome: WebDriver = chrome_driver()
    chrome.get(urls['youtube'])
    print('Page title: ', chrome.title)

    search_bar: WebElement = chrome.find_element(*locators["youtube_searchbar"])
    search_bar.send_keys("Cats videos")
    search_btn: WebElement = chrome.find_element(*locators["youtube_searchbar_btn"])
    search_btn.click()
    chrome.quit()


def task_6():
    chrome: WebDriver = chrome_driver()
    chrome.get(urls['google_translate'])
    print('Page title: ', chrome.title)

    textArea: WebElement = chrome.find_element(*locators["google_translate_source"])
    textArea2: WebElement = chrome.find_element(*locators["google_translate_source_2"])
    textArea3: WebElement = chrome.find_element(*locators["google_translate_source_3"])
    print(textArea)
    print(textArea2)
    print(textArea3)
    chrome.quit()


def task_7():
    chrome: WebDriver = chrome_driver()
    chrome.get(urls['facebook'])
    print('Page title: ', chrome.title)

    user_name: str = "my_user"
    user_password: str = "my_password"

    login: WebElement = chrome.find_element(*locators["facebook_login"])
    password: WebElement = chrome.find_element(*locators["facebook_password"])
    login_btn: WebElement = chrome.find_element(*locators["facebook_login_btn"])

    login.send_keys(user_name)
    password.send_keys(user_password)
    login_btn.click()
    chrome.quit()


def task_8():
    chrome: WebDriver = chrome_driver()
    chrome.get(urls['facebook'])
    print('Page title: ', chrome.title)

    chrome.delete_all_cookies()
    cookies: set = chrome.get_cookies()
    print(cookies)
    chrome.quit()


def task_9():
    chrome: WebDriver = chrome_driver()
    chrome.get(urls['github'])
    print('Page title: ', chrome.title)

    github_search = chrome.find_element(*locators['github_search'])
    github_search.send_keys("selenium", Keys.RETURN)
    chrome.quit()


# task_1()
# task_2()
# task_3()
# task_4()
# task_5()
task_6()
# task_7()
# task_8()
# task_9()
