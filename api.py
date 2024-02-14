import requests
from bs4 import BeautifulSoup
import csv
import time

csv_file_path = 'data.csv'

symbol = "https://seeking-alpha.p.rapidapi.com/transcripts/v2/list"
headers = {
    "X-RapidAPI-Key": "c9f7c1c3e6msh3c74da27d61c57bp10d5a5jsn6d02057ed4e1",
    "X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
}

res = []
dates = [str(i) for i in range(2000, 2025)]
quarters = ['Q1', 'Q2', 'Q3', 'Q4']

# JPM
jpm_params = {
    'id': 'jpm',
    'size': '40'
}
response = requests.get(symbol, headers=headers, params=jpm_params)
if response.status_code == 200:
    data = response.json()
    for d in data['data']:
        id = d['id']
        date = 'N/A'
        quarter = 'N/A'
        for date_ in dates:
            if date_ in d['attributes']['title']:
                date = date_
        for quarter_ in quarters:
            if quarter_ in d['attributes']['title']:
                quarter = quarter_
        res.append(('jpm', quarter, date, id))
else:
    print("Failed to fetch data:", response.status_code)

# GS
gs_params = {
    'id': 'gs',
    'size': '40'
}
response = requests.get(symbol, headers=headers, params=gs_params)
if response.status_code == 200:
    data = response.json()
    for d in data['data']:
        id = d['id']
        date = 'N/A'
        quarter = 'N/A'
        for date_ in dates:
            if date_ in d['attributes']['title']:
                date = date_
        for quarter_ in quarters:
            if quarter_ in d['attributes']['title']:
                quarter = quarter_
        res.append(('gs', quarter, date, id))
else:
    print("Failed to fetch data:", response.status_code)

# BAC
bac_params = {
    'id': 'bac',
    'size': '40'
}
response = requests.get(symbol, headers=headers, params=bac_params)
if response.status_code == 200:
    data = response.json()
    for d in data['data']:
        id = d['id']
        date = 'N/A'
        quarter = 'N/A'
        for date_ in dates:
            if date_ in d['attributes']['title']:
                date = date_
        for quarter_ in quarters:
            if quarter_ in d['attributes']['title']:
                quarter = quarter_
        res.append(('bac', quarter, date, id))
else:
    print("Failed to fetch data:", response.status_code)

# C
c_params = {
    'id': 'c',
    'size': '40'
}
response = requests.get(symbol, headers=headers, params=c_params)
if response.status_code == 200:
    data = response.json()
    for d in data['data']:
        id = d['id']
        date = 'N/A'
        quarter = 'N/A'
        for date_ in dates:
            if date_ in d['attributes']['title']:
                date = date_
        for quarter_ in quarters:
            if quarter_ in d['attributes']['title']:
                quarter = quarter_
        res.append(('c', quarter, date, id))
else:
    print("Failed to fetch data:", response.status_code)

# MS
ms_params = {
    'id': 'ms',
    'size': '40'
}
response = requests.get(symbol, headers=headers, params=ms_params)
if response.status_code == 200:
    data = response.json()
    for d in data['data']:
        id = d['id']
        date = 'N/A'
        quarter = 'N/A'
        for date_ in dates:
            if date_ in d['attributes']['title']:
                date = date_
        for quarter_ in quarters:
            if quarter_ in d['attributes']['title']:
                quarter = quarter_
        res.append(('ms', quarter, date, id))
else:
    print("Failed to fetch data:", response.status_code)

# BCS
bcs_params = {
    'id': 'bcs',
    'size': '40'
}
response = requests.get(symbol, headers=headers, params=bcs_params)
if response.status_code == 200:
    data = response.json()
    for d in data['data']:
        id = d['id']
        date = 'N/A'
        quarter = 'N/A'
        for date_ in dates:
            if date_ in d['attributes']['title']:
                date = date_
        for quarter_ in quarters:
            if quarter_ in d['attributes']['title']:
                quarter = quarter_
        res.append(('bcs', quarter, date, id))
else:
    print("Failed to fetch data:", response.status_code)

# DB
db_params = {
    'id': 'db',
    'size': '40'
}
response = requests.get(symbol, headers=headers, params=db_params)
if response.status_code == 200:
    data = response.json()
    for d in data['data']:
        id = d['id']
        date = 'N/A'
        quarter = 'N/A'
        for date_ in dates:
            if date_ in d['attributes']['title']:
                date = date_
        for quarter_ in quarters:
            if quarter_ in d['attributes']['title']:
                quarter = quarter_
        res.append(('db', quarter, date, id))
else:
    print("Failed to fetch data:", response.status_code)

# BMO
bmo_params = {
    'id': 'bmo',
    'size': '40'
}
response = requests.get(symbol, headers=headers, params=bmo_params)
if response.status_code == 200:
    data = response.json()
    for d in data['data']:
        id = d['id']
        date = 'N/A'
        quarter = 'N/A'
        for date_ in dates:
            if date_ in d['attributes']['title']:
                date = date_
        for quarter_ in quarters:
            if quarter_ in d['attributes']['title']:
                quarter = quarter_
        res.append(('bmo', quarter, date, id))
else:
    print("Failed to fetch data:", response.status_code)





symbol = "https://seeking-alpha.p.rapidapi.com/transcripts/v2/get-details"
headers = {
    "X-RapidAPI-Key": "c9f7c1c3e6msh3c74da27d61c57bp10d5a5jsn6d02057ed4e1",
    "X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
}

new_res = []

for company, quarter, date, id in res:
    time.sleep(1)
    print(company, quarter, date, id)
    params = {
        'id': id
    }
    response = requests.get(symbol, headers=headers, params=params)
    if response.status_code == 200:
        transcript = response.json()['data']['attributes']['content']
        new_res.append((company, quarter, date, f'"{transcript}"'))
    else:
        print("Failed to fetch data:", response.status_code)

print('Done!')

with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Company', 'Quarter', 'Year', 'Transcript'])
    for row in new_res:
        writer.writerow(row)

# url = "https://seeking-alpha.p.rapidapi.com/transcripts/v2/get-details"
# headers = {
#     "X-RapidAPI-Key": "338b9dfb53msh2b64a076e2958d7p165774jsna4c256032bd7",
#     "X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
# }

# transcripts=[]
# for i in data:
#     params = {
#         'id': i
#     }

#     response = requests.get(url, headers=headers, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         transcripts.append(data['data']['attributess']['content'])
            
#     else:
#         print("Failed to fetch data:", response.status_code)

# from bs4 import BeautifulSoup
# cleaned_transcripts=[]
# # GET CLEANED VERSION OF TRANSCRIPTS
# for i in transcripts:
#     soup = BeautifulSoup(i, 'html.parser')


#     text_only = soup.get_text(separator='\n', strip=True)

#     cleaned_transcripts.append(text_only)


# print(cleaned_transcripts)