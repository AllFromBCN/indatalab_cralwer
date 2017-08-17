#Google Play review-crawling
#Programmed by SooMin, Jeong
#crawls 100 positive reviews and another 100 negative reviews
import time
from multiprocessing import Pool
from time import localtime, strftime
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from socket import *

#URLs
#hanhwa
hanhwa = "https://play.google.com/store/apps/details?id=com.hanwhalife.mobilecenter"

#set server
serverName = "localhost"
serverPort = 4444
BUFFER_SIZE = 1024
s = socket(AF_INET, SOCK_STREAM)
s.bind((serverName, serverPort))
s.listen(1)
#end

def permitCheck(num):
    permit = False
    if (num <= 100):
        permit = True
    return permit

def main(input):
    #Creating a text file to write the reviews from Google Play
    site = input[1]
    name = input[0]
    fileName = name + strftime("_%m%d_%Hh%M")+'.txt'
    output = open(fileName, "w", -1, "utf-8")

    driver = webdriver.Chrome()
    driver.get(site)

    button = driver.find_element_by_xpath('//*[@id="body-content"]/div/div/div[1]/div[2]/div[2]/div[1]/div[4]/button[2]/div[2]/div/div')
    button.click()

    i=0

    while(True):
        try:
            print('[page:'+str(i)+']')
            i=i+1
            #containing single reviews
            reviewList = driver.find_elements_by_class_name('single-review')

            for eachReview in reviewList:
                content = eachReview.find_element_by_class_name('review-body')

                # getting the star rating from current rate
                currentRate = eachReview.find_element_by_class_name('current-rating')
                starRate = currentRate.get_attribute('style')[7:9]
                star = int(int(starRate) / 20)
                if (star == 0):
                    star = 5

                if(len(content.text)>2):
                    output.write(str(star) + '\t' + content.text + '\n')
                    print(str(star) + '\t'+content.text)

            button.click()


        except ElementNotVisibleException:
            print("Error - Element Not Visible")
            break

        except NoSuchElementException:
            print("Error - No such Element")
            break

        except OSError:
            s.close()
            continue

    output.close()
    driver.quit()

if __name__ == '__main__':
    start_time = time.time()
    args = []
    siteInput = open("170816_googlePlaysites.txt", "r")

    for line in siteInput:
        lineArray = line.split()
        args.append(lineArray)
    siteInput.close()

    pool = Pool(processes=3)
    pool.map(main, args)

    #for a single process
    # args = ['test', 'https://play.google.com/store/apps/details?id=com.psvn.masha_and_the_bear_mini']
    # main(args)
    print("--- %s seconds ---", (time.time()- start_time))
