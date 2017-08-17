#dc_inside_wannaone date collecter
#designed by Soo Min, JEONG

from selenium import webdriver
from time import strftime
from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoSuchWindowException

def halfTheJump(jump):
    jump = int (jump / 2)
    if (jump <= 1):
        jump = 1
    return jump

def checkDate(postNum):
    driver.get("http://gall.dcinside.com/board/view/?id=wannaone&no=" + str(postNum))
    date = driver.find_element_by_class_name("w_top_right").find_element_by_tag_name('b').text
    # Unnecessary condition below, since the site was developed on 19th of June,
    # and it is being crawled in August! ----------Aug
    # if (date.text[5]==0): -------Aug
    cdMonth = int(date[6])
    # else: -----------------------Aug
    #     month = int(date.text[5:7])
    cdDay = int(date[8:10])
    monAndDay = [cdMonth, cdDay]
    return monAndDay

#insert the month and the day
todayMonth = 8
todayDay = 9
startMonth = 6
startDay = 19

chromeOptions = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)
fileName = "WannaOne_date" + strftime("_%m%d_%Hh%M") + '.txt'
#output = open(fileName, "w", 1, "utf-8")

postNum=1
found = False

prevMonth = startMonth
prevDay = startDay

while(found==False):
    try:
        jump=10000
        newDayToFind = False
        while(newDayToFind==False):
            try:
                newMonth, newDay = checkDate(postNum)
                print("prev:[%d/%d], cu.pointer: [%d/%d] ---%d" % (prevMonth, prevDay, newMonth, newDay, postNum))

                # if we are still checking posts uploaded on the same day, pass
                if (prevMonth == newMonth and prevDay == newDay):
                    try:
                        postNum+= jump
                        print (">>JUMP:", str(postNum))
                    except NoSuchElementException:
                        postNum+=1
                        continue

                elif (prevMonth == newMonth and prevDay+1 == newDay):
                    try:
                        while(driver.get("http://gall.dcinside.com/board/view/?id=wannaone&no=" + str(postNum))==False):
                            postNum-=1

                        tempMonth,tempDay = checkDate(postNum-1)
                        print("<<one post back:", str(postNum-1))

                        if (tempMonth == prevMonth and tempDay == prevDay):
                            with open(fileName, 'a') as f:
                                f.write(str(newPost) + '\t' + str(newMonth) + '\t' + str(newDay)+'\n')
                            newDayToFind = True
                            print("====NEW DAY FOUND====")
                            print("====", str(newPost) + '\t' + str(newMonth) + '\t' + str(newDay), "====")

                        # In case of reaching the days apart from the current date
                        # as much as 2 days or more
                        elif(tempMonth == newMonth and tempDay == newDay):
                            postNum -= jump
                            print("<<JUMP/2:", str(postNum), " [Nope, keep going!]")

                    except NoSuchElementException:
                        continue

                else:
                    while(prevMonth == newMonth and prevDay < newDay):
                        postNum -= jump
                        print("<< JUMP:", str(postNum))

            except NoSuchElementException:
                print("No Such Element for one day:", str(postNum))
                postNum+=1

            jump = halfTheJump(jump)

                if(tempMonth == prevMonth and tempDay == prevDay):
                    with open(fileName, 'a') as f:
                        f.write(str(postNum + 1) + '\t' + str(temp) + '\t' + str(oneMoreDay)+'\n')
                    newDayToFind = True
                    print("====No Such element Exception====")
                    print("====", (str(postNum + 1) + '\t' + str(oneMoreMonth) + '\t' + str(oneMoreDay)), "====")

                oneMoreMonth, oneMoreDay = checkDate(postNum+1)

                if (oneMoreMonth == prevMonth and oneMoreDay == prevDay+1):
                    minusTwoDaysMonth, minusTwoDaysDay = checkDate(postNum-2)
                    print("<< two posts back:", str(postNum - 2), "[%d/%d]" %(minusTwoDaysMonth, minusTwoDaysDay))

                    if (minusTwoDaysMonth == prevMonth and minusTwoDaysDay == prevDay):
                        #output.write(str(postNum+1) + '\t' + str(oneMoreMonth) + '\t' + str(oneMoreDay))
                        with open(fileName, 'a') as f:
                            f.write(str(postNum+1) + '\t' + str(oneMoreMonth) + '\t' + str(oneMoreDay)+'\n')
                        newDayToFind = True
                        print("====Exactly in the middle====")
                        print("====", (str(postNum+1) + '\t' + str(oneMoreMonth) + '\t' + str(oneMoreDay)), "====")
                    else:
                        jump = halfTheJump(jump)
                        postNum -= jump
                else:
                    postNum +=1
                continue

            # setting a new day to find
            if (newDayToFind):
                print("...Setting a new Target...")
                prevDay = newDay
                prevMonth = newMonth

                if ((newDay == 30 and newMonth == 6) or (newDay == 31)):
                    newDay = 1
                    newMonth += 1
                else:
                    newDay += 1

                newDayToFind = False
                jump = jump

         #if the final date(today's date) is found
        if (newMonth == todayMonth+1 and newDay == todayDay+1):
         found = True

    except NoSuchElementException:
        print("No Such Element for the final date:", str(postNum))
        postNum+=1
        continue

driver.quit()