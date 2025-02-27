import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(r"user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

def get_purchase_price(element: WebElement):
    b_element_text = element.find_element(By.TAG_NAME, value="b").text
    price = b_element_text.split(" - ")[1].replace(",", "")
    return float(price)

def check_purchases():
    my_money = float(driver.find_element(By.ID, value="money").text.replace(",", ""))
    all_purchases = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    purchases = [element for element in all_purchases if element.find_elements(By.TAG_NAME, "b")]
    available_purchases = [item for item in purchases if item.get_attribute("class") != "grayed"]
    if len(available_purchases) > 0:
        available_purchases.sort(key=get_purchase_price, reverse=True)
        for purchase in available_purchases:
            if my_money >= get_purchase_price(purchase):
                purchase.click()
                break

quit_timeout = time.time() + 5 * 60
check_purchases_timeout = time.time() + 5
cookie = driver.find_element(By.ID, value="cookie")
while True:
    cookie.click()
    if time.time() >= quit_timeout:
        cookies_per_second_element = driver.find_element(By.ID, value="cps")
        print(f"Cookies per second: {cookies_per_second_element.text}")
        driver.quit()
        break
    if time.time() >= check_purchases_timeout:
        check_purchases()
