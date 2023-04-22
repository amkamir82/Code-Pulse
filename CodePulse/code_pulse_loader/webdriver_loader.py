from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import *
from selenium.webdriver.chrome.options import Options


# driver.get("http://127.0.0.1:35389")
# time.sleep(100)


def load_webdriver(port):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    driver.get(f"http://127.0.0.1:{port}")
    # return driver


# def load_codepulse_on_web(driver, port):
#     pass