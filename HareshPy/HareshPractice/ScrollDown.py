from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="D:\Haresh\Software\Python Automation\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://en.wikipedia.org")
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
driver.close()