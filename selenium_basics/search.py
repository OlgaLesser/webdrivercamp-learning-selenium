from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com")
search_field = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@id='gh-ac']")))
print(driver.current_url)
search_field.send_keys("women watch")
search_button = driver.find_element(By.XPATH, "//button[@id='gh-search-btn']")
search_button.click()
header_element = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//h1[@class='srp"
                                                                                           "-controls__count-heading']")))
assert "results for women watch" in header_element.text
driver.quit()