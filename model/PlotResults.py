import matplotlib.pyplot as plt
import pandas as pd
import csv
import daveTrash as dt

data = {}
header = []
with open(r'C:\Users\Davu\PycharmProjects\TablicnaMisa\yolov5\runs\train\exp71\results.csv', 'r') as f:
	csvReader = csv.reader(f, delimiter=',')
	lineCount = 0
	for row in csvReader:
		if lineCount == 0:
			for i in row:
				header.append(i.replace(' ', ''))
				data[i.replace(' ', '')] = []
			lineCount += 1
		else:
			for i, item in enumerate(row):
				data[header[i]].append(float(item))
			lineCount += 1

dataframe = pd.DataFrame(data)
# dataframe = dataframe.drop(columns=['epoch'])
dt.ConfigurePlt()
plt.figure()
dataframe.plot(x='epoch', y=['train/box_loss', 'train/obj_loss', 'train/cls_loss', 'metrics/mAP_0.5', 'metrics/mAP_0.5:0.95',\
                             'val/box_loss', 'val/obj_loss', 'val/cls_loss'])
plt.show()
