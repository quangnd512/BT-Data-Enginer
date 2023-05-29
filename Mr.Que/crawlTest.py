import requests
from bs4 import BeautifulSoup

# Define the starting URL
url = 'https://tuyensinhso.vn/'

# Make a request to the URL
response = requests.get(url)

# Parse the HTML response
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Print the links
for link in links:
    print(link['href'])
