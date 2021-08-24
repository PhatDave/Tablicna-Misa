import torch
import sys
import cv2
import daveTrash as dt
from shutil import copyfile
import numpy as np
from model.utils.plots import plot_one_box, colors
from utils.general import non_max_suppression, scale_coords, xyxy2xywh
from timeit import default_timer as dft
from tqdm import tqdm
import os

sys.path.insert(0, r'C:\Users\Davu\Desktop\yolov5')
model = torch.load(r'C:\Users\Davu\Desktop\yolov5\runs\train\exp26\weights\best.pt')['model']
model.half()
model.cuda()
device = torch.device("cuda")
model.to(device)

imgs = []
imgNames = []
rootDir = '.\\newDataset\\'
for i in tqdm(os.listdir(f'{rootDir}\\images\\'), desc='Loading images'):
	if not 'Bonkd' in i:
		imgs.append(cv2.imread(f'{rootDir}\\images\\{i}'))
		imgNames.append(i.split('.')[0])
# print(len(imgs), "loaded")


def Pad(i, n):
	i = str(i)
	return '0' * (n - len(i)) + i


def PadInt(string, length):
	string = str(string)
	while len(string) < length:
		string += '0'
	return string


pbar = tqdm(total=len(imgs))
for cout, img in enumerate(imgs):
	pbar.update(cout)
	im0 = img.copy()
	im1 = img.copy()

	if img.shape[0] > 480 or img.shape[1] > 640:
		# print("Resizing image to 640x480", img.shape)
		img = cv2.resize(img, (640, 480), interpolation=cv2.INTER_AREA)

	img = img / 255.0
	img = img.transpose((2, 0, 1))[::-1]
	img = np.ascontiguousarray(img)
	img = img[None]
	img = torch.from_numpy(img)
	img = img.cuda()
	img = img.half()

	start = dft()
	pred = model(img)[0]
	pred = non_max_suppression(pred, 0.25, 0.45, max_det=10)
	for i, det in enumerate(pred):
		det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()
		output = ""
		for *xyxy, conf, cls in reversed(det):
			# print(xyxy)

			box = [i.cpu().item() for i in xyxy]
			height = im0.shape[0]
			width = im0.shape[1]
			normW = (box[2] - box[0]) / width
			normH = (box[3] - box[1]) / height
			normX = (box[0] + ((box[2] - box[0]) / 2)) / width
			normY = (box[1] + ((box[3] - box[1]) / 2)) / height

			output += f'0\t{PadInt(round(normX, 6), 8)}\t{PadInt(round(normY, 6), 8)}\t{PadInt(round(normW, 6), 8)}\t{PadInt(round(normH, 6), 8)}\n'
			im1 = plot_one_box(xyxy, im1, label=str(round(conf.item(), 3)), color=colors(int(cls), True), line_width=2)
		with open(f'{rootDir}\\labels\\{Pad(cout, 5)}.txt', 'w') as f:
			f.write(output)

	# print((dft() - start) * 1e3)
	pbar.desc = str((dft() - start) * 1e3)
	pbar.refresh()
	copyfile(f'{rootDir}\\images\\{imgNames[cout]}.jpg', f'{rootDir}\\imagesSorted\\{Pad(cout, 5)}.jpg')
	cv2.imwrite(f'{rootDir}\\imagesOutput\\{Pad(cout, 5)}.jpg', im1)
