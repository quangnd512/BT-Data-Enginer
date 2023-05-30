import requests
from bs4 import BeautifulSoup
import html2markdown

def convert_html_to_markdown(html_content):
    # Remove ads if any
    soup = BeautifulSoup(html_content, 'html.parser')
    ads = soup.find_all(class_='ad')  # Replace 'ad' with the appropriate class name for ads
    for ad in ads:
        ad.decompose()

    # Convert HTML to Markdown
    markdown_content = html2markdown.convert(str(soup))

    return markdown_content

# Provide the URL of the website you want to scrape
url = "https://tuyensinhso.vn/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful (status code 200)
""" 
In the provided code snippet, response.status_code == 200 is used to check if the HTTP response status code is 200, 
which corresponds to a successful request.

HTTP status code 200 indicates that the request was successful and the server responded with the requested resource. 
It is commonly used as a standard code for successful HTTP requests.

By checking if response.status_code == 200, the code ensures that the request to the specified URL was successful 
before proceeding with further actions, such as accessing the HTML content, saving it to a file, or converting it to Markdown.

If the response status code is not 200, it may indicate an error or an unsuccessful request, and appropriate actions 
can be taken based on the specific scenario.
"""
if response.status_code == 200:
    # Access the HTML content of the response
    html_content = response.text

    # Save HTML content to a .txt file
    with open('File_text/html_content.txt', 'w', encoding='utf-8') as file:
        file.write(html_content)

    # Convert HTML content to Markdown
    markdown_content = convert_html_to_markdown(html_content)

    # Save Markdown content to a .txt file
    with open('File_text/markdown_content.txt', 'w', encoding='utf-8') as file:
        file.write(markdown_content)

    print("Conversion completed and files saved.")
else:
    print("Failed to retrieve the website content.")