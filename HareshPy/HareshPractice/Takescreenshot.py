from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\Ritu\\PycharmProjects\\HareshPy\\Drivers\\chromedriver.exe")
driver.maximize_window()
path = "D:\\Haresh\\Usersignupdata.xlsx"
driver.get("https://coinbase.hcshub.in/user/registration")
driver.save_screenshot("C:\\Users\\Ritu\\PycharmProjects\\HareshPy\\Images\\image.png")
driver.close()