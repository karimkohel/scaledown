#!/usr/bin/env python3
import cv2
import sys

########## init ##########

helpString = """
pyramid is a simple program to scale down images

USAGE : pyramids <image to scale down> [options]

OPTIONS :
	-n <path or name to produced image>
			the name or path of the produced image

	-t <number of times to scale down>
			the programe will scale down the image by a factor of 1/2 the number of times specified
"""

########## FX ##########

def check_input():
	if sys.argv[1] == "--help":
		print(helpString)
		sys.exit()

	elif 2 > len(sys.argv) > 4:
		print("Usage : pyramids <image to scale down> [options]")
		print("for help use the --help flag")
		sys.exit()

def check_times():
	if "-t" in sys.argv:
		index = sys.argv.index("-t") + 1
		return sys.argv[index]
	else:
		return 0

def check_name():
	try:
		filename, extention = sys.argv[1].split(".")
	except Exception:
		print("Error loading image")
		sys.exit()
	else:
		if "-n" in sys.argv:
			index = sys.argv.index("-n") + 1

			if extention in sys.argv[index]:
				name = sys.argv[index]
			else:
				name = sys.argv[index] + "." + extention
		
		else:
			name = filename + "2." + extention
		return name

def get_img():
	try:
		img = cv2.imread(sys.argv[1])
	except Exception:
		print("Error loading image, check image file")
		sys.exit()
	else:
		return img

########## Main ##########

check_input()
img = get_img()
times = int(check_times())
destination = check_name()

if times > 0:
	times -= 1
	for i in range(times):
		img = cv2.pyrDown(img)
else:
	img = cv2.pyrDown(img)

cv2.imwrite(destination, img)