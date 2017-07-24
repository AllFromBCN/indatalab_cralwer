#11stCrawler
#Designed by Soo Min, JEONG

#v2 : removed all the duplicated reviews
#   : goes through the reviews with 5, 2, or 1 star automatically (by index error handling)

import time
from multiprocessing import Pool
from time import localtime, strftime
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
# for explicit waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def crawl(driver, output):

    wait = WebDriverWait(driver, 5)

    for starNum in [5,2,1]:
        print ("========="+str(starNum)+" stars"+"=========")

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
            while(True):
                for i in range(0,9):
                    pageNum+=1
                    print("[ page: ", pageNum, "]")
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

                        if (oldComment == currentComment):
                            dupliReviews.append(oldComment)
                        elif (lenComment>3 and currentComment not in dupliReviews):
                            oldComment = currentComment
                            output.write(str(starNum) + '\t' + str(currentComment))
                            # print(str(starNum) + '\t' + str(currentComment))

                    #click the next list of 10 pages ('>>')
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

def main(args):
    driver = webdriver.Chrome()
    driver.get(args[0])
    driver.switch_to.frame('ifrmReview')

    name = args[1]
    fileName = name + strftime("_%m%d_%Hh%M")+'.txt'
    output = open(fileName, "a", -1, "utf-8")

    crawl(driver, output)

    driver.quit()
    output.close()

args[0] = "http://deal.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=961905132&trTypeCd=37#"

main ("http://deal.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=961905132&trTypeCd=37#")