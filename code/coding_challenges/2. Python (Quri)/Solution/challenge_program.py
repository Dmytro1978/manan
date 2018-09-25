from __future__ import division
import datetime
import os
from csv import reader

brandInfoList = {
	"Cola": [15,18,21,24],
	"Pepsi": [27,30,33,36],
	"Mtn Dew": [39,42,45,48], 
	"Bud Light": [51,54,57,60],	
	"Michelob Ultra": [63,66,69,72],
	"Skittles":[75,77,80,83],
	"Snickers":[86,89,92,95],
	"Doritos":[98,101,104,107],
	"Tostitos":[110,113,116,119]
}

#class Brand contains information about Brand in particular store: 
# - brand name;
# - information about displays, locations, and answers for current brand
# - list of answers for each display.
class Brand:
	def __init__(self, brandName, answerColumnList, line):
		self.displayDic = {}
		self.brandName=brandName
		self.answerColumnList=answerColumnList
		for i in range(len(answerColumnList)): #this loop creates a dictionary: {displayN:[[answer<Y,N>],[display_type],[location]]}
			if brandName=="Skittles" and i==0:
				dList=[line[self.answerColumnList[i]], "", line[self.answerColumnList[i]+1]] #Skittles brand does not have display type. Whis code imitates a workaround that can happen in a real situation
			else:
				dList=[line[self.answerColumnList[i]], line[self.answerColumnList[i]+1],line[self.answerColumnList[i]+2]] #["answer(Y/N)", "display type","location"]
			self.displayDic["Display"+str(i+1)]=dList
			
	def getName(self):
		return self.brandName
		
	def getDisplay(self, num): #return Yes/No (found/not found) for specified display 
		if (num < 1 or num > 4):
			return "Invalid index"
		else:
			return self.displayDic["Display"+str(i-1)]

	def getDisplayDic(self):
		return self.displayDic
			
	def getNumDisplays(self): #returns number of displays for current brand
		numDisplay=0
		for display in self.displayDic:
			if self.displayDic[display][0] == "Yes":	
				numDisplay += 1
		return numDisplay
		
#class Store contains information aboiut particular store:
# - store name
# - store address
# - retailerName
# - information about Brands located in the store	
class Store:
	def __init__(self, retailerName, storeName, storeAddress):
		self.storeName=storeName
		self.storeAddress=storeAddress
		self.retailerName=retailerName

	def getRetailerName(self):
		return self.retailerName
		
	def getName(self):
		return self.storeName
		
	def getAddress():
		return self.storeAddress
				
	def getBrands(self):
		return self.brandList
		
	def setBrands(self, brandList):
		self.brandList=brandList
		
	def showBrands(self):
		retString=""
		for brand in self.brandList:
			retString += brand.getName()+";"
		return retString

#-----------------Main script--------------------------		
if not os.path.exists("output"):
    os.makedirs("output")
		
inputFile = open('superbowl_data.csv')
outputFile1 = open('output/brand_store.csv','w')
outputFile2 = open('output/disp_loc.csv','w')
outputFile3 = open('output/brand_loc.csv','w')
outputFile4 = open('output/retl_disp.csv','w')

