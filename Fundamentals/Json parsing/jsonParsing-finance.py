import json
import pandas as pd
import requests

# src = requests.get("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json")

data = json.load(src.text)

with open('finance.json', 'w') as wf:
    data = json.load(data, wf, indent=2)

print(data)
