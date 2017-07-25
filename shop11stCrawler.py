#11stCrawler
#designed by Soo Min, JEONG

#v2 : removed all the duplicated reviews
#   : goes through the reviews with 5, 2, or 1 star automatically (by index error handling)
#v3 : keep the balance of the numbers between positive reviews and the negative ones
#v4 : returns the total number of reviews
#v5 : Multiprocessing

import time
from time import localtime, strftime
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
# for explicit waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def crawl(driver, output):

    wait = WebDriverWait(driver, 5)
    negReviews = 0
    posReviews = 0
    #When the balance between the negative reviews and the positive is broken
    stop4bal = False

    for starNum in [1,2,5]:
        print ("========="+str(starNum)+" star(s)"+"=========")

        # changing the category into 5stars, 2stars, and 1star
        category = driver.find_element_by_xpath('//*[@id="detailViewGrade"]')
        category.click()
        cate = driver.find_element_by_css_selector('input[id="star0'+str(starNum)+'"]')
        cate.click()
        driver.switch_to.default_content()
        driver.switch_to.frame('ifrmReview')

        # The list of duplicated reviews
        dupliReviews= []

        pageNum=0

        try:
            while(True and stop4bal == False):
                for i in range(0,9):
                    pageNum+=1
                    #print("[ page: ", pageNum, "]")
                    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'review_list')))
                    reviewList = driver.find_element_by_class_name('review_list')
                    pages = reviewList.find_element_by_class_name('s_paging_v2').find_elements_by_id('paging_page')
                    reviews = reviewList.find_elements_by_class_name('cfix')
                    oldComment = ''

                    #crawling each review
                    # -- if you would like to simply check the page switching, line-comment this part
                    for review in reviews:
                        star_temp = review.find_element_by_class_name('selr_star')
                        comment_temp = review.find_element_by_class_name('summ_conts')
                        currentComment = comment_temp.text
                        lenComment = len(comment_temp.text)

                        if ( (negReviews==0 and posReviews==0 and starNum!=5) or negReviews > posReviews):
                            if (oldComment == currentComment):
                                dupliReviews.append(oldComment)
                            elif (lenComment>5 and currentComment not in dupliReviews):
                                oldComment = currentComment
                                output.write(str(starNum) + '\t' + str(currentComment) +'\n')
                                if (starNum == 1 or starNum == 2) : negReviews +=1
                                elif (starNum == 5): posReviews+=1
                                # print(str(starNum) + '\t' + str(currentComment))

                        else:
                            stop4bal = True
                            break

                    #click the next list of 10 pages ('>>')
                    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'review_list')))
                    nextPage = pages[i].click()

                wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'review_list')))
                reviewList = driver.find_element_by_class_name('review_list')
                lastPage = reviewList.find_element_by_class_name('s_paging_v2').find_element_by_id('paging_next')
                lastPage.click()

        except IndexError:
            continue

        except NoSuchElementException:
            print("Error - End of the page")
            continue

        except TimeoutError:
            driver.implicitly_wait(30)
            continue

    print ("negative : %d, positive : %d" %(negReviews, posReviews))
    return posReviews + negReviews

def access(args):
    driver = webdriver.Chrome()
    driver.get(args[1])
    driver.switch_to.frame('ifrmReview')

    name = args[0]
    fileName = name + strftime("_%m%d_%Hh%M")+'.txt'
    print(fileName)
    output = open(fileName, "w", -1, "utf-8")

    numReviews = crawl(driver, output)

    driver.quit()
    output.close()

    return numReviews

