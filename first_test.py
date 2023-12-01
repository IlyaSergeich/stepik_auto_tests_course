import math

from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_tag_name('body > div > form > div.first_block > div.form-group.first_class > input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_tag_name('body > div > form > div.first_block > div.form-group.second_class > input')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_tag_name('body > div > form > div.first_block > div.form-group.third_class > input')
    input3.send_keys("Smolensk")
    input5 = browser.find_element_by_tag_name('body > div > form > div.second_block > div.form-group.first_class > input')
    input5.send_keys("12345678")
    input4 = browser.find_element_by_tag_name('body > div > form > div.second_block > div.form-group.second_class > input')
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("/html/body/div/form/button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла