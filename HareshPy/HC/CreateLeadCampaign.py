import time

import pyautogui as pyautogui
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Haresh\Software\Python Automation\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://coinbase.hcshub.in/brand/login")
email = driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-login[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys("hareshbrand@yopmail.com")
time.sleep(1)
password1 = driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-login[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys("Brand@123")
time.sleep(1)
signin = driver.find_element_by_xpath("//button[contains(text(),'Sign In')]").click()
time.sleep(1)
#New Campaign
newcampaign=driver.find_element_by_xpath("//a[contains(text(),'New Campaign')]")
newcampaign.click()
#selectlead
selectlead=driver.find_element_by_xpath("//button[@id='Lead']").click()
#Nextbtn
nextbtn=driver.find_element_by_xpath("//i[@class='fa fa-long-arrow-right']")
nextbtn.click()
time.sleep(5)
#browse
time.sleep(2)
browsers=driver.find_element_by_xpath("//i[@class='fa fa-camera']")
browsers.click()
pyautogui.click(x=227, y=417)
time.sleep(2)
pyautogui.write("Sample.jpg")
pyautogui.click(x=488, y=447)
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#Total Budget
Totalbudget=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-campaign-target[1]/div[1]/div[1]/div[1]/div[1]/app-create-campaign[1]/div[1]/form[1]/div[1]/div[3]/div[1]/div[1]/input[1]")
Totalbudget.send_keys("100")
time.sleep(2)
startdate= driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-campaign-target[1]/div[1]/div[1]/div[1]/div[1]/app-create-campaign[1]/div[1]/form[1]/div[1]/div[3]/div[5]/div[1]/div[1]/div[1]/ngx-datepicker[1]/div[1]/input[1]")
startdate.click()
time.sleep(2)

selectdate=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-campaign-target[1]/div[1]/div[1]/div[1]/div[1]/app-create-campaign[1]/div[1]/form[1]/div[1]/div[3]/div[5]/div[1]/div[1]/div[1]/ngx-datepicker[1]/div[1]/div[1]/div[2]/div[2]/span[10]")
selectdate.click()
time.sleep(2)
enddate=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-campaign-target[1]/div[1]/div[1]/div[1]/div[1]/app-create-campaign[1]/div[1]/form[1]/div[1]/div[3]/div[5]/div[1]/div[2]/div[1]/ngx-datepicker[1]/div[1]/input[1]")
enddate.click()
time.sleep(2)
selectenddate=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-campaign-target[1]/div[1]/div[1]/div[1]/div[1]/app-create-campaign[1]/div[1]/form[1]/div[1]/div[3]/div[5]/div[1]/div[2]/div[1]/ngx-datepicker[1]/div[1]/div[1]/div[2]/div[2]/span[12]")
selectenddate.click()
time.sleep(2)
campname=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-campaign-target[1]/div[1]/div[1]/div[1]/div[1]/app-create-campaign[1]/div[1]/form[1]/div[1]/div[3]/div[6]/div[1]/input[1]")
campname.send_keys("SH_Lead_Auto")
time.sleep(2)
prodinfo=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-campaign-target[1]/div[1]/div[1]/div[1]/div[1]/app-create-campaign[1]/div[1]/form[1]/div[1]/div[3]/div[7]/div[1]/textarea[1]")
prodinfo.send_keys("Test product information")
time.sleep(2)
nextbtn=driver.find_element_by_xpath("//button[normalize-space()='Next']")
nextbtn.click()
time.sleep(2)
window_before = driver.window_handles[0]
print(window_before)
pyautogui.click(x=1121, y=724)
time.sleep(1)
pyautogui.click(x=1121, y=724)
time.sleep(1)
pyautogui.click(x=1121, y=724)
time.sleep(4)
driver.implicitly_wait(3)
window_after = driver.window_handles[1]
driver.switch_to_window(window_after)
print(window_after)
driver.maximize_window()
driver.find_element_by_id("email").send_keys("sb-43cblu7503636@personal.example.com")
time.sleep(1)
driver.find_element_by_id("btnNext").click()
time.sleep(3)
driver.find_element_by_id("password").send_keys("m&m8Y#F6")
time.sleep(2)
driver.find_element_by_id("btnLogin").click()
time.sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
driver.find_element_by_id("payment-submit-btn").click()
time.sleep(2)
#Click on my campaign
driver.switch_to.window(window_before)
driver.find_element_by_xpath("//button[normalize-space()='My campaigns']").click()
time.sleep(2)



