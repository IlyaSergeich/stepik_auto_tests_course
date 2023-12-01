from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #time.sleep(2)
    # Ваш код, который заполняет обязательные поля
    elements = browser.find_elements_by_xpath("//div[@class='form-group']//input")
    for element in elements:
        element.send_keys("Здарова")
     
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    
    file_name = "test_lesson2_2_step8.txt"
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, file_name)
    
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    #отправляем файл
    element.send_keys(file_path)

    #time.sleep(2)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #time.sleep(1)

    # находим элемент, содержащий текст
    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    #welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    #assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()