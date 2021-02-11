class Rectangle:
	
	def __init__(self,length, width):
	 		
		self.length = length
	 		
		self.width = width 
	 
	def isSquare(self):
			return self.length == self.width
	
	def output(self):
		if self.isSquare() :
			print "Square:", self.length, "x", self.width 		
		else:
		 	print "Rectangle:", self.length, "x", self.width
		 					
			
		

rect = Rectangle(6,10)

rect.isSquare()
rect.output()
rect2 = Rectangle(10,10)
rect2.isSquare()
rect2.output()