#!/usr/bin/env python3
import cgi
print("Content-Type: text/html")
print('')

from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(chrome_options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities())
driver.get("http://www.python.org")

el = driver.find_element_by_tag_name('body')
el.screenshot("hi2.png")

driver.close()
