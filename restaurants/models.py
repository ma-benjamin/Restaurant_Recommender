from django.db import models
import requests
import json

# Create your models here.
zipcode = "07039"

url = "https://restaurants-near-me-usa.p.rapidapi.com/restaurants/location/zipcode/" + zipcode + "/"

headers = {
	"X-RapidAPI-Key": "3db43c0fcdmsha2a61395a567ad1p1319a1jsnf749161215d9",
	"X-RapidAPI-Host": "restaurants-near-me-usa.p.rapidapi.com"
}

# response = requests.get(url, headers=headers)

# f = open("./zipcodes/07039.json", 'r')
# data = json.load(f)
# f.close()
# results = data['matching_results']
# for i in range(1, results // 10 + 1):
#     response = requests.get(url + str(i), headers = headers)
#     page = response.json()
#     data['restaurants'] = data['restaurants'] + page['restaurants']

# json_data = json.dumps(data)
# with open("./zipcodes/07039_all.json", 'w') as f:
#     f.write(json_data)