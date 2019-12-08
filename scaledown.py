#!/usr/bin/env python3
import cv2
import sys

########## FX ##########

def check_and_get():
	if len(sys.argv) < 2:
		print(f"Usage pyramids <file to use> ")
		sys.exit()
	elif sys.argv[1] == "--help":
		print("""
			---------------------------------------------------------------------\n
			pyramid is a simple program to scale down images\n
			usage : pyramids <image to scale down> <how many times to scale down>\n
			---------------------------------------------------------------------\n
			there is no other options yet
			""")
		sys.exit()

def save(img):
	pass

########## Main ##########

img = cv2.imread(sys.argv[1])
lr = cv2.pyrDown(img)

cv2.imshow("original", img)
cv2.imshow("pydown", lr)

########## clean up ##########

cv2.waitKey()
cv2.destroyAllWindows()