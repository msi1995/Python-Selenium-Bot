## Dixon Rec Center Reservation Bot
##
## Bot capable of navigating itself through Dixon Recreation Center's booking pages and automatically
## booking the desired date nearly instantly. Created because reservations were filling too fast and only
## open at midnight. Packaged into a neat executable with pyInstaller and chromedriver binaries bundled in.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import sys
import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def initialize_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(resource_path('./webdriver/chromedriver.exe'))
    driver.set_window_size(1920, 1080)
    return driver


def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))


def click_element(driver, locator):
    element = wait_for_element(driver, locator)
    element.click()


def wait_and_click_element(driver, locator, timeout=10):
    element = wait_for_element(driver, locator, timeout)
    element.click()


def pick_time_slot(driver, user_time_slot):
    locator = (By.XPATH, f"//*[@id='divBookingSlots']/div[2]/div[{user_time_slot}]/div/button")
    wait_and_click_element(driver, locator)


def book_reservation(driver, user_time_slot_real, user_time_slot_real2):
    try:
        click_element(driver, (By.XPATH, user_time_slot_real))
        time.sleep(0.4)
        return True
    except:
        print("First choice wasn't present yet, or was full. Trying second choice...")
    
    try:
        click_element(driver, (By.XPATH, user_time_slot_real2))
        time.sleep(0.4)
        return True
    except:
        print("Second choice couldn't be clicked.")
    
    return False


def check_reservation(driver):
    try:
        driver.find_element(By.CLASS_NAME, "glyphicon-ok")
        return True
    except:
        return False


