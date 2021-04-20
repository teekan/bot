from selenium import webdriver
import time, os
from selenium.webdriver.firefox.options import Options
opts = Options()
opts.headless = True
path = os.getcwd()+"/geckodriver"
driver = webdriver.Firefox(options=opts,executable_path=path)
driver.get("http://www.slutbags.tk")
ads = driver.find_elements_by_tag_name("iframe")
ads[0].click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[1])
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollTo(0,0)")
time.sleep(1)
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(1)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
driver.execute_script("window.scrollTo(0,0)")
time.sleep(1)
driver.close()
