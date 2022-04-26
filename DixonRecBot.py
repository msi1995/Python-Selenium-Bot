## Dixon Rec Center Reservation Bot
## Author: Doug Lloyd
##
## Bot capable of navigating itself through Dixon Recreation Center's booking pages and automatically
## booking the desired date nearly instantly. Created because reservations were filling too fast and only
## open at midnight.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
from pytz import timezone
import pytz
import sys
import os

current_time = str(datetime.datetime.now())
chrome_options = Options()
chrome_options.add_argument("--headless")
flag = 0
refreshpage = 0
dateChanged = False

print("Dixon Rec Bot [Master Copy]\n")

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

driver = webdriver.Chrome(resource_path('./webdriver/chromedriver.exe'))
#driver = webdriver.Chrome()
driver.set_window_size(1920,1080)
driver.get("https://shop.recsports.oregonstate.edu/booking")

print ("\n\nDixon Recreation Center Reservation Bot, v3.0")
print("________________________________________________________")
time.sleep(3)
print ("DixonBot: " + "Time initialized. Current time PST is: ", end="")
print (current_time[11:19] + ".")
current_time = str(datetime.datetime.now())
print ("\n["+ current_time[11:19] + "]" + " DixonBot: " "Please follow the instructions below.")


userReady = input("\n[" + current_time[11:19] + "]" + " DixonBot: " "The booking page should be open. Click the Dixon image and sign in with\nyour account and DUO authentication. Once you have done this, press enter.")


current_time = str(datetime.datetime.now())
userTimeSlot = int(input("\n\n["+ current_time[11:19] + "]" + " DixonBot: " + "Pick the time slot under whichever day you are trying to book and then press enter. \nEnter 99 to monitor availability on a day that you already missed booking for. \n\n" 
+"Mon-Fri times:\n1 for 6-7AM \n2 for 7-8AM \n3 for 8-9AM \n4 for 9-10AM \n5 for 10-11AM \n6 for 11-12PM \n7 for 12-1PM \n8 for 1-2PM"
+"\n9 for 2-3PM \n10 for 3-4PM \n11 for 4-5PM \n12 for 5-6PM \n13 for 6-7PM \n14 for 7-8PM \n15 for 8-9PM \n16 for 9-10PM\n\n"
+"Sat times:\n1 for 9-10AM \n2 for 10-11AM \n3 for 11-12PM \n4 for 12-1PM \n5 for 1-2PM \n6 for 2-3PM \n7 for 3-4PM \n8 for 4-5PM \n9 for 5-6PM \n10 for 6-7PM \n11 for 7-8PM \n12 for 8-9PM\n\n"
+"Sun times:\n1 for 10-11AM \n2 for 11-12PM \n3 for 12-1PM \n4 for 1-2PM \n5 for 2-3PM \n6 for 3-4PM \n7 for 4-5PM \n8 for 5-6PM \n9 for 6-7PM \n10 for 7-8PM \n11 for 8-9PM\n\n"))

if(userTimeSlot == 99):
    driver.get("https://shop.recsports.oregonstate.edu/booking/47c87f69-0234-4aba-9c22-99d036560eb8")
    whichDay = int(input("Which day? 1 for today, 2 for tomorrow, 3 for 2 days ahead: "))
    while(userTimeSlot == 99):

        try:
            driver.refresh()
            element = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[9]/div[2]/div[2]/button[" + str(whichDay) + "]")))
            element.click()
            time.sleep(1)
        except:
            pass

        try:
            element = WebDriverWait(driver, 4).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='divBookingSlots']/div[2]/div[1]/div/button")))
            element.click()
            current_time = str(datetime.datetime.now())
            print("\n["+ current_time[11:19] + "]" +" DixonBot: " +  "I reserved something. Stopping.")
            sys.exit("")

        except:
            current_time = str(datetime.datetime.now())
            print("\n["+ current_time[11:19] + "]" +" DixonBot: " +  "No slots were open. trying again.")

current_time = str(datetime.datetime.now())
userTimeSlot2 = int(input("\n["+ current_time[11:19] + "]" + " DixonBot: " + "Enter a backup time slot. The bot will try to get this one \nif your initial timeslot cannot be grabbed.\n\n"))

