#install selenium using pip
from selenium import webdriver

browser=webdriver.Chrome('C:\Users\collins\Downloads\chromedriver_win32')
browser.get('https://thecodex.me/projects')
elem=browser.find_element_by_link_text('Dashboard')
elem.text()
elem.get_attribute('href')
#to click the link use click function
elem.click()
serachabra=browser.find_elements_by_id('')
#to populate the text field  send_keys() function is used
serachabra.send_keys('downloads')
