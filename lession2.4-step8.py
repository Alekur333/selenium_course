from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

# 1.Открыть страницу http://suninjuly.github.io/explicit_wait2.html
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")


# 2.Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )

# 3.Нажать на кнопку "Book"
button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )
button.click()

# 4.Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

x = browser.find_element_by_id('input_value').text
y = str(math.log(abs(12 * math.sin(int(x)))))
input = browser.find_element_by_id('answer').send_keys(y)
button2 = browser.find_element_by_css_selector("[type='submit']").click()

