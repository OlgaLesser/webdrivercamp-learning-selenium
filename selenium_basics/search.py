from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://www.ebay.com")
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, "gh-ac")))
print(driver.current_url)
element.send_keys("women watch")
search = driver.find_element(By.ID, "gh-btn")
search.click()
header = driver.find_element(By.CLASS_NAME, "srp-controls__count-heading")
assert "830,000+ results for women watch" in header.text
driver.quit()