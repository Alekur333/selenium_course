from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    # 1.Открыть страницу
    link = "http://suninjuly.github.io/selects1.html"
    # Когда ваш код заработает, попробуйте запустить его на
    # странице http://suninjuly.github.io/selects2.html.
    # Ваш код и для нее тоже ﻿должен пройти успешно.
    browser = webdriver.Chrome()
    browser.get(link)


    # 2.Посчитать сумму заданных чисел
    x1 = browser.find_element_by_id('num1').text
    x2 = browser.find_element_by_id('num2').text
    value = str(int(x1) + int(x2))
    print(value)

    # 3.Выбрать в выпадающем списке значение равное расчитанной сумме
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(value)

    #4. Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector("[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



