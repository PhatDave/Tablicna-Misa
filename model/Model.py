import daveTrash as dt
import sys
import json
from timeit import default_timer as dft
import numpy as np
import torch
import cv2

from utils.augmentations import letterbox
from utils.general import non_max_suppression, scale_coords
from utils.plots import plot_one_box, colors


class ModelConfig:
	def __init__(self):
		self.plateSize = 640
		self.OCRSize = 320

		self.plateConfThresh = 0.75
		self.plateIOUConfThresh = 0.75
		self.maxPlates = 20

		self.OCRConfThresh = 0.55
		self.OCRIOUConfThresh = 0.55
		self.maxOCR = 20

		self.plateThiccness = 2
		self.plateConf = True
		self.plateLabel = False

		self.OCRThiccness = 1
		self.OCRConf = False
		self.OCRLabel = True

		self.plateModel = 0

		# self.SaveJson()
		self.LoadJson()

	def ToDict(self):
		dict = {
			'plateSize'         : self.plateSize,
			'OCRSize'           : self.OCRSize,

			'plateConfThresh'   : self.plateConfThresh,
			'plateIOUConfThresh': self.plateIOUConfThresh,
			'maxPlates'         : self.maxPlates,

			'OCRConfThresh'     : self.OCRConfThresh,
			'OCRIOUConfThresh'  : self.OCRIOUConfThresh,
			'maxOCR'            : self.maxOCR,

			'plateThiccness'    : self.plateThiccness,
			'plateConf'         : self.plateConf,
			'plateLabel'        : self.plateLabel,

			'OCRThiccness'      : self.OCRThiccness,
			'OCRConf'           : self.OCRConf,
			'OCRLabel'          : self.OCRLabel,

			'plateModel'        : self.plateModel,
		}
		return dict

	def FromDict(self, data):
		self.plateSize = data['plateSize']
		self.OCRSize = data['OCRSize']

		self.plateConfThresh = data['plateConfThresh']
		self.plateIOUConfThresh = data['plateIOUConfThresh']
		self.maxPlates = data['maxPlates']

		self.OCRConfThresh = data['OCRConfThresh']
		self.OCRIOUConfThresh = data['OCRIOUConfThresh']
		self.maxOCR = data['maxOCR']

		self.plateThiccness = data['plateThiccness']
		self.plateConf = data['plateConf']
		self.plateLabel = data['plateLabel']

		self.OCRThiccness = data['OCRThiccness']
		self.OCRConf = data['OCRConf']
		self.OCRLabel = data['OCRLabel']

		self.useSmall = data['plateModel']

	def SaveJson(self):
		data = self.ToDict()
		with open('config.json', 'w') as f:
			f.write(json.dumps(data, indent=4))

	def LoadJson(self, file='config.json'):
		with open(file, 'r') as f:
			self.FromDict(json.load(f))


