import os
import random
import cv2
import daveTrash as dt
from shutil import copyfile
import pytesseract as pyt


def Pad(i, n):
	i = str(i)
	return '0' * (n - len(i)) + i


def PadInt(string, length):
    string = str(string)
    while len(string) < length:
        string += '0'
    return string


labels = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F',\
		  'G','H','I','J','K','L','M','N','O','P','R','S','T','U','V','W','X','Y','Z','Š','Č','Ć','Đ','Ž']

digit4boxes = [
	[0.163915, 0.500000, 0.087264, 0.731604],
	[0.255896, 0.502771, 0.091981, 0.714976],
	[0.439858, 0.488915, 0.082547, 0.720519],
	[0.524764, 0.500000, 0.084906, 0.698349],
	[0.609670, 0.500000, 0.082547, 0.687264],
	[0.696344, 0.494458, 0.090802, 0.731604],
	[0.832547, 0.491686, 0.091981, 0.737146],
	[0.925118, 0.488915, 0.086085, 0.709434],
]
digit3boxes = [
	[0.172759, 0.502771, 0.090802, 0.714976],
	[0.270637, 0.488915, 0.095519, 0.698349],
	[0.485849, 0.497229, 0.084906, 0.703892],
	[0.581368, 0.480601, 0.087264, 0.714976],
	[0.676297, 0.483373, 0.090802, 0.709434],
	[0.833137, 0.486144, 0.090802, 0.714976],
	[0.926297, 0.494458, 0.088443, 0.731604],
]

images = os.listdir('output\\')
images = [i for i in images if '.png' in i]

for bigCount, i in enumerate(images):
	name = i.split('.')[0]
	output = ""
	if len(name) == 10:
		offset = 0
		for count, box in enumerate(digit3boxes):
			while name[count + offset] == ' ' or name[count + offset] == '-':
				offset += 1
			output += str(labels.index(name[count + offset])) + ' '
			for b in box:
				output += str(b) + ' '
			output += '\n'
	elif len(name) == 11:
		offset = 0
		for count, box in enumerate(digit4boxes):
			while name[count + offset] == ' ' or name[count + offset] == '-':
				offset += 1
			output += str(labels.index(name[count + offset])) + ' '
			for b in box:
				output += PadInt(str(b), 8) + ' '
			output += '\n'
	with open(f'output\\labels\\{Pad(bigCount, 5)}.txt', 'w') as f:
		f.write(output)
	copyfile(f'output\\{name}.png', f'output\\images\\{Pad(bigCount, 5)}.jpg')