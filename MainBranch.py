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

from Post_Protocol import Post

from Hashtags import hs
from Captions import cap

import random


from Vars import usernames as us, passwords as ps, HostPages as Hp
# from Vars import ProfileXpath as ProfileXp
# from Vars import LogOXpath as LogOXp
from Vars import PagesToFollowFrom as PTFF
from Vars import PageTypes as PT

#pentru orice disperat se uita aici, nu nu am pus parolele direct aici
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
    if first==0:
        not_now = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Accept All")]'))).click()

def InstaLogin(Vusername, Vpassword):
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

    username.clear()
    password.clear()

    username.send_keys(Vusername)
    password.send_keys(Vpassword)
    time.sleep(3)
    log_in = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

    not_now = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
    time.sleep(1)
    if first==0:
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
    time.sleep(1)



def GoToPageByPhoto():
    post = '//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div/a/div/div[2]'
    page = '/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div/span/a'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, post))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, page))).click()

def SavePost(imgsrc):
    path = os.getcwd()
    path = os.path.join(path, "Posts")

    save_as = os.path.join(path, 'post1' + '.jpg')
    wget.download(imgsrc, save_as)

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
    SavePost(imgsrc=imagessrc[remeber])


def GoToFirstPost( h ):
    time.sleep(3)

    clickableimages = driver.find_elements_by_class_name('_9AhH0')
    clicknow = clickableimages[h]
    clicknow.click()

def LogOut():
    time.sleep(1)
    choices = driver.find_elements_by_xpath("//span[@class='_2dbep qNELH']")
    cautat = choices[0]
    prof = cautat.find_element_by_xpath('..')
    prof.click()
    time.sleep(0.5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Log Out")]'))).click()

def GoToLikes():
    time.sleep(1)
    #vcOH2
    T = driver.find_elements_by_class_name('vcOH2')
    if len(T)!=0 :
        x = driver.find_element_by_class_name("wpO6b  ")
        actions = ActionChains(driver)
        actions.click(x).perform()
        time.sleep(0.5)
        return 0
    T = driver.find_elements_by_class_name('fXIG0')
    if len(T) != 0:
        x = driver.find_element_by_class_name("wpO6b  ")
        actions = ActionChains(driver)
        actions.click(x).perform()
        time.sleep(0.5)
        return 0
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "zV_Nj"))).click()
    return 1
    # lk = '/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/a/span'
    # lk2 = '/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div[2]/a/span'
    # lk3 = '/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/a'
    # lk4 = '/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div[2]/a/span'
    #zV_Nj
    # WebDriverWait(driver, 10).until(   (EC.element_to_be_clickable((By.XPATH, lk)))||(EC.element_to_be_clickable((By.XPATH, lk2)))   ).click()

def FollowFromHost(number):
    Tp = PT[pageNr]
    k = random.randint(0,len(PTFF[Tp])-1)
    print(len(PTFF[Tp])-1 , k , "randomnumb")
    SearchForPage(PTFF[Tp][k])
    ind = 0
    GoToFirstPost(ind)

    while GoToLikes()==0:
        ind+=1
        GoToFirstPost(ind)

    Follow(number)

    x = driver.find_elements_by_class_name("WaOAr")
    print(len(x))
    actions = ActionChains(driver)
    actions.click(x[1]).perform()
    time.sleep(0.5)

    x = driver.find_element_by_class_name("wpO6b  ")
    actions = ActionChains(driver)
    actions.click(x).perform()
    time.sleep(0.5)

def ScrollTo(el):
    el.location_once_scrolled_into_view
    # element=el
    # actions = ActionChains(driver)
    # actions.move_to_element(element).perform()
    # driver.execute_script("arguments[0].scrollIntoView();", element)


def Follow(number):
    time.sleep(2)
    toFollow = driver.find_elements_by_class_name('L3NKy')
    cnt = 0
    ta = int(len(toFollow) / 2 + 1)
    A = toFollow[ta]
    B = A
    while (number > 0):
        #print (len(toFollow))
        ta = int(len(toFollow) / 2 + 1)
        for i in range(ta, len(toFollow) - 1):
            Fl = toFollow[i]
            Fl.location_once_scrolled_into_view
            if number<0:
                return
            if(Fl.text == 'Follow'):
                number -= 1
                #print(number)

                ScrollTo(Fl)
                time.sleep(random.random() + 0.1)
                Fl.click()
                time.sleep(random.random() + 2.2)

            ScrollTo(Fl)
            time.sleep(1.4+random.random())
        #print(number, "number")
        B=A
        toFollow = driver.find_elements_by_class_name('L3NKy')
        ta = int(len(toFollow) / 2 + 1)
        A = toFollow[ta]
        if A == B :
            return


def GetFirstPic():
    time.sleep(1)


    ind = 0
    GoToFirstPost(ind)

    while GoToLikes() == 0:
        ind += 1
        GoToFirstPost(ind)

    x = '/ html / body / div[7] / div / div / div[1] / div / div[2]'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x))).click()
    x = '/html/body/div[6]/div[3]/button'
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, x))).click()
    time.sleep(1)

    images = driver.find_elements_by_class_name('FFVAD')
    print(len(images))
    imagessrc = [image.get_attribute('src') for image in images]
    imagessrc = imagessrc[:-2]
    SavePost(imagessrc[ind])

def RandomizeCapt_Post():

    type = PT[pageNr]
    k = random.randint(0, len(cap[type])-1)
    k1 = random.randint(0, len(hs[type])-1)

    Post(caption=cap[type][k], hashtags=hs[type][k1],p=pageNr)


def PostFromHost():
    SearchForPage(Hp[pageNr])
    GetFirstPic()
    RandomizeCapt_Post()


def SearchForPage(page):
    # target the search input field
    searchbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
    searchbox.clear()


    # _01UL2
    # search for the hashtag cat
    keyword = page
    searchbox.send_keys(keyword)
    time.sleep(1)
    Trash = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "_01UL2")))
    time.sleep(2)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(1)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(0.5)


def LoginAndInit(k):
    if first==0:
        AcceptCookies()

    InstaLogin(us[k], ps[k])



def FollowProtocolFull():
    for t in range(0,10):
        at = time.localtime()
        current_time = time.strftime("%H:%M:%S", at)
        print(current_time, " ----------------------------------- ")
        global pageNr
        global Pageln
        pageNr=0
        for i in range(0,Pageln):

            if i>0:
                global first
                first=1
            LoginAndInit(pageNr)
            time.sleep(3)
            FollowFromHost(30)

            LogOut()
            pageNr+=1
            ToWait = random.random() + 1.5
            time.sleep(ToWait * 60)

            time.sleep(3)
        at = time.localtime()
        current_time = time.strftime("%H:%M:%S", at)
        print(current_time, " ----------------------------------- ")
        ToWait = random.random() + 0.1 + random.randint(5, 8)
        time.sleep(ToWait*60)

def GetFirst():
    return first

def PostProtocolFull():
    global pageNr
    global Pageln

    for i in range(0, Pageln):

        if i > 0:
            global first
            first = 1
        LoginAndInit(pageNr)
        time.sleep(2)
        PostFromHost()
        LogOut()
        pageNr += 1

        time.sleep(3)


first=0
pageNr=0

Pageln = len(us)-pageNr


#PostProtocolFull()
FollowProtocolFull()

