from Utilities import ExcelReader
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Haresh\PythonAutomation\Drivers\\chromedriver.exe")
driver.maximize_window()
path = "/TestData/Usersignupdata.xlsx"
rows = ExcelReader.getRowCount(path, 'Sheet1')
for r in range(2, rows + 1):
    FirstName = ExcelReader.readdata(path, 'Sheet1', r, 1)
    LastName = ExcelReader.readdata(path, 'Sheet1', r, 2)
    DateofBirth = ExcelReader.readdata(path, 'Sheet1', r, 3)
    EmailIDforlogin = ExcelReader.readdata(path, 'Sheet1', r, 4)
    Phonenumber = ExcelReader.readdata(path, 'Sheet1', r, 5)
    Genderexcel = ExcelReader.readdata(path, 'Sheet1', r, 6)
    Countryexcel = ExcelReader.readdata(path, 'Sheet1', r, 7)
    State = ExcelReader.readdata(path, 'Sheet1', r, 8)
    City = ExcelReader.readdata(path, 'Sheet1', r, 9)
    Password = ExcelReader.readdata(path, 'Sheet1', r, 10)
    Confirmpassword = ExcelReader.readdata(path, 'Sheet1', r, 11)
    driver.get("https://coinbase.hcshub.in/user/registration")
    driver.save_screenshot("image.png")

#time.sleep(5)
#driver.find_element_by_xpath("//a[contains(text(),'Sign in')]").click()
#time.sleep(5)
#driver.find_element_by_xpath("//button[@routerlink='../user/registration']").click()
#time.sleep(5)

    # Firstname
    Firstname=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[4]/div[1]/input[1]")
    Firstname.send_keys(FirstName)
    # LastName
    lastname=driver.find_element_by_xpath("/html/body/app-root/div/app-registration/div/div/form/div/div[5]/div/input")
    lastname.send_keys(LastName)
    # DateofBirth
    dob = driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[6]/div[1]/ng2-flatpickr[1]/div[1]/input[1]")
    dob.click()
    time.sleep(2)
    objmonth = Select(driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/select"))
    objmonth.select_by_visible_text("March")
    time.sleep(3)
#   # EmailID
    Emailid = driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[7]/div[1]/input[1]")
    Emailid.send_keys(EmailIDforlogin)
    time.sleep(2)
    #Gender
    Gender=driver.find_element_by_xpath("//select[@aria-label='Default select example']")
    Gender.send_keys(Genderexcel)
    time.sleep(3)
    #Country
    country = driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[10]/div[1]/select[1]")
    country.send_keys(Countryexcel)
    time.sleep(3)
    #State
    state=driver.find_element_by_xpath("//select[@formcontrolname='state']")
    state.send_keys(State)
    time.sleep(3)
    # CITY
    city = driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[11]/div[1]/div[2]/input[1]")
    city.send_keys(City)
    time.sleep(2)
    # Password
    password = driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[12]/div[1]/div[1]/input[1]")
    password.send_keys(Password)
    # ConfirmPassword
    repassword = driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[12]/div[1]/div[2]/input[1]")
    repassword.send_keys(Confirmpassword)
    time.sleep(2)
    # Signupbtn
    signupbtn = driver.find_element_by_xpath("//button[normalize-space()='Sign Up']")
    signupbtn.click()
    time.sleep(4)
    driver.refresh()
'''
dob=driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-registration[1]/div[1]/div[1]/form[1]/div[1]/div[6]/div[1]/ng2-flatpickr[1]/div[1]/input[1]")
dob.click() #DateofBirth
selectdate=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/span[33]")
selectdate.click()
time.sleep(3)
emailidname="hareshauto3@mailinator.com"
'''

'''
print("Total number of options in gender field is",len(Gender.options))
# Print all the options
all_options=Gender.options
for option in all_options:
    print(option.text)
'''

'''

   driver.get("https://www.mailinator.com/")
mailisearch=driver.find_element_by_xpath("//input[@id='addOverlay']")
mailisearch.send_keys(emailidname)
time.sleep(5)
...
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

'''

driver.close()