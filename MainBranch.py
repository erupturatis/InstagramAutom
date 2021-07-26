#Selenium imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import os.path
from os import path
import wget
import time
import FetchPostData
from Post_Protocol import Post
from Hashtags import hs
from Captions import cap
from random import randint,seed,random


from Vars import username as us, password as ps #pentru orice disperat se uita aici, nu nu am pus parolele direct aici
# si nu le am dat commit ,
# semnat,eugen din trecut

#Other imports here
import os
import wget

####################################################################################################
driver = webdriver.Chrome('E:/chromedriver/chromedriver.exe')
driver.get("https://www.instagram.com/")
####################################################################################################


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
    time.sleep(2)
    log_in = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    not_now = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    not_now2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

def GoToHashtag(keyword):
    # target the search input field
    searchbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
    searchbox.clear()
    # search for the hashtag cat
    searchbox.send_keys(keyword)
    time.sleep(1)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(0.5)
    searchbox.send_keys(Keys.ENTER)

def GoToExplore():

    #el = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]'
    el = '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]'
    ExploreDaddy = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, el))).click()
    time.sleep(3)
    driver.refresh()


def GoToPageByPhoto():
    post = '//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div/a/div/div[2]'
    page = '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div/span/a'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, post))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, page))).click()

def SelectAndDownloadImgFromPage():
    time.sleep(2)
    clickableimages = driver.find_elements_by_class_name('_9AhH0')

    links = []
    likes = []
    x = '/html/body/div[5]/div[3]/button'
    lk = '/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/a/span'
    lngt = len(clickableimages)
    for i in range(0, min(15,lngt-1)):
        clicknow = clickableimages[i]
        clicknow.click()
        time.sleep(1.2)
        if(len(driver.find_elements_by_class_name('fXIG0'))!=0):
            print("e video ...")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x))).click()
            i-=1
            continue

        links.append(driver.current_url)
        likes.append(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, lk))).text)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x))).click()


        time.sleep(0.1)
    ##appends images links and likes

    images = driver.find_elements_by_class_name('FFVAD')

    imagessrc = [image.get_attribute('src') for image in images]
    imagessrc = imagessrc[:-2]
    ##images src for download purposes

    remeber = -1
    max = 0

    for i in range(0, len(likes)):
        liksconv = likes[i].replace(",", "")
        liksconv = int(liksconv)
        if (max < liksconv):
            max = (liksconv)
            remember = i
    ##remember is the chose img
    keyword = "lambo"
    path = os.getcwd()
    path = os.path.join(path, "Posts")

    save_as = os.path.join(path, 'post1' + '.jpg')
    wget.download(imagessrc[remember],save_as)

def GoToFirstPost():
    time.sleep(3)

    clickableimages = driver.find_elements_by_class_name('_9AhH0')
    clicknow = clickableimages[0]
    clicknow.click()

def GoToLikes():
    lk = '/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/a/span'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, lk))).click()

def FollowPeopleFromExploreFirstPage():
    GoToExplore()
    GoToPageByPhoto()
    GoToFirstPost()
    # bug when video comes in
    GoToLikes()
    Follow(40)

def ScrollTo(el):
    element=el
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()

    driver.execute_script("arguments[0].scrollIntoView();", element)


def Follow(number):
    time.sleep(2)
    toFollow = driver.find_elements_by_class_name('L3NKy')
    cnt = 0
    prevNumber = number
    ta = int(len(toFollow) / 2 + 1)
    while (number > 0):
        for i in range(ta, len(toFollow) - 1):
            number -= 1
            print(number)
            time.sleep(random() + 0.1)
            Fl = toFollow[i]
            ScrollTo(Fl)
            time.sleep( random() + 0.1 )
            Fl.click()

            time.sleep(0.5)
        if number == prevNumber :
            return
        else:
            prevNumber=number
        toFollow = driver.find_elements_by_class_name('L3NKy')

def LoginAndExploreChoseAndPost():
    #Goes to explore pick post, picks page, picks post, downloads it, and posts it

    GoToExplore()
    GoToPageByPhoto()
    SelectAndDownloadImgFromPage()

    seed(time.time())
    k=randint(0, 9)

    Post(caption=cap[k], hashtags=hs[0])


def LoginAndInit():
    AcceptCookies()
    InstaLogin(us, ps)

LoginAndInit()
#GoToExplore()
FollowPeopleFromExploreFirstPage()



# time.sleep(3)
# for i in range(1,5):
#
#     GoToExplore()
#     time.sleep(1)
#     GoToPageByPhoto()
#     SelectAndDownloadImgFromPage()
#     Post(caption="This is and absolute beast", hashtags=hs[0])

