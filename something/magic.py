from selenium import webdriver
from something.very_important import url_address, msg


def do_something():
    driver = webdriver.Safari()
    driver.get(url_address)
    print(msg)

