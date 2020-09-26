link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
from selenium.common.exceptions import NoSuchElementException

def test_find_buttonaddfor_basket(browser):
	browser.get(link)
	browser.find_element_by_css_selector("#login_link")
	try:
		elem = browser.find_element_by_xpath("//button[@type='submit]")
		return True
	except NoSuchElementException:
		return False
	assert is_element_present(elem)==True, "корзинка не найдена"