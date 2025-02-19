from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0")
rolex_checkbox = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//input[@aria-label='Rolex']")))
rolex_checkbox.click()
mismatches = []
result_rolex_items = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='srp-river-results clearfix']/ul/li[position() <= 2]")))
original_window = driver.current_window_handle
for item in result_rolex_items:
    rolex_item_title = item.find_element(By.XPATH, ".//span[@role='heading']").text
    try:
        assert "rolex" in rolex_item_title.lower(), f"Result {rolex_item_title} title does not contain 'rolex'"
    except AssertionError as e:
        mismatches.append(f"AssertionError: {e}")
    rolex_item_price = item.find_element(By.XPATH, ".//span[@class='s-item__price']").text
    item.click()
    WebDriverWait(driver, 10).until(ec.number_of_windows_to_be(2))
    new_window = [handle for handle in driver.window_handles if handle != original_window][0]
    driver.switch_to.window(new_window)
    item_page_title = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//h1[@class='x-item-title__mainTitle']/span"))).text
    item_page_price = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH, "//div[@class='x-price-primary']/span"))).text
    try:
        assert rolex_item_title in item_page_title, f"Item page title mismatch for result: {rolex_item_title} vs. {item_page_title}"
    except AssertionError as e:
        mismatches.append(f"AssertionError: {e}")
    try:
        assert rolex_item_price in item_page_price, f"Item page price mismatch for result: {rolex_item_price} vs. {item_page_price}"
    except AssertionError as e:
        mismatches.append(f"AssertionError: {e}")
    driver.close()
    driver.switch_to.window(original_window)
rolex_checkbox = driver.find_element(By.XPATH, "//input[@aria-label='Rolex']")
rolex_checkbox.click()
casio_checkbox = driver.find_element(By.XPATH, "//input[@aria-label='Casio']")
casio_checkbox.click()
result_casio_items = WebDriverWait(driver, 10).until(ec.presence_of_all_elements_located((By.XPATH, "//div[@class='srp-river-results clearfix']/ul/li[@class='s-item s-item__pl-on-bottom' or @class='s-item s-item__before-answer s-item__pl-on-bottom'][position()>last()-2]")))
for item in result_casio_items:
    casio_item_title = item.find_element(By.XPATH, ".//span[@role='heading']").text
    try:
        assert "casio" in casio_item_title.lower(), f"Result {casio_item_title} title does not contain 'casio'"
    except AssertionError as e:
        mismatches.append(f"AssertionError: {e}")
print(mismatches)