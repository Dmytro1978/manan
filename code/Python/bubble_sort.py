# this code implements a bubble sort algorithm  
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