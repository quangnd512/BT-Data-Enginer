import requests
from bs4 import BeautifulSoup
import json

url = "https://khoahoc.vietjack.com/thi-online/bo-15-de-thi-danh-gia-nang-luc-truong-dhqg-hcm-co-dap-an/79126/thi"

cookies = {
    "cross-site-cookie": "bar",
    "Aff": "1688442040.621",
    "XSRF-TOKEN": "eyJpdiI6IkY2dHJ0K05jeFQxVXNDc2VVSVwvWldnPT0iLCJ2YWx1ZSI6IkpqTDZuSWFGTlwvUWdtMDBBWUJJSXNtM0UwZE9JS2o1SU5Ka1dwcUN5WXI0bFdON3VjUVVNTUpsa3ZJMDN5NTRkIiwibWFjIjoiZTNmMDBkNmMxYjY3YmMwOTQ0YjdkZjY2NTY3MjUzOTc5ZmE4ZWI3MzEyZGQwNzAyOTI3MGY1NzdlZDRlMzE2NyJ9",
    "khoahocvietjackcom_session": "eyJpdiI6IjMxMzJZeU80UkVzcDJIMlwvNmVDeDN3PT0iLCJ2YWx1ZSI6Inl0dUgwc09QOEtoWUd0XC92ejZKKzVqQlR3OU5Xb0RwODNTU29aVmNZRzFXNDdiT05ZZkFVMnRMVXdZb3BhQkVjY0RvNjVNWnUrTlwvWHU4WTFrNUhEY3VwaW1jY2NJWTlGVnY0QW9kWHFHVXNFd1M4RE9rdlRNNVpUbWxkVE9wU0kiLCJtYWMiOiIzMTI3ZDE2ZmE5NGVlZGU3MWQ3ZGM4OGVjZWNhYjYxOTFmZGEwYjM5ZmQ0ZjE2MzcwOGJmOGYwNjVmNjgzYzRmIn0%3D",
}

response = requests.get(url, cookies=cookies)
soup = BeautifulSoup(response.text, "html.parser")

# Extract the data and create a dictionary
data = {
    "url": url,
    "questions": []
}

question_items = soup.find_all("div", class_="quiz-answer-item")
for question_item in question_items:
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
            answer = {
                "answer": answer_div.text.strip(),
                "is_correct": answer_item.find("span").get("title") == "Đáp án đúng"
            }
            question["Danh sách đáp án"].append(answer)
    
    data["questions"].append(question)

# Save the data to a JSON file
with open("De-79126.json", "w", encoding= "utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print("Data saved")

