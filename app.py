from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
# this returns a web element
# now to click this, you can simply call the click method
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("tomascarignano")
password_box = browser.find_element_by_id("password")
password_box.send_keys("abcdefg")
password_box.submit()

assert "tomascarignano" in browser.page_source
