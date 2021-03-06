LIST
======================================TASK======================================
Reverse the list
---------------------------------
list1 = [1,2,3,4,5,6,7]
print(list1)
list2 = []
for n in reversed(list1):
	list2.insert(len(list1), n)
print(list2)
================================================================================

======================================TASK======================================
Reverse the string
------------------------------------SOLUTION1-----------------------------------
#using reversed function
def reverse(str1):
    str2 = ""
    for s in reversed(str1):
        str2 += s
    return str2
print reverse("abcd")
------------------------------------SOLUTION2-----------------------------------
#without using reversed function
def reverse(str1):
    str2 = ""
    l = len(str1)
    for i in range(len(str1)):
        str2 += str1[l-1]
        l -=1
    return str2
    
print reverse("abcd")
================================================================================
======================================TASK======================================
Given an array of ints, return True if 6 appears as either the first or last element in the array. 
The array will be length 1 or more.

first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
------------------------------------SOLUTION------------------------------------
def first_last6(nums):
  if nums[0] == 6 or nums[len(nums)-1] == 6:
    return True
  else:
    return False
================================================================================

======================================TASK======================================

Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
------------------------------------SOLUTION------------------------------------
def same_first_last(nums):
  if len(nums) > 0 and nums[0] == nums[len(nums)-1]:
    return True
  else:
    return False
================================================================================

======================================TASK======================================
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

make_pi() → [3, 1, 4]
------------------------------------SOLUTION1-----------------------------------
#straight forvard
def make_pi():
  return [3,1,4]
------------------------------------SOLUTION2-----------------------------------
#extract from PI 
def make_pi():
  pi = math.pi
  s  = str(pi)
  return [int(s[0]), int(s[2]), int(s[3])] 
================================================================================

======================================TASK======================================
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
------------------------------------SOLUTION------------------------------------
def rotate_left3(nums):
  nums1=list(nums) #copy list to a new one
  x=nums[0]
  for n in range(0,len(nums)-1):
    nums[n]=nums[n+1]
  nums[len(nums)-1]=x
  return nums
================================================================================

======================================TASK======================================

Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
------------------------------------SOLUTION------------------------------------
def reverse3(nums):
  list=[]
  for n in reversed(nums):
    list.append(n)
  return list
================================================================================

======================================TASK======================================LIST
======================================TASK======================================
Reverse the list
---------------------------------
list1 = [1,2,3,4,5,6,7]
print(list1)
list2 = []
for n in reversed(list1):
	list2.insert(len(list1), n)
print(list2)
================================================================================

======================================TASK======================================
Given an array of ints, return True if 6 appears as either the first or last element in the array. 
The array will be length 1 or more.

first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
------------------------------------SOLUTION------------------------------------
def first_last6(nums):
  if nums[0] == 6 or nums[len(nums)-1] == 6:
    return True
  else:
    return False
================================================================================

======================================TASK======================================

Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
------------------------------------SOLUTION------------------------------------
def same_first_last(nums):
  if len(nums) > 0 and nums[0] == nums[len(nums)-1]:
    return True
  else:
    return False
================================================================================

======================================TASK======================================
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

make_pi() → [3, 1, 4]
------------------------------------SOLUTION1-----------------------------------
#straight forvard
def make_pi():
  return [3,1,4]
------------------------------------SOLUTION2-----------------------------------
#extract from PI 
def make_pi():
  pi = math.pi
  s  = str(pi)
  return [int(s[0]), int(s[2]), int(s[3])] 
================================================================================

======================================TASK======================================
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
------------------------------------SOLUTION------------------------------------
def rotate_left3(nums):
  nums1=list(nums) #copy list to a new one
  x=nums[0]
  for n in range(0,len(nums)-1):
    nums[n]=nums[n+1]
  nums[len(nums)-1]=x
  return nums
================================================================================

======================================TASK======================================

Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
------------------------------------SOLUTION------------------------------------
def reverse3(nums):
  list=[]
  for n in reversed(nums):
    list.append(n)
  return list
