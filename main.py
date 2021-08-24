import threading
from timeit import default_timer as dft
import daveTrash as dt
import cv2

import ui.mainUi as ui
from Person import Person
from Registration import Registration
from database.mainDatabase import Database
from input.inputMain import Input
from model.Model import Model

db = Database()
dbThread = threading.Thread(target=db.Start)
dbThread.setDaemon(True)
dbThread.start()

UI = ui.UI()
UI.database = db
UIThread = threading.Thread(target=UI.Start)
UIThread.setDaemon(True)
UIThread.start()
UI.sem.acquire()
db.UI = UI

model = Model()
UI.LoadConfig(model.config)
# model.plateModel = model.LoadModel(71)

minTimeGap = 2
lastTime = 0
currentPlate = ""
currentConf = 0

inputFile = Input()
# inputFile.LoadFile('Clip.mp4')
inputFile.LoadFile('test.jpg')
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