import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from googlesearch import search


def is_wipo(url):
    """
    Determines whether a certain url is from the patentscope website
    """
    if "patentscope.wipo.int" in url:
        return True
    return False


# Not used in current workflow
def contains_name(htmlelement, name):
    """
    Determines whether a certain html element contains a certain
    applicant's name string
    """
    if name in htmlelement:
        return True
    return False




def lookup_pool(contender_name):
            webpage = requests.get(url)
            soup = BeautifulSoup(webpage.content, "html.parser")
            elements = soup.find_all(attrs={"class": "biblio-person-list--name"})

            # 3. Extract the applicant name text from the html element
            for element in elements:
                shaved_element = re.findall(r"(?:<.*>\w+)(.*)", str(element))
                if fuzz.token_sort_ratio(shaved_element, english_name) >= 88:
                    text = element.get_text()

                    chinese_name = ""
                    for character in range(len(text)):
                        if detect_chinese(text[character]) is True:
                            chinese_name += text[character]

                    if chinese_name == "":
                        chinese_name = None
                    break
            else:
                continue
            return chinese_name


if __name__ == "__main__":
    # test1 = lookup_chinese("QIQIHAR RAILWAY ROLLING STOCK CO LTD")