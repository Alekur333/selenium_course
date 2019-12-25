from selenium import webdriver
import time
import math

#def calc(x):
#    return str(ln(abs(12*sin(int(x)))))

try:
    # 1.Открыть страницу http://SunInJuly.github.io/execute_script.html.
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2.Считать значение для переменной x.
    x = browser.find_element_by_id('input_value').text
    
    # 3. Посчитать математическую функцию от x.
    y = str(math.log(abs(12*math.sin(int(x)))))
    print(y)

    # 4. Проскроллить страницу вниз.
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #button.click()
    #time.sleep(2)

    # 5.Ввести ответ в текстовое поле.
    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    # 6. Выбрать checkbox "I'm the robot".
    robot = browser.find_element_by_id('robotCheckbox').click()
    #time.sleep(2)

    # 7. Переключить radiobutton "Robots rule!".
    rule = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", rule)
    rule.click()
    #time.sleep(2)

    #4. Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector("[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
