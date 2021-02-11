print "Welcome to Abed's vending machine!"
class VendingMachine:
	def __init__(self, paymentSum):
		self.paymentSum = paymentSum
		paymentSum = 0
	def insertMoney(self):
		while True:
			self.paymentSum = raw_input("Amount of money inserted: ")
			try:
				self.paymentSum = float(self.paymentSum)
				if self.paymentSum <= 0:
					print "Invalid payment. Must enter a positive number."
					
				else:
					break
			except ValueError:
				print "Invalid payment. Must enter a positive number. "
		
	def selectItem(self):
		if self.paymentSum == 0:
			print "Sorry, you can't select, since you haven't inserted money yet"
			return False
		while True:
			price = raw_input("Selected item's price: ")
			try:
				price = float(price)
				if price > self.paymentSum:
					print "Invalid selection. Price exceeds payment."
				elif price == 0:
					print "Invalid price. Must enter a positive number"
				else:
					break 
			except ValueError:
				print "Invalid price. Must enter a positive number."
		change = (self.paymentSum - price) * 100
		quarters = int(change // 25)
		dimes = int(change % 25 // 10)
		nickles = int(change % 25 % 10 // 5)
		pennies = int(change % 5)
		print "Your change is"
		print quarters, "quarter(s)"
		print dimes, "dime(s)"
		print nickles, "nickle(s)"
		print pennies, "penny(ies)"
		self.paymentSum = 0
		
machine = VendingMachine(0)
while True: 
	print "\nOptions: (i)nsert money, (s)elect an item, (q)uit"
	enter = raw_input("Enter i, s, or q ==> ")
	enter = enter.lower()
	if enter == "s":
		machine.selectItem()
	elif enter == "i":
		machine.insertMoney()
	elif enter == "q":
		break
	else:
		print "Invalid selection."
