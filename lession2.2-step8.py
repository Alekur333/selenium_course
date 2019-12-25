from selenium import webdriver
import time
import os


try:
    # 1.Открыть страницу http://suninjuly.github.io/file_input.html.
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2.Заполнить текстовые поля: имя, фамилия, email
    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys('firstname')
    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys('lastname')
    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys('email@mail.ru')

    # 3. Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    element = browser.find_element_by_id("file")
    element.send_keys(file_path)
    #time.sleep(2)

    #4. Нажать кнопку "Submit"
    button = browser.find_element_by_css_selector("[type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
