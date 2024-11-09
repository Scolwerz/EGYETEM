#!/usr/bin/env python3


# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pyautogui
import time


def main():
    # Webdriver létrehozása (ChromeDriver chromium alaphoz)
    #driver = webdriver.Chrome()

    # Oldal betöltése
    #driver.get('https://clickcounter.io')
    #time.sleep(5)
    
    # Elem keresése
    #box_location = driver.find_element_by_class_name("circle2")

    #for i in range(2023):
    #    box_location.click()
    #    time.sleep(0.1)

    # Böngésző bezárása
    #time.sleep(10)
    #driver.quit()
    
    
    for i in range(2023):
        button_loc = pyautogui.locateCenterOnScreen("button.png")
        pyautogui.click(button_location)
        time.sleep(0.1)


#############################################################################

if __name__ == "__main__":
    main()