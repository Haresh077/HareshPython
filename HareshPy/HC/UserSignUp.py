from excel.Utilities import ExcelReader
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\Haresh\Software\Python Automation\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
path = "D:\\Haresh\\cred.xlsx"
rows = ExcelReader.getRowCount(path, 'Sheet1')
username = ExcelReader.readdata(path, 'Sheet1', 2, 1)
driver.get("https://coinbase.hcshub.in/")
time.sleep(5)
driver.find_element_by_xpath("//a[contains(text(),'Sign in')]").click()
time.sleep(5)
driver.find_element_by_xpath("//button[@routerlink='../user/registration']").click()
time.sleep(5)
Firstname=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/input[1]")
Firstname.send_keys(username)
lastname=driver.find_element_by_xpath("/html/body/app-root/div/app-registration/div/div/form/div/div[5]/div/input")
lastname.send_keys("Sankaliya")
dob=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[6]/div[1]/ng2-flatpickr[1]/div[1]/input[1]")
dob.click()
time.sleep(2)
objmonth=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/span[33]")
selectdate.click()
time.sleep(3)

emailidname="hareshauto3@mailinator.com"

Emailid=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[7]/div[1]/input[1]")
Emailid.send_keys(emailidname)

Gender=Select(driver.find_element_by_xpath("//select[@aria-label='Default select example']"))
Gender.select_by_visible_text("Female")
print("Total number of options in gender field is",len(Gender.options))
# Print all the options
all_options=Gender.options
for option in all_options:
    print(option.text)

time.sleep(3)
country=Select(driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[10]/div[1]/select[1]"))
country.select_by_visible_text("India")

time.sleep(3)
state=Select(driver.find_element_by_xpath("//select[@formcontrolname='state']"))
state.select_by_visible_text("Gujarat")

time.sleep(3)
city=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[11]/div[1]/div[2]/input[1]")
city.send_keys("Ahmedabad")

password=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[12]/div[1]/div[1]/input[1]")
password.send_keys("User@1234")

repassword=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[12]/div[1]/div[2]/input[1]")
repassword.send_keys("User@1234")
time.sleep(20)

signupbtn=driver.find_element_by_xpath("//button[normalize-space()='Sign Up']")
signupbtn.click()
time.sleep(5)
driver.get("https://www.mailinator.com/")

mailisearch=driver.find_element_by_xpath("//input[@id='addOverlay']")
mailisearch.send_keys(emailidname)
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
driver.close()