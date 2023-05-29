import requests
from bs4 import BeautifulSoup
import jsonlines

url = 'https://tuyensinhso.vn/diem-chuan/diem-chuan-cac-truong-dai-hoc-hoc-vien-khu-vuc-mien-trung-c48009.html'

def get_diem_chuan_mien_trung_link(url):
    diemchuanmientrungLink = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all('a')
    keywords = ["diem-chuan"]
    excluded_keywords = ["ban-tin",
                         "tin-moi"]
    for link in links:
        href = link.get('href')
        if href and any(keyword in href for keyword in keywords) and not any(ex_keyword in href for ex_keyword in excluded_keywords):
            diemchuanmientrungLink.append(href)
    return diemchuanmientrungLink

result5_2 = get_diem_chuan_mien_trung_link(url)
print("Điểm chuẩn khu vực miền trung: ", result5_2)
print("------------------------------")

output_file = 'data_5_2.jsonl'
with jsonlines.open(output_file, mode='w') as writer:
    for link in result5_2:
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


