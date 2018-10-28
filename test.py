#
Family_Birthdays = open('Family_Birthdays.txt','w+')

import os 
import sys 
import math 
import datetime
import pandas as pd 
import numpy as np 
import re
import matplotlib.pyplot as plt
import webbrowser

from urllib.request import urlopen, Request
from datetime import date 
from array import array 

print("""
-------------------------------------
+ AERONAUTICAL PHYSICS CALCULATOR	
+ v1.0.0					        
+ Build Date: 14 October 2018		
+ Author: Richard Sponseller 	
-------------------------------------
	""")

#webbrowser.open('https://stackoverflow.com/questions/4302027/how-to-open-a-url-in-python')

url = 'https://weather.com/weather/tenday/l/21787:4:US'
request = Request(url)
response = urlopen(request)
html = response.read()
response.close

print(html)
# args = sys.argv
# if len(args) < 4:
# 	print('Invalid number of arguments entered. Try again')
# 	sys.exit()
# else: 
# 	print('Valid number of arguments entered. Continuing...\n')
# 	program_name = args[0]
# 	aircraft_type = args[1]
# 	fuel_weight_fraction = args[2]
# 	payload_weight = args[3]
# list_of_aircraft_data = open('aircraft_type.txt','r')
# data = [] 
# with open('aircraft_type.txt','r') as list_of_aircraft_data:
# 	for line in list_of_aircraft_data: 
# 		data = list_of_aircraft_data.readlines()
# 		aircraft_type_quantity = len(data)
# list_of_aircraft_data.close()

# data_aircraft_type = [str()] * 5
# print(data_aircraft_type)
# for i in range(aircraft_type_quantity):
# 	data_aircraft_type[line] = line.split(',')
# 	#print(data_aircraft_type)
	
# print(data_aircraft_type)

# #print(data_aircraft_type)

# print('Enter Aircraft Type:')
# aircraft_type = str(input())
# print('Enter Fuel Weight Fraction:')
# fuel_weight_fraction = float(input())
# print('Enter Payload Weight (lbs):')
# payload_weight = float(input())

# class Airplane: 
# 	def __init__(aircraft_type, fuel_weight_fraction, payload_weight):





# def hourly_salary(salary):
# 	salary = float(salary)
# 	hourly_salary = salary / 2080
# 	print('Your annual salary is: $%5.2f' %salary)
# 	print('Your hourly salary is: $%5.2f' %hourly_salary)

# today_date = date.today()
# #Family_Birthdays.write(datetime.time())
# Family_Birthdays.write('Date {} \n'.format(today_date))

# def ask_ok(prompt, retries=4, reminder='Please try again!'):
# 	while True: 
# 		ok = input(prompt)
# 		if ok in ('y','ye','yes'): 
# 			return True 
# 		if ok in ('n','no','nop','nope'): 
# 			return False 
# 		retries = retries - 1
# 		if retries < 0: 
# 			raise ValueError('invalid user response')
# 		print(reminder) 

# ask_ok('Do you really want to quit?',2)


# class Birthday: 
# 	def __init__(self, name,day, month, year):
# 		self.n = name
# 		self.d = day 
# 		self.m = month
# 		self.y = year 

# x = Birthday('Michael', 12, 2, 1994)

# Family_Birthdays.write('Name: {} \n'.format(x.n))
# Family_Birthdays.write('Birthday: {} - {} - {}'.format(x.y,x.m,x.d))

# x = np.arange(0.0,2.0,0.01)

# col = []
# for i, value in enumerate(x, start=1): 
# 	col = x

# y = 1 + np.sin(2*np.pi*x)
# plt.plot(x,y)
# plt.xlabel('time(s)')
# plt.ylabel('voltage(mv)')
# plt.savefig("test.png")
# plt.show
