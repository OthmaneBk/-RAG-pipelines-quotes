from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time 
import os
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

PATH_TO_CHROMEDRIVER = os.getenv("PATH_TO_CHROMEDRIVER")

service=Service(executable_path=PATH_TO_CHROMEDRIVER)
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = uc.Chrome(service=service, use_subprocess=True, options=options)


driver.get("https://www.google.com")


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)


input_element=driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.clear()
input_element.send_keys("LLM" + Keys.ENTER)


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Les 4 étapes pour entrainer un LLM"))
)

link=driver.find_element(By.PARTIAL_LINK_TEXT, "Les 4 étapes pour entrainer un LLM")
link.click()


time.sleep(10)
driver.quit()