current_time = str(datetime.datetime.now())
print("\n\n["+ current_time[11:19] + "]" + " DixonBot: " + "The bot is self-functional now and will start at midnight. You \ndon't need to do anything else. You may minimize, but do not close or resize the Chrome window.\nEnsure your PC/laptop isn't going to sleep/shutdown, either.\n")

userTimeSlotReal = "//*[@id='divBookingSlots']/div[2]/div[" + str(userTimeSlot)  + "]/div/button"
userTimeSlotReal2 = "//*[@id='divBookingSlots']/div[2]/div[" + str(userTimeSlot2)  + "]/div/button"

driver.get("https://shop.recsports.oregonstate.edu/booking/47c87f69-0234-4aba-9c22-99d036560eb8")
element = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.CLASS_NAME, "single-date-select-one-click")))
firstDate = element.get_attribute("data-day")



while(flag == 0):
    current_time = str(datetime.datetime.now())   ##refresh the current time.

    ## check if its midnight (00 in the hours slot).
    if(current_time[11:13] != "00"):
        refreshpage += 1
        ## this refreshes the page every 5 minutes so we don't get stale/timeout while waiting.
        if(refreshpage == 60):
            driver.refresh()
            refreshpage = 0

        print("\n["+ current_time[11:19] + "]" +" DixonBot: " +  "Waiting for midnight...\n")
        time.sleep(5) ##sleep so we aren't running a while loop hundreds of times a second for hours.


    else:
        flag = 1        ## if it's midnight, we want to bail out of this while loop.



if(current_time[11:13] == "00"):
    current_time = str(datetime.datetime.now())
    print("\n["+ current_time[11:19] + "]" + " DixonBot: " +  "Bot online @ 12:00 AM. Checking page for availability.")
    driver.refresh()

    ## loop here until the "data-day" attribute on the first date that can be selected is different than 
    ## when the program was first started. If the attribute is different, that means a different date is
    ## now in the first slot (meaning a new day has been added and is open for reservations). Once this
    ## happens, we want to exit this loop so we can actually click and book the new day.
    while(dateChanged == False):
        element = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.CLASS_NAME, "single-date-select-one-click")))
        compareDate = element.get_attribute("data-day")
        if(compareDate != firstDate):
            break
        time.sleep(0.1)
        driver.refresh()


    for i in range(50):

        ## click the new date posted (2 days out)
        try:
            element = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[9]/div[2]/div[2]/button[3]")))
            element.click()
        except:
            current_time = str(datetime.datetime.now())
            print("\n["+ current_time[11:19] + "]" + " DixonBot: " + "Wasn't able to click date. This should never happen.")
            driver.refresh()


        ## click the time slot we want and attempt to book. Use try catches tons here
        ## because we cant afford to have the bot crash if a link doesnt populate.

        try:
            element = WebDriverWait(driver, 6).until(
                EC.presence_of_element_located((By.XPATH, userTimeSlotReal)))
            element.click()
            time.sleep(0.4)

        except:
            current_time = str(datetime.datetime.now())
            print("\n["+ current_time[11:19] + "]" + " DixonBot: " + "First choice wasn't present yet, or was full. Trying second choice...\n")

        #click the backup time slot we want and attempt to book
        try:
            element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, userTimeSlotReal2)))
            element.click()
            time.sleep(0.4)

        except:
            current_time = str(datetime.datetime.now())
            print("\n["+ current_time[11:19] + "]" + " DixonBot: " + "Second choice couldn't be clicked.")


        ## check for presence of a completed booking. Stop executing if a booking was made
        try:
           element = driver.find_element_by_class_name("glyphicon-ok")
           current_time = str(datetime.datetime.now())
           print("\n["+ current_time[11:19] + "]" + " DixonBot: " + "A reservation was successfully booked.")
           break;
        except:
           pass


        ##refresh the page so the bot can try again if something broke
        driver.refresh()
        current_time = str(datetime.datetime.now())
        print("\n["+ current_time[11:19] + "]" + " DixonBot: " + "Trying again.")

