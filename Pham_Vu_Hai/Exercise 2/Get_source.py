
import requests

url = "https://khoahoc.vietjack.com/thi-online/bo-15-de-thi-danh-gia-nang-luc-truong-dhqg-hcm-co-dap-an/78521/thi"

cookies = {
    "cross-site-cookie": "bar",
    "Aff": "1688442040.621",
    "XSRF-TOKEN": "eyJpdiI6IkY2dHJ0K05jeFQxVXNDc2VVSVwvWldnPT0iLCJ2YWx1ZSI6IkpqTDZuSWFGTlwvUWdtMDBBWUJJSXNtM0UwZE9JS2o1SU5Ka1dwcUN5WXI0bFdON3VjUVVNTUpsa3ZJMDN5NTRkIiwibWFjIjoiZTNmMDBkNmMxYjY3YmMwOTQ0YjdkZjY2NTY3MjUzOTc5ZmE4ZWI3MzEyZGQwNzAyOTI3MGY1NzdlZDRlMzE2NyJ9",
    "khoahocvietjackcom_session": "eyJpdiI6IjMxMzJZeU80UkVzcDJIMlwvNmVDeDN3PT0iLCJ2YWx1ZSI6Inl0dUgwc09QOEtoWUd0XC92ejZKKzVqQlR3OU5Xb0RwODNTU29aVmNZRzFXNDdiT05ZZkFVMnRMVXdZb3BhQkVjY0RvNjVNWnUrTlwvWHU4WTFrNUhEY3VwaW1jY2NJWTlGVnY0QW9kWHFHVXNFd1M4RE9rdlRNNVpUbWxkVE9wU0kiLCJtYWMiOiIzMTI3ZDE2ZmE5NGVlZGU3MWQ3ZGM4OGVjZWNhYjYxOTFmZGEwYjM5ZmQ0ZjE2MzcwOGJmOGYwNjVmNjgzYzRmIn0%3D",
}

response = requests.get(url, cookies=cookies)

# Save the response to a new file
with open("response.html", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Response saved to response.html")

