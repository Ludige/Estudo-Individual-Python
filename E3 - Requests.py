import requests

proxies = {
    # 'https': 'https://140.227.69.170:6000'
}

url = "https://ipinfo.io/json"

response = requests.get(url, proxies=proxies)
print(response.json())
print(response.json()['city'])