try:

	next(inputFile) #skip header

	lines = [] #input lines
	stores = [] #list of wtores

	for line in reader(inputFile): #read all lines from file

		lines.append(line)
		retailerName=line[3]
		storeName = line[4]
		storeAddress=line[5]
	
		#create Store object
		currStore=Store(retailerName, storeName, storeAddress)
	
		#create list of brands for the store
		brandList = []
		for brandInfo in brandInfoList:
			brandList.append(Brand(brandInfo, brandInfoList[brandInfo], line))

		currStore.setBrands(brandList)
		stores.append(currStore)

	#Dictionaries for output datasets:
	#Percentage of stores per brand that had at least 1 display found
	brandDic = {} #{brand1:num_of_stores, brand2:num_of_stores, brandN:num_of_stores,...}

	#Percentage of locations per display of stores that had at least 1 display found
	dispLocDic={"Display1": {}, "Display2": {}, "Display3": {}, "Display4": {}}#dictionary for second output dataset

	#Number of locatons per brand of stores that had at least 1 display found
	brandLocDic={} #{brand1: {location1: count1, location2: count2, ..., locationN:countN}, brand2:{location1: count1, location2: count2, ..., locationN:countN},...}

	#Number of displays per display type per retailer
	retailerDic={} #dictionary for fourth output dataset: {retailer_name1:{display1:count1,display2:count2,...,displayN:countN},retailer_name2:{display1:count1,display2:count2,...,displayN:countN},...}

	storeNum=len(stores)
	for store in stores:
		storeName=store.getName()
		brandList=store.getBrands()
		retailerName=store.getRetailerName()
		tmpDic={}
		for brand in brandList:
			#prepare dataset1
			brandName = brand.getName()
			n=0
			if brandName in brandDic:
				n = brandDic[brandName]
			if brand.getNumDisplays() > 0:
				n += 1
				brandDic[brandName] = n 
		
			#prepare dataset2
			location =""
			displayDic=brand.getDisplayDic()
			for display in displayDic:
				location=displayDic[display][2]
				if location != "":
					n=0
					dic = dispLocDic[display]
					if location in dic:
						n = dic[location]
					n += 1
					dic[location] = n
					dispLocDic[display]=dic

			#prepare dataset3		
			locationDic={}
			location=""
			for display in displayDic:
				m=0
				yesNo=displayDic[display][0]
				if yesNo == "Yes":
					if brandName in brandLocDic:
						locationDic=brandLocDic[brandName]
					location=displayDic[display][2]
					if location in locationDic:
						m=locationDic[location] #location count						
					m += 1
					locationDic[location]=m
					brandLocDic[brandName]=locationDic
		
			#check if there are any displays in particular store (for any brand)
			for display in displayDic:
				yesNo=displayDic[display][0]
				if yesNo=="Yes":
					tmpDic[display]=1
				else:
					tmpDic[display]=0
	
		#prepare dataset4		
		retDisplayDic={}
		if retailerName in retailerDic:
			retDisplayDic=retailerDic[retailerName]
		for display in tmpDic:
			n=0
			if display in retDisplayDic:
				n=retDisplayDic[display]
			n += tmpDic[display]
			retDisplayDic[display] = n
		retailerDic[retailerName]=retDisplayDic 

	#create dictionary with display totals
	dicTotal={}
	total=0
	for display in dispLocDic:
		dic = dispLocDic[display]
		for d in dic:
			total += dic[d]
		dicTotal[display]= total
		total=0	

	#-------------report 1------------- 
	outputFile1.writelines("Brand, num of stores, total num of stores, prc\n")
	for k,v in brandDic.iteritems():
		outputFile1.writelines("%s,%s,%s,%.2f%s" % (k, v, storeNum, (v/storeNum)*100, "%\n"))

	#-------------report 2-------------
	outputFile2.writelines("display, location, count, total counts, prc\n")
	for display in dispLocDic:
		dic = dispLocDic[display]
		for d in dic:
			outputFile2.writelines("%s,%s,%s,%s,%.2f%s" % (display, d, dic[d], dicTotal[display], (dic[d]/dicTotal[display])*100,"%\n"))
	
	#-------------report 3-------------
	outputFile3.writelines("brand, location, count\n")
	for brandName in brandLocDic:
		locationDic=brandLocDic[brandName]
		for location in locationDic:
			outputFile3.writelines("%s,%s,%s\n" % (brandName, location, locationDic[location]))

	#-------------report 4-------------
	outStr=""
	outputFile4.writelines("retailer,display1,display2,display3,display4\n")
	for retailerName in retailerDic:
		displayDic=retailerDic[retailerName]
		i=0
		for display in displayDic:
			outStr += str(displayDic["Display" + str(i+1)]) + ","
			i+=1
		outputFile4.writelines("%s,%s\n" % (retailerName, outStr))
		outStr=""

finally:
	inputFile.close()
	outputFile1.close()
	outputFile2.close()
	outputFile3.close()
	outputFile4.close()
