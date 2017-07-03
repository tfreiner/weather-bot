from requests import get
import json
import requests

url = 'https://api.darksky.net/forecast/811e00011c83311213fecbc8c54810d6/38.4726,-90.3978'
summary = get(url).json()['currently']['summary']
high = get(url).json()['daily']['data'][0]['temperatureMax']
precipProbability = get(url).json()['daily']['data'][0]['precipProbability']
precipProbability = precipProbability * 100
text = 'Good morning! Today looks ' + summary + '. There is a ' + str(precipProbability) + ' percent chance of rain and the high will be ' + str(high) + ' degrees.'

bot_id = '69bb60f3a73c7eb8f132000f69'
post_url = 'https://api.groupme.com/v3/bots/post?bot_id=' + bot_id + '&text=' + text 
#r = requests.post(post_url)
