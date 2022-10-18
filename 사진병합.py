import requests
from PIL import Image  
import os
from img2pdf import convert

# outpath1 == outpath2 == outpath3
outpath1 = "C:\\Users\\kjs\\Desktop"
outpath2 = os.path.dirname(os.path.realpath(__file__))
outpath3 = os.path.dirname(os.path.realpath('__file__'))

with open("complete.pdf", "wb") as f:
	pdf_list = []

	for file in os.listdir(outpath3):
		if file.endswith(".jpg"):
			pdf_list.append(file)

	pdf = convert(pdf_list)
	f.write(pdf)
