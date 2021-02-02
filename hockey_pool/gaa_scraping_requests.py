from bs4 import BeautifulSoup
import requests


url = "http://www.nhl.com/stats/teams"

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")

team_stats = soup.find_all("div", attrs={"class": "rt-tr-group"})

print(soup.prettify())
# 
# data = {}
# for table, headings in zip(gdp_table_data[1].find_all("table"), headings):
#     t_headers = []
#     for th in table.find_all("th"):
#         t_headers.append(th.text.replace("\n", " ").strip())
# 
#     table_data = []
#     for tr in table.tbody.find_all("tr"):
#         t_row = {}
#         for td, th in zip(tr.find_all("td"), t_headers):
#             t_row[th] = td.text.replace("\n", " ").strip()
#         table_data.append(t_row)
#     data[headings] = table_data


# //*[@id="root"]/main/div[5]/div[1]/div[2]/div[1]/div/div[17]
