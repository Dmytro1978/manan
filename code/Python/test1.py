#sample output :
#sum67([1, 2, 2]) -> 5
#sum67([1, 2, 2, 6, 99, 99, 7]) -> 5
#sum67([1, 1, 6, 7, 2]) -> 4



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