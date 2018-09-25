#Function that uses a loop to calculate car's depresiation
#Input parameters:
# 1 - Car price
#Command format: python car_depreciation_loop.py <car price>
#Example: python car_depreciation_loop.py 25000 

import sys

def car_depreciation_loop(car_price):
    
    years = 0
    while car_price > 2000:
        car_price = car_price*0.9
        years += 1
    return years
     
#check input arguments
if len(sys.argv) < 2:
    print 'Too few arguments. The format is: python %s <car price>. \n Example: %s 25000' % (sys.argv[0], sys.argv[0])
    sys.exit(1)

#Read a car price from args
try:
    car_price = int(sys.argv[1])
except:
    print 'The argument type is not integer! Please enter integer value.'
    sys.exit(1)  

#Output the result
print 'Total years to reach 2000 threshold: %s' % car_depreciation_loop(car_price)