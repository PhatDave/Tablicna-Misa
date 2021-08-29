from textdistance import levenshtein
from timeit import default_timer as dft


class PlateManager:
	def __init__(self, UI):
		self.ui = UI
		self.database = None
		self.confThreshold = 5

	def Manage(self, plates):
		try: self.ui.plates[self.ui.platePointer].displayTime = dft()
		except IndexError: pass
		for plate in plates:
			if plate.confidence < self.confThreshold:
				continue
			displayID = self.IsPlateDisplayed(plate)
			if displayID is False:
				plate.displayTime = dft()
				self.ui.plates.append(plate)
				if self.ui.platePointer == -1:
					self.ui.platePointer = 0
					self.ui.PointerChanged()
				# Query from database
				self.database.GetRegistration(plate.registration)
				continue
			"""
			try:
				if plate.confidence > self.ui.plates[displayID].confidence * 1.1 and plate.confidence > 3:
					print("Better plate!")
					plate.displayTime = dft()
					self.ui.plates[displayID] = plate
					# Also query from database
					self.database.GetRegistration(plate)
					print([str(i) for i in self.ui.plates])
			except Exception: continue
			"""
		for i, plate in enumerate(self.ui.plates):
			if dft() - plate.displayTime > 5:
				if self.ui.platePointer > i:
					self.ui.platePointer -= 1
				self.ui.plates.pop(i)
				i -= 1
				continue

	def IsPlateDisplayed(self, plate):
		for i, uiPlate in enumerate(self.ui.plates):
			if levenshtein(plate.registration, uiPlate.registration) < 4:
				return i
		return False