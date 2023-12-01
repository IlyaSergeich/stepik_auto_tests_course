# Задание на execute_script
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

# from selenium.webdriver.support.ui import Select

#функция подсчета по заданию
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))  # What is ln(abs(12*sin(x))), where x = 148?

# current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла

try:
    link = "http://suninjuly.github.io/alert_accept.html"

    # Отключение ошибки(опции) Bluetooth: bluetooth_adapter_winrt.cc:1055 Getting Default Adapter failed
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=chromeOptions)  # driver = webdriver.Chrome(options=chromeOptions)

    browser.get(link)

    # находим элемент "кнопка" с названием "I want to go on a magical journey!" и тапаем
    browser.find_element(By.CSS_SELECTOR, ".btn").click()

    # подтверждение confirm-а
    confirm = browser.switch_to.alert
    confirm.accept()

    # поиск значения Х и подсчет функции из предусловия
    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    # вводим ответ в поле
    vv = browser.find_element(By.XPATH, "//input[@id='answer']")
    vv.send_keys(y)
    #time.sleep(1)



    # Ваш код, который заполняет обязательные поля
    #elements = browser.find_elements(By.CSS_SELECTOR,".form-control")
    #for element in elements:
    #    element.send_keys("TEST")

    # file = browser.find_element_by_css_selector("[type='file']")
    #browser.find_element(By.CSS_SELECTOR,"#file").send_keys(file_path)  # нашли куда отправлять и отправили

    # находим элемент "кнопка" и и тапаем
    browser.find_element(By.CSS_SELECTOR,".btn").click()

    # подтверждение confirm-а
    alert = browser.switch_to.alert
    print (alert.text)
    alert.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()