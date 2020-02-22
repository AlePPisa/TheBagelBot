#! python3.6

import requests

payload = {'password': 'Gomiloca1', 'username': 'BagelBotAleStephan',
           'user': 'YggytkFbE6BH-g:M1aJKjMaUu45U-M0dvmYBbN3W2Q'}
r = requests.post(r'https://www.reddit.com/api/v1/access_token',data=payload)
print(r.text)
