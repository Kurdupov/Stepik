#Этот файл отредактирован!!!!

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys("Andrew")

    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys("Sukhanov")

    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys("suxanov.2001.andrey@gmail.com")

    #with open("test.txt", "w") as file:
    #    content = file.write("automationbypython")  # create test.txt file
    
    #current_dir = os.path.abspath(os.path.dirname(r"C:\Users\пк\Desktop"))
    #file_path = os.path.join(current_dir, 'file.txt')

    input4 = browser.find_element_by_css_selector('[type="file"]')
    input4.send_keys(r"C:\Users\пк\Desktop")
    

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
   

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


#Этот файл отредактирован!!!!
