import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()    
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('site', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_put_answer_get_hint(browser, site):
    link = f"https://stepik.org/lesson/{site}/step/1"
    browser.get(link)
    time.sleep(10)
    answer = str(math.log(int(time.time())))
    input_text = browser.find_element_by_css_selector("textarea")
    input_text.send_keys(answer)
    send = browser.find_element_by_css_selector(".submit-submission")
    send.click()
    time.sleep(2)
    check = browser.find_element_by_css_selector(".smart-hints__hint").text
    assert "Correct!" == check, "Ответ не верный, найди кусочeк загадочного сообщения"
