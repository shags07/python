import time 
import math 
def TimeCalculate(func): 
	def timecalculation(*args, **kwargs):  
		begin = time.time() 
		func(*args, **kwargs) 
		end = time.time() 
		print("Time taken in : ", func.__name__, end - begin) 
	return timecalculation
@TimeCalculate
def factorial(num):
	print(math.factorial(num)) 
factorial(5) 

