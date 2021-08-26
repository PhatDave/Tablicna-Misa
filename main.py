import threading
import time
from math import ceil

import torch
from tqdm import tqdm

import ui.mainUi as ui
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

minTimeGap = 2
lastTime = 0
currentPlate = ""
currentConf = 0

inputFile = Input()
inputFile.modelConfig = model.config
inputFile.LoadFile('Clip.mp4')
inputThread = threading.Thread(target=inputFile.Run)
inputThread.setDaemon(True)
inputThread.start()


# inputFile.LoadFile('test.jpg')
# inputFile.LoadDirectory('test'


def BenchmarkBatchSizes():
	open('out.txt', 'w')
	pbar = tqdm(desc='okk')
	for i in range(10, 70):
		torch.cuda.empty_cache()
		size = 64 * i
		count = 240
		step = count / 2
		model.config.plateSize = 64 * i
		while step > 1:
			try:
				inputFile.frameStackSize = int(count)
				if len(inputFile.frameStack) < inputFile.frameStackSize and inputFile.frameStackFull:
					inputFile.frameStackFull = False
					inputFile.frameStackFullSemaphore.release()
				while not inputFile.frameStackFull: time.sleep(0.1)
				pbar.desc = f'{inputFile.frameStackSize}, {len(inputFile.frameStack)}, {model.config.plateSize}, {step}'
				pbar.refresh()
				frames = inputFile.GetFrames()
				process = model.ProcessBatch(frames)
				process = model.ProcessBatch(frames)
				process = model.ProcessBatch(frames)
				process = model.ProcessBatch(frames)
				count += step
			except (RuntimeError):
				count -= step
				step = ceil(step / 2)
				torch.cuda.empty_cache()
		with open('out.txt', 'a') as f:
			f.write(f'{int(count)} images of {model.config.plateSize} size\n')
	quit()


while True:
	frames = inputFile.GetFrames()
	process = model.ProcessBatch(frames)
	[UI.frameBuffer.append(i) for i in process[0]]
	print(len(UI.frameBuffer))
	[UI.frameBufferSem.release() for i in process[0]]

# print(db.GetRegistration('ZG 0000-00'))
input()

"""
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
"""
