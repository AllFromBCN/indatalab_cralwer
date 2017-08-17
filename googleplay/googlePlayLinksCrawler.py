from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException

def main(listURL):
    chromeOptions = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_settings.images":2}
    chromeOptions.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chromeOptions)

    f = open("170816_googlePlaysites.txt", "w", -1, 'UTF-8')

    driver.get(listURL)

    names = driver.find_elements_by_class_name("details")
    for app in names:
        nameAndURL = app.find_elements_by_tag_name('a')[1]
        name = nameAndURL.get_attribute('title')
        url = nameAndURL.get_attribute('href')
        print(name, url)
        baseURL = "https://play.google.com" + url
        f.write(name+'\t'+baseURL+'\n')

    f.close()
    driver.quit()

main("https://play.google.com/store/apps/collection/topselling_free")
