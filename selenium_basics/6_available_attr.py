from selenium import webdriver
from components.filter import LeftFilter

driver = webdriver.Chrome()
left_filter = LeftFilter(driver)

print(', '.join(dir(left_filter)))
