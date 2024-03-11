#Inheritance Lab.py

#Vanessa Crighton

#Purpose: to create a parent class that is to be inherited by two child classes.


from datetime import datetime


#Parent class
class Employee:
	def __init__(self, employee_number, office_number, name, birthdate):
			self.employee_number = employee_number
			self.office_number = office_number
			self.name = name
			self.birthdate = birthdate
			
		#Variables
	employee_number = 0
	office_number = 0
	name = "First Last"
	birthday = date.today()
		
		#set employee number
	def getEmployee_number(self):
				return self.employee_number
	def setEmployee_number(self, employee_number):
				self.employee_number = employee_number
		#set office number 		
	def getOffice_number(self):
				return self.office_number
	def setOffice_number(self, office_number):
				if office_number < 100 or office_number > 500:
					return False
				else:
					self.office_number = office_number
					return True
		#set name
	def get_name(self):
				return self.name
	def set_name(self, name):
				self.name = name
			
		#birthday
	def get_birthdate(self):
			return self.Birthdate
	
	def set_birthdate(self, Birthdate):
			if Birthdate.month < 1 or Birthdate.month > 12 or Birthdate.day < 1 or Birthdate.day > 31:
				return False
			else:
				self.Birthdate = Birthdate
				return True
			
	def is_birthday(self):
			currentDate = date.today() #Get current date
			if currentDate.month == self.Birthdate.month and currentDate.day == self.Birthdate.day:
				return True
			else:
				return False
	
		
#1st child class
		
		
class HourlyEmployee(Employee):
	def __init__(self, employee_number, office_number, name, birthdate, hourly_salary, Overtime_hourly_salary, hours_worked, overtime_hours_worked):
		Employee(<#employee_number#>, <#office_number#>, <#name#>, <#birthdate#>)
		self.hourly_salary = hourly_salary
		self.OverTime_hourly_salary = OverTime_hourly_salary
		self.hours_worked = hours_worked
		self.overtime_hours_worked = overtime_hours_worked
		
	#Variables
	hourly_employee_salary = 0
	OverTime_hourly_salary = 0
	hours_worked = 0
	overtime_hours_worked = 0
	
	def getHours_worked(self):
		return self.hours_worked
	
	def add_hours(self, hours):
		if hours <= 9:
			self.hours_worked += hours
		else:
			self.hours_worked +=9
			self.overTimeHours_worked += hours - 9
			
	def getOverTime_hours(self):
		return self.overtimeHours_worked
	def get_salary(self):
		return (self.hours_worked * self.hourly_salary) + (self.overtime_hours_worked * self.OverTime_hourly_salary)
	
	
#2nd child class
class CommissionEmployee(Employee):
	def __init__(self, employee_number, office_number, name, birthdate, commission_percentage, total_sales): 
		Employee(<#employee_number#>, <#office_number#>, <#name#>, <#birthdate#>)
		self.commission_percentage = commission_percentage
		self.total_sales = total_sales
		
	def get_commission(self):
		return self.commission_percentage
	
	def get_total_sales(self):
		return self.total_sales
	
	def add_sales(self, sales):
		self.total_sales += sales
		
	def get_salary(self):
		salary = self.commission_percentage * self.total_sales
		if self.total_sales > 300000:
			salary = salary + (salary * 0.03)
		return salary
	
