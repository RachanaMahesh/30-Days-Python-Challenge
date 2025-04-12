from urllib.request import urlopen
import json

# import requests
# source = requests.get("http://api.currencylayer.com/live?access_key=38039657d836512d51ba10b5261c9007").text

with urlopen("http://api.currencylayer.com/live?access_key=38039657d836512d51ba10b5261c9007") as response:
    source = response.read()

# print(source)
data = json.loads(source)
# print(json.dumps(data,indent=2))
print(len(data['quotes']))
# print(data['quotes'])
item =  data['quotes']
print(item['USDAFN'])

# yt example below 
# import json
# from urllib.request import urlopen

# with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
#     source = response.read()

# data = json.loads(source)
# print(json.dumps(data, indent=2))
# usd_rates = dict()

# for item in data['list']['resources']:
#     name = item['resource']['fields']['name']
#     price = item['resource']['fields']['price']
#     usd_rates[name] = price

# print(50 * float(usd_rates['USD/EUR']))
# print(50 * float(usd_rates['USD/INR']))