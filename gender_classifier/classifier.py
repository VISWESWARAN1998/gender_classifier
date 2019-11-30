# SWAMI KARUPPASWAMI THUNNAI

import requests
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array


class GenderClassifier:


	def __init__(self):
		self.model = load_model("gender_classifier/gender_v2.h5")

	def classify_gender(self, image_path):
		image = load_img(image_path, color_mode="grayscale", target_size=(100, 100))
		image_array = np.array(img_to_array(image)).reshape(1, 100, 100, 1)
		return self.model.predict(image_array)[0][0]
