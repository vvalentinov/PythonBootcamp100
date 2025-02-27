from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(r"user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# anchor = driver.find_element(By.XPATH, value="//*[@id=\"articlecount\"]/ul/li[2]/a[1]")
# print(anchor.text)

anchor = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")[1]
anchor.click()

driver.quit()