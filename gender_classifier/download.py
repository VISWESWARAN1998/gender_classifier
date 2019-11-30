# SWAMI KARUPPASWAMI THUNNAI

import requests

def latest_model():
	r = requests.get("", stream=True)
	with open("gender_classifier/gender_v5.json", "wb") as file:
		count = 1
		for i in r.iter_content(chunk_size=1024):
			print("Downloading chunk {}".format(count))
			count += 1
			file.write(i)
