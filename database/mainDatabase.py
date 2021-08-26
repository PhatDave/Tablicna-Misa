import sqlite3
import os
import threading

from Registration import Registration
from Person import Person


class Database:
	def __init__(self):
		self.cur = None
		self.con = None
		self.writeBuffer = []
		self.readRequests = []
		self.readBuffer = []
		self.sem = threading.Semaphore(0)
		self.readSem = threading.Semaphore(0)
		self.UI = None
		self.waitingThread = None

	def Start(self):
		self.GetDatabase()
		while True:
			self.sem.acquire()
			if len(self.writeBuffer) + len(self.readRequests) == 0:
				continue
			if len(self.writeBuffer) > 0:
				reg = self.writeBuffer.pop(0)
				self.cur.execute(f"INSERT INTO auti VALUES (\'{reg.registration}\', \'{reg.person.name}\', \'{reg.person.lastname}\', \'{reg.person.DOB}\', \'{reg.person.address}\', \'{reg.person.phoneNumber}\', \'{reg.person.email}\', \'{reg.model}\', \'{reg.chassis}\', \'{reg.insuranceHouse}\', \'{reg.insuranceNo}\')")
				self.con.commit()
				continue
			if len(self.readRequests) > 0:
				lookFor = self.readRequests.pop(0)
				self.cur.execute(f"SELECT * FROM auti WHERE registracija LIKE \'{lookFor}\'")
				fetch = self.cur.fetchone()
				try:
					self.readBuffer.append(Registration(Person(fetch[1], fetch[2], fetch[4], fetch[3], fetch[5], fetch[6]), \
				                    fetch[0], fetch[7], fetch[8], fetch[9], fetch[10]))
				except TypeError:
					self.readBuffer.append(None)
				self.readSem.release()

	def GetDatabase(self):
		list = os.listdir('./database/')
		if 'database.db' not in list:
			self.CreateDatabase()
		else:
			self.ConnectToDatabase()

	def CreateDatabase(self):
		self.ConnectToDatabase()
		try:
			self.cur.execute(r"CREATE TABLE auti (registracija, ime, prezime, godinaRodenja, adresa, telefon, email, tipAutomobila, brSasije, osiguravajucaKuca, brPolice)")
		except sqlite3.OperationalError:
			return

	def ConnectToDatabase(self):
		self.con = sqlite3.connect('./database/database.db')
		self.cur = self.con.cursor()

	def GetRegistration(self, lookFor):
		self.readRequests.append(lookFor)
		# print(len(self.readRequests))
		self.waitingThread = threading.Thread(target=self.DisplayRegistration, args=(self.readSem, ))
		self.waitingThread.start()
		self.sem.release()
		# return Registration(Person())

	def DisplayRegistration(self, sem):
		sem.acquire()
		fetch = self.readBuffer.pop(0)
		for i, plate in enumerate(self.UI.plates):
			if fetch == plate:
				self.UI.plates[i] = fetch
				self.UI.PointerChanged()
				break
		# if fetch is not None:
			# self.UI.DisplayRegistration(fetch)

	def AddRegistration(self, reg):
		self.writeBuffer.append(reg)
		self.sem.release()