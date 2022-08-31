import requests
from django import forms

url = "https://api.apilayer.com/exchangerates_data/latest?base=eur"
headers = {"apikey": "jyPTa6JhStjFizB47kHFMTeyEKJJRwfk"}
response = requests.request("GET", url, headers=headers)
status_code = response.status_code
result = response.json()
result=result['rates']
print(result)


CHOICES=()
for key in result:
    CHOICES+=(key,key),

class CurencyForm(forms.Form):

    cur_amount = forms.IntegerField(label='количество',widget=forms.NumberInput(attrs={'class':"form-control form-control-sm"}))
    first_cur = forms.ChoiceField(label='вторая валюта',widget=forms.Select(attrs={'class':"form-select form-select-sm"}),choices = CHOICES)
    second_cur = forms.ChoiceField(label='вторая валюта',widget=forms.Select(attrs={'class':"form-select form-select-sm"}),choices = CHOICES)