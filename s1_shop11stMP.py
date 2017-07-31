from shop11stCrawler_v5 import access
from selenium import webdriver

from time import time, strftime
from multiprocessing import Pool

def main(args):
    #URL crawling
    start =0
    driver = webdriver.Chrome()
    driver.get(args[1])
    box_pd = driver.find_element_by_id('layBodyWrap').find_elements_by_class_name('box_pd')

    totalReviews = 0

    for eachDeal in box_pd[start:]:
        url = eachDeal.find_element_by_tag_name('a').get_attribute('href')
        args[1] = url
        totalReviews += access(args)
        print ("accumulative:", totalReviews)


if __name__ == '__main__':
    start_time = time()
    args = []
    siteInput = open("sites", "r")
    for i in range(0,14):
        line = siteInput.readline()
        line.split()
        args.append(line.split())
    siteInput.close()
    #args = args[0]

    #pool = Pool(processes=4)
    #pool.map(main, args)
    main(args[0])
    print("--- %s seconds ---", (time.time()- start_time))

