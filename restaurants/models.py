from django.db import models
import requests
import pandas as pd

# Create your models here.
headers = {
	"X-RapidAPI-Key": "3db43c0fcdmsha2a61395a567ad1p1319a1jsnf749161215d9",
	"X-RapidAPI-Host": "restaurants-near-me-usa.p.rapidapi.com"
}

# response = requests.get(url, headers=headers)

def search_restaurants(zip):
	# request first page of restaurants
	url = "https://restaurants-near-me-usa.p.rapidapi.com/restaurants/location/zipcode/" + zip + "/"
	response = requests.get(url + "0", headers=headers)
	data = response.json()
	
	# if there are more pages, request those pages
	try:
		results = data['matching_results']
		for i in range(1, results // 10 + 1):
			response = requests.get(url + str(i), headers = headers)
			page = response.json()
			data['restaurants'] = data['restaurants'] + page['restaurants']

		# save list in json
		df = data['restaurants']
		df.to_csv("./restaurants/zipcodes/" + zip + ".csv", index=False)
	except:
		print("no pages")

def add_review(zip, id, review):
	zip_path = "./restaurants/zipcodes/" + zip + ".csv"
	df = pd.read_csv(zip_path)
	res_id = int(id)
	rest_review = df.loc[df['id'] == res_id, 'review']
	print(review)
	print(type(rest_review))
	print(rest_review == review)
	if rest_review.any() == review:
		df.loc[df['id'] == int(id), 'review'] = 0
	else:
		df.loc[df['id'] == int(id), 'review'] = review
	df = df.sort_values(by=['review'], ascending=False)
	df.to_csv(zip_path, index=False)

# zip = "07039"
# zip_path = "./zipcodes/" + zip + ".csv"
# df = pd.read_csv(zip_path)
# df.to_csv(zip_path, index=False)
# print(df)
# add_review(zip, 0, 2)