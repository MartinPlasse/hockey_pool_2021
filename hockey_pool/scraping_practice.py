from bs4 import BeautifulSoup
import requests
# import csv

url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")

gdp_table = soup.find("table", attrs={"class": "wikitable"})
gdp_table_data = gdp_table.tbody.find_all("tr")

headings = []
for td in gdp_table_data[0].find_all("td"):
    headings.append(td.b.text.replace("\n", " ").strip())

data = {}
for table, headings in zip(gdp_table_data[1].find_all("table"), headings):
    t_headers = []
    for th in table.find_all("th"):
        t_headers.append(th.text.replace("\n", " ").strip())

    table_data = []
    for tr in table.tbody.find_all("tr"):
        t_row = {}
        for td, th in zip(tr.find_all("td"), t_headers):
            t_row[th] = td.text.replace("\n", " ").strip()
        table_data.append(t_row)
    data[headings] = table_data


if __name__ == "__main__":
    print(soup.title)

    # print(soup.title.text)
    #
    # for link in soup.find_all("a"):
    #     print(f"Inner text: {link.text}")
    #     print(f"Title: {link.get('title')}")
    #     print(f"href: {link.get('href')}")

    print(data)

    # for topic, table in data.items():
    #     with open(f"{topic}.csv", 'w', encoding='utf8') as out_file:
    #         headers = [
    #             "Country/Territory",
    #             "GDP(US$million)",
    #             "Rank"
    #         ]
    #         writer = csv.DictWriter(out_file, headers)
    #         writer.writeheader()
    #         for row in table:
    #             if row:
    #                 writer.writerow(row)
