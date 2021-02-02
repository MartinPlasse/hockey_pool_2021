from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome(
    executable_path=r"C:\Users\marti\Downloads\chromedriver_win32\chromedriver.exe"
)

url = "http://www.nhl.com/stats/teams"

driver.get(url)
time.sleep(10)

table_rows = driver.find_elements_by_xpath('//*[@id="root"]/main/div[5]/div[1]/div[2]')
row = driver.find_elements_by_class_name("rt-tr-group")
soup = BeautifulSoup(row, "lxml")

print(soup.prettify())

driver.quit()
