from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # 1.Открыть страницу
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2.Считать значение для переменной x
    x_element = browser.find_element_by_css_selector('span#input_value')

    # 3.Посчитать математическую функцию от x
    x = x_element.text
    y = calc(x)

    # 4.Ввести ответ в текстовое поле.
    input1 = browser.find_element_by_css_selector("form #answer")
    input1.send_keys(y)

    # 5.Отметить checkbox "I'm the robot".
    input2 = browser.find_element_by_id("robotCheckbox")
    input2.click()

    # 6.Выбрать radiobutton "Robots rule!".
    input3 = browser.find_element_by_id("robotsRule")
    input3.click()

    # 7.Нажать на кнопку Submit.
    button = browser.find_element_by_css_selector("button[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
