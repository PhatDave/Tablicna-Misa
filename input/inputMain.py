import daveTrash as dt
import cv2


class Input:
	def __init__(self):
		self.cap = None
		self.fps = 30

	def LoadFile(self, file):
		self.cap = cv2.VideoCapture(file)

	def GetFrame(self):
		if self.cap.isOpened():
			ret, frame = self.cap.read()
			return frame
		return None
