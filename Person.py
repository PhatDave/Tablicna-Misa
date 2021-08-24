class Person:
	def __init__(self, name="", lastname="", address="", DOB="", phoneNumber="", email=""):
		self.name = name
		self.lastname = lastname
		self.address = address
		self.DOB = DOB
		self.phoneNumber = phoneNumber
		self.email = email

	def __str__(self):
		return f'{self.name} {self.lastname} {self.address} {self.DOB} {self.phoneNumber} {self.email}'