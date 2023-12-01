#Задание на execute_script
from selenium import webdriver
import time
import math
#from selenium.webdriver.support.ui import Select

#функция подсчета по заданию
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #time.sleep(2)
    # Ваш код, который заполняет обязательные поля
    
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
    #x = x_element.get_attribute("valuex")
    x = x_element.text
    y = calc(x)
    
    #находим элемент "кнопка" и скролим до нее
    button = browser.find_element_by_css_selector("button.btn")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    #вводим ответ в поле
    vv = browser.find_element_by_xpath("//input[@id='answer']")
    vv.send_keys(y)
    time.sleep(1)
    
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #поиск чекбокса
    chk = browser.find_element_by_css_selector("[type='checkbox']")
    chk.click()
    
    
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #поиск радиобаттона
    rb = browser.find_element_by_css_selector("[id='robotsRule']")
    rb.click()
    
    
    
    #select = Select(browser.find_element_by_tag_name("select")) #нашли список и кликнули
    #select.select_by_value(str(c)) #выбрали ответ 
    

    time.sleep(1)
    # Отправляем заполненную форму
    #button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()