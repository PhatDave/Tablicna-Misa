from Person import Person
from textdistance import levenshtein


class Registration:
	def __init__(self, person=Person(), registration="", model="", chassis="", insuranceHouse="", insuranceNo="", confidence=0):
		self.registration = registration
		self.person = person
		self.model = model
		self.chassis = chassis
		self.insuranceHouse = insuranceHouse
		self.insuranceNo = insuranceNo
		self.displayTime = 0
		self.confidence = confidence

	def __str__(self):
		return f'{self.person} {self.registration} {self.model} {self.chassis} {self.insuranceHouse} {self.insuranceNo}'

	def __cmp__(self, other):
		return levenshtein(self.registration, other.registration) < 4