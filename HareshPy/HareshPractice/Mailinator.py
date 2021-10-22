import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Ritu\\PycharmProjects\\pythonProject1\\Drivers\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.mailinator.com/")

mailisearch=driver.find_element_by_xpath("//input[@id='addOverlay']")
mailisearch.send_keys("hareshauto")
time.sleep(5)

gobutton = driver.find_element_by_xpath("//button[@id='go-to-public']")
gobutton.click()
time.sleep(7)

driver.find_element_by_xpath("//td[contains(text(),'Dropforcoin-User Activation link')]").click()
time.sleep(5)

emlbody = driver.find_element_by_id("html_msg_body")
driver.switch_to.frame(emlbody)
time.sleep(4)
actbtn=driver.find_element_by_xpath("/html/body/table/tbody/tr/td/div[3]/div/div/div/div/div/div[5]/a/span/span/strong")
actbtn.click()