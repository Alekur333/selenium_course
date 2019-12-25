from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # 1.Открыть страницу
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2.Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
    box = browser.find_element_by_id("treasure")

    # 3.Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x = box.get_attribute("valuex")

    # 4.Посчитать математическую функцию от x (сама функция остаётся неизменной).
    y = calc(x)

    # 5.Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    # 5.Отметить checkbox "I'm the robot".
    input2 = browser.find_element_by_id("robotCheckbox").click()
    #input2.click()

    # 6.Выбрать radiobutton "Robots rule!".
    input3 = browser.find_element_by_id("robotsRule").click()
    #input3.click()

    # 7.Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("button[type='submit']").click()
    #button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
