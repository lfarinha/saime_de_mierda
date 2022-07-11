from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

from datetime import datetime
import json

def verify_saime_shitty_page():
    path_to_firefox_driver = ''c:\\Users\\leona\\selenium-driver\\firefox\\geckodriver.exe''
    service = Service(path_to_firefox_driver)
    driver = webdriver.Firefox(service=service)

    driver.get("https://tramites.saime.gob.ve/")
    driver.maximize_window()

    # wait until the puta image is visible
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@src='construccion-web.png']")))

    result = {}

    if element.is_displayed():
        result.update({"status": "fucking image is there.", "timestamp": str(datetime.now())})
    else:
        result.update({"status": "fucking image is NOT there.", "timestamp": str(datetime.now())})


    with open('log.txt', 'a') as log_file:
        json.dump(result, log_file, ensure_ascii=False, indent=4)

    driver.close()
    driver.quit()

