from selenium import webdriver
import time

driver = webdriver.Edge(
    executable_path=r"C:\Users\marti\Downloads\edgedriver_win641\msedgedriver.exe"
)

url = "http://www.nhl.com/stats/teams"

driver.get(url)
time.sleep(10)

table_rows = driver.find_elements_by_css_selector("#root > main > div.ReactTable.-striped.-highlight.rthfc-kkh9slcs.rthfc.-sp > div.rt-table > div.rt-tbody")

# row = table_rows.find_elements_by_tag_name('div')
for div in table_rows:
    print(div.text)

driver.quit()
