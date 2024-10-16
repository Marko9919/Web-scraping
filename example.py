import requests
from bs4 import BeautifulSoup
import re


def scrape(web_page):
    r = requests.get(web_page)
    soup = BeautifulSoup(r.text, "html.parser")
    title = soup.find('title')

    logo_text = title.string.strip()
    print("Logo Text:",logo_text)

    phone_num = None
    phone_num_patterns = re.compile(r'\+\d[\d\s\-(\)]{7,}')

    for element in soup.find_all(string=True):
        match = phone_num_patterns.search(element)
        if match:
            phone_num = match.group()
            break

    if phone_num:
        print("Phone number:",phone_num)
    else:
        print("Phone number not found")


def main():
    web_page1 = "https://www.menisk.hr/"
    web_page2 = "https://tpp.hr/"
    web_page3 = "https://africau.edu/"

    # Select one web page to pass to a function
    scrape(web_page1)


if __name__ == '__main__':
    main()