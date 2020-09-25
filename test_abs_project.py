import unittest
from selenium import webdriver
import time

class TestAbs(unittest.TestCase):
	def test_abs1(self):
		try:
			link = "http://suninjuly.github.io/registration1.html"
			browser = webdriver.Chrome()
			browser.get(link)
			first_name = browser.find_element_by_xpath("//input[@placeholder='Input your first name']").send_keys('firstmane')
			last_name = browser.find_element_by_xpath("//input[@placeholder='Input your last name']").send_keys('firstmane')
			Email = browser.find_element_by_xpath("//input[@placeholder='Input your email']").send_keys('Email')
			Phone = browser.find_element_by_xpath("//input[@placeholder='Input your phone:']").send_keys('Phone')
			Address = browser.find_element_by_xpath("//input[@placeholder='Input your address:']").send_keys('Address')
			button_ckick = browser.find_element_by_xpath("//button[@type='submit']").click()
			welcome_text_elt = browser.find_element_by_tag_name("h1")
			# записываем в переменную welcome_text текст из элемента welcome_text_elt
			welcome_text = welcome_text_elt.text
			# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
			self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "message")
		finally:
			# успеваем скопировать код за 30 секунд
			time.sleep(10)
			# закрываем браузер после всех манипуляций
			browser.quit()

	def test_abs2(self):
		try:
			link = "http://suninjuly.github.io/registration2.html"
			browser = webdriver.Chrome()
			browser.get(link)
			first_name = browser.find_element_by_xpath("//input[@placeholder='Input your first name']").send_keys('firstmane')
			last_name = browser.find_element_by_xpath("//input[@placeholder='Input your last name']").send_keys('firstmane')
			Email = browser.find_element_by_xpath("//input[@placeholder='Input your email']").send_keys('Email')
			Phone = browser.find_element_by_xpath("//input[@placeholder='Input your phone:']").send_keys('Phone')
			Address = browser.find_element_by_xpath("//input[@placeholder='Input your address:']").send_keys('Address')
			button_ckick = browser.find_element_by_xpath("//button[@type='submit']").click()
			welcome_text_elt = browser.find_element_by_tag_name("h1")
			# записываем в переменную welcome_text текст из элемента welcome_text_elt
			welcome_text = welcome_text_elt.text
			# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
			self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "message")
		finally:
			# успеваем скопировать код за 30 секунд
			time.sleep(10)
			# закрываем браузер после всех манипуляций
			browser.quit()
if __name__ == "__main__":
    unittest.main()