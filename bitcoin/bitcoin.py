import requests
import json
import sys

if len(sys.argv) !=2:
    raise Exception("Missing command-line argument")
    sys.exit()

try:
    bitcoins = float(sys.argv[1])
except:
    print("Command-line argument is not a number")
    sys.exit(1)

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
#print(type(response))
response = response.json()
#print(type(response))
# print(dir(response))
# print(response)
# response = response.text
# print(response)
#response = json.dumps(response.json(), indent=3)
price = response['bpi']['USD']['rate'].replace(",","")

try:
    price = float(price)
except requests.RequestException:
    pass

cost = bitcoins * price
print(f'${cost:,.4f}') #format 4 decimal places and commas too