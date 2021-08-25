import os
import threading
from timeit import default_timer as dft
import daveTrash as dt
import cv2

# import ui.mainUi as ui
from Person import Person
from Registration import Registration
from database.mainDatabase import Database
from input.inputMain import Input
from model.Model import Model
from utils.augmentations import letterbox
from utils.general import non_max_suppression, scale_coords

db = Database()
dbThread = threading.Thread(target=db.Start)
dbThread.setDaemon(True)
dbThread.start()

"""
UI = ui.UI()
UI.database = db
UIThread = threading.Thread(target=UI.Start)
UIThread.setDaemon(True)
UIThread.start()
UI.sem.acquire()
db.UI = UI
"""

model = Model()
# UI.LoadConfig(model.config)

minTimeGap = 2
lastTime = 0
currentPlate = ""
currentConf = 0

inputFile = Input()
# inputFile.LoadFile('Clip.mp4')
# inputFile.LoadFile('test.jpg')
inputFile.LoadDirectory('test')

# Guranteed shape
# img = letterbox(inputFile.GetFrame(), 1920, auto=False)[0]
# TODO:
# Batch images and pre process to gurantee same shape
# Figure out what the fuck the model outputs
# ???
# Profit

testImage = cv2.imread('goodOne.jpg')
frames = []
for i in os.listdir('test'):
	if '.png' in i or '.jpg' in i:
		frames.append(cv2.imread(f'test\\{i}'))

framesP, plates, ocr, time = model.ProcessBatch(frames)
framesP, plates, ocr, time = model.ProcessBatch(frames)
print(ocr, time)
for i, img in enumerate(framesP):
	cv2.imwrite(f'cunf{i}.jpg', img)

quit()

while True:
	frame = inputFile.GetFrame()
	if frame is None:
		break
	process = model.ProcessImage(frame)
	UI.nextFrame = process[0]
	UI.AddItem(process[3], UI.modelProcessingTime)
	maxConf = (0, 0)
	for i in process[2]:
		if i == 0:
			continue
		if i[1] > maxConf[0]:
			maxConf = [i[1], i[0]]
	if dft() - lastTime > minTimeGap:
		currentConf = 0
	if maxConf[0] > (currentConf * 1.07):
		plate = maxConf[1]
		if plate == 0:
			continue
		UI.DisplayRegistration(Registration(Person(), registration=plate))
		db.GetRegistration(plate)
		lastTime = dft()
		currentPlate = plate
		currentConf = maxConf[0]
	UI.feedUpdateSem.release()

# print(db.GetRegistration('ZG 0000-00'))
input()
