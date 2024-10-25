from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0")
search = driver.find_element(By.XPATH, "//li[@class='x-refine__main__list--value' and @name='Brand']//input[@aria-label='Rolex']")
search.click()
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".s-item__title")))

def verify_rolex_in_results(driver_):
    results = driver_.find_elements(By.CSS_SELECTOR, ".s-item__title >span")
    filtered_list = [item for item in results if item.text] #filters empty results
    rolex_mismatches = []
    for x, result_ in enumerate(filtered_list[:2]):
        title = result_.text.lower()
        print(title)
        if "rolex" not in title:
            rolex_mismatches.append(f"Expected 'Rolex' in title {x + 1}, but got '{title}'")
    if rolex_mismatches:
        print("Mismatches for Rolex:")
        for mismatch in rolex_mismatches:
            print(mismatch)
verify_rolex_in_results(driver)

def get_results_info(driver_):
    results = []
    search_results = driver.find_elements(By.CSS_SELECTOR, ".s-item")
    filtered_list = [item for item in search_results if item.text]  # filters empty results
    try:
        for result_ in filtered_list[:2]:
            title_element = result_.find_element(By.CSS_SELECTOR, ".s-item__title")
            price_element = result_.find_element(By.CSS_SELECTOR, ".s-item__price")
            link = result_.find_element(By.CSS_SELECTOR, ".s-item__link")
            title = title_element.text
            price = re.sub(r'[^\d\-+\.]', '', price_element.text)  # Removes non-numeric characters
            result_info = {"title": title, "price": price, "link": link}
            results.append(result_info)
        return results
    except Exception as e:
        print(f"An error occurred while scraping data: {e}")
        return []

results_data = get_results_info(driver)
all_handles = driver.window_handles
if results_data:
    for i, result in enumerate(results_data):
        print(f"Title: {result['title']}\nPrice: {result['price']}\n")
        result['link'].click()
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".x-item-title__mainTitle")))
        actual_title = driver.find_element(By.CSS_SELECTOR, ".x-item-title__mainTitle").text
        actual_price = re.sub(r'[^\d\-+\.]', '', driver.find_element(By.CSS_SELECTOR, ".x-price-primary").text) # Removes non-numeric characters
        assert actual_title == result['title'], f"Expected title: {result['title']}, Actual title: {actual_title}"
        assert actual_price == result['price'], f"Expected price: {result['price']}, Actual price: {actual_price}"
        driver.switch_to.window(all_handles[0])
else:
    print("No data found for the first two results.")
search = driver.find_element(By.XPATH, "//li[@class='x-refine__main__list--value' and @name='Brand']//input[@aria-label='Rolex']")
search.click()
search = driver.find_element(By.XPATH, "//li[@class='x-refine__main__list--value' and @name='Brand']//input[@aria-label='Casio']")
search.click()

def verify_casio_in_results(driver_1):
    results = driver_1.find_elements(By.CSS_SELECTOR, ".s-item__title >span")
    filtered_list = [item for item in results if item.text] #filters empty results
    casio_mismatches = []
    for x, result_ in enumerate(filtered_list[-2:]):
        title = result_.text.lower()
        print(title)
        if "casio" not in title:
            casio_mismatches.append(f"Expected 'Casio' in title {x + 3}, but got '{title}'")
    if casio_mismatches:
        print("Mismatches for Casio:")
        for mismatch in casio_mismatches:
            print(mismatch)
verify_casio_in_results(driver)
driver.quit()