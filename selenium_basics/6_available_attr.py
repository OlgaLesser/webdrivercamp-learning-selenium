from selenium import webdriver
from components.filter import LeftFilter

driver = webdriver.Chrome
left_filter = LeftFilter(driver)
print(dir(left_filter))
