import os
import glob


def TimKiem(root_dir, ext):
 return glob.glob(os.path.join(
 root_dir, f'**/*{ext}'), recursive=True)


folder = r"C:\Users\vvn20206205\Desktop\solutions"
files = TimKiem(folder, '.md')
for f in files:
 print(f)


# import requests
# from bs4 import BeautifulSoup

# url = "https://ddd-practitioners.com/home/glossary/"
# response = requests.get(url)

# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     html_content = response.content

#     # Parse the HTML content
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Extract text and links
#     entries = soup.find_all('a')
#     for entry in entries:
#         text = entry.get_text(strip=True)
#         link = entry['href']
#         print(f"Text: {text}\nLink: {link}\n")
# else:
#     print(f"Failed to retrieve content. Status Code: {response.status_code}")
