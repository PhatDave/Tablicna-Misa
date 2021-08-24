import torch
import sys
import cv2
import daveTrash as dt
import numpy as np
from model.utils.plots import plot_one_box, colors
from utils.general import non_max_suppression, scale_coords, xyxy2xywh
from timeit import default_timer as dft

# 23 valja (15 epoha)
# 26 isto valja, mozda je bolji (150 epoha)

sys.path.insert(0, r'C:\Users\Davu\Desktop\yolov5')
model = torch.load(r'C:\Users\Davu\Desktop\yolov5\runs\train\exp26\weights\best.pt')['model']
model.half()
model.cuda()
device = torch.device("cuda")
model.to(device)

imgs = [cv2.imread(f'test{i}.jpg') for i in range(8)]
for img in imgs:
	im0 = img.copy()

	if img.shape[0] > 480 or img.shape[1] > 640:
		print("Resizing image to 640x480", img.shape)
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
		gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]
		for *xyxy, conf, cls in reversed(det):
			# xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()
			print(xyxy)
			im0 = plot_one_box(xyxy, im0, label='Tablica', color=colors(int(cls), True), line_width=2)
	print((dft() - start) * 1e3)
	dt.imshow(im0)
