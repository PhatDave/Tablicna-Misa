import sys
import threading

import cv2
from timeit import default_timer as dft

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow
from Person import Person
from Registration import Registration
from ui.newest import Ui_MainWindow


# self.postavkeWidget
# self.menuPostavke

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


class UI:
	def __init__(self):
		self.app = None
		self.window = None
		self.sem = threading.Semaphore(0)
		self.readOnly = False
		self.database = None

		self.nextFrame = None
		self.liveFeed = False
		self.liveFeedThread = None
		self.feedUpdateSem = threading.Semaphore(0)

		self.liveFeedFps = []
		self.modelProcessingTime = []
		self.fpsItemLimit = 15
		self.lastUpdate = dft()

	def Start(self):
		self.app = QApplication(sys.argv)
		self.window = MainWindow()
		self.window.show()
		self.sem.release()
		self.modelConfig = None

		self.window.ui.postavkeWidget.hide()
		self.window.ui.gumb_baza.clicked.connect(self.DodajUBazuGumb)
		self.window.ui.gumb_emitiranje_uzivo.clicked.connect(self.LiveFeedGumb)
		self.window.ui.toolButton.clicked.connect(self.PostavkeGumb)
		self.window.ui.gumb_zatvori.clicked.connect(lambda x:self.window.ui.postavkeWidget.hide())

		self.window.ui.horizontalSlider_t_confidence.setTickInterval(5)
		self.window.ui.horizontalSlider_z_confidence.setTickInterval(5)
		self.window.ui.horizontalSlider_t_iouconfidence.setTickInterval(5)
		self.window.ui.horizontalSlider_z_iouconfidence.setTickInterval(5)

		self.window.ui.horizontalSlider_t_confidence.sliderMoved.connect(self.SliderConfidence1)
		self.window.ui.label_31.textChanged.connect(self.LabelConfidence1)

		self.window.ui.horizontalSlider_t_iouconfidence.sliderMoved.connect(self.SliderIOUConfidence1)
		self.window.ui.label_38.textChanged.connect(self.LabelIOUConfidence1)

		self.window.ui.horizontalSlider_z_confidence.sliderMoved.connect(self.SliderConfidence2)
		self.window.ui.label_31.textChanged.connect(self.LabelConfidence2)

		self.window.ui.horizontalSlider_z_iouconfidence.sliderMoved.connect(self.SliderIOUConfidence2)
		self.window.ui.label_31.textChanged.connect(self.LabelIOUConfidence2)

		self.window.ui.lineEdit.textChanged.connect(self.PlateThickness)
		self.window.ui.lineEdit_2.textEdited.connect(self.PlateResolution)
		self.window.ui.lineEdit_7.textChanged.connect(self.OCRThickness)
		self.window.ui.lineEdit_8.textEdited.connect(self.OCRResolution)

		self.window.ui.checkBox_t_confidence.stateChanged.connect(self.PlateConfidenceDisplay)
		self.window.ui.checkBox_t_label.stateChanged.connect(self.PlateLabelDisplay)
		self.window.ui.checkBox_z_confidence.stateChanged.connect(self.OCRConfidenceDisplay)
		self.window.ui.checkBox_z_label.stateChanged.connect(self.OCRLabelDisplay)

		sys.exit(self.app.exec())

	def PlateConfidenceDisplay(self):
		self.modelConfig.plateConf = self.window.ui.checkBox_t_confidence.isChecked()
		self.modelConfig.SaveJson()
	def PlateLabelDisplay(self):
		self.modelConfig.plateLabel = self.window.ui.checkBox_t_label.isChecked()
		self.modelConfig.SaveJson()
	def OCRConfidenceDisplay(self):
		self.modelConfig.OCRConf = self.window.ui.checkBox_z_confidence.isChecked()
		self.modelConfig.SaveJson()
	def OCRLabelDisplay(self):
		self.modelConfig.OCRLabel = self.window.ui.checkBox_z_label.isChecked()
		self.modelConfig.SaveJson()

	def PlateThickness(self):
		try: val = int(self.window.ui.lineEdit.text()) or 1
		except ValueError: return
		self.modelConfig.plateThiccness = val
		self.modelConfig.SaveJson()
	def PlateResolution(self):
		try: val = int(self.window.ui.lineEdit_2.text()) or 1
		except ValueError: return
		if val < 32: val = 32
		if val > 4400: val = 4400
		val = int(val / 32) * 32
		# self.window.ui.lineEdit_2.setText(str(val))
		self.modelConfig.plateSize = val
		self.modelConfig.SaveJson()
	def OCRThickness(self):
		try: val = int(self.window.ui.lineEdit_7.text()) or 1
		except ValueError: return
		self.modelConfig.OCRThiccness = val
		self.modelConfig.SaveJson()
	def OCRResolution(self):
		try: val = int(self.window.ui.lineEdit_8.text()) or 1
		except ValueError: return
		if val < 32: val = 32
		if val > 4400: val = 4400
		val = int(val / 32) * 32
		# self.window.ui.lineEdit_8.setText(str(val))
		self.modelConfig.OCRSize = val
		self.modelConfig.SaveJson()

	def SliderConfidence1(self):
		val = (self.window.ui.horizontalSlider_t_confidence.value() / 100) or 0.01
		self.modelConfig.plateConfThresh = val
		self.modelConfig.SaveJson()
		self.window.ui.label_31.setText(str(val))
	def LabelConfidence1(self):
		try: val = float(self.window.ui.label_31.text()) or 0.01
		except ValueError: return
		if val > 0.99:
			val = 0.99
		self.window.ui.label_31.setText(str(val))
		self.modelConfig.plateConfThresh = val
		self.modelConfig.SaveJson()
		self.window.ui.horizontalSlider_t_confidence.setValue(int(val * 100))

	def SliderIOUConfidence1(self):
		val = (self.window.ui.horizontalSlider_t_iouconfidence.value() / 100) or 0.01
		self.modelConfig.plateIOUConfThresh = val
		self.modelConfig.SaveJson()
		self.window.ui.label_38.setText(str(val))
	def LabelIOUConfidence1(self):
		try: val = float(self.window.ui.label_38.text()) or 0.01
		except ValueError: return
		if val > 0.99:
			val = 0.99
		self.window.ui.label_38.setText(str(val))
		self.modelConfig.plateIOUConfThresh = val
		self.modelConfig.SaveJson()
		self.window.ui.horizontalSlider_t_iouconfidence.setValue(int(val * 100))

	def SliderConfidence2(self):
		val = (self.window.ui.horizontalSlider_z_confidence.value() / 100) or 0.01
		self.modelConfig.OCRConfThresh = val
		self.modelConfig.SaveJson()
		self.window.ui.label_40.setText(str(val))
	def LabelConfidence2(self):
		try: val = float(self.window.ui.label_40.text()) or 0.01
		except ValueError: return
		if val > 0.99:
			val = 0.99
		self.window.ui.label_40.setText(str(val))
		self.modelConfig.OCRConfThresh = val
		self.modelConfig.SaveJson()
		self.window.ui.horizontalSlider_z_confidence.setValue(int(val * 100))

	def SliderIOUConfidence2(self):
		val = (self.window.ui.horizontalSlider_z_iouconfidence.value() / 100) or 0.01
		self.modelConfig.OCRIOUConfThresh = val
		self.modelConfig.SaveJson()
		self.window.ui.label_39.setText(str(val))
	def LabelIOUConfidence2(self):
		try: val = float(self.window.ui.label_39.text()) or 0.01
		except ValueError: return
		if val > 0.99:
			val = 0.99
		self.window.ui.label_39.setText(str(val))
		self.modelConfig.OCRIOUConfThresh = val
		self.modelConfig.SaveJson()
		self.window.ui.horizontalSlider_z_iouconfidence.setValue(int(val * 100))

	def LoadConfig(self, config):
		self.modelConfig = config

		self.window.ui.label_39.setText(str(self.modelConfig.OCRIOUConfThresh))
		self.window.ui.horizontalSlider_z_iouconfidence.setValue(int(self.modelConfig.OCRIOUConfThresh * 100))
		self.window.ui.label_40.setText(str(self.modelConfig.OCRConfThresh))
		self.window.ui.horizontalSlider_z_confidence.setValue(int(self.modelConfig.OCRConfThresh * 100))

		self.window.ui.label_31.setText(str(self.modelConfig.plateConfThresh))
		self.window.ui.horizontalSlider_t_confidence.setValue(int(self.modelConfig.plateConfThresh * 100))
		self.window.ui.label_38.setText(str(self.modelConfig.plateIOUConfThresh))
		self.window.ui.horizontalSlider_t_iouconfidence.setValue(int(self.modelConfig.plateIOUConfThresh * 100))

		self.window.ui.lineEdit_2.setText(str(self.modelConfig.plateSize))
		self.window.ui.lineEdit_8.setText(str(self.modelConfig.OCRSize))
		self.window.ui.lineEdit.setText(str(self.modelConfig.plateThiccness))
		self.window.ui.lineEdit_7.setText(str(self.modelConfig.OCRThiccness))

		self.window.ui.checkBox_t_confidence.setChecked(self.modelConfig.plateConf)
		self.window.ui.checkBox_t_label.setChecked(self.modelConfig.plateLabel)
		self.window.ui.checkBox_z_confidence.setChecked(self.modelConfig.OCRConf)
		self.window.ui.checkBox_z_label.setChecked(self.modelConfig.OCRLabel)


	def PostavkeGumb(self):
		if self.window.ui.postavkeWidget.isHidden():
			self.window.ui.postavkeWidget.show()
		else:
			self.window.ui.postavkeWidget.hide()

	def AddItem(self, item, array):
		array.append(item)
		if len(array) > self.fpsItemLimit:
			array.pop(0)

	def DodajUBazuGumb(self):
		self.database.AddRegistration(self.GetRegistration(self.GetPerson()))

	def GetAverage(self, array):
		return sum(array) / len(array)

	def LiveFeedGumb(self):
		self.liveFeed = not self.liveFeed
		if self.liveFeed:
			self.liveFeedThread = threading.Thread(target=self.LiveFeed)
			self.liveFeedThread.start()
		else:
			del self.liveFeedThread

	def LiveFeed(self):
		cv2.namedWindow('Live Feed')
		while self.liveFeed:
			self.feedUpdateSem.acquire()
			self.AddItem((dft() - self.lastUpdate), self.liveFeedFps)
			if self.nextFrame is None:
				break
			cv2.putText(self.nextFrame,
			            f'{str(round(1 / self.GetAverage(self.liveFeedFps), 1))}FPS {round(self.GetAverage(self.modelProcessingTime), 2)}ms', \
			            (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 0), 2, cv2.LINE_AA)
			cv2.imshow('Live Feed', self.nextFrame)
			self.lastUpdate = dft()
			if cv2.waitKey(1) == 27:
				break
		cv2.destroyAllWindows()
		self.liveFeed = False

	def DisplayPerson(self, person):
		self.window.ui.lineEdit_prezime.setText(person.lastname)
		self.window.ui.lineEdit_ime.setText(person.name)
		self.window.ui.lineEdit_adresa.setText(person.address)
		self.window.ui.lineEdit_datum.setText(person.DOB)
		self.window.ui.lineEdit_telefon.setText(person.phoneNumber)
		self.window.ui.lineEdit_email.setText(person.email)

	def DisplayRegistration(self, registration):
		self.DisplayPerson(registration.person)
		self.window.ui.label_prikaz_registracije.setText(registration.registration)
		self.window.ui.lineEdit_tip_auta.setText(registration.model)
		self.window.ui.lineEdit_br_sasije.setText(registration.chassis)
		self.window.ui.lineEdit_osig_kuca.setText(registration.insuranceHouse)
		self.window.ui.lineEdit_br_police.setText(registration.insuranceNo)

	def GetPerson(self):
		return Person(self.window.ui.lineEdit_ime.text(), self.window.ui.lineEdit_prezime.text(),
		              self.window.ui.lineEdit_adresa.text(), \
		              self.window.ui.lineEdit_datum.text(), self.window.ui.lineEdit_telefon.text(),
		              self.window.ui.lineEdit_email.text())

	def GetRegistration(self, person=None):
		return Registration(person, self.window.ui.label_prikaz_registracije.text(),
		                    self.window.ui.lineEdit_tip_auta.text(), \
		                    self.window.ui.lineEdit_br_sasije.text(), self.window.ui.lineEdit_osig_kuca.text(), \
		                    self.window.ui.lineEdit_br_police.text())

	def ToggleFields(self):
		if self.readOnly:
			self.window.ui.lineEdit_prezime.setReadOnly(False)
			self.window.ui.lineEdit_ime.setReadOnly(False)
			self.window.ui.lineEdit_adresa.setReadOnly(False)
			self.window.ui.lineEdit_datum.setReadOnly(False)
			self.window.ui.lineEdit_telefon.setReadOnly(False)
			self.window.ui.lineEdit_email.setReadOnly(False)
			self.window.ui.lineEdit_tip_auta.setReadOnly(False)
			self.window.ui.lineEdit_br_sasije.setReadOnly(False)
			self.window.ui.lineEdit_osig_kuca.setReadOnly(False)
			self.window.ui.lineEdit_br_police.setReadOnly(False)
		else:
			self.window.ui.lineEdit_prezime.setReadOnly(True)
			self.window.ui.lineEdit_ime.setReadOnly(True)
			self.window.ui.lineEdit_adresa.setReadOnly(True)
			self.window.ui.lineEdit_datum.setReadOnly(True)
			self.window.ui.lineEdit_telefon.setReadOnly(True)
			self.window.ui.lineEdit_email.setReadOnly(True)
			self.window.ui.lineEdit_tip_auta.setReadOnly(True)
			self.window.ui.lineEdit_br_sasije.setReadOnly(True)
			self.window.ui.lineEdit_osig_kuca.setReadOnly(True)
			self.window.ui.lineEdit_br_police.setReadOnly(True)
