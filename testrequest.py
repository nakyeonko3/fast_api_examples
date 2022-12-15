import json
import requests
response = requests.get('https://api.waifu.pics/sfw/waifu')
responseDict= response.json()
print(responseDict['url'])

# 바로 받는 게 아니네?