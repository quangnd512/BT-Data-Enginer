import requests
import re
from bs4 import BeautifulSoup

def extract_urls(main_url, keywords):
    response = requests.get(main_url)
    soup = BeautifulSoup(response.text, "html.parser")

    urls = set()

    for keyword in keywords:
        anchor_tags = soup.find_all("a", href=lambda href: href and keyword in href)
        for i, tag in enumerate(anchor_tags):
            url = tag.get("href")
            if url.startswith("http") and i >= 2:
                urls.add(url)

    return urls


def extract_urls_from_sources(urls, keywords):
    extracted_urls = set()

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        for keyword in keywords:
            anchor_tags = soup.find_all("a", href=lambda href: href and keyword in href)
            for i, tag in enumerate(anchor_tags):
                url = tag.get("href")
                if url.startswith("http") and i >= 2:
                    extracted_urls.add(url)

    return extracted_urls


main_url = "https://khoahoc.vietjack.com/trac-nghiem/danh-gia-nang-luc/mon-dhqg-ho-chi-minh/tieng-anh"
initial_keywords = ["thi-online"]
extracted_urls = extract_urls(main_url, initial_keywords)

# Continue extracting more links from the sources of extracted URLs
more_keywords = ["thi-hien-tai", "thi-qua-khu", "thi-tuong-lai", "cac-dang-thuc", "cau", "menh-de", "tu", "doc-hieu"]
additional_urls = extract_urls_from_sources(extracted_urls, more_keywords)

# Print the additional extracted URLs ending with a forward slash and a number
for url in additional_urls:
    if re.search(r"/\d+$", url) and not url.endswith("/"):
        print("Additional URL:", url)
