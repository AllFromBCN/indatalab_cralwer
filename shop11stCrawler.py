#11st crawler
#v1 : reads the list of reviews with a certain number of stars

import time
from multiprocessing import Pool
from time import localtime, strftime
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException

def access(site):
    name = "Women_BEST_100"
    fileName = name + strftime("_%m%d_%Hh%M")+'.txt'
    output = open(fileName, "a", -1, "utf-8")

    #switching the frame to iframe
    driver = webdriver.Chrome()
    driver.get(site)
    driver.switch_to.frame('ifrmReview')

    #changing the category into 5stars, 2stars, and 1star
    category = driver.find_element_by_xpath('//*[@id="detailViewGrade"]')
    category.click()

    #selectorInput = ('input[id="star0'+str(i)+'"]')
    #print("selector Input:", selectorInput)
    cate = driver.find_element_by_css_selector('input[id="star05"]')
    cate.click()
    driver.switch_to.default_content()
    driver.switch_to.frame('ifrmReview')

    reviewList= driver.find_element_by_class_name('review_list')
    pages = reviewList.find_element_by_class_name('s_paging_v2').find_elements_by_id('paging_page')
    reviews = reviewList.find_elements_by_class_name('cfix')

    pageNum=0

    try:
        while(True):
            for i in range(0,9):
                pageNum+=1
                print("[page: ", pageNum, "]")
                reviewList = driver.find_element_by_class_name('review_list')
                pages = reviewList.find_element_by_class_name('s_paging_v2').find_elements_by_id('paging_page')
                reviews = reviewList.find_elements_by_class_name('cfix')

                for review in reviews:
                    star_temp = review.find_element_by_class_name('selr_star')
                    comment_temp = review.find_element_by_class_name('summ_conts')
                    lenComment = len(comment_temp.text)
                    if (lenComment == 0):
                        break

                    if (lenComment>3 and comment_temp.text not in ('잘 받았습니다. 많이 파세요 ^^', '빠른 배송 감사합니다. ㅋㅋ', '완전 강추합니다.')):
                        # if (i == 5):
                        #     po+=1
                        # else : ne+=1
                        temp_print = str(star_temp.text[13]) + '\t' + str(comment_temp.text)
                        output.write(temp_print)
                        print(temp_print)

                #click the next page
                nextPage = pages[i].click()

            reviewList = driver.find_element_by_class_name('review_list')
            lastPage = reviewList.find_element_by_class_name('s_paging_v2').find_element_by_id('paging_next')
            lastPage.click()

    except Exception:
        print("error")

    output.close()

    driver.quit()


access("http://deal.11st.co.kr/product/SellerProductDetail.tmall?method=getSellerProductDetail&prdNo=961905132&trTypeCd=37#")