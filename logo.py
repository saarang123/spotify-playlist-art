import random
import cv2
import numpy as np
import os

A = 160 #change

def dataset(directory = 'albumart'):
	images = []
	for filename in os.listdir(directory):
		f = os.path.join(directory, filename)

		if os.path.isfile(f):
			image = cv2.imread(f)
			border_size = 20
			image = cv2.resize(image, (A - 2 * border_size, A - 2 * border_size))
			row, col = image.shape[:2]
			bottom = image[row-2:row, 0:col]
			mean = 0
			border = cv2.copyMakeBorder(
			    image,
			    top=border_size,
			    bottom=border_size,
			    left=border_size,
			    right=border_size,
			    borderType=cv2.BORDER_CONSTANT,
			    value=[mean, mean, mean]
			)
			image = cv2.resize(image, (A, A))
			images.append(border)
	return images

images = dataset()
length = len(images)
print(len(images))

blank = cv2.imread('blank.png')
blank = cv2.resize(blank, (A, A))
image_index = 0

qrcode = cv2.imread('qrcode.png')
qrcode = cv2.cvtColor(qrcode, cv2.COLOR_BGR2GRAY)
# qrcode = cv2.resize(qrcode, (50, 50))
colours = np.asarray(qrcode)
print(colours.shape)

# colours = [[1] * 16] * 16

print("start")

vertical_stack = []
for row in colours:
	horizontal = []
	print(len(vertical_stack))
	for pixel in row:
		if pixel >= 250:
			horizontal.append(blank)
		else:
			horizontal.append(images[image_index])
			# print(horizontal[-1].shape)
			image_index += 1
			image_index %= length
			if image_index == 0:
				np.random.shuffle(images)

	vertical_stack.append(np.hstack(horizontal))

print("done")

collage = np.vstack(vertical_stack)

# cv2.imshow("Final Collage", collage)
cv2.imwrite("test4.jpeg", collage)
cv2.destroyAllWindows()
