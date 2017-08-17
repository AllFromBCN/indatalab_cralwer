from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from multiprocessing import Pool
import time

def urlget():
    tar_url = 'https://www.instagram.com/explore/tags/%s/'%u'코드제로a9'
    driver = webdriver.Chrome()
    driver.get(tar_url)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/a').click()

    lastHeight = driver.execute_script("return document.body.scrollHeight")
    while True:
        for lol in range(1,6):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(0.5)
        newHeight = driver.execute_script("return document.body.scrollHeight")
        if newHeight == lastHeight:
                break
        else:
            lastHeight = newHeight

        
    urlList=[]

    for line in driver.find_elements_by_class_name('_myci9'):
        for post in line.find_elements_by_class_name('_8mlbc'):
            urlList.append(post.find_element_by_tag_name('a').get_attribute('href'))
    time.sleep(2)
    driver.close()
    return urlList


def eachpage(urls):
    fw = open('insta_crawler.txt','a',-1,'utf-8')
    driver = webdriver.Chrome()
    for url in urls:
        forwrite=[]
       
        driver.get(url)
        forwrite.append(url)
        forwrite.append(driver.find_element_by_class_name('_hghxm').text.replace('\n',' '))
        forwrite.append(driver.find_element_by_class_name('_3fmp4').find_element_by_class_name('_9gcwa').get_attribute('title'))
        forwrite.append(driver.find_element_by_class_name('_h3rdq').text.replace('\n',' '))
        fw.write('\t'.join(forwrite))
        fw.write('\n')
        time.sleep(2)
    driver.close()
    fw.close()

def spliturl(urlList,num):
    return [urlList[i:i+int(len(urlList)/num)+1]for i in range (0, len(urlList),int(len(urlList)/num)+1)]

if __name__ == '__main__':
    start_time = time.time()
    urlList = urlget()
    pool = Pool(processes=3)
    pool.map(eachpage,spliturl(urlList,3))
    print("--- %s seconds ---" % (time.time() - start_time))
