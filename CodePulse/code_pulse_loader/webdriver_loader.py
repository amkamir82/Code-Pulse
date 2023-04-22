from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def load_codepulse_on_web(ip, port):
    driver = _load_webdriver()
    print(ip)
    print(port)
    driver.get(f"http://{ip}:{port}")


def _load_webdriver():
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    return driver
