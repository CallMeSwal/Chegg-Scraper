#!/usr/bin/env python3
import cgi
print("Content-Type: text/html")
print('')
from selenium import webdriver

form = cgi.FieldStorage() 
if form.getvalue("link_url"): 
    link_url = form.getvalue("link_url")
    print(link_url)
