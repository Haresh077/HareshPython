import time
from selenium import webdriver
from Utilities import ExcelReader

driver = webdriver.Chrome(executable_path="D:\Haresh\PythonQA\HareshPython\Drivers\chromedriver.exe")

driver.maximize_window()
driver.get("https://coinbase.hcshub.in/brand/login")

path = ".\\TestData\\Credentials.xlsx"
rows = ExcelReader.getRowCount(path, 'Sheet1')

for r in range(2, rows + 1):
    username = ExcelReader.readdata(path, 'Sheet1', r, 1)
    password = ExcelReader.readdata(path, 'Sheet1', r, 2)
    email = driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-login[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/input[1]").send_keys(username)
    time.sleep(1)
    password1 = driver.find_element_by_xpath("//body/app-root[1]/div[1]/app-login[1]/div[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys(password)
    time.sleep(1)
    signin = driver.find_element_by_xpath("//button[contains(text(),'Sign In')]").click()
    time.sleep(1)
    if driver.title=="Drop For coin":
            print(username,password, "--Login successfully")
            ExcelReader.writedata(path, 'Sheet1', r, 3, 'Test passed')
    else:
        print(username,password,"---Login failed")
        ExcelReader.writedata(path, 'Sheet1', r, 3, 'Test Failed')
    driver.get("https://coinbase.hcshub.in/brand/login")
driver.close()
# driver.back()
