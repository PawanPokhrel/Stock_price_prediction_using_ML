# import selenium
from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://merolagani.com/CompanyDetail.aspx?symbol=GBIME")
print(driver.title)
