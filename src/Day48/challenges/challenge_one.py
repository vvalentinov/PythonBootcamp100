from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(r"user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org")

li_elements = driver.find_elements(By.CSS_SELECTOR, value=".list-widgets .last .shrubbery .menu li")

events = {}
for n in range(len(li_elements)):
    li_element = li_elements[n]
    events[n] = {
        "time": li_element.find_element(By.TAG_NAME, value="time").text,
        "name": li_element.find_element(By.TAG_NAME, value="a").text
    }

print(events)

driver.quit()
