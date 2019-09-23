import webbrowser as browser
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# address = pyperclip.paste()
# browser.open('https://www.google.com/maps/place/'+address)
# browser.open('https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error')

browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
browser.get('http://facebook.com')
email = browser.find_element_by_id('email')
password = browser.find_element_by_id('pass')
submit = browser.find_element_by_id('u_0_b')

email.send_keys('marvelike7@gmail.com')
password.send_keys('Theowalcott@@77')
submit.submit()


