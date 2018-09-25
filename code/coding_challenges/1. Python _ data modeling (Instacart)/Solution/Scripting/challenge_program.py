
import datetime

def is_number(s): #function checks whether incoming parameter is number or not
    try:
        float(s)
        return True
    except ValueError:
        return False

s_tab="	"  #Tab separator
		
input_file = open('scripting_challenge_input_file.txt')
next(input_file) #skip header

lines = [] #input lines
for line in input_file: #read all lines from file
	cols = []
	cols=line.split(s_tab) #split all values separated by Tab saparator and write them in a list
	lines.append(cols)
input_file.close()

#for cols in lines:
#	print cols

o_cols =[] #output column list
for cols in lines:
	
	error_mes=""

	cols0 = cols[0].split(":")  # split first column into words to retrieve order_id and order_date
	if len(cols0) >= 2:        
		order_id = cols0[0]	
		order_date=cols0[1]
	elif len(cols0) == 1:
		order_id = cols0[0]
		order_date=""
	else:
		order_id = ""
		order_date=""
	
	if not is_number(order_id): #check if order_id is number or not
		order_id=""
		error_mes="Invalid order id;"
	
	if is_number(order_date) and len(order_date) == 8:  #check if order_date is date or not
		order_date=datetime.datetime.strptime(order_date, '%Y%m%d').strftime('%Y-%m-%d') #convert YYYYMMDD to YYYY-MM-DD
	else:
		order_date=""
		error_mes += "Invalid date;"
	
	user_id=cols[1] #retrive user_id
	
	if not is_number(user_id): # check if user_id is number or not
		user_id=""
		error_mes+="Invalid user id"
	
	item_cnt = 0 #a variable to store a denominator to calculate average item price
	avg_item_price=0
	
	item_price_1 = cols[2] #retrive item_price_1
	i_item_price_1=0
	if is_number(item_price_1): #check if item_price_1 is number or not
		i_item_price_1=float(item_price_1) 
		item_cnt +=1
	else:
		error_mes+="Invalid item price 1;"

	item_price_2 = cols[3] #retrive item_price_2
	i_item_price_2=0
	if is_number(item_price_2): #check if item_price_2 is number or not
		i_item_price_2=float(item_price_2)	
		item_cnt +=1 #increment the denominator
	else:
		error_mes+="Invalid item price 2;"

	item_price_3 = cols[4] #retrive item_price_3
	i_item_price_3=0
	if is_number(item_price_3): #check if item_price_3 is number or not
		i_item_price_3=float(item_price_3)	
		item_cnt +=1
	else:
		error_mes+="Invalid item price 3;"		
		
	item_price_4 = cols[5] #retrive item_price_4
	i_item_price_4=0
	if is_number(item_price_4): #check if item_price_4 is number or not
		i_item_price_4=float(item_price_4)	
		item_cnt +=1
	else:
		error_mes+="Invalid item price 4;"		
		
	if item_cnt > 0: #calculate average item price (if there is something to calculate)
		avg_item_price=(i_item_price_1 + i_item_price_2 + i_item_price_3 + i_item_price_4)/item_cnt
		
	start_page_url=""
	if cols[6].find("http://www.insacart.com") > -1:  #check whether start_page_url is valid URL or not
		start_page_url = cols[6].replace("\n", "") #remove \n from URL
	else:
		start_page_url=""
		error_mes+="Invalid URL"
	#concatenate all output items into a string and add to list
	o_cols.append(str(order_id) + s_tab + str(order_date) + s_tab + str(user_id) + s_tab + str(avg_item_price) + s_tab + start_page_url + s_tab + error_mes + "\n")

#write output data to file
output_file = open('scripting_challenge_output_file.txt', 'w')
output_file.writelines("order_id	order_date	user_id	avg_item_price	start_page_url	error_msg\n")
for line in o_cols:
	output_file.writelines(line)
output_file.close()
		