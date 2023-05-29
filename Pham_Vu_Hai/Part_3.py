import requests
from bs4 import BeautifulSoup
import jsonlines

url = 'https://tuyensinhso.vn/nhom-nganh-dao-tao.html'

def get_nganh_dao_tao_link(url):
    nganhdaotaoLink = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all('a')
    keywords = ["nhom-nganh-dao-tao"]
    excluded_keywords = ["ban-tin",
                         "tin-moi",
                         "diem-chuan"]
    for link in links:
        href = link.get('href')
        if href and any(keyword in href for keyword in keywords) and not any(ex_keyword in href for ex_keyword in excluded_keywords):
            nganhdaotaoLink.append(href)
    return nganhdaotaoLink

result3 = get_nganh_dao_tao_link(url)
print("Các ngành đào tạo: ", result3)

output_file = 'data_3.jsonl'
with jsonlines.open(output_file, mode='w') as writer:
    for link in result3:
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

 
