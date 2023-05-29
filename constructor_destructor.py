class PartyAnymal:
	x = 0
	def __init__ (self):
		print ("PartyAnymal constructed")
	def party(self):
		self.x = self.x +1
		print(f"So far {self.x}")
	def __del__(self):
		print("PartyAnymal destructed")

an = PartyAnymal()
an.party()
an.party()
