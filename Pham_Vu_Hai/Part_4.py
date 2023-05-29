import requests
from bs4 import BeautifulSoup
import jsonlines

url = 'https://tuyensinhso.vn/dai-hoc-hoc-vien-theo-khoi.html'

def get_khoi_thi_link(url):
    khoithiLink = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all('a')
    keywords = ["khoi"]
    excluded_keywords = ["ban-tin",
                         "tin-moi",
                         "diem-chuan"]
    for link in links:
        href = link.get('href')
        if href and any(keyword in href for keyword in keywords) and not any(ex_keyword in href for ex_keyword in excluded_keywords):
            khoithiLink.append(href)
    return khoithiLink

result4 = get_khoi_thi_link(url)
print("Đại học, Học viện theo khối: ", result4)
print("------------------------------")

output_file = 'data_4.jsonl'
with jsonlines.open(output_file, mode='w') as writer:
    for link in result4:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")
        title_element = soup.find("h1", class_="detail_title")
        content_element = soup.find("div", class_="detail-content")
        if title_element and content_element:
            title = title_element.text
            content = content_element.text.replace('\n', '')
            writer.write({'title': title, 
                          'content': content, 
                          'url': link})

print("Data saved to", output_file)


