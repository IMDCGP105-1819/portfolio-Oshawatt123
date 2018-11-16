class Car():
	def __init__(self, colour, manufacturer, model, doors):
		self.colour = colour
		self.manufacturer = manufacturer
		self.model = model
		self.doors = doors
	
	def __str__(self):
		return "Colour: " + self.colour + " Manufacturer: " + self.manufacturer + " Model: " + self.model + " No. of Doors: " + self.doors
	
	def changeColour(self, colour):
		self.colour = colour
	
myCar = Car("Green", "Alfa Romeo", "Giuletta", "3")
myCar.changeColour("Orange")
print(myCar)
