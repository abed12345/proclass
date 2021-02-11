floor = range(1,101)
floor.remove(13)
class Elevator:
	
	def __init__(self,current_floor, last_floor):
		self.current_floor = current_floor
		self.last_floor = last_floor
		self.last_floor = 1
		self.current_floor = self.last_floor
	def fireAlarm(self):
		print "Danger! You must exit the building now!"
		if self.current_floor > 1 and self.last_floor > 13:
			for i in floor[self.current_floor-2: 1: -1]:
				print i, "...",
			print "2... 1... ding",
		if self.current_floor > 1 and self.last_floor < 13:
			print "going down",
			for i in floor[self.current_floor-1: 1: -1]:
				print i, "...",
			print "2... 1... ding",
		self.last_floor = 1
		self.current_floor = 1
	def selectFloor(self):
		while True:
			self.current_floor = raw_input("Enter the floor that you'd like to go to ==> ")
			try:
				self.current_floor = int(self.current_floor)
				if self.current_floor == 13 or self.current_floor <0 or self.current_floor > 100:
					print "Invalid floor selection - must be between 1 and 100, excluding 13."
				else: 
					break
			except ValueError:
				print "Invalid floor selection - must be between 1 and 100, excluding 13."
		if self.current_floor > self.last_floor and self.current_floor > 13:
			print "going up",
			for i in floor[self.last_floor - 1: self.current_floor - 1:]:
				print i, "...",
			print " ding",
			
		if self.current_floor > self.last_floor and self.current_floor < 13:
			print "going up",
			for i in floor[self.last_floor - 1: self.current_floor :]:
				print i, "...",
			print " ding",
		if self.current_floor < self.last_floor and self.current_floor < 13:
			print "going down",
			for i in floor[self.last_floor-2 : self.current_floor-2 : -1]:
				print i, "...",
			print "ding"
		if self.current_floor < self.last_floor and self.current_floor > 13:
			print "going down"
			for i in floor[self.last_floor-2 : self.current_floor-2 : -1]:
				print i, "...",
			print "ding"
		#print self.last_floor
		self.last_floor = self.current_floor
		#print self.last_floor
		
			
			
			
		
#the loop that plays the game 

elevator = Elevator(0,0)
print "Welcome to Abed's elevator simulator!"
while True:
	print "\nOptions: (s)elect a floor, (f)ire alarm, (q)uit"
	enter = raw_input("Enter s, f, or q ==> ")
	enter = enter.lower()
	if enter == "s":
		elevator.selectFloor()
		
	elif enter == "f":
		elevator.fireAlarm()
		
	elif enter == "q":
		break
	else:
		print "Invalid selection."
	#print last_floor