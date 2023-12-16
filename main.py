from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASS = os.getenv("PASS")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")

time.sleep(5)
login_btn = driver.find_element(By.XPATH, value='//*[@id="u-1919424827"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_btn.click()

time.sleep(5)
login_fb_btn = driver.find_element(By.XPATH, value='//*[@id="u647161393"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button')
login_fb_btn.click()

time.sleep(7)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
email_bar = driver.find_element(By.NAME, value="email")
email_bar.send_keys(EMAIL)

pass_bar = driver.find_element(By.NAME, value="pass")
pass_bar.send_keys(PASS)

submit_btn = driver.find_element(By.NAME, value="login")
submit_btn.click()

driver.switch_to.window(base_window)

time.sleep(5)
allow_cookies = driver.find_element(By.XPATH, value='//*[@id="u647161393"]/main/div[2]/div/div/div[1]/div[1]/button')
allow_cookies.click()

time.sleep(4)
allow_loc = driver.find_element(By.XPATH, value='//*[@id="u647161393"]/main/div/div/div/div[3]/button[1]')
allow_loc.click()

time.sleep(4)
dismiss_notif = driver.find_element(By.XPATH, value='//*[@id="u647161393"]/main/div/div/div/div[3]/button[2]')
dismiss_notif.click()

for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.ARROW_RIGHT)

driver.quit()