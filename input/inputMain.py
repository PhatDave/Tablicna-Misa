import os
import cv2
import daveTrash as dt
from daveTrash.ScanCodes import ScanCodes as sc


class Input:
	def __init__(self):
		self.cap = None
		self.image = None
		self.images = []
		self.pointer = 0

	def LoadFile(self, file):
		if '.mp4' in file:
			self.cap = cv2.VideoCapture(file)
		if '.jpg' or '.png' in file:
			self.image = cv2.imread(file)

	def GetFrame(self):
		if len(self.images) > 0:
			return self.images[self.pointer].copy()
		if self.image is not None:
			return self.image.copy()
		if self.cap.isOpened():
			ret, frame = self.cap.read()
			return frame
		return None

	def LoadDirectory(self, path):
		for i in os.listdir(path):
			if '.png' in i or '.jpg' in i:
				self.images.append(cv2.imread(f'{path}\\{i}'))
		self.MakeControls()

	def MakeControls(self):
		dt.AddHotkey([sc.left], self.GoLeft)
		dt.AddHotkey([sc.right], self.GoRight)

	def GoRight(self):
		self.pointer += 1
		if self.pointer >= len(self.images):
			self.pointer = 0

	def GoLeft(self):
		self.pointer -= 1
		if self.pointer < 0:
			self.pointer = len(self.images) - 1
