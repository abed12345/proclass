floor = range(1,101)
floor.remove(13)
current_floor= 1
last_floor = 2
current_floor = int(current_floor)
last_floor = int(last_floor)
string = "..."
class Elevator:
	def fireAlarm(self):
		global last_floor
		global current_floor
		print "Danger! You must exit the building now!"
		if current_floor != 1:
			last_floor = 1
			print "going down",
			for current_floor in floor[current_floor-1:last_floor-1:-1]:
				print current_floor, string,
			print "1 ... ding",
		
	def selectFloor(self):
		global current_floor
		global last_floor
		while True:
			current_floor = raw_input("Enter the floor that you'd like to go to ==> ")
			try:
				current_floor = int(current_floor)
				if current_floor == 13 or current_floor <0 or current_floor > 100:
					print "Invalid floor selection - must be between 1 and 100, excluding 13."
				else: 
					break
			except ValueError:
				print "Invalid floor selection - must be between 1 and 100, excluding 13."
		if current_floor == 1:
			print "going down",
			for current_floor in floor[last_floor-2: current_floor-1: -1]:
				print current_floor, string,
			print "2 ... 1 ... ding",
			current_floor = 1
		elif current_floor < last_floor :
			print "going down",
			for current_floor in floor[last_floor-2: current_floor-2: -1]:
				print current_floor, string,
			print "ding",
		if last_floor < current_floor:
			if last_floor < 2:
				last_floor = 2
			print "going up",
			for current_floor in floor[last_floor-2:current_floor-1]:
				print current_floor, string,
			print "ding",
			
			
		
#the loop that plays the game 

elevator = Elevator()
print "Welcome to Abed's elevator simulator!"
while True:
	print "\nOptions: (s)elect a floor, (f)ire alarm, (q)uit"
	enter = raw_input("Enter s, f, or q ==> ")
	enter = enter.lower()
	if enter == "s":
		elevator.selectFloor()
		last_floor = current_floor
	elif enter == "f":
		elevator.fireAlarm()
		last_floor = 2
	elif enter == "q":
		break
	else:
		print "Invalid selection."
	#print last_floor