#!/usr/bin/env python3
import cv2
import sys

########## init ##########

helpString = """
pyramid is a simple program to scale down images
usage : pyramids <image to scale down> <destination>

there is no other options yet
"""

########## FX ##########

def check():
	if sys.argv[1] == "--help":
		print(helpString)
		sys.exit()

	elif len(sys.argv) < 3:
		print(f"Usage pyramids <file to use> <destination>")
		sys.exit()

def save(lower_reselution, name):
	cv2.imwrite(name, lower_reselution)

########## Main ##########

check()

img = cv2.imread(sys.argv[1])

lr = cv2.pyrDown(img)

destination = sys.argv[2]

save(lr, destination)