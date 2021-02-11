first = int(raw_input("Enter first score: ")) 
second = int(raw_input("Enter second score: "))
third = int(raw_input("Enter third score: "))
fourth = int(raw_input("Enter fourth score: "))
fifth = int(raw_input("Enter fifth score: "))

scores =[first, second, third, fourth, fifth]
scores.remove(min(scores))
avg = sum(scores) / len(scores) + (sum(scores) % len(scores) > 0)

if avg >= 90:
	print "Your average is %d. Your grade is A." %avg
if avg <= 89 and avg >= 80:
	print "Your average is %d. Your grade is B." %avg
if avg <= 79 and avg >= 70:
	print "Your average is %d. Your grade is C." %avg
if avg <= 69 and avg >= 60:
	print "Your average is %d. Your grade is D." %avg
if avg <= 60:
	print "Your average is %d. Your grade is F." %avg 
	