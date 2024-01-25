import random
import cv2
import numpy as np
import os

A = 640 #change

def dataset(directory = 'albumart'):
	images = []
	for filename in os.listdir(directory):
		f = os.path.join(directory, filename)

		if os.path.isfile(f):
			image = cv2.imread(f)
			image = cv2.resize(image, (A, A))
			images.append(image)
	return images

images = dataset()
length = len(images)
print(len(images))

blank = cv2.imread('blank.png')
blank = cv2.resize(blank, (A, A))
image_index = 0

qrcode = cv2.imread('qrcode.png')
qrcode = cv2.cvtColor(qrcode, cv2.COLOR_BGR2GRAY)
qrcode = cv2.resize(qrcode, (50, 50))
colours = np.asarray(qrcode)
print(colours.shape)

colours = [[1] * 16] * 16

vectical_stack = []
for row in colours:
	horizontal = []
	for pixel in row:
		if pixel == 255:
			horizontal.append(blank)
		else:
			horizontal.append(images[image_index])
			image_index += 1
			image_index %= length
			if image_index == 0:
				np.random.shuffle(images)

	vectical_stack.append(np.hstack(horizontal))

collage = np.vstack(vectical_stack)

cv2.imshow("Final Collage", collage)
cv2.imwrite("test2.jpeg", collage)
cv2.waitKey(0)
cv2.destroyAllWindows()
