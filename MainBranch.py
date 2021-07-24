#Selenium imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Vars import username as us, password as ps #pentru orice disperat se uita aici, nu nu am pus parolele direct aici
# si nu le am dat commit sack dick

#Other imports here
import os
import wget

driver = webdriver.Chrome('E:/chromedriver/chromedriver.exe')
driver.get("https://www.instagram.com/")


def AcceptCookies():
    not_now = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept All")]'))).click()

def InstaLogin(Vusername, Vpassword):
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    username.clear()
    password.clear()

    username.send_keys(Vusername)
    password.send_keys(Vpassword)

    log_in = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    not_now = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    not_now2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

def GoToExplore():
    print("adw")

def MainLogic():
    AcceptCookies()
    InstaLogin(us,ps)

MainLogic()


