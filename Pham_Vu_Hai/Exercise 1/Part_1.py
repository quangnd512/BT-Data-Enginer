import requests
from bs4 import BeautifulSoup
import jsonlines
import json

url = 'https://tuyensinhso.vn/dai-hoc-hoc-vien.html'

def get_dai_hoc_links(url):
    daihocLink = []
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all('a')
    keywords = ["khu-vuc", "cong-lap", "dan-lap"]
    excluded_keywords = ["ban-tin", "tin-moi", "diem-chuan"]
    for link in links:
        href = link.get('href')
        if href and any(keyword in href for keyword in keywords) and not any(ex_keyword in href for ex_keyword in excluded_keywords):
            daihocLink.append(href)
    return daihocLink

result1 = get_dai_hoc_links(url)
print("Các trường đại học và học viện: ", result1)
print("-----------------------------------------")

output_file = 'data_1.jsonl'
with open(output_file, 'w', encoding='utf-8') as file:
    with jsonlines.Writer(file) as writer:
        for link in result1:
            response = requests.get(link)
            soup = BeautifulSoup(response.content, "html.parser")
            title_element = soup.find("h1", class_="detail_title")
            content_element = soup.find("div", class_="detail-content")
            if title_element and content_element:
                title = title_element.text
                content = content_element.get_text(separator='\n')
                writer.write({'title': title,
                              'content': content,
                              'url': link})
                
print("Data saved to", output_file)
print("----------------------------------------------------------------")

# Load the JSON lines file and convert content to readable markdown format
markdown_data = []
with jsonlines.open(output_file) as file:
    for line in file.iter():
        title = line['title']
        content = line['content']
        url = line['url']
        markdown = f"## {title}\n\n{content}\n\n[Source]({url})\n"
        markdown_data.append(markdown)

# Join all markdown data into a single string
markdown_output = "\n".join(markdown_data)

# Save the markdown output to a new file
output_markdown_file = 'output_1.md'
with open(output_markdown_file, 'w', encoding='utf-8') as file:
    file.write(markdown_output)

print("Data saved to", output_markdown_file)
print("-----------------------------------------")


