#A simple calculator
import math

def mul(x,y):
	return x * y
	
def add(x,y):
	return x + y
	
def sub(x,y):
	return x - y	

def dev(x,y):
	return x / y
	
while True:
	i=input("To calculate, type: \n+ for addition \n- for subbtraction \n* for multiplication \n/ for devision  \nx to close: ")
	
	try:
		if i == "+":
			print(int(add(int(input("Insert number:" )),int(input("Insert another  number:" )))))
		
		elif i == "-":
			print(int(sub(int(input("Insert number:" )),int(input("Insert another  number:" )))))
		
		elif i == "*":
			print(int(mul(int(input("Insert number:" )),int(input("Insert another  number:" )))))
		
		elif i == "/":
			print(float(dev(float(input("Insert number:" )),float(input("Insert another number:" )))))
		
		elif i == "x":
			break
			
		else:
			print("Input error")
	
	except :
		print("Division by zero")
