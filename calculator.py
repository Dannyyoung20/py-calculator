# A Simple Py Terminal Calculator 

class Calculator():

	def __init__(self):
		self.temp = 0
		self.calInit = False
		self.inOperation = True

		# Begin the calculator
		print('Welcome to your py terminal calculator')
		number = self.getANumber()
		self.calculatorOperation(number)


	def addition(self, number):
		# Simply just add the numbers
		self.temp += number
		return self.temp

	def subtraction(self, number):
		# Simply subtract the two numbers
		self.temp -= number
		return self.temp

	def multiplication(self, number):
		# Multiply the two numbers
		self.temp *= number
		return self.temp

	def division(self, number):
		# Divide the two numbers
		try:
			self.temp /= number
			return self.temp
		except ZeroDivisionError as e:
			print('You cannot divide a number by zero')
	
	def getANumber(self):
		print('Please input a number... \t')
		number = int(input())
		return number

	def checkIfTempIsInit(self, number):
		if self.temp == False and self.calInit == False:
			self.temp = number

	def getAnOperand(self):
		print('Please select an operation...')
		print('For Addition select A, for Subtraction S, Divison D and Multiplication M, Equals E')
		userOperand = input().lower()
		return userOperand

	def calculatorOperation(self, number):
		if self.checkIfTempIsInit(number):
			o = self.getAnOperand()

		userNum = self.getANumber()

		o = self.getAnOperand()

		if o == 'a':
			self.addition(userNum)
		elif o == 'm':
			self.multiplication(userNum)
		elif o == 'd':
			self.divison
		elif o == 's':
			self.subtraction(userNum)
		elif o == 'e':
			print('Your final answer is ', self.temp)
			print('Thanks for your time')
			self.inOperation = False
		else:
			print('Invalid String given... Breaking out of loop!!')
			exit()


		while self.inOperation == True:
			self.calculatorOperation(self.temp)


calculator = Calculator()