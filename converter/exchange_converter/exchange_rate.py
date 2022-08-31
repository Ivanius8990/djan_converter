import requests

def exch():

  url = "https://api.apilayer.com/exchangerates_data/latest?base=eur"

  payload = {}
  headers = {
    "apikey": "jyPTa6JhStjFizB47kHFMTeyEKJJRwfk"
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  status_code = response.status_code
  result = response.json()
  return result['rates']

