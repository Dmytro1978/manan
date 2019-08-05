# this code finds accurancies of each unique element in the array
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

