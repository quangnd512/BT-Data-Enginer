import requests
from bs4 import BeautifulSoup
import jsonlines

url = 'https://tuyensinhso.vn/dai-hoc-hoc-vien.html'

def get_link(url):
    daihoc_link = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all('a')
    keywords = ["khu-vuc", "cong-lap", "dan-lap"]
    excluded_keywords = ["ban-tin", "tin-moi", "diem-chuan"]
    for link in links:
        href = link.get('href')
        if href and any(keyword in href for keyword in keywords) and not any(ex_keyword in href for ex_keyword in excluded_keywords):
            daihoc_link.append(href)
    return daihoc_link

result1 = get_link(url)
print("Các trường đại học và học viện: ",result1)
print("-----------------------------------------")

output_file = 'data.jsonl'
with jsonlines.open(output_file, mode='w') as writer:
    for link in result1:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")
        title_element = soup.find("h1", class_="detail_title")
        content_element = soup.find("div", class_="detail-content")
        if title_element and content_element:
            title = title_element.text
            content = content_element.text
            writer.write({'title': title, 'content': content, 'url': link})

print("Data saved to", output_file)