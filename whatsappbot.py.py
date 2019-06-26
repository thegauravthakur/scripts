from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://web.whatsapp.com')
driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div/div/div/div[2]/div[1]/div[1]/span/span').click()
text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
text_box.clear()
count = 1
while count < 1000:
    text_box.send_keys("Hello Mr. Anup!! This is message no. : ", count, Keys.RETURN)
    count = count + 1
    time.sleep(2)
driver.close()
