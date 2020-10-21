from time import sleep
from selenium import webdriver


def test_A():
    browser = webdriver.Chrome()
    browser.get('https://yandex.ru/')
    browser.execute_script("alert('hello');")
    sleep(2)
    browser.switch_to.alert.accept()
    sleep(10)
