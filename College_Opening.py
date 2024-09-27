from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import sqlite3
import Speak as s  # Assuming Speak.py contains your custom speak function

def opening():
    # Specify the path to the ChromeDriver executable
    chrome_driver_path = "C:/Users/Asus/Downloads/chrome-win64/chrome-win64/chrome.exe"
    
    # Set Chrome options
    chrome_options = Options()
    chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"  # Path to Chrome executable
    
    # Set ChromeDriver executable path
    chrome_options.add_argument(f"webdriver.chrome.driver={chrome_driver_path}")
    
    # Initialize Chrome driver with Chrome options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://myclass.lpu.in/')  # Fixed typo in URL

    reg = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[1]')
    reg.send_keys('11703695')

    password = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[6]/input[2]')
    password.send_keys('Ravi@1')

    submit = driver.find_element_by_xpath('/html/body/div[2]/div/form/div[7]/button')
    submit.click()
    s.speak("ID and password have been entered")

    view_meetings = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
    view_meetings.click()
    s.speak("Class Meeting is clicked")
    
    now = datetime.now()
    hour = int(now.strftime("%H"))
    time.sleep(5)
    
    try: 
        if hour > 12:
            hour -= 12
        if hour == 9:                              
            meeting = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[10]/td[2]')
        elif hour == 10:
            meeting = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[11]/td[2]')
        elif hour == 11:
            meeting = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[12]/td[2]')
        elif hour == 12:
            meeting = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[13]/td[2]')
        elif hour == 1:
            meeting = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[14]/td[2]')
        elif hour == 2:
            meeting = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[15]/td[2]')
        elif hour == 3:
            meeting = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[16]/td[2]')
        elif hour == 4:
            meeting = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[17]/td[2]')
        elif hour == 5:
            meeting = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[18]/td[2]')
        elif hour == 6:
            meeting = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[2]/table/tbody/tr[19]/td[2]')
        else:
            s.speak("Not done")
        meeting.click()
        join = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
        join.click()
    except Exception as e:
        talk = "While attending class I got an exception. I think you did not have any class, but still trying to access."
        s.speak(talk)
 
def database():
    conn = sqlite3.connect('classes.db')
    c = conn.cursor()
    date = datetime.now()
    date_is = date.strftime("%y:%m:%d")
    date_is = date_is.split(':')
    day_is = datetime(int(date_is[0]), int(date_is[1]), int(date_is[2]))
    day_is = day_is.strftime("%A")
    hour = int(date.strftime("%H"))
    if hour > 12:
        hour -= 12

    flag = True
    for row in c.execute("SELECT * FROM  class_timings"):
        if row[0] == day_is and row[1] == hour:
            s.speak("I am attending now......")
            flag = False

    if flag:
        s.speak("Sir, I have checked the database.")
        if day_is == "Saturday" or day_is == "Sunday" or day_is == 'Friday':
            s.speak("It's your weekend, don't worry about class.")
        else:
            s.speak("You don't have class now. You have class at")
            for row in c.execute("SELECT * from class_timings"):
                if row[0] == day_is:
                    if row[1] > 8:
                        s.speak(str(row[1]) + "AM")
                    else:
                        s.speak(str(row[1]) + "PM")

    return flag


if __name__ == "__main__":
    opening()
