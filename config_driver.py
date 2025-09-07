from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import os
from dotenv import load_dotenv
load_dotenv()

def configure_driver(url):
    PATH_TO_CHROMEDRIVER = os.getenv("PATH_TO_CHROMEDRIVER")

    service = Service(executable_path=PATH_TO_CHROMEDRIVER)
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")

    driver = uc.Chrome(version_main=136,service=service, options=options, use_subprocess=True)
    driver.get(url)
    return driver