================================================================================

======================================TASK======================================
Sort a list
list_sort([1,8,5,3,4,2,7,6,20,19,18,17,16,15,14,13,12,11,10,9]) → [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_sort([3,1,2]) → [1,2,3]
------------------------------------SOLUTION------------------------------------
def list_sort(l):
	print l #print unsorted list
	itn=0
	for i in range(0,len(l)-1):
		for j in range(len(l)-1):
			if l[j] >l[j+1]:
				x=l[j+1]
				l[j+1]=l[j]
				l[j]=x
				itn += 1
	print l #sorted list
	print itn #print number of iterations
================================================================================

======================================TASK======================================

Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the 
other elements to be that value. Return the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
------------------------------------SOLUTION------------------------------------
def max_end3(nums):
  if nums[0] >= nums[2]:
    x = nums[0]
  else:
    x = nums[2]
  
  for i in range(len(nums)):
    nums[i] = x
  return nums
================================================================================

======================================TASK======================================
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars 
is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
Return True if the party with the given values is successful, or False otherwise.

------------------------------------SOLUTION------------------------------------
def cigar_party(cigars, is_weekend):
  if cigars < 40:
    return False
  elif is_weekend:
    return True
  elif cigars > 60:
    return False
  else:
    return True
================================================================================ 

======================================TASK======================================
"Return the 'centered' average of an array of ints, which we'll say is the mean average of the values, except ignoring the 
largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise 
for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more."

centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3

------------------------------------SOLUTION------------------------------------
def centered_average(nums):
  minv = min(nums)
  maxv = max(nums)
  maxvc = nums.count(maxv)
  minvc = nums.count(minv)
  l=[]
  for n in nums:
    if (n == maxv and maxvc == 1) or (n == minv and minvc == 1):
      continue
    elif n in l:
      continue
    else:
      l.append(n)
  avgv = int(sum(l)/len(l))
  return avgv
================================================================================ 

======================================TASK======================================
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

has22([1, 2, 2]) → True
has22([1, 2, 1, 2]) → False
has22([2, 1, 2]) → False
------------------------------------SOLUTION------------------------------------
def has22(nums):
  n_prev = 0
  ret = False
  for i in range(len(nums)):
    if nums[i] == 2 and nums[i] == n_prev:
      ret = True
    n_prev = nums[i]
  return ret
================================================================================ 

======================================TASK======================================
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 
(every 6 will be followed by at least one 7). Return 0 for no numbers:
sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
------------------------------------SOLUTION------------------------------------
def sum67(nums):
  n6 = 0
  l = []
  for n in nums:
    if n == 6 or n6:
      n6 = True
    else:
      l.append(n)
    if n == 7:
      n6 = False
  return sum(l)
================================================================================

======================================TASK======================================
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks 
(5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder 
than it looks and can be done without any loops. See also: Introduction to MakeBricks

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
------------------------------------SOLUTION------------------------------------
def make_bricks(small, big, goal):
  need_big = int(goal/5)
  if big <= need_big and small + big*5 >= goal:
    return True
  elif big >= need_big and goal%5 == 0:
    return True
  elif big >= need_big and need_big*5 + small >= goal:
    return True
  else:
    return False
================================================================================ 

======================================TASK======================================
Count all odd numbers in the list usig recursion
------------------------------------SOLUTION------------------------------------
def countOdd(l):
	print l
	if l == list(): #if list is empty
		return 0
	return l[0] % 2 + countOdd(l[1:])

print countOdd([1,2,3,4,5,6,7,8,9,10,11])
================================================================================ 

======================================TASK======================================
Find number of substrings in a string:
substr_count('aaaaa') → 4
substr_count(' abc done abc ', ' ') → 4
substr_count('abcdoneabc', ' abc') → 2
substr_count('ababa', 'aba') → 2
------------------------------------SOLUTION------------------------------------
def substr_count(input_string, sub_string):
	i = 0
	while True:
		if sub_string in input_string:
			ind = input_string.index(sub_string)
			i += 1
			input_string = input_string[ind+1:]
		else:
			break
	return i
================================================================================ 

======================================TASK======================================
Define a function has two arguments: list and item.
Return the number of times the item occurs in the list.
count([1,2,3], 2) → 1
count([1,2,3,'a','b',2], 2) → 2
count([1,2,3,['a','b',1],8,'ddd',[1,2,44,'ttt']], 1) → 1
count([1,'bbb','ccc',4,'bbb'], 'bbb') → 2
count(['bbb',1,[1,2,['bbb']],'ccc'],'bbb') → 1
------------------------------------SOLUTION------------------------------------	
def count(sequence, item):
	cnt=0
	for n in sequence:
		if n == item:
			cnt += 1
            
	return cnt
    
#print count([1,2,'aaa', [5,4,3],2],2)
================================================================================ 
======================================TASK======================================
Remove all vowels from a word:
"Hey You!" → "Hy Y!"
"Congratulation!" → "Cngrtltn!" 
------------------------------------SOLUTION------------------------------------	
def anti_vowel(str1):
    outStr=""
    vowelStr="aeiou"
    for v in str1:
    	if str.lower(v) in vowelStr:
    		continue
    	else:
    		outStr += v
    return outStr
print anti_vowel("Hey You!")
================================================================================ 

======================================TASK======================================
Find all pairs of braces in a string and return True if each opening brace has a corresponding closing brace,
else return False:
findPairBrace("()") -> True
findPairBrace(")(") ->  False
findPairBrace(")()") -> False
findPairBrace("(()") -> False
findPairBrace(")((()))(") -> False
findPairBrace("()(()()") -> False
findPairBrace("()(())()") -> True
findPairBrace(")))))(((((") -> False
findPairBrace("((((()()))))") -> True
findPairBrace("(24+31*(18/6))*6/((19+12)*655-(89-78))") -> True
------------------------------------SOLUTION------------------------------------	
def findPairBrace(inStr):

	cntPair = 0
	
	lst = list(inStr) #convert  input string to a list to be able to refer to list elements 
	lCnt = lst.count("(") #get number of opening braces
	rCnt = lst.count(")") #get number of closing braces

	for ind, elem in enumerate(lst): #go through the list to find next "("
		if elem == "(": 
			for ind1, elem1 in enumerate(lst): #go through the list again to find corresponding ")"
				if elem1 == ")" and ind1 > ind: # find ")" with the index that is greater than the index of current "("
					cntPair += 1 #if found then increase the number of valid pairs
					lst[ind1] = "_" # erase used ")"
					break				
			lst[ind] = "_" # erase used "("
		#print st
	
	if cntPair*2 == lCnt + rCnt:
		res = "true"
	else:
		res = "false"
		
	print "'%s': -> left: %s, right: %s, pairs: %s, result: %s" % (inStr, lCnt, rCnt, cntPair, res)
================================================================================

======================================TASK======================================
Implement Bubble Sort algorithm
------------------------------------SOLUTION------------------------------------
s = [3,6,1,9,5,11,2,4,17,8]
print s

def bubble_sort(s):

    swap = True
    while swap: 
        swap = False
        for i in range(0,len(s)-1):
            if s[i] > s[i+1]:
                tmp = s[i]
                s[i] = s[i+1]
                s[i+1] = tmp
                swap = True
    return s

print bubble_sort(s)
================================================================================

======================================TASK======================================
Find number of unique occurancies of each element in the array
------------------------------------SOLUTION------------------------------------
arr = ['a','b','b','c','b','d','d'] # initial array
print arr

def occur_num(arr):
    dic = {}
    for n in arr:
        if n in dic:
            dic[n] += 1 
        else:
            dic[n] = 1
    return dic

print occur_num(arr)
================================================================================

======================================TASK======================================
Write a program named fizzbuzz that prints all integers in 1 through 10, inclusive. 
For odd numbers print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are both odd and a multiple of five, print “FizzBuzz”:
Fizz
2
Fizz
4
FizzBuzz
6
Fizz
8
Fizz
Buzz
------------------------------------SOLUTION------------------------------------
list = range(1,11)

def fizzbuzz(list):
    for n in list:
        if (n%2 > 0) & (n%5 == 0): 
            print 'FizzBuzz'
        elif n%5 == 0: 
            print 'Buzz'
        elif n%2 > 0: 
            print 'Fizz'
        else:
            print n

fizzbuzz(list)
================================================================================

======================================TASK======================================
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 
and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers:
sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
------------------------------------SOLUTION------------------------------------
def sum67(list):
    flag = False
    sm = 0
    for n in list:
        if n == 6:
            flag = True
        elif n == 7:
            flag = False
        elif flag:
            continue
        else:
            sm += n
    print 'total: ' + str(sm)


sum67([1, 2, 2])
sum67([1, 2, 2, 6, 99, 99, 7])
sum67([1, 1, 6, 7, 2])
================================================================================


======================================TASK======================================
Fix the bug in the code:

class MathUtils:

    @staticmethod
    def average(a, b):
        return a + b / 2

print(MathUtils.average(2, 1))
------------------------------------SOLUTION------------------------------------
# add parathensys to the formula, because to calculate an average value for a set of numbers first sum up all numbers and then divide on the total 
# of all numbers

class MathUtils:

    @staticmethod
    def average(a, b):
        return (a + b) / 2 # <-- the error was here

print(MathUtils.average(2, 1))


======================================TASK======================================

def nth_lowest_selling(sales, n):

    dic = {i:sales.count(i) for i in sales} #get counts for each unique book id

    dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])} # sort the dictionary by value

    if n <= 0 or n > len(dic):
        return None # return None if the n-th lowest selling is out range
    else:
        return list(dic)[n-1] # get the book id by n-th lowest selling

        
