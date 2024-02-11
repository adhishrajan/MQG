import requests

symbol = "https://seeking-alpha.p.rapidapi.com/transcripts/v2/list"
headers = {
    "X-RapidAPI-Key": "338b9dfb53msh2b64a076e2958d7p165774jsna4c256032bd7",
    "X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
}

params = {
    'id': 'aapl'
}

response = requests.get(symbol, headers=headers, params=params)
ids = []
if response.status_code == 200:
    data = response.json()
    for d in data['data']:
        ids.append(d['id'])

else:
    print("Failed to fetch data:", response.status_code)




url = "https://seeking-alpha.p.rapidapi.com/transcripts/v2/get-details"
headers = {
    "X-RapidAPI-Key": "338b9dfb53msh2b64a076e2958d7p165774jsna4c256032bd7",
    "X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
}

for i in ids:
    params = {
        'id': i
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print("Failed to fetch data:", response.status_code)

