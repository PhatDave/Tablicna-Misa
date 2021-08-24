class Registration:
	def __init__(self, person=None, registration="", model="", chassis="", insuranceHouse="", insuranceNo=""):
		self.registration = registration
		self.person = person
		self.model = model
		self.chassis = chassis
		self.insuranceHouse = insuranceHouse
		self.insuranceNo = insuranceNo

	def __str__(self):
		return f'{self.person} {self.registration} {self.model} {self.chassis} {self.insuranceHouse} {self.insuranceNo}'