def main():
    current_time = str(datetime.datetime.now())
    driver = initialize_driver()

    print("Dixon Rec Bot [Master Copy]\n")
    print("Dixon Recreation Center Reservation Bot, v3.0")
    print("________________________________________________________")
    time.sleep(3)
    print("DixonBot: " + "Time initialized. Current time PST is: ", end="")
    print(current_time[11:19] + ".")
    current_time = str(datetime.datetime.now())
    print("\n[" + current_time[11:19] + "]" + " DixonBot: " "Please follow the instructions below.")

    user_ready = input("\n[" + current_time[11:19] + "]" + " DixonBot: " "The booking page should be open. Click the Dixon image and sign in with\nyour account and DUO authentication. Once you have done this, press enter.")

    current_time = str(datetime.datetime.now())
    user_time_slot = int(input("\n\n[" + current_time[11:19] + "]" + " DixonBot: " + "Pick the time slot under whichever day you are trying to book and then press enter. \nEnter 99 to monitor availability on a day that you already missed booking for. \n\n"
                               + "Mon-Fri times:\n1 for 6-7AM \n2 for 7-8AM \n3 for 8-9AM \n4 for 9-10AM \n5 for 10-11AM \n6 for 11-12PM \n7 for 12-1PM \n8 for 1-2PM"
                               + "\n9 for 2-3PM \n10 for 3-4PM \n11 for 4-5PM \n12 for 5-6PM \n13 for 6-7PM \n14 for 7-8PM \n15 for 8-9PM \n16 for 9-10PM\n\n"
                               + "Sat times:\n1 for 9-10AM \n2 for 10-11AM \n3 for 11-12PM \n4 for 12-1PM \n5 for 1-2PM \n6 for 2-3PM \n7 for 3-4PM \n8 for 4-5PM \n9 for 5-6PM \n10 for 6-7PM \n11 for 7-8PM \n12 for 8-9PM\n\n"
                               + "Sun times:\n1 for 10-11AM \n2 for 11-12PM \n3 for 12-1PM \n4 for 1-2PM \n5 for 2-3PM \n6 for 3-4PM \n7 for 4-5PM \n8 for 5-6PM \n9 for 6-7PM \n10 for 7-8PM \n11 for 8-9PM\n\n"))

    if user_time_slot == 99:
        driver.get("https://shop.recsports.oregonstate.edu/booking/47c87f69-0234-4aba-9c22-99d036560eb8")
        which_day = int(input("Which day? 1 for today, 2 for tomorrow, 3 for 2 days ahead: "))

        while user_time_slot == 99:
            try:
                driver.refresh()
                element = wait_for_element(driver, (By.XPATH, f"/html/body/div[3]/div[1]/div[2]/div[9]/div[2]/div[2]/button[{which_day}]"))
                element.click()
                time.sleep(1)
            except:
                pass

            try:
                element = wait_for_element(driver, (By.XPATH, "//*[@id='divBookingSlots']/div[2]/div[1]/div/button"), timeout=4)
                element.click()
                current_time = str(datetime.datetime.now())
                print("\n[" + current_time[11:19] + "]" + " DixonBot: " + "I reserved something. Stopping.")
                sys.exit("")
            except:
                current_time = str(datetime.datetime.now())
                print("\n[" + current_time[11:19] + "]" + " DixonBot: " + "No slots were open. trying again.")

    current_time = str(datetime.datetime.now())
    user_time_slot2 = int(input("\n[" + current_time[11:19] + "]" + " DixonBot: " + "Enter a backup time slot. The bot will try to get this one \nif your initial timeslot cannot be grabbed.\n\n"))

    current_time = str(datetime.datetime.now())
    print("\n\n[" + current_time[11:19] + "]" + " DixonBot: " + "The bot is self-functional now and will start at midnight. You \ndon't need to do anything else. You may minimize, but do not close or resize the Chrome window.\nEnsure your PC/laptop isn't going to sleep/shutdown, either.\n")

    user_time_slot_real = "//*[@id='divBookingSlots']/div[2]/div[" + str(user_time_slot) + "]/div/button"
    user_time_slot_real2 = "//*[@id='divBookingSlots']/div[2]/div[" + str(user_time_slot2) + "]/div/button"

    driver.get("https://shop.recsports.oregonstate.edu/booking/47c87f69-0234-4aba-9c22-99d036560eb8")
    element = wait_for_element(driver, (By.CLASS_NAME, "single-date-select-one-click"))
    first_date = element.get_attribute("data-day")

    while flag == 0:
        current_time = str(datetime.datetime.now())  # refresh the current time.

        # check if it's midnight (00 in the hours slot).
        if current_time[11:13] != "00":
            refreshpage += 1
            # this refreshes the page every 5 minutes so we don't get stale/timeout while waiting.
            if refreshpage == 60:
                driver.refresh()
                refreshpage = 0

            print("\n[" + current_time[11:19] + "]" + " DixonBot: " + "Waiting for midnight...\n")
            time.sleep(5)  # sleep so we aren't running a while loop hundreds of times a second for hours.

        else:
            flag = 1  # if it's midnight, we want to bail out of this while loop.

    if current_time[11:13] == "00":
        current_time = str(datetime.datetime.now())
        print("\n[" + current_time[11:19] + "]" + " DixonBot: " + "Bot online @ 12:00 AM. Checking page for availability.")
        driver.refresh()

        # loop here until the "data-day" attribute on the first date that can be selected is different than
        # when the program was first started. If the attribute is different, that means a different date is
        # now in the first slot (meaning a new day has been added and is open for reservations). Once this
        # happens, we want to exit this loop so we can actually click and book the new day.
        while date_changed == False:
            element = wait_for_element(driver, (By.CLASS_NAME, "single-date-select-one-click"))
            compare_date = element.get_attribute("data-day")
            if compare_date != first_date:
                break
            time.sleep(0.1)
            driver.refresh()

        for i in range(50):
            # click the new date posted (2 days out)
            try:
                element = wait_for_element(driver, (By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[9]/div[2]/div[2]/button[3]"))
                element.click()
            except:
                current_time = str(datetime.datetime.now())
                print("\n[" + current_time[11:19] + "]" + " DixonBot: " + "Wasn't able to click date. This should never happen.")
                driver.refresh()

            # click the time slot we want and attempt to book. Use try catches tons here
            # because we can't afford to have the bot crash if a link doesn't populate.
            try:
                element = wait_for_element(driver, (By.XPATH, user_time_slot_real))
                element.click()
                time.sleep(0.4)
            except:
                current_time = str(datetime.datetime.now())
                print("\n[" + current_time[11:19] + "]" + " DixonBot: " + "First choice wasn't present yet, or was full. Trying second choice...")
                try:
                    element = wait_for_element(driver, (By.XPATH, user_time_slot_real2))
                    element.click()
                    time.sleep(0.4)
                except:
                    current_time = str(datetime.datetime.now())
                    print("\n[" + current_time[11:19] + "]" + " DixonBot: " + "Second choice couldn't be clicked.")
                    pass

            # check if the reservation went through by searching for the 'glyphicon-ok' class that
            # displays if the reservation was successful.
            if check_reservation(driver):
                current_time = str(datetime.datetime.now())
                print("\n[" + current_time[11:19] + "]" + " DixonBot: " + "Reservation successful!")
                break
            else:
                current_time = str(datetime.datetime.now())
                print("\n[" + current_time[11:19] + "]" + " DixonBot: " + "Reservation unsuccessful. Retrying in 10 seconds.")
                time.sleep(10)
                driver.refresh()

        if check_reservation(driver) == False:
            current_time = str(datetime.datetime.now())
            print("\n[" + current_time[11:19] + "]" + " DixonBot: " + "Could not reserve any time slots on the new day.")

    driver.quit()


if __name__ == "__main__":
    main()
