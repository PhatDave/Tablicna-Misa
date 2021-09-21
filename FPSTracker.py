import cv2

class FPSTracker:
	def __init__(self):
		self.execTimeStack = []
		self.execTimeStackSize = 10

	def AppendExecTime(self, val):
		self.execTimeStack.append(val)
		if len(self.execTimeStack) > self.execTimeStackSize:
			self.execTimeStack.pop(0)

	def GetAverage(self, array):
		if len(array) > 0:
			return sum(array) / len(array)
		return 1

	def GetExecTime(self):
		return round(self.GetAverage(self.execTimeStack), 1)

	def GetFPS(self):
		return round((1 / self.GetAverage(self.execTimeStack)) * 1e3, 1)

	def DrawFPS(self, img):
		return cv2.putText(img, f'FPS {self.GetFPS()}', (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 2, cv2.LINE_AA)

	def DrawExecTime(self, img):
		return cv2.putText(img, f'Frame time {self.GetExecTime()}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 2, cv2.LINE_AA)