class Model:
	def __init__(self, yoloPath='yolov5'):
		self.plateModel = None
		self.smallModel = None
		self.models = []
		self.OCRModel = None
		self.yoloPath = yoloPath
		sys.path.insert(0, yoloPath)

		self.OCRLabels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
		                  'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		# self.plateModel = self.LoadModel(34)
		# self.OCRModel = self.LoadModel(53)
		self.plateModel = self.LoadModelPath('plate.pt')
		self.smallModel = self.LoadModelPath('yolov3.pt')
		self.models = [self.plateModel, self.smallModel]
		self.OCRModel = self.LoadModelPath('OCR.pt')
		self.config = ModelConfig()

		open('log.txt', 'w')

	def LoadModelPath(self, path):
		model = torch.load(path)['model']
		model.half()
		model.cuda()
		model.eval()
		return model

	def LoadModel(self, index):
		model = torch.load(f'{self.yoloPath}\\runs\\train\\exp{index}\\weights\\best.pt')['model']
		model.half()
		model.cuda()
		model.eval()
		return model

	def ImagePreprocess(self, img, imgSize=640):
		originalShape = img.shape
		imgSize = int(imgSize / 32) * 32
		img = letterbox(img, imgSize)[0]
		img = img.transpose((2, 0, 1))[::-1]
		img = np.ascontiguousarray(img)

		img = torch.from_numpy(img)
		img = img.cuda()
		img = img / 255.0
		img = img[None]
		img = img.half()
		return img, originalShape

	def BatchFrames(self, frames, imageSize=640):
		originalShapes = []
		for i in frames:
			originalShapes.append(i.shape)
		# start = dft()

		frames = frames.copy()
		imgSize = int(imageSize / 32) * 32
		for i, frame in enumerate(frames):
			frames[i] = letterbox(frames[i], imgSize, auto=False)[0]
			frames[i] = frames[i].transpose((2, 0, 1))[::-1]
			frames[i] = np.ascontiguousarray(frames[i])

		# 24, h, w, d
		# 24, d, h, w
		# 24, w, h, d
		# frames = np.swapaxes(frames, 1, 2)
		# 24, d, h, w
		# frames = np.swapaxes(frames, 1, 3)

		batchTensor = torch.from_numpy(np.asarray(frames))
		batchTensor = batchTensor.cuda()
		batchTensor = batchTensor / 255.0
		batchTensor = batchTensor.half()
		# print((dft() - start) * 1e3)
		return batchTensor, originalShapes

	def RunInference(self, img, model, imgSize=640, confThresh=0.85, iouThresh=0.85, maxDet=20):
		img, imgShape = self.ImagePreprocess(img, imgSize=imgSize)
		output = []
		with torch.no_grad():
			pred = model(img)[0]
		pred = non_max_suppression(pred, confThresh, iouThresh, max_det=maxDet)
		for i, det in enumerate(pred):
			det[:, :4] = scale_coords(img.shape[2:], det[:, :4], imgShape).round()
			for *xyxy, conf, cls in reversed(det):
				output.append((xyxy, round(conf.item(), 3), cls))
		return output

	def RunBatchInference(self, frames, model, imgSize=640, confThresh=0.85, iouThresh=0.85, maxDet=20):
		batch, originalShapes = self.BatchFrames(frames, imageSize=imgSize)
		output = []
		if len(batch) == 0:
			return output
		with torch.no_grad():
			pred = model(batch)[0]
		batch.cpu()
		pred = non_max_suppression(pred, confThresh, iouThresh, max_det=maxDet)
		# pred.cpu()
		for i, det in enumerate(pred):
			temp = []
			det[:, :4] = scale_coords(batch[i].shape[1:], det[:, :4], originalShapes[i]).round()
			for *xyxy, conf, cls in reversed(det):
				temp.append((xyxy, round(conf.item(), 3), cls))
			output.append(temp)
		del batch, pred
		return output

	def GetPlates(self, img, batch=False):
		method = self.RunInference
		if batch:
			method = self.RunBatchInference
		return method(img,
		              self.models[self.config.plateModel],
		              self.config.plateSize,
		              self.config.plateConfThresh,
		              self.config.plateIOUConfThresh,
		              self.config.maxPlates)

	def GetOCR(self, img, batch=False):
		method = self.RunInference
		if batch:
			method = self.RunBatchInference
		return method(img,
		              self.OCRModel,
		              self.config.OCRSize,
		              self.config.OCRConfThresh,
		              self.config.OCRIOUConfThresh,
		              self.config.maxOCR)

	def CropPlate(self, img, box):
		box = [i.cpu().item() for i in box[0]]

		x = int(box[0])
		y = int(box[1])
		x2 = int(box[2])
		y2 = int(box[3])
		h = int(abs(y2 - y))
		w = int(abs(x2 - x))

		plate = img[y:y + h, x:x + w]
		return plate

	def ScaleOCRBoxToImage(self, OCRResult, plateBox):
		x = int(plateBox[0][0])
		y = int(plateBox[0][1])
		scaledResults = []
		for j in OCRResult:
			scaledResults.append(([j[0][0] + x, j[0][1] + y, j[0][2] + x, j[0][3] + y], j[1], j[2]))
		return scaledResults

	def DrawBox(self, img, box, thiccness=2, label=None, showConf=False, showLabel=True):
		if not img.data.contiguous:
			img = np.ascontiguousarray(img)
		if label is None and showLabel:
			label = self.OCRLabels[int(box[2].item())]
		if showConf:
			if label is None:
				label = str(round(box[1], 2))
			else:
				label += ' ' + str(round(box[1], 2))
		if label is None:
			label = ""
		return plot_one_box(box[0], img, label=label, color=colors(0, True), line_width=thiccness)

	def DrawBoxes(self, img, boxes, thiccness=2, label=None, showConf=False, showLabel=True):
		if len(boxes) > 0:
			for i in boxes:
				img = self.DrawBox(img, i, thiccness=thiccness, label=label, showConf=showConf, showLabel=showLabel)
		return img

	def BatchDrawBoxes(self, batch, boxes, thiccness=2, label=None, showConf=False, showLabel=True):
		if len(boxes) > 0:
			for i, box in enumerate(boxes):
				img = batch[i]
				for j in box:
					img = self.DrawBox(img, j, thiccness=thiccness, label=label, showConf=showConf, showLabel=showLabel)
		return batch

	def SortOCR(self, OCRResults, filter=False):
		results = []
		for i in OCRResults:
			results.append((i[0][0], i))
		results.sort(key=lambda x: x[0])
		results = [i[1] for i in results]
		if filter:
			resultsSorted = [[]]
			pointer = 0
			for i in range(1, len(results)):
				if abs(results[i - 1][0][0] - results[i][0][0]) < 5:
					better = results[i - 1]
					if results[i][1] > results[i - 1][1]:
						better = results[i]
					resultsSorted[pointer].append(better)
				else:
					resultsSorted.append([results[i]])
					pointer += 1
			results = []
			for i in resultsSorted:
				try:
					best = i[0]
					for j in i:
						if j[1] > best[1]:
							best = j
					results.append(best)
				except IndexError:
					continue
			# print(resultsSorted, results)
			return results
		else:
			return results

	def TranslateOCR(self, OCRResults):
		OCRResults = self.SortOCR(OCRResults)
		output = ""
		for i in OCRResults:
			output += self.OCRLabels[int(i[2].item())]
		return output

	def ProcessImage(self, img, drawPlates=True, drawOCR=True):
		start = dft()
		plates = self.GetPlates(img)
		if len(plates) == 0:
			return img, 0, (0, 0), (dft() - start) * 1e3
		if drawPlates:
			img = self.DrawBoxes(img, plates, self.config.plateThiccness, None, self.config.plateConf,
			                     self.config.plateLabel)
		croppedPlates = []
		ocr = []
		for plate in plates:
			cropped = self.CropPlate(img, plate)
			plateOCR = self.GetOCR(cropped)
			croppedPlates.append(cropped)
			ocr.append((self.TranslateOCR(plateOCR), sum([item[1] for i, item in enumerate(plateOCR) if i <= 9])))
			if drawOCR:
				img = self.DrawBoxes(img, self.ScaleOCRBoxToImage(plateOCR, plate), self.config.OCRThiccness, None,
				                     self.config.OCRConf, self.config.OCRLabel)
		return img, croppedPlates, ocr, (dft() - start) * 1e3

	def ProcessBatch(self, frames, drawPlates=True, drawOCR=True):
		start = dft()
		plates = self.GetPlates(frames, True)
		if all([len(i) == 0 for i in plates]):
			return frames, 0, (0, 0), (dft() - start) * 1e3
		if drawPlates:
			frames = self.BatchDrawBoxes(frames, plates, self.config.plateThiccness, None, self.config.plateConf,
			                             self.config.plateLabel)
		croppedPlates = []
		ocr = []
		bindings = []
		for i, plate in enumerate(plates):
			for j in plate:
				bindings.append(-1)
				bindings[len(croppedPlates)] = (i, j)
				croppedPlates.append(self.CropPlate(frames[i], j))
		ocrResults = self.GetOCR(croppedPlates, True)
		for i in range(len(plates)): ocr.append([])
		if drawOCR:
			for i, res in enumerate(ocrResults):
				frames[bindings[i][0]] = self.DrawBoxes(frames[bindings[i][0]],
				                                        self.ScaleOCRBoxToImage(res, bindings[i][1]),
				                                        self.config.OCRThiccness,
				                                        None,
				                                        self.config.OCRConf,
				                                        self.config.OCRLabel)
		for i, res in enumerate(ocrResults):
			if len(res) > 0:
				ocr[bindings[i][0]].append((self.TranslateOCR(res), sum([item[1] for j, item in enumerate(res) if j <= 9])))
		return frames, croppedPlates, ocr, (dft() - start) * 1e3

	def Test(self, file):
		img = cv2.imread(file)
		img, plates, ocr, time = self.ProcessImage(img)
		print(ocr, time)
		dt.imshow(img)

	def Log(self, msg):
		with open('log.txt', 'a') as f:
			f.write(str(msg))
