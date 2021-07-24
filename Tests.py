#Selenium imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Vars import username as us, password as ps #pentru orice disperat se uita aici, nu nu am pus parolele direct aici
# si nu le am dat commit sack dick
from MainBranch import driver


import os
import wget


def Testeazachestie():
    print("test")
    import time

    # target the search input field
    searchbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
    searchbox.clear()
    print("aj1")
    # search for the hashtag cat
    keyword = "#lamborghini"
    searchbox.send_keys(keyword)
    print("aj2")


print("no genocide in tiananmen")



