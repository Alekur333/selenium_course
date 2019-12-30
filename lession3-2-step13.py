from selenium import webdriver
import unittest
import time


class TestReg(unittest.TestCase):

    def test_reg1(self):

        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        input1 = browser.find_element_by_css_selector("input.form-control.first[required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("input.form-control.second[required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("input.form-control.third[required]")
        input3.send_keys("1@mail.m")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, "not registered!")

        browser.quit()

    def test_reg2(self):

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector("input.form-control.first[required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("input.form-control.second[required]")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("input.form-control.third[required]")
        input3.send_keys("1@mail.m")

        time.sleep(2)

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, "not registered!")

        browser.quit()

if __name__ == "__main__":
    unittest.main()

