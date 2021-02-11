class Employee(object):
	def __init__(self, name, social, paycheck):
		self.name = name
		self.social = social
		self.paycheck = paycheck
	def input(self):
		self.name = raw_input("Name ==> ")
		self.social = raw_input("Social security number ==> ")
	def getEarning(self):
		if self.paycheck > 1000:
			self.paycheck = 1000
		
	def toString(self):
		print "employee:", self.name
		print "social security number:", self.social
		print "paycheck:", self.paycheck
class Hourly(Employee):
	def in_hourly(self):
		self.hourly_pay = hourly_pay
		self.hours_worked = hours_worked
	def input(self):
		super(Hourly, self).input()
		self.hourly_pay = int(raw_input("Hourly pay ==> "))
		self.hours_worked = int(raw_input("Hours worked this past week ==> ")) 
	def getEarning(self):
		self.paycheck = self.hourly_pay * self.hours_worked
		super(Hourly, self).getEarning()
class Salaried(Employee):
	def in_salaried(self):
		self.salary = salary
	def input(self):
		super(Salaried, self).input()
		self.salary = int(raw_input("Salary ==> "))
	def getEarning(self):
		self.paycheck = self.salary
		super(Salaried, self).getEarning()
		
class Commission(Salaried):
	def in_commission(self):
		self.sales = sales
		self.rate = rate
	def input(self):
		super(Commission, self).input()
		self.sales = int(raw_input("Sales for this past week ==> "))
		self.rate = float(raw_input("Sales commission rate (fraction paid to employee) ==> "))
	def getEarning(self):
		self.paycheck = int((self.sales * self.rate) + self.salary)
		super(Commission, self).getEarning()
		


#runs input output stuff
number = int(raw_input("Number of employees: "))
employees = []
Employee(0,0,0)
i = 0
print ""
while i < number:
	print "PROFILE FOR EMPLOYEE #%d" %i
	print "type Hourly(1), Salaried(2), Salaried plus Commission(3)"
	enter = int(raw_input("Enter 1, 2, or 3 ==> "))
	print ""
	if enter == 1:
		employees.append(Hourly(0, 0, 0))
		
		
	if enter == 2:
		employees.append(Salaried(0, 0, 0))
		
	if enter == 3:
		employees.append(Commission(0, 0, 0))
	print ""
	employees[i].input()
	employees[i].getEarning()
	i += 1
#prints lines 
print "PAYCHECK REPORT:"
for my_employee in employees:
	my_employee.toString()
	
