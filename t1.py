floor = range(1,101)
floor.remove(13)
current_floor= raw_input('flor')
last_floor = 1
current_floor = int(current_floor)
last_floor = int(last_floor)
string= "..."
for i in floor[last_floor - 1: current_floor]:
	print i, "...",
print "Ding"
