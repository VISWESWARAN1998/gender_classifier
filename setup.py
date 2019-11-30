# SWAMI KARUPPASWAMI THUNNAI

import setuptools

def read():
	with open("ReadMe.md", "r") as file:
		content = file.read()
	return content

setuptools.setup(
     name="gender_classifier",  
     version="1.0",
     author="Visweswaran N",
     author_email="visweswaran.nagasivam98@gmail.com",
     description="A simple gender classifier",
     long_description=read(),
     long_description_content_type="text/markdown",
     url="https://gender-classifier.visweswaran.com",
     packages=["gender_classifier"],
     install_requires=["numpy", "tensorflow", "keras"],
     include_package_data=True,
     data_files = [('', ['gender_classifier/gender_v2.h5'])],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ]
 )
