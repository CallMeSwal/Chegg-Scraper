#!/usr/bin/env python3
import cgi
print("Content-Type: text/html")
print('')
from selenium import webdriver
import os
import baseconvert

#url = str(input("Enter url:"))
'''
form = cgi.FieldStorage() 
if form.getvalue("link_url"): 
    url = form.getvalue("link_url")
    print(url)

    url_filename = url.replace(":", "").replace("/", "").replace(".", "").replace("#", "").replace("%", "").replace("&", "").replace("*", "").replace("/", "").replace("{", "").replace("}", "").replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace("?", "").replace("|", "").replace("+", "").replace("-", "")
    #url_filename = str(int.from_bytes(url.encode('utf-8'), 'little'))
    #url_filename = str(base(int.from_bytes(url.encode('utf-8'), 'little'), 10, 32))
    url_filename +=".png"

    if not(os.path.isfile('img/'+url_filename)):
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_experimental_option('useAutomationExtension', False)

        driver = webdriver.Chrome(chrome_options=chromeOptions, desired_capabilities=chromeOptions.to_capabilities())
        driver.get(url)

        el = driver.find_element_by_tag_name('body')
        el.screenshot("img/"+url_filename)

        driver.close()
'''
print("heyo")
