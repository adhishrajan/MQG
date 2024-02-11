import requests
from bs4 import BeautifulSoup
import csv
from time import sleep


base_url = 'https://seekingalpha.com/earnings/earnings-call-transcripts'
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')


link_elements = soup.find_all('a', class_='text-share-text')


links = [element.get('href') for element in link_elements]

links = [link for link in links if 'earnings-call-transcript' in link]
links = ["https://seekingalpha.com" + link for link in links]

print(len(links))



extracted_texts = []

# for link in links:
#     response = requests.get(link)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.text, 'html.parser')
#         target_div = soup.find('div', class_='gk_s4')
#         if target_div:
#             extracted_texts.append(target_div.get_text(strip=True))
#         else:
#             extracted_texts.append("No content found in div.gk_s4")
#     else:
#         extracted_texts.append(f"Failed to fetch content from {link}")

#     sleep(5)

# for text in extracted_texts:
#     print(text)

# csv_file_name = 'transcripts.csv'

# # Open the file in write mode ('w') and create a CSV writer object
# with open(csv_file_name, mode='w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
    
#     # Iterate over your transcripts array
#     for transcript in extracted_texts:
#         # Write each transcript as a new row
#         writer.writerow([transcript])

# for text in extracted_texts:
#     print(text)