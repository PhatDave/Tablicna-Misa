import daveTrash as dt
import cv2


class Input:
	def __init__(self):
		self.cap = None
		self.image = None

	def LoadFile(self, file):
		if '.mp4' in file:
			self.cap = cv2.VideoCapture(file)
		if '.jpg' or '.png' in file:
			self.image = cv2.imread(file)

	def GetFrame(self):
		if self.image is not None:
			return self.image.copy()
		if self.cap.isOpened():
			ret, frame = self.cap.read()
			return frame
		return None
