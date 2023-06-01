import requests
from bs4 import BeautifulSoup
import jsonlines
import html2text

url = 'https://tuyensinhso.vn/cao-dang.html'

def get_cao_dang_link(url):
    caodangLink = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all('a')
    keywords = ["cd",
                "dan-lap",
                "cong-lap",
                "khu-vuc",
                "hot"]
    excluded_keywords = ["ban-tin",
                         "tin-moi",
                         "diem-chuan",
                         "cdn-cgi",
                         "Protection"]
    for link in links:
        href = link.get('href')
        if href and any(keyword in href for keyword in keywords) and not any(ex_keyword in href for ex_keyword in excluded_keywords):
            caodangLink.append(href)
    return caodangLink

result2 = get_cao_dang_link(url)
print("Các trường cao đẳng: ", result2)
print("------------------------------")

output_file = 'data_2.jsonl'
with jsonlines.open(output_file, mode='w') as writer:
    for link in result2:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, "html.parser")
        title_element = soup.find("h1", class_="detail_title")
        content_element = soup.find("div", class_="detail-content")
        if title_element and content_element:
            title = title_element.text
            content = content_element.encode_contents().decode()
            converter = html2text.HTML2Text()
            converter.body_width = 0
            markdown_content = converter.handle(content)
            writer.write({'title': title, 
                          'content': markdown_content, 
                          'url': link})

print("Data saved to", output_file)
print("----------------------------------------------------------------")
            
markdown_data = []
with jsonlines.open(output_file) as file:
    for line in file.iter():
        title = line['title']
        content = line['content']
        url = line['url']
        markdown = f"## {title}\n\n{content}\n\n[Source]({url})\n"
        markdown_data.append(markdown)

markdown_output = "\n".join(markdown_data)

output_markdown_file = 'output_2.md'
with open(output_markdown_file, 'w', encoding='utf-8') as file:
    file.write(markdown_output)

print("Data saved to", output_markdown_file)
print("-----------------------------------")



print("Data saved to", output_file)


