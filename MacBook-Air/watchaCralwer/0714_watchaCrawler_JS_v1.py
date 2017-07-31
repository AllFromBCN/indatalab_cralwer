#Watcha(watcha.net) Cralwer
#Developed by Soo Min, JEONG

#!!!!CheckLIST!!!!
#Change the id and password to the corporate address

'''
Basic Feature :
- Getting all the URLS from the list of movies with audience more than one million
'''

from multiprocessing import Pool
from time import localtime, strftime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

def main(site):
    fileName = "watcha" +strftime("_%m%d_%Hh%M")+".txt"
    output = open(fileName, "w", -1, "utf-8")

    driver = webdriver.Chrome()
    driver.get(site)

    #Inserting the id and pw
    wcId = 'soominjeong93@gmail.com'
    wcPw = 'PASSWORD'
    idin = driver.find_element_by_xpath('//*[@id="user_email"]')
    idin.send_keys(wcId)
    pwin = driver.find_element_by_xpath('//*[@id="user_password"]')
    pwin.send_keys(wcPw)
    driver.find_element_by_xpath('//*[@id="new_user"]/input[4]').click()
    driver.get("https://watcha.net/evalmore")

    posterList = driver.find_elements_by_class_name("movie-card")
    for poster in posterList:
        poster.find_element_by_class_name('detail-opener').click()
        active = driver.switch_to_active_element()
        print(active)
        print(driver.current_url)
        print("So far...")
    #driver.refresh()
    '''
    driver.implicitly_wait(3)
    driver.refresh()
    temp = driver.find_element_by_class_name('story')
    temp.click()
    print(driver.current_url)
    print("hello")
    '''


        #name = poster.find_elementa_by_xpath('//*[@id="movie-cards"]/div[1]/div/div[4]/div[1]')
        #print(name)


    #driver.quit()

main("https://watcha.net/login")

