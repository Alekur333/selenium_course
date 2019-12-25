from selenium import webdriver
import time
import math


try:
    # 1. Открыть страницу http://suninjuly.github.io/redirect_accept.html.
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2. Нажать на кнопку
    window1 = browser.window_handles[0]
    button1 = browser.find_element_by_css_selector("[type='submit']").click()

    # 3. Переключиться на новую вкладку
    window2 = browser.window_handles[1]
    browser.switch_to.window(window2)

    # 4. Пройти капчу для робота и получить число-ответ
    x = browser.find_element_by_id('input_value').text
    y = str(math.log(abs(12 * math.sin(int(x)))))
    input = browser.find_element_by_id('answer').send_keys(y)
    button2 = browser.find_element_by_css_selector("[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
