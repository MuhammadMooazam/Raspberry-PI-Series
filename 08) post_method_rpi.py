import requests

url = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update'

data1 = {
    'api_key': '9UCLDBXSK07CD8UH',
    'status': 'Good evening form Raspberry PI'
    }

x = requests.post(url, data = data1)

print(x.text)