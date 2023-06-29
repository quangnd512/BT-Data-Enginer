import requests
from bs4 import BeautifulSoup
import json

def extract_urls(main_url):
    response = requests.get(main_url)
    soup = BeautifulSoup(response.text, "html.parser")

    urls = set()
    keyword = "de-luyen-thi-ngon-ngu-dhqg-hcm-co-dap-an"

    anchor_tags = soup.find_all("a", href=lambda href: href and keyword in href)
    for i, tag in enumerate(anchor_tags):
        url = tag.get("href")
        if url.startswith("http"):
            if i < 2:
                continue
            url += "/thi"  # Append "/thi" to the extracted URL
            urls.add(url)
            print("Extracted URL:", url)

    return urls

main_url = "https://khoahoc.vietjack.com/thi-online/de-luyen-thi-ngon-ngu-dhqg-hcm-co-dap-an"
urls = extract_urls(main_url)
