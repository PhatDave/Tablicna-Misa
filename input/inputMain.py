import os
import threading

import cv2
import daveTrash as dt
from daveTrash.ScanCodes import ScanCodes as sc
import json

import win32gui
import win32ui


class Input:
	def __init__(self):
		self.cap = None
		self.image = None
		self.images = []
		self.pointer = 0
		self.file = None

		self.frameStack = []
		# self.frameStackSize = 120
		self.frameStackFull = False
		self.frameStackFullSemaphore = threading.Semaphore(1)

		self.frameStackWithdrawSemaphore = threading.Semaphore(1)

		self.batchDict = []
		self.batchConfigFile = 'batchConfig.json'
		self.LoadConfig()
		self.modelConfig = None
		self.filePlayback = False
		self.screenCap = False
		self.screenMainWindow = 0

	def SwitchWindow(self):
		print(self.screenMainWindow)
		self.screenMainWindow = win32gui.GetForegroundWindow()
		print(self.screenMainWindow)

	def DoScreencap(self):
		self.screenCap = True
		self.screenMainWindow = win32gui.GetForegroundWindow()
		dt.AddHotkey([sc.end], self.SwitchWindow)

	def LoadConfig(self):
		with open(self.batchConfigFile, 'r') as f:
			self.batchDict = json.load(f)

	def LoadFile(self, file):
		if '.mp4' in file:
			self.file = file
			self.cap = cv2.VideoCapture(file)
			self.filePlayback = True
		if '.jpg' or '.png' in file:
			self.image = cv2.imread(file)

	def GetFrame(self):
		if len(self.images) > 0:
			return [self.images[self.pointer].copy()]
		elif self.image is not None:
			return self.image.copy()
		elif self.screenCap:
			return dt.GetScreenshot(handle=self.screenMainWindow)
		elif self.cap.isOpened():
			ret, frame = self.cap.read()
			return frame
		return None

	def AppendFrame(self, frame):
		self.frameStack.append(frame)
		# if len(self.frameStack) >= self.frameStackSize:
		try: maxSize = self.batchDict[str(int(self.modelConfig.plateSize / 64) * 64)]
		except KeyError: maxSize = 2
		if not self.filePlayback:
			maxSize = int(maxSize / 1)
		# print("Batching", maxSize)
		if self.screenCap:
			maxSize = 10
		if len(self.frameStack) >= int(maxSize * 0.8):
			self.frameStackFull = True
			self.frameStackWithdrawSemaphore.release()
			self.frameStackFullSemaphore.acquire()

	def Run(self):
		while True:
			if self.cap is not None:
				while self.cap.isOpened():
					self.frameStackFullSemaphore.acquire()
					self.frameStackWithdrawSemaphore.acquire()
					ret, frame = self.cap.read()
					if frame is None:
						self.frameStackFullSemaphore.release()
						self.frameStackWithdrawSemaphore.release()
						break
					self.AppendFrame(frame)
					self.frameStackFullSemaphore.release()
					self.frameStackWithdrawSemaphore.release()
				del self.cap
				self.cap = cv2.VideoCapture(self.file)
			elif self.screenCap:
				self.frameStackFullSemaphore.acquire()
				self.frameStackWithdrawSemaphore.acquire()
				frame = dt.GetScreenshot(handle=self.screenMainWindow)
				if frame is None:
					self.frameStackFullSemaphore.release()
					self.frameStackWithdrawSemaphore.release()
					break
				self.AppendFrame(frame)
				self.frameStackFullSemaphore.release()
				self.frameStackWithdrawSemaphore.release()
			elif self.images is not None:
				self.frameStackFullSemaphore.acquire()
				self.frameStackWithdrawSemaphore.acquire()
				frame = self.images[self.pointer].copy()
				if frame is None:
					self.frameStackFullSemaphore.release()
					self.frameStackWithdrawSemaphore.release()
					break
				self.AppendFrame(frame)
				self.frameStackFullSemaphore.release()
				self.frameStackWithdrawSemaphore.release()

	def GetFrames(self):
		self.frameStackWithdrawSemaphore.acquire()
		frames = self.frameStack.copy()
		self.frameStack = []
		if self.frameStackFull:
			self.frameStackFull = False
			self.frameStackFullSemaphore.release()
		self.frameStackWithdrawSemaphore.release()
		return frames

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
