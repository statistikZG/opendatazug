import requests
import json

headers = {"accept": "application/json"}
query_params = {
            'jahr': "^20(1[0-9]|2[01])", # matches years in the range 2010-2021
            "typ": "^(Motorräder|Personenwagen)", # matches typ Motorräder or Personenwagen
            "_limit": 100,
            "_offset": 0
           }

r = requests.get("https://data.zg.ch/rowstore/dataset/e7d5d361-7a16-48db-805a-05d5e6a6f7f7", params=query_params, headers=headers)

# check the constructed url
print(r.url)

# print the json response
print(json.dumps(r.json(), indent=4))
