#Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

#def calc(x):
#  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #time.sleep(2)
    # Ваш код, который заполняет обязательные поля
    
    #x_element = browser.find_element_by_tag_name("img")
    #x = x_element.get_attribute("valuex")
    #y = calc(x)
    
    a = browser.find_element_by_xpath("//span[@id='num1']").text
    b = browser.find_element_by_xpath("//span[@id='num2']").text
    #t = browser.find_element_by_xpath("//h2/span[3]").text
    c = int(a)+ int(b)
    print(c)
    
    
    select = Select(browser.find_element_by_tag_name("select")) #нашли список и кликнули
    select.select_by_value(str(c)) #выбрали ответ 
    

    time.sleep(2)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()