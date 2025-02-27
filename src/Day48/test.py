from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(r"user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data")
chrome_options.add_argument("--profile-directory=Default")

driver = webdriver.Chrome(options=chrome_options)

# Amazon
# driver.get("https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# Python Website - test
# driver.get("https://www.python.org")
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# docs_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(docs_link.text)
# bug_link = driver.find_element(By.XPATH, value="//*[@id=\"site-map\"]/div[2]/div/ul/li[3]/a")
# print(bug_link.text)

# Wiki
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# anchor = driver.find_element(By.LINK_TEXT, value="Wikiversity")
# anchor.click()
# input = driver.find_element(By.NAME, value="search")
# input.send_keys("Python", Keys.ENTER)

# Newsletter form
# driver.get("https://secure-retreat-92358.herokuapp.com/")
# first_name_input = driver.find_element(By.NAME, value="fName")
# last_name_input = driver.find_element(By.NAME, value="lName")
# email_input = driver.find_element(By.NAME, value="email")
# first_name_input.send_keys("Some First Name Here...")
# last_name_input.send_keys("Some Last Name Here...")
# email_input.send_keys("test@gmail.com")
# button = driver.find_element(By.TAG_NAME, value="button")
# button.click()

# driver.close()
# driver.quit()