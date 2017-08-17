from shop11st_Crawler_v6 import access
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

    for eachDeal in box_pd[50:]:
        url = eachDeal.find_element_by_tag_name('a').get_attribute('href')
        args[1] = url
        totalReviews += access(args)
        print ("accumulative:", totalReviews)


if __name__ == '__main__':
    start_time = time()
    args = []
    siteInput = open("170811_sites.txt", "r")

    for line in siteInput:
        lineArray = line.split()
        args.append(lineArray)
    siteInput.close()

    pool = Pool(processes=3)
    pool.map(main, args)

    #for a single process
    #main(args)
    print("--- %s seconds ---", (time.time()- start_time))

