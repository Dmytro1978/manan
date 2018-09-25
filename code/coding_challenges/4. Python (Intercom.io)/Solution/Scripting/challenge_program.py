import math
import os
import json
from math import acos
from math import sin
from math import cos

#function checks whether incoming parameter is number or not
def is_number(s): 
    try:
        float(s)
        return True
    except ValueError:
        return False	

#function converts string input value to float
def to_number(s): 
	if is_number(s):
		return float(s)
	else:
		return 0

#Class Customer		
class Customer:
	def __init__(self, userId, firstName, lastName, latitude, longitude, distance):
		self.userId=userId
		self.firstName=firstName
		self.lastName=lastName
		self.latitude=latitude
		self.longitude=longitude
		self.distance=distance
		
	def getUserId(self):
		return self.userId
		
	def getFirstName(self):
		return self.firstName
		
	def getLastName(self):
		return self.lastName
		
	def getLatitude(self):
		return self.latitude
		
	def getLongitude(self):
		return self.longitude
	
	def getDistance(self):
		return self.distance
	
dublinLatitude=53.3381985
dublinLongitude=-6.2592576
earthRadius=6371.3

inputFile = open('customers.json')
outputFile = open('invited_customers.csv','w')
try:
    
	customerList=[]
	#read input file
	for line in inputFile:
		#parse json format
		jsonObj=json.loads(line)
		fullName=jsonObj["name"].split(" ")
		custLatitude = to_number(jsonObj["latitude"])
		custLongitude = to_number(jsonObj["longitude"])
		userId = jsonObj["user_id"]
		longitudeDelta = abs(abs(dublinLongitude) - abs(custLongitude))
		
		#calculate central angle
		centralAngle = acos(sin(dublinLatitude)*sin(custLatitude) + cos(dublinLatitude)*cos(custLatitude)*cos(longitudeDelta))*0.0174533 # finally convert to radians
		#calcilate distance (arc length)
		distance = round(centralAngle*earthRadius,2)
	
		customer=Customer(userId, fullName[0], fullName[1], custLatitude, custLongitude, distance)
		customerList.append(customer)
	
	invCustList={}
	#create a list of only invited customers
	for i in range(len(customerList)):
		customer=customerList[i]
		if customer.getDistance() <= 100:
			invCustList[customer.getUserId()] = "%s,%s,%s" % (customer.getFirstName(), customer.getLastName(), customer.getDistance())

	#create header (column names)
	outputFile.write("user_id,first_name,last_name,distance\n")
	#write to file
	for key in sorted(invCustList.iterkeys()):
		outputFile.write("%s, %s\n" % (key, invCustList[key]))

finally:
	#close all resources
	inputFile.close()	
	outputFile.close()
