balance = input("Enter starting balance: ")
for years in range(125):
	sum = balance * 2 ** years
	if sum >= 100000  and sum <200000:
		print "It takes %d years to reach 100,000" %years 
	if sum >= 1000000 and sum < 2000000:
		print "It takes %d years to reach 1,000,000" %years
## the reason i use range(125) is because python does not support for loops in the for(i= something, i < something_else, i++) way so the maximum number of times the for loop will run is 124. i figured no human would live past that number. 