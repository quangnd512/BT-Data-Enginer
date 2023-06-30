import requests
import re
from bs4 import BeautifulSoup
import json

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


main_url = "https://khoahoc.vietjack.com/trac-nghiem/danh-gia-nang-luc/mon-dh-bach-khoa/hoa-hoc-3"
initial_keywords = ["thi-online"]
extracted_urls = extract_urls(main_url, initial_keywords)

# Continue extracting more links from the sources of extracted URLs
more_keywords = ["hoa-hoc", "dien-li", "dung-dich", "muoi", "halogen", "chlorine", "oxygen", "luu-huynh", "nitrogen", "phosphor", "carbon", "silic", "kim-loai", "aluminium", "chromium", "huu-co", "alkane", "alknene", "ankadien", "ankin", "benzen", "ancol", "phenol", "andehit", "axit", "ester", "lipid", "amine", "amino", "peptide", "protein", "polymer"]
additional_urls = extract_urls_from_sources(extracted_urls, more_keywords)

cookies = {
    # Your cookies here
    "cross-site-cookie": "bar",
    "Aff": "1688442040.621",
    "XSRF-TOKEN": "eyJpdiI6IkY2dHJ0K05jeFQxVXNDc2VVSVwvWldnPT0iLCJ2YWx1ZSI6IkpqTDZuSWFGTlwvUWdtMDBBWUJJSXNtM0UwZE9JS2o1SU5Ka1dwcUN5WXI0bFdON3VjUVVNTUpsa3ZJMDN5NTRkIiwibWFjIjoiZTNmMDBkNmMxYjY3YmMwOTQ0YjdkZjY2NTY3MjUzOTc5ZmE4ZWI3MzEyZGQwNzAyOTI3MGY1NzdlZDRlMzE2NyJ9",
    "khoahocvietjackcom_session": "eyJpdiI6IjMxMzJZeU80UkVzcDJIMlwvNmVDeDN3PT0iLCJ2YWx1ZSI6Inl0dUgwc09QOEtoWUd0XC92ejZKKzVqQlR3OU5Xb0RwODNTU29aVmNZRzFXNDdiT05ZZkFVMnRMVXdZb3BhQkVjY0RvNjVNWnUrTlwvWHU4WTFrNUhEY3VwaW1jY2NJWTlGVnY0QW9kWHFHVXNFd1M4RE9rdlRNNVpUbWxkVE9wU0kiLCJtYWMiOiIzMTI3ZDE2ZmE5NGVlZGU3MWQ3ZGM4OGVjZWNhYjYxOTFmZGEwYjM5ZmQ0ZjE2MzcwOGJmOGYwNjVmNjgzYzRmIn0%3D",
}

for url in additional_urls:
    if re.search(r"/\d+$", url) and not url.endswith("/"):
        url += "/thi"
        print("Additional URL:", url)

    response = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the data and create a dictionary
    data = {
        "url": url,
        "questions": []
    }

    question_items = soup.find_all("div", class_="quiz-answer-item")
    for question_item in question_items:
        try:
            question = {
                "Câu số": question_item.find("div", class_="num").text.strip(),
                "Câu hỏi": question_item.find("div", class_="question-name").text.strip(),
                "Danh sách đáp án": [],
                "Giải thích": question_item.find("div", class_="question-reason").text.strip()
            }

            answer_items = question_item.find_all("div", class_="anwser-item")
            for answer_item in answer_items:
                answer_div = answer_item.find("div")
                if answer_div:
                    result_answer = answer_item.find("input", class_="result-anwser")
                    answer = {
                        "answer": answer_div.text.strip(),
                        "is_correct": result_answer.get("value") == "Y",

                    }
                    question["Danh sách đáp án"].append(answer)

            data["questions"].append(question)

        except AttributeError:
            # Skip the current URL if 'question_item.find' returns None
            print("AttributeError: Skipping URL:", url)
            continue

    # Save the data to a JSON file
    json_file_name = f"De-{url.split('/')[-2]}.json"
    with open(json_file_name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    print("JSON data saved to:", json_file_name)

    # Save the data to a Markdown file
    md_file_name = f"De-{url.split('/')[-2]}.md"
    with open(md_file_name, "w", encoding="utf-8") as file:
        file.write("# Questions\n\n")
        for question in data["questions"]:
            file.write(f"## {question['Câu số']}\n\n")
            file.write(f"**Question:** {question['Câu hỏi']}\n\n")
            file.write("**Answer Options:**\n")
            for i, answer in enumerate(question["Danh sách đáp án"], start=1):
                prefix = "✅" if answer["is_correct"] else "❌"
                file.write(f"{prefix} Option {i}: {answer['answer']}\n")
            file.write(f"\n**Explanation:** {question['Giải thích']}\n\n")
            file.write("---\n\n")

    print("Markdown data saved to:", md_file_name)
    print("-" * 20)