print(nth_lowest_selling([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))
print(nth_lowest_selling([100, 100, 100, 100, 80, 90, 80, 80], 2))

======================================TASK======================================

def count_substring(string, sub_string):
    cnt = 0
    
    return find_substring(string, sub_string, cnt)

def find_substring(string, sub_string, cnt):
    ind = string.find(sub_string)
    if ind > -1:
        cnt += 1
        string = string[ind+1: len(string)]
        return find_substring(string, sub_string, cnt)
    else:
        return cnt


if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count

======================================TASK======================================
Convert a number to binary:
DecimalToBinary(7) → 111
DecimalToBinary(6) → 110
------------------------------------SOLUTION------------------------------------

def DecimalToBinary(num):
    if num > 1:
        DecimalToBinary(num // 2)
    print(num % 2)
print DecimalToBinary(7)

================================================================================


======================================TASK======================================
List comprehensions
You are given three integers X, Y and Z representing the dimensions of a cuboid along with an integer N. You have to print a list of all possible 
coordinates given by (i,j,k) on a 3D grid where the sum of i + j+ k is not equal to N. Here, 0 < i < X; 0 < j < Y; 0 < k < Z; 

list_comprehensions(x,y,z,n)
list_comprehensions(1,1,1,2) → [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

The basic syntax of a list comprehension is

[ expression for item in list if conditional ]

This is equivalent to

for item in list:
    if conditional:
        expression
------------------------------------SOLUTION------------------------------------

def list_comprehensions(x,y,z,n):
if __name__ == '__main__':

    print([ [x1,y1,z1] for x1 in range(x+1) for y1 in range(y+1) for z1 in range(z+1) if (x1+y1+z1) != n ])

    '''
    it's equivalent to the following code:
    res = []
    for x1 in range(x+1):
        for y1 in range(y+1):
            for z1 in range(z+1):
                if (x1+y1+z1) != n:
                    res.append([x1,y1,z1])
    print(res)
    '''

================================================================================

======================================TASK======================================
You are given a string S. 
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format
A single line containing a string S.
Constraints

0 < len(S) < 1000

Output Format
In the first line, print True if S has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if S has any alphabetical characters. Otherwise, print False. 
In the third line, print True if S has any digits. Otherwise, print False. 
In the fourth line, print True if S has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if S has any uppercase characters. Otherwise, print False.
------------------------------------SOLUTION------------------------------------

def string_validation(s):

    has_alnum = False
    has_alpha = False
    has_digit = False
    has_lower = False
    has_upper = False

    for n in s:
        if n.isalnum():
            has_alnum = True
        if n.isalpha():
            has_alpha = True
        if n.isdigit():
            has_digit = True
        if n.islower():
            has_lower = True
        if n.isupper():
            has_upper = True
        
        if has_alnum and has_alpha and has_digit and has_lower and has_upper:
            break

    print(has_alnum)
    print(has_alpha)
    print(has_digit)
    print(has_lower)
    print(has_upper)

================================================================================

======================================TASK======================================
Given a non-empty array of integers, every element appears twice except for one. Find that single one:

single_number([2,2,1]) → 1 
single_number(4,1,2,1,2] → 4 
------------------------------------SOLUTION------------------------------------
def single_number(nums):

    dic = {} #use dictionary because operation on it are faster than on a list

    for n in nums: # iterate over all the elements in nums
        if n in dic: # if some number is already in  dictionary, remove it
            del dic[n]
        else:  # if some number in nums is new to the dictionary, append it
            dic[n] = 1
    return list(dic)[0] # in result the dictionary will only contain the number which is single in the list

print(single_number([1, 2, 1, 2, 4]))

================================================================================

======================================TASK======================================
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

missingNumber([3,0,1]) → 2 
missingNumber([9,6,4,2,3,5,7,0,1]) → 8
------------------------------------SOLUTION------------------------------------

def missingNumber(nums):

  nums.sort()
        
  etalon_lst = range(len(nums) + 1) # all numbers from 0 to n
  for n in etalon_lst:
    if n not in nums:
      return n
================================================================================

======================================TASK======================================
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, find the duplicate one.

findDuplicate([1,3,4,2,2]) → 2
findDuplicate([3,1,3,4,2]) → 3

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
------------------------------------SOLUTION------------------------------------
def findDuplicate(self, nums):
        
  dic = {}

  for n in nums:
    if n in dic:
      return n
    else:
      dic[n] = 1
================================================================================

======================================TASK======================================
Given an unsorted integer array, find the smallest missing positive integer:

firstMissingPositive([1,2,0]) → 3 
firstMissingPositive([3,4,-1,1]) → 2
firstMissingPositive([7,8,9,11,12]) → 1

Your algorithm should run in O(n) time and uses constant extra space.
------------------------------------SOLUTION------------------------------------

def firstMissingPositive(nums):
    for n in range(len(nums) + 2):
        if n not in nums and n != 0:
            return n
================================================================================

======================================TASK======================================
singleNumber([4, 1, 2, 1, 2]) → 4
singleNumber([1, 2, 1, 8, 2]) → 8

------------------------------------SOLUTION------------------------------------
import operator
def singleNumber(nums):

    dic = {i: nums.count(i) for i in nums}

    # Python 2.7
    lst = sorted(dic.items(), key=operator.itemgetter(1))
    return lst[0][0]

    # Python 3.x
    dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1])}
    return list(dic.keys())[0]


print(singleNumber([4, 1, 2, 1, 2]))
print(singleNumber([1, 2, 1, 8, 2]))
================================================================================

======================================TASK======================================
------------------------------------SOLUTION------------------------------------
================================================================================

======================================TASK======================================
------------------------------------SOLUTION------------------------------------
================================================================================