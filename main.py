from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
from config_driver import configure_driver
import json


url="https://quotes.toscrape.com/js/"

def scrappSite(url=url):
    
    driver = configure_driver(url)
    quotes_data = {}

    j=0

    try:
        while True:
            
            # Attendre que les éléments .quote soient chargés
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
            )

            # Récupérer toutes les citations
            quotes = driver.find_elements(By.CLASS_NAME, "quote")
            key = driver.current_url

            # Initialiser une seule fois une liste par page si elle n'existe pas
            if key not in quotes_data:
                quotes_data[key] = []

            for quote in quotes:
                text = quote.find_element(By.CLASS_NAME, "text").text
                author = quote.find_element(By.CLASS_NAME, "author").text
                tags = quote.find_elements(By.CLASS_NAME, "tag")
                tags_list = [tag.text for tag in tags]
                tags_str = " ; ".join(tags_list)

                # Ajouter un dictionnaire représentant UNE citation
                quotes_data[key].append({
                    "quote": text,
                    "author": author,
                    "tags": tags_str
                })

            # Tenter de trouver le bouton "Next"
            try:
                
                next_button = driver.find_element(By.CSS_SELECTOR, 'li.next > a')
                next_button.click()
                time.sleep(2)  # laisser le temps à la page de charger
            except:
                # Pas de bouton Next → fin
                break
            j+=1

        with open("quotes_data.json", "w", encoding="utf-8-sig") as f:
            json.dump(quotes_data, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print("Erreur :", e)

    finally:
        driver.quit()



def login_buttonPage(url=url):

    login_pageDict={}
    driver = configure_driver(url)

    #pour attendre la charge de la page
    WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'p > a'))
            )
    
    login_page = driver.find_element(By.CSS_SELECTOR, 'p > a')
    login_page.click()

    
    # Attendre que les champs de login soient visibles
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "container"))
    )

    # Scraper les éléments
    labels = driver.find_elements(By.CSS_SELECTOR, 'label[for="username"]')

    username_text = labels[0].text
    password_text = labels[1].text

    login_button= driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
    login_button_text = login_button.get_attribute('value')

    key=driver.current_url
    if key not in login_pageDict:
        login_pageDict[key] = []
                
    # Remplir le dictionnaire
    login_pageDict[key].append({
                    "username": username_text,
                    "password": password_text,
                    "login_button": login_button_text
                })


    with open("login_page.json", "w", encoding="utf-8-sig") as f:
        json.dump(login_pageDict, f, ensure_ascii=False, indent=4)


    time.sleep(10)  # Laisser le temps à la page de charger


scrappSite()
