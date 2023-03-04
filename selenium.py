from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.get('https://www.chennaisuperkings.com')
driver.find_element_by_xpath("//p[contains(text(),'LOGIN')]